# 1 Користувач вводить рядок та індекс. Виведіть символ під цим індексом.
# Якщо індекс завеликий, виведіть інформацію про помилку.

# text = input("Ведіть текст: ")
# index = int(input("Введіть індекс: "))

# if index < 0 or index >= len(text):
#    print("індекс не відповідає тексту")

# else:
#    print(text[index])


# 2 Користувач вводить рядок та два індекси. Виведіть зріз рядка.
# Виправіть помилку в коді

# text = input("Введіть рядок: ")

# start = int(input("Введіть початковий індекс: "))
# end = int(input("Введіть кінцевий індекс: "))

# segment = text[start:end]

# print(segment)


# 3 Користувач вводить рядок та число n. Виведіть перші n символів.
# Також виведіть останні n символів.

# text = input("Введіть рядок: ")
# start = int(input("Введіть індекс: "))

# segment_start = text[:start]
# segment_end = text[-start:]

# print(segment_start)
# print(segment_end)


# 4 Користувач вводить рядок. Перевірте чи це
# речення(закінчується на .!?)

# text = input("Введіть рядок: ")
# symbols = ".!?"

# if text and text[-1] in symbols:
#    print("Це речення")

# else:
#    print("Це не речення")


# 5 Користувач вводить рядок. Перевірте чи перший
# символ – це велика літера. Виправіть помилку в коді

# text = input("Введіть рядок: ")

# if text[0].isupper():
#    print(f"Перший символ — велика літера {text}")
# else:
#    print("Перший символ — не велика літера")


# 6 Користувач вводить рядок. Перевірте чи це
# паліндром(читається задом наперед так само).
# Приклади: Кіт утік, око, потоп

# text = input("Введіть рядок: ").lower()

# cleaned = text.replace(" ", "")

# if cleaned == cleaned[::-1]:
#    print(f"Це паліндром {text}")
# else:
#    print("Це не поліндром")


# 7 Користувач вводить рядок та символ. Виведіть індекс
# цього символу.

# text = input("Введіть рядок: ").lower()
# symbols = input("Введіть символ: ")

# if symbols in text:
#    print(f"Символ: {symbols}, Індекс = {text.index(symbols)}")

# else:
#    print("Такого символу немає")


# 8 Користувач вводить рядок та символ. Виведіть усі
# індекси цього символу, якщо він зустрічається декілька
# разів.

# text = input("Введіть рядок: ").lower()
# symbols = input("Введіть символ: ")
# found = False

# for i in range(len(text)):
#    if text[i] == symbols:
#        print(f"Символ: {text[i]}, Індекс: {i}")
#        found = True

# if not found:
#    print("Такого символу немає")


# 9 Користувач вводить слова поки не введе слово END.
# Збережіть це слово до одного з 4-ох рядків:
# ● герундій – закінчується на ing
# ● дієслово past tense – закінчується на ed
# ● починаються на голосну – aeuio
# ● решта

# gerund = ""
# past_tense = ""
# vowels = ""
# other = ""

# while True:
#    text = input("Введіть рядок: ").strip().lower()

#    if text == "end":
#        break

#    if text.endswith("ing"):
#        gerund += text + " "
#    elif text.endswith("ed"):
#        past_tense += text + " "
#    elif text[0] in "aeuio":
#        vowels += text + " "
#    else:
#        other += text + " "

# print(f"Це герундій: {gerund.strip()}")
# print(f"Це дієслово: {past_tense.strip()}")
# print(f"Починаються на голосну: {vowels.strip()}")
# print(f"Решта: {other.strip()}")


# 10 Користувач вводить математичний вираз, наприклад 23+45. Виведіть результат
# Обробіть такі математичні операції – +*/-
# Реалізуйте як консольну програму(закінчити якщо введено EXIT)

# while True:
#    calculator = input("Введіть математичний вираз: ")

#    if "+" in calculator:
#        a, b = calculator.split("+")
#        print(f"Результат: {float(a) + float(b)}")
#        print()

#    elif "-" in calculator:
#        a, b = calculator.split("-")
#        print(f"Результат: {float(a) - float(b)}")
#        print()

#    elif "*" in calculator:
#        a, b = calculator.split("*")
#        print(f"Результат: {float(a) * float(b)}")
#        print()

#    elif "/" in calculator:
#        a, b = calculator.split("/")
#        print(f"Результат: {float(a) / float(b)}")
#        print()

#    elif calculator == "EXIT":
#        print("EXIT")
#        break

#    else:
#        print("Невідома дія")


# 11 Користувач вводить текст та число. Зробіть циклічний зсув,
# тобто індекси всіх символів збільшуються на певне число,
# а символи з кінця опиняються спереду.
# Приклади
# abcde 1 – eabcd
# abcde 3 – cdeab
# abcde -1 – bcdea

# text = input("Введіть рядок: ").strip().lower()
# number = int(input("Введіть число: "))

# if len(text) > 0:
#    number = number % len(text)
#    numbers = text[-number:] + text[:-number]
#    print(f"{text}: зсув на {number} символів, результат: {numbers}")

# else:
#    print("результат")


# 12 Реалізуйте римське шифрування – кожен символ замінюється
# на інший, який знаходиться на певній відстані в алфавіті.
# Користувач вводить текст, число та пропонує зашифрувати або
# розшифрувати текст.
# Щоб отримати позицію в алфавіті – ord(letter)
# Щоб отримати символ за позицією – chr(num)


text = input("Введіть рядок: ").strip()
number = int(input("Введіть число: "))
shifr = int(input("Зашифрувати чи розшифрувати? (1/2): "))

if shifr == 2:
    number = -number

elif shifr != 1:
    print("Невідома дія, використовується шифрування")

result = ""

for char in text:
    if "a" <= char <= "z":
        base = ord("a")
        result += chr((ord(char) - base + number) % 26 + base)
    elif "A" <= char <= "Z":
        base = ord("A")
        result += chr((ord(char) - base + number) % 26 + base)
    else:
        result += char

print(f"Результат: {result}")
