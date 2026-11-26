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

# salaries = []
# while True:
#    salarie = int(input("Ведіть зарплати: "))

#    if salarie == -1:
#        break
#    salaries.append(salarie)

# salary_percentage = int(input("Введіть % збільшення ЗП: "))

# for i in range(len(salaries)):
#    salaries[i] = salaries[i] * (1 + salary_percentage / 100)
# print(f"{salaries = }")


# 5 Користувач вводить кількість днів, після чого
# температуру повітря кожного дня.
# Збережіть температури у список
# Для кожного дня порахуйте різницю температур з
# попереднім днем.

# temperatures = []
# days = int(input("Введіть кількість днів: "))

# for i in range(days):

#    temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
#    temperatures.append(temperature)

# print("Температури:", temperatures)

# for i in range(days):
#    difference = temperatures[i] - temperatures[i - 1]
#    print(f"Різниця температур за {i + 1}-й день: {difference}")


# 6 Створіть застосунок банк. Є список з рахунками клієнтів.
# Користувач вибирає одну з команд
# ● Додати клієнта
# ● Видалити клієнта
# ● Поповнити рахунок
# ● Зняти кошти
# ● Вихід
# При додаванні клієнта, добавте рахунок в 0грн в кінець списку.
# В інших випадках запросіть ID(індекс) клієнта і якщо він вірний, то проведіть операцію

print("1 - Додати клієнта")
print("2 - Видалити клієнта")
print("3 - Поповнити рахунок")
print("4 - Зняти кошти")
print("5 - Вихід")

clients = []
checks = []

while True:
    menu = int(input("Введіть команду (1-5): "))
    if menu == 1:
        client = input("Введіть ім'я клієнта: ")
        clients.append(client)
        checks.append(0)

    elif menu == 2:
        client = input("Введіть ім'я клієнта: ")
        clients.pop(client)
        checks.pop(0)

    elif menu == 3:
        client = input("Введіть ім'я клієнта: ")
        if client in clients:
            idx = clients.index(client)
            amount = int(input("Введіть суму: "))
            checks[idx] += amount
            print(f"Рахунок: {client}, поповнено {amount}, Cума рахунку: {checks[idx]}")

    elif menu == 4:
        client = input("Введіть ім'я клієнта: ")
        if client in clients:
            idx = clients.index(client)
            amount = int(input("Введіть суму: "))
            checks[idx] -= amount
            print(f"Рахунок: {client}, знято {amount}, Cума рахунку: {checks[idx]}")

    else:
        print("Вихід")
        break
