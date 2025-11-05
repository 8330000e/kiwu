# week02_kiosk05
# Americano : 2000, Cafe latte : 3000
total_price = 0
prices = [2200, 3500]
while True:
    menu = input(f"1) Americano {prices[0]} won 2) Cafe latte {prices[1]} won 3) Exit : ")
    if menu == "1":
        print(f"Americano ordered. Price : {prices[0]} won")
        total_price = total_price + prices[0]
    elif menu == "2":
        print(f"Cafe latte ordered. Price : {prices[1]} won")
        total_price = total_price + prices[1]
    elif menu == "3":
        print("Finish order!")
        break
print(f"Total price : {total_price} won")
