# week03_kiosk23
total_price = 0  # 총 금액
drinks = ["Espresso", "Cafe latte", "Hot choco", "Plain smoothie"]  # 음료 리스트
prices = [2200, 3500, 3800, 5000]  # 가격 리스트
# drinks = ["Espresso", "Cafe latte"]  # 음료 리스트
# prices = [2200, 3500]  # 가격 리스트
# 수량
amounts = [0] * len(drinks)  # 파이썬 곱셈을 이용해서 해결 (내부 최적화)
# 디스플레이 메뉴
menu_texts = ''.join([f"{j+1}) {drinks[j]} {prices[j]} won " for j in range(len(drinks))])
menu_texts = menu_texts + f" {len(drinks)+1}) Exit : "

def order_process(idx):
    global total_price  # order_process 함수 바깥 쪽에 선언되어 있는 total_price 전역 변수를 참조하기 위해 사용
    print(f"{drinks[idx]} ordered. Price : {prices[idx]} won")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1


while True:
    try:
        menu = int(input(menu_texts))
        if len(drinks) >= menu >= 1:
            order_process(menu - 1)
        elif menu == len(drinks) + 1:
            print("Finish order!")
            break
        else:
            print(f"{menu} is not available menu. Please choose from the above menu.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"Product        Price  Amount  Subtotal")
for i in range(len(drinks)):
    if amounts[i] > 0:  # if amounts[i] != 0:
        print(f"{drinks[i]:15} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]} won")
print(f"Total price : {total_price} won")
