# week02_kiosk04
# Americano : 2000, Cafe latte : 3000
total_price = 0
while True:
    menu = input("1) Americano 2000 won 2) Cafe latte 3000 won 3) Exit : ")
    if menu == "1":
        print("Americano ordered. Price : 2000 won")
        total_price = total_price + 2000
    elif menu == "2":
        print("Cafe latte ordered. Price : 3000 won")
        total_price = total_price + 3000
    elif menu == "3":
        print("Finish order!")
        break
print(f"Total price : {total_price} won")
