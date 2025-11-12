#app(객체) = Flask(__name__)(생성자랑 이름)
#led_states라는 걸로 led들을 관리하겠다
#@app.route 웹페이지에 접근했을때 어떤 것을 보여줄거냐
#'/'는 root(최상위폴더)를 뜻함
#@=어노테이션 route(어디를보여줄지)
#return render_template('index.html', states=led_states) = index.html와 led_states를 보냄
#led_states에서 led1랑 led2의 값을 가진다고 바인딩했음
#다음 어노테이션route는 led 번호랑 그 상태 경로를 받음.
#그래서 접근하면 control_led 함수가 돌아감
#1번led가 켜져있으면 led_states['led1']에 1로 저장 꺼져있으면 0으로 저장
#아니면 led2 상태 저장
#다음 어노테이션은 모든 led의 상태 경로를 받음
#그리고 all_leds 함수가 돌아감
#led1,led2상태 저장하고 
#if __name__ == '__main__': <-제일 먼저 동작하는 부분
#

from flask import Flask, render_template, request, redirect, url_for
#import RPi.GPIO as GPIO
from gpiozero import LED

app = Flask(__name__)

# GPIO 설정
# GPIO.setmode(GPIO.BCM)
# LED1 = 20
# LED2 = 21

led1 = LED(20)
led2 = LED(21)

# GPIO.setup(LED1, GPIO.OUT)
# GPIO.setup(LED2, GPIO.OUT)

# LED 상태 저장
led_states = {'led1': 0, 'led2': 0}

@app.route('/')
def index():
    return render_template('index.html', states=led_states)

@app.route('/led/<int:led_num>/<int:state>')
def control_led(led_num, state):
    """개별 LED 제어"""
    if led_num == 1:
        #GPIO.output(LED1, state)
        if state == 1:
            led1.on()
        else:
            led1.off()
        led_states['led1'] = state
    elif led_num == 2:
        # GPIO.output(LED2, state)
        if state == 1:
            led2.on()
        else:
            led2.off()
        led_states['led2'] = state
    
    return redirect(url_for('index'))

@app.route('/all/<int:state>')
def all_leds(state):
    """모든 LED 동시 제어"""
    # GPIO.output(LED1, state)
    # GPIO.output(LED2, state)
    if state == 1:
        led1.on()
        led2.on()
    else:
        led1.off()
        led2.off()
    led_states['led1'] = state
    led_states['led2'] = state
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        #GPIO.cleanup()
        pass