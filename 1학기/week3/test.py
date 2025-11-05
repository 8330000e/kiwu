

# try:
#     number1 = int(input("분자 입력 : "))
#     number2 = int(input("분모 입력 : "))
#     print(number1 / number2)
#     subjects = ["자료구조", "파이썬", "Iot", "PHP"]
#     print(subjects[2])
#     print(subjects[6])  # ! 예외 발생
# except IndexError as err:
#     print("인덱스 범위를 벗어 났습니다.")
#     print(err)
# except ValueError:
#     print("문자는 입력할 수 없습니다. 입력 값은 숫자여야 합니다.")
# except ZeroDivisionError as err:
#     print(f"분모에 0이 올 수 없습니다 : {err}")


# subjects = ["자료구조", "파이썬", "Iot", "PHP"]
# print(subjects)
# # "자료구조 / 파이썬 / Iot / PHP"
# texts = " / ".join(subjects)
# print(texts)


# drinks = ["Espresso", "Cafe latte", "Hot choco", "Plain smoothie"]  # 음료 리스트
# prices = [2200, 3500, 3800, 5000]
# menu_texts = ''.join([f"{j+1}) {drinks[j]} {prices[j]} won " for j in range(len(drinks))])
# menu_texts = menu_texts + f" {len(drinks)+1}) Exit : "
# print(menu_texts)

# menu_texts = ''
# for j in range(len(drinks)):
#     menu_texts = menu_texts + f"{j+1}) {drinks[j]} {prices[j]} won "
# menu_texts = menu_texts + f" {len(drinks)+1}) Exit : "