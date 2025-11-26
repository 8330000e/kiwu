from flask import Flask, render_template, jsonify 
#flask는 웹서버, render_template는 html파일 렌더링, jsonify는 json형태로 반환
from gpiozero import LED, Button
import time
import random
import threading #비동기

app = Flask(__name__) #flask 객체 생성

# GPIO 설정
led = LED(17)
button = Button(27, pull_up=True) #버튼 객체 생성, 풀업저항 사용(라즈베리파이는 내부저항있음)

# 스레드 안전성을 위한 락
state_lock = threading.Lock() #Lock = 잠금. 스레드간 자원경쟁 방지

#스레드: 동시 실행 시 동기화 문제 발생 가능성 있음. 
# 스레드 동기화 (Thread Synchronization): 여러 스레드가 공유 자원에 접근할 때,
# 자바 synchronlzed: 멀티스레드 환경에서 동기화를 구현하는 기본적 . 파이썬에는 threading 모듈의 Lock 클래스 사용.
#Lock 객체의 acquire()와 release() 메서드를 사용하여 스레드 간의 접근을 제어.
# 데이터의 일관성을 유지하기 위해 스레드 간의 작업 순서를 조정하는 기법.
#스레드 데드락: 두 스레드가 서로가 가진 자원을 기다리며 무한대기 상태에 빠지는 것.
#스레드 데드락 레이스 컨디션 락: 여러 스레드가 동시에 공유 자원에 접근하려고 할 때 발생하는 문제.
#락을 사용하면 한 스레드가 자원을 사용할 때 다른 스레드는 대기하게 되어 이러한 문제를 방지할 수 있다.

# 게임 상태
game_state = {
    'status': 'ready',  # ready, waiting(대기상태), measuring(측정중), result(결과), early_press(너무 빨리 누름), timeout(타임아웃)
    'reaction_time': 0,
    'start_time': 0,
    'best_score': None
}

# 타임아웃 타이머
timeout_timer = None #타임아웃 타이머 ''전역변수''

def game_logic():
    """버튼이 눌렸을 때 실행"""
    global timeout_timer #전역변수 사용
    
    with state_lock:
        if game_state['status'] == 'measuring': #측정중일 때
            # 정상 반응 - 반응 시간 측정
            reaction = (time.time() - game_state['start_time']) * 1000  # ms로 변환
            game_state['reaction_time'] = round(reaction, 2)
            game_state['status'] = 'result'
            led.off()
            
            # 타임아웃 타이머 취소
            if timeout_timer:
                timeout_timer.cancel()
            
            # 최고 기록 업데이트
            if game_state['best_score'] is None or reaction < game_state['best_score']: #None은 최초기록
                game_state['best_score'] = round(reaction, 2)
        
        elif game_state['status'] == 'waiting': #대기상태일 때
            # 너무 빨리 누름 (얼리 프레스)
            game_state['status'] = 'early_press'
            game_state['reaction_time'] = 0
            led.off()
            
            # 타임아웃 타이머 취소
            if timeout_timer:
                timeout_timer.cancel()

# 버튼 이벤트 연결
button.when_pressed = game_logic

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    """게임 시작"""
    global timeout_timer
    
    with state_lock:
        # waiting 상태가 유지되는지 확인 (얼리 프레스로 취소되지 않았는지)
        if game_state['status'] != 'ready':
            return jsonify({'error': '게임이 이미 진행중입니다'}), 400
        
        game_state['status'] = 'waiting'
        game_state['reaction_time'] = 0
        game_state['start_time'] = 0
    
    def delayed_led():
        global timeout_timer
        
        # 1~4초 사이 랜덤 대기
        delay = random.uniform(1, 4) #일양분포
        time.sleep(delay)

        
        with state_lock:
            # waiting 상태가 유지되는지 확인 (얼리 프레스로 취소되지 않았는지)
            if game_state['status'] == 'waiting':
                led.on()
                game_state['start_time'] = time.time()
                game_state['status'] = 'measuring'
        
        # 타임아웃 설정 (5초)
        def handle_timeout():
            with state_lock: #with구문 close() 안써도 자동으로 close됨
                if game_state['status'] == 'measuring':
                    led.off()
                    game_state['status'] = 'timeout'
                    game_state['reaction_time'] = 0
        
        timeout_timer = threading.Timer(5.0, handle_timeout) #5초 후 타임아웃 함수 실행
        timeout_timer.start() #시작 조절은 바로위에서.
    
    thread = threading.Thread(target=delayed_led) #88번라인 delayed_led()와 연동
    thread.daemon = True #daemon 스레드로 설정(백그라운드에서 주 스레드를 보조(종속됨. 메인스레드가 먼저 죽지않는것을 보증), 메인 스레드 종료시 같이 종료) 시작하려면 start()써야함
                            #자바도 join으로 비슷한게 있음
                            #코틀린 코루틴 launch(Dispatchers.Default) 이런식으로 백그라운드 스레드 실행 가능
    thread.start()
                            #코틀린이라고 경량 스레드같은게 있는데 (생명주기영어)기능이 있는데 그게 비동기
    
    return jsonify({'message': '준비... LED가 켜지면 버튼을 누르세요!'})

@app.route('/status')
def get_status():
    """현재 상태 반환"""
    with state_lock: #권한을 획득한 스레드라고 하면 status은 (위에있는거라생략) reaction_time은 반응시간, best_score는 최고기록이 담김
        return jsonify({
            'status': game_state['status'],
            'reaction_time': game_state['reaction_time'],
            'best_score': game_state['best_score']
        })

@app.route('/reset', methods=['POST'])
def reset_game():
    """게임 리셋"""
    global timeout_timer
    
    # 타임아웃 타이머 취소
    if timeout_timer:
        timeout_timer.cancel()
    
    led.off()
    
    with state_lock:
        game_state['status'] = 'ready'
        game_state['reaction_time'] = 0
        game_state['start_time'] = 0
    
    return jsonify({'message': '리셋 완료'}) #json로 응답

if __name__ == '__main__':
    try:
        # 재시작 방지 및 프로덕션 모드
        # import os
        # os.environ['WERKZEUG_RUN_MAIN'] = 'true'
        print("반응속도 게임 서버 시작...")
        print("http://0.0.0.0:5000 접속하세요")
        app.run(host='0.0.0.0', port=5000, use_reloader=False)
    except KeyboardInterrupt:
        print("\n서버를 종료합니다...")
    finally:
        led.off()
        print("GPIO 정리 완료")