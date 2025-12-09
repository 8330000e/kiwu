# week02_kiosk06
# Americano : 2000, Cafe latte : 3000
total_price = 0
drinks = ["Canadiano", "Cafe latte"]
prices = [2200, 3500]
while True:
    menu = input(f"1) {drinks[0]} {prices[0]} won 2) {drinks[1]} {prices[1]} won 3) Exit : ")
    if menu == "1":
        print(f"{drinks[0]} ordered. Price : {prices[0]} won")
        total_price = total_price + prices[0]
    elif menu == "2":
        print(f"{drinks[1]} ordered. Price : {prices[1]} won")
        total_price = total_price + prices[1]
    elif menu == "3":
        print("Finish order!")
        break
print(f"Total price : {total_price} won")
