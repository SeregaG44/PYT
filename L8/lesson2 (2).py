# цикл while


# water = 0
# while water < 200:
#     user_water = int(input("Скільки води наллєте: "))
#     water += user_water
#
#     print(f"{water = }")
#     print(f"{water < 200 = }")
#     print()
#
# print("цикл закінчтвся")
# print(f"{water < 200 = }")


# цикл ніколи не закінчиться

# water = 0
# while water < 200:
#     water -= 50
#
#     print(f"{water = }")
#     print(f"{water < 200 = }")
#     print()


# спецаільно нескінченний цикл

# while True:
#     print("цей цикл працює вічно")
#
#     # якщо тут можна перевірити чи треба зупинити цикл то робимо тут


# while True:
#     key = input("Знайшли ключі так/ні: ")
#
#     if key == "так":
#         break  # зупиняємо цикл
#
#     print("Продовжуємо шукати")
#
# print("Пошук завершено")


# # піжрахунок кілометраж
# total_dist = 0
#
# while True:
#     is_driven = input("Чи їде автомобіль: ")
#
#     if is_driven == "ні":
#         # автомобіль зупинено
#         break
#
#     # запитуємо скільки проїхали км
#     dist = int(input("Скільки проїхали кілометрів: "))
#
#     # додаємо до загальної кількість проїханих кілометрів
#     total_dist += dist
#
#     print(f"Ви проїхали {total_dist} км")
#     print()


# break може бути в середині вкладених if elif else
# while True:
#     key = input("Знайшли ключі так/ні: ")
#
#     if key == "так":
#         is_sure = input("Ви впевнені: ")
#
#         if is_sure == "так":
#             break
#
#     print("Продовжуємо шукати")
#
# print("Пошук завершено")


# while True:
#     key = input("Знайшли ключі так/ні: ")
#
#     if key == "так":
#         break
#
#     print("Продовжуємо шукати")
#
# print("Пошук завершено")


# while True:
#     if time_left <= 0:
#         print("Кінець зміни")
#         break
#
#     if boss == "так":
#         print("Прийшов бос")
#         break
#
#     if guests <= 0:
#         print("Всі гості вийшли")
#         break



# перевірка чи ввів користувач щось правильно
# так/ні

# просимо вводити поки не введе правильно
while True:
    answer = input("Ввеідть так/ні ")

    # коли закінчуємо цикл
    if answer == "так" or answer == "ні":
        break

    print("Вивели неправильну відповідь")

print(f"Ввели {answer}")
