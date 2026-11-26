# 1 Створіть список чисел [1, 8, -5, 9]
# ● Виведіть на екран елементи цього списку
# ● Збільшіть кожне число в 3 рази та виведіть результат
# ● Замініть усі числа більші 10 на 0 та виведіть результат

# num = [1, 8, -5, 9]
# print(num)
# for i in range(len(num)):
#    num[i] *= 3

#    if num[i] > 10:
#        num[i] = 0
#        print(f"{num =}")


# 2 Користувач вводить числа, поки не введе -1. Збережіть усі ці
# числа в список. Виведіть їхню кількість, суму, мінімальне, максимальне та середнє.
# Скористайтесь функціями min, max, sum, len

# numbers = []
# while True:
#    num = int(input("Введіть число: "))

#    if num == -1:
#        break

#    numbers.append(num)
#    print(
#        f"Кількість: {len(numbers)}, Сума: {sum(numbers)}, Мін: {min(numbers)}"
#        f", Макс: {max(numbers)}, Середнє:{sum(numbers) / len(numbers)}"
#    )


# 3 Користувач вводить числа, поки не введе 0. Створіть
# два нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.
# Виправіть помилку в коді

# positive = []
# negative = []

# while True:
#    number = int(input("Введіть число (0 для завершення): "))

#    if number > 0:
#        positive.append(number)
#        print("Додатні числа:", positive)

#    elif number == 0:
#        break

#    else:
#        negative.append(number)
#        print("Від'ємні числа:", negative)


# 4 Користувач вводить зарплати співробітників, поки не
# введе -1. Після чого вводить відсоток на який треба
# збільшити усім зарплату.
# Виведіть нові зарплати

salaries = []
while True:
    salarie = int(input("Ведіть зарплати: "))

    if salarie == -1:
        break
    salaries.append(salarie)

salary_percentage = int(input("Введіть % збільшення ЗП: "))

for i in range(len(salaries)):
    salaries[i] = salaries[i] * (1 + salary_percentage / 100)
print(f"{salaries = }")
