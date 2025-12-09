# week02_kiosk07
# Americano : 2000, Cafe latte : 3000
total_price = 0  # 총 금액
order_list = ''  # 주문 목록
drinks = ["Canadiano", "Cafe latte"]  # 음료 리스트
prices = [2200, 3500]  # 가격 리스트
while True:
    menu = input(f"1) {drinks[0]} {prices[0]} won 2) {drinks[1]} {prices[1]} won 3) Exit : ")
    if menu == "1":
        print(f"{drinks[0]} ordered. Price : {prices[0]} won")
        total_price = total_price + prices[0]
        order_list = order_list + drinks[0] + '\n'
    elif menu == "2":
        print(f"{drinks[1]} ordered. Price : {prices[1]} won")
        total_price = total_price + prices[1]
        order_list = order_list + drinks[1] + '\n'
    elif menu == "3":
        print("Finish order!")
        break
print(order_list)
print(f"Total price : {total_price} won")
