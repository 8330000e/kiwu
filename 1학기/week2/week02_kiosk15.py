# week02_kiosk14
total_price = 0  # 총 금액
drinks = ["Espresso", "Cafe latte", "Hot choco", "Plain smoothie"]  # 음료 리스트
prices = [2200, 3500, 3800, 5000]  # 가격 리스트
# 수량
# amounts = [0 for _ in range(len(drinks))]  # list comprehension
amounts = list()
menu_texts = ''
for j in range(len(drinks)):
    amounts.append(0)
    menu_texts = menu_texts + f"{j+1}) {drinks[j]} {prices[j]} won "
menu_texts = menu_texts + f" {len(drinks)+1}) Exit : "
print(amounts)

while True:
    menu = input(menu_texts)
    if menu == "1":
        print(f"{drinks[0]} ordered. Price : {prices[0]} won")
        total_price = total_price + prices[0]
        amounts[0] = amounts[0] + 1
    elif menu == "2":
        print(f"{drinks[1]} ordered. Price : {prices[1]} won")
        total_price = total_price + prices[1]
        amounts[1] = amounts[1] + 1
    elif menu == "3":
        print(f"{drinks[2]} ordered. Price : {prices[2]} won")
        total_price = total_price + prices[2]
        amounts[2] = amounts[2] + 1
    elif menu == "4":
        print("Finish order!")
        break

print(f"품명 단가 수량 소계")
for i in range(len(drinks)):
    if amounts[i] != 0:
        print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]} won")
print(f"Total price : {total_price} won")
