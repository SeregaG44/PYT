# 1 Користувач вводить число від 1 до 9. Потрібно вивести
# для цього числа таблицю множення.
# Наприклад для 5 це буде:
# 1х5=5
# 2х5=10
# …
# 9х5=45
# 10х5=50
# Якщо користувач ввів неправильне число то
# продовжувати запитувати поки не введе правильне.



#while True:
#    number = int(input("Введіть число від 1 до 9: "))

#    if number <= 0 or number >= 10:
#        print("ви ввели неправильне число")
#        continue

#    for step in range(1, 11):
#        result = number * step
#        print(f"{step} х {number}= {result}")
#    break



#2 Користувач вводить свої оцінки поки не введе 0.
# Після чого програма виводить середню оцінку.
#Виправіть помилку в коді

#total = 0
#count = 0

#while True:
#    grade = int(input("Введіть оцінку: "))

#    if grade == 0:
#        break

#    count += 1
#    total += grade
#    average_grade = total / count

#print(f"середня оцінка: {average_grade}")


# 3 Напишіть простий калькулятор
# Користувач вводить два числа після чого обирає яку дію виконати:
# 1. сума
# 2. різниця
# 3. добуток
# 4. частка
# 5. вихід
# Якщо користувач обрав частку, то переконайтесь що не буде ділення на 0.
# У випадку проблеми виведіть відповідне повідомлення.


#number1 = int(input("ведіть перше число: "))
#number2 = int(input("ведіть друге число: "))

#while True:
#    print("1. сума")
#    print("2. різниця")
#    print("3. добуток")
#    print("4. частка")
#    print("5. вихід")

#    function = int(input("Введіть номер функції: "))

#    if function == 5:
#        print("Програма завершена")
#        break

#    if function == 1:
#        sum = number1 + number2
#        print(f"{number1} + {number2} = {sum:.2f}")
#        break

#    if function == 2:
#        sum = number1 - number2
#        print(f"{number1} - {number2} = {sum:.2f}")
#        break

#    if function == 3:
#        sum = number1 * number2
#        print(f"{number1} х {number2} = {sum:.2f}")
#        break

#    if function == 4:
#        if number2 == 0:
#            print("ділити на 0 не можна")
#            print()
#            continue

#        sum = number1 / number2
#        print(f"{number1} / {number2} = {sum:.2f}")
#        break


#4 Програма повинна зареєструвати рівно 3 учасників.
# Для цього користувач вводить їхні імена, але ім’я admin уже зайняте.
#Виправіть помилку в коді

#i = 0

#while i < 3:

#    name = input("Введіть ім'я: ")
#    i += 1

#    if name == "admin":
#        i -= 1
#        print("Це ім'я недоступне")
#        continue

#    print(f"Учасник №{i}: {name}")


#4 4 Напишіть гру «Вгадай число».
#Користувач має відгадати число від 0 до 100. Коли користувач пропонує власне число,
# програма має вивести одне з повідомлень:
#● Замало
#● Забагато
#● Ви вгадали(кінець програми)
#Після того як користувач відгадав число треба показати скільки у нього пішло на це спроб.
#Також якщо користувач вводить замість числа слово stop, програма показує число та
# кількість спроб і припиняє роботу.
#Для того щоб згенерувати випадкове число на початку програми напишіть

#import random
#attempt = 0
#secret_num = random.randint(0, 100)
#while True:
#    guess_number = int(input("Вгадай число від 0 до 100: "))


#    if guess_number < secret_num:
#        print("Замало")
#        attempt += 1

#    if guess_number > secret_num:
#        print("Забагато")
#        attempt += 1

#    if guess_number == secret_num:
#        print(f"Ви вгадали за {attempt} спроб")
#        break



# 5 Напишіть гру «Камінь, ножиці, папір»
# Спочатку користувач пропонується вибір:
# 1. Нова гра
# 2. Вихід
# Якщо вибрана нова гра, то користувач вводить кількість раундів.
# На кожному раунді користувач вводить одне зі слів: «камінь», «ножиці» або «папір». Якщо користувач вводить щось інше, зарахуйте це як програш в раунді.
# Коли всі раунди закінчились потрібно вивести кількість перемог, програшів та нічиї.
# Щоб згенерувати вибір комп’ютера використайте такий код

#import random

#print("1. Нова гра")
#print("2. Вихід")
#print()

#while True:

#    new_game = input("Зробить свій вибір: ")

#    if new_game == "2":
#        print("Вихід")
#        break

#    if new_game != "1":
#        print("Ви ввели невірну команду ")
#        continue

#    round = int(input("Введіть кількість раундів: "))

#    counter_guessed = 0   # перемога
#    counter_incorrect = 0 # програш
#    counter_draw = 0      # ніч'я

#    for num in range(0, round):
#       game = input("камінь, ножиці, папір: ")
#        computer_choice = random.choice(["камінь", "ножиці", "папір"])

#        if game == computer_choice:
#            counter_draw += 1

#        elif game == "камінь" and computer_choice == "ножиці":
#            counter_guessed += 1

#        elif game == "камінь" and computer_choice == "папір":
#            counter_incorrect += 1

#        elif game == "ножиці" and computer_choice == "камінь":
#            counter_incorrect += 1

#        elif game == "ножиці" and computer_choice == "папір":
#            counter_guessed += 1

#        elif game == "папір" and computer_choice == "камінь":
#            counter_guessed += 1

#        elif game == "папір" and computer_choice == "ножиці":
#            counter_incorrect += 1

#        else:
#            counter_incorrect += 1

#   print(f"Кількість перемог: {counter_guessed}, \nКількість програшів: {counter_incorrect}, \nНіч'я: {counter_draw}")
#   break



# 6 Змініть завдання 5 так, щоб на можна було грати декілька ігор.
# Для цього програма пропонує вибір:
# 1. Нова гра
# 2. Вихід

import random

print("1. Нова гра")
print("2. Вихід")
print()

while True:

    new_game = input("Зробить свій вибір: ")

    if new_game == "2":
        print("Вихід")
        break

    if new_game != "1":
        print("Ви ввели невірну команду ")
        continue

    round = int(input("Введіть кількість раундів: "))

    counter_guessed = 0   # перемога
    counter_incorrect = 0 # програш
    counter_draw = 0      # ніч'я

    for num in range(0, round):
        game = input("камінь, ножиці, папір: ")
        computer_choice = random.choice(["камінь", "ножиці", "папір"])

        if game == computer_choice:
            counter_draw += 1

        elif game == "камінь" and computer_choice == "ножиці":
            counter_guessed += 1

        elif game == "камінь" and computer_choice == "папір":
            counter_incorrect += 1

        elif game == "ножиці" and computer_choice == "камінь":
            counter_incorrect += 1

        elif game == "ножиці" and computer_choice == "папір":
            counter_guessed += 1

        elif game == "папір" and computer_choice == "камінь":
            counter_guessed += 1

        elif game == "папір" and computer_choice == "ножиці":
            counter_incorrect += 1

        else:
            counter_incorrect += 1

    print(f"Кількість перемог: {counter_guessed}, \nКількість програшів: {counter_incorrect}, \nНіч'я: {counter_draw}")









