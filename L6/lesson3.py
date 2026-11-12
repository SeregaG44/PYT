# дз

# # if 2 + 2 == 4:
# #     print("yes")
# # else: print("no")
#
# # result = 10 if 2 + 2 == 4 else 0
# #
# if 2 + 2==4:
#         result = 10
# else:
#     result = 0
#
# # user_password
# # years



# є умови
# повнолітані
# дохід більще 10000
# немає судимостей

# ви пройшли якщо виконані хоча б 2 з 3 умов

# # лічильник виконаних умов
# cond_count = 0
#
# # дані
# age = 30
# income = 100_000
# has_criminal_record = False
#
# # рахуємо виконані умови
# if age > 18:
#     cond_count += 1
#
# if income > 10000:
#     cond_count += 1
#
# if not has_criminal_record:
#     cond_count += 1
#
#
# # перевіряємо скільки виконано умов
# if cond_count >= 2:
#     print("ви пройшли")
# else:
#     print("ви не пройшли")
#
# print(f"виконано {cond_count}")



# користувач замовляє морозиво
# 1 кулька морозива -- 20 грн
# можна купити сироп(за бажанням)
# карамельний -- 5 грн
# шоколадний -- 4 грн
# полуничний -- 7 грн

# Якщо замовили більше 3 кульки та
# з сиропом(один будь який) -- знижка 10%

# # константи(налаштування)
# BALL_PRICE = 30  # ціна однієї кільку
#
# SYRUP_CARAMEL = 5
# SYRUP_CHOCOLATE = 4
# SYRUP_STRAWBERRY = 7
#
# DISCOUNT_PERCENT = 10
#
#
# # введення дані
# ice_cream_balls = int(input("Скільки кульок морозива бажаєте? "))
# with_syrup = input("Чи бажаєте сироп(так/ні)? ")
#
# # уточнуємо який саме сироп
#
# # заглушка для змінної syrup щоб була в пам'яті комп'ютера
# syrup = None
# if with_syrup == "так":
#     syrup = input("Який сироп бажаєте(карамельний, шоколадний, полуничний)? ")
#
# # обрахунок ціни морозива
# # кульки
#
# total = ice_cream_balls * BALL_PRICE
#
# # сироп
# if syrup == "карамельний":
#     total += SYRUP_CARAMEL
# elif syrup == "шоколадний":
#     total += SYRUP_CHOCOLATE
# elif syrup == "полуничний":
#     total += SYRUP_STRAWBERRY
#
# # Якщо замовили більше 3 кульки та
# # з сиропом(один будь який) -- знижка 10%
# if with_syrup == "так" and ice_cream_balls >= 3:
#     discount = total / 100 * DISCOUNT_PERCENT
#     total -= discount
#
# # вивід результатів
# print(f"за {ice_cream_balls} кульок")
#
# if with_syrup == "так":
#     print(f"разом з {syrup} сиропом")
#
# print(f"з вас {total} грн")




#Користувач вводить свій вік.
# Якщо менше 18 років – вивести повідомлення «Надто малий»
# Інакше спитати чи є водійські права(відповідь так або ні).
# Якщо є -- вивести повідомлення «Можна водити авто», інакше
# – «Отримайте права»


# отримання даних
#age = int(input("Введіть ваш вік: "))

# if age < 18:  # неповнолітній
#     print("Надто малий")
#
# else:
#     # уточнуємо за водійські права
#     has_license = input("Чи є у вас водійські права(так/ні)? ")
#
#     if has_license == "так":
#         print("Можна водити авто")
#     else:
#         print("Отримайте права")

# теж саме тільки стартова умова age >= 18

#if age >= 18:
#    has_license = input("Чи є у вас водійські права(так/ні)? ")

#    if has_license == "так":
#        print("Можна водити авто")
#    else:
#        print("Отримайте права")

#else:
#    print("Надто малий")

is_raining = False

if not is_raining:
    print("Можна йти без парасолі")
else:
    print("Потрібна парасоля")
