# 1

# text = input("ведіть текст: ")
# symbol = input("Введіть символ: ")
# count = 0
# count = text.count(symbol)

# print(f"символ зустрічається {symbol} разів {count}")

# for char in text:
#    if char == symbol:
#        count += 1
# print(f"символ зустрічається {symbol} разів {count}")


# 2

# text = input("ведіть текст: ")

# count_text = len(text)
# print(f"\nкількість символів: {count_text}")

# if "python" in text.lower():
#    print("слово python присутьнє")

# else:
#    print("слово python немає")

# count_szh = 0
# for char in text.lower():
#    if char in "szh":
#        count_szh += 1

# print(f"символ зустрічається s, z, h: \nразів {count_szh}")


# 3

# text = input("Введіть текст: ")

# result = text.replace(" ", "-")
# print(f"Змінений текст: {result}")


# 4

# text = input("ведіть текст: ")
# word = input("Введіть слово: ")
# count = 0

# count = text.count(word)

# print(f"Cлово: {word} \nзустрічається: {count} разів")


# 5

# items = input("Введіть ваші речі: ")
# items = items.lower()

# if "ніж" in items or "гроші" in items or "отрута" in items:
#    print("У вас є речі які заборонено перевозити")

# else:
#    print("Оформлено доставку")


# 6

# text = input("ведіть текст: ")
# count_letters = 0
# count_digits = 0

# for ch in text:
#    if ch.isdigit():
#        count_digits += 1

#    else:
#        count_letters += 1

# print(f"Кількість цифр: {count_digits} \nКількість літер: {count_letters}")


# 7

print("Правильний пароль повинен:")

print("Бути довшим за 8 символів")
print("Містити хоча б одну цифру")
print("Містити хоча б одну літеру")
print()

while True:
    password = input("Задайте новий пароль: ")
    length = len(password)
    count_letters = 0
    count_digits = 0

    for ch in password:
        if ch.isdigit():
            count_digits += 1
        else:
            count_letters += 1

    if length > 8 and count_digits >= 1 and count_letters >= 1:
        print("Ви ввели вірний пароль")
        break

    if length < 8:
        print("Пароль повинен бути довшим за 8 символів ")

        continue

    if count_digits == 0:
        print("Пароль повинен містит хоча б онду цифру ")

        continue

    if count_letters == 0:
        print("Пароль повинен містит хоча б онду літеру ")

        continue

    else:
        print("Пароль повинен бути довшим за 8 символів ")
