# week02_kiosk02
# Americano : 2000, Cafe latte : 3000
while True:
    menu = input("1) Americano  2) Cafe latte  3) Exit : ")
    if menu == "1":
        print("Americano ordered. Price : 2000")
    elif menu == "2":
        print("Cafe latte ordered. Price : 3000")
    elif menu == "3":
        print("Finish order!")
        break