# цикл for

# for house in 1,2,3:
#     print("листоноша прийшов")
#     print(f"Листи для будинку №{house}")
#     print()
#
# # теж саме але без циклу
#
#
# house = 1
# print("листоноша прийшов")
# print(f"Листи для будинку №{house}")
# print()
#
# house = 2
# print("листоноша прийшов")
# print(f"Листи для будинку №{house}")
# print()
#
# house = 3
# print("листоноша прийшов")
# print(f"Листи для будинку №{house}")
# print()


# щоб легко задати послідовнфсть є функція range

# range(stop) -- 0, 1 2 ... stop-1 (очаток з 0, кінець не включно)

# for num in range(5):
#     print(num)

# range(start, stop) -- start, start+1, ... stop-1(початок та кінець(невключно діапазону)

# for num in range(10, 20):
#     print(num)

# range(start, stop, step) -- початок start, кінець(невключно) stop, крок step

# for num in range(10, 20, 3):
#     print(num)

# num = -1
#
# for num in range(5):  # 0 1 2 3 4
#     print()
#
# num = 0
# print()
#
# num = 1
# print()
#
# num = 2
# print()
#
# num = 3
# print()
#
# num = 4
# print()
#
# print(num)


# # задом наперед
# for num in range(5, 0, -1):
#     print(num)


# порахувати суму чисел та їхню кількість

# # змінні для суми та кількості
# total = 0
# count = 0
#
# # цикл
# for number in range(10, 20):
#     #price = int(input("ведіть ціну товару: "))
#
#     total += number
#     count += 1
#
#
# print(f"сума {total}")
# print(f"кількість {count}")


# # користувач сам вводіть кількість кіл в циклі
# count = int(input("Скільки разів вивести фразу hello: "))
# step = int(input("Крок"))
#
# for num in range(0, count, step):
#     print("hello", num)
