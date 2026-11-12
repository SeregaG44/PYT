# and or

# text = "name"
# name = "Jhon"
#
# print(text)
# print(name)

# відвідати клуб можна лише якщи ви повнолітні та маєте квиток

# age = 20
# has_ticket = input("чи маєте ви квиток? ")
#
# if age >= 18 and has_ticket == "так":
#     print("Прохід дозволено")
# else:
#     print("Прохід заборонено")

# визанчіть чи є день тижня вихідним чи буднем

# day = "понеділок"
#
# # умова1 and умова2
# # умова1 or умова2
# # if day == "субота" or day == "неділя":
# #     print("вихідний")
# # else:
# #     print("будень")
#
# # неправильно
# if day == "субота" or "неділя":
#     print("вихідний")
# else:
#     print("будень")


# перетворення типів

# text = "3.5"
# num = float(text)
#
# print(num + 1)

# перетворення в тип даних bool

# text = "3.5"
# cond = bool(text)
#
# print(cond)

# # 0 -- False, всі інші числа -- True
# print(f"{bool(0) = }")
# print(f"{bool(1) = }")
# print(f"{bool(-5) = }")
# print(f"{bool(3.5) = }")
# print(f"{bool(0.45645) = }")
#
# # прожоній рядок -- False, якщо є якісь символи -- True
# print(f"{bool('') = }")
# print(f"{bool(' ') = }")
# print(f"{bool('f') = }")
# print(f"{bool('hello') = }")
# print(f"{bool('False') = }")
#
# day = "понеділок"
#
# if day == "субота" or day == "неділя":
#     print("вихідний")
# else:
#     print("будень")

# is_weekend = day == "субота" or day == "неділя"
#
# if age > 18 and is_weekend
#
# if day == "понеліок" or day == "вівторок" or day == "середа" ..


# по номеру місяця вивести пору року

month_num = 8


# зиму
if month_num == 12 or month_num == 1 or month_num == 2:
    print("зима")

elif month_num >= 3 and month_num <= 5:
    print("весна")

elif month_num >= 6 and month_num <= 8:
    print("літо")

else:
    print("осінь")

# для діапазонів є скорочення

if month_num == 12 or month_num == 1 or month_num == 2:
    print("зима")

elif 3 <= month_num <= 5:
    print("весна")

elif 6 <= month_num <= 8:
    print("літо")

else:
    print("осінь")

