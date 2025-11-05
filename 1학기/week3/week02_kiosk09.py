# week02_kiosk09
total_price = 0  # 총 금액
drinks = ["Espresso", "Cafe latte", "Hot choco"]  # 음료 리스트
prices = [2200, 3500, 3800]  # 가격 리스트
amounts = [0, 0, 0]  # 수량
while True:
    menu = input(f"1) {drinks[0]} {prices[0]} won 2) {drinks[1]} {prices[1]} won 3) {drinks[2]} {prices[2]} won 4) Exit : ")
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

# print(f"{drinks[0]} x{amounts[0]}")
# print(f"{drinks[1]} x{amounts[1]}")
# print(f"{drinks[2]} x{amounts[2]}")
for i in range(len(drinks)):
    if amounts[i] != 0:
        print(f"{drinks[i]} x{amounts[i]}")

print(f"Total price : {total_price} won")
