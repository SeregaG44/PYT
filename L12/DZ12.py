# 1

# text = input("Введіть рядок англійською мовою: ")

# count = 0
# vowels = "aeiou"

# for letter in text:
#    if letter in vowels:
#        count += 1

# print(f"Кількість голосних літер: {count}")


# 2 Користувач вводить текст.
# Після чого запускається цикл і користувач вводить певне слово.
# Треба це слово в тексті замінити на верхній регістр.
# Цикл закінчується коли введено EXIT


# text = input("Введіть текст: ")

# while True:
#    word = input("Введіть слово: ")
#    if word == "EXIT":
#        print("До побачення")
#        break

#    if word != "EXIT":
#        upper_word = word.upper()
#        new = text.replace(word, upper_word)
#        print(f"{new}")


# 3 Користувач вводить текст. Порахуйте скільки в ньому речень

text = input("Введіть текст: ")

symbol = ".?!"
count = 0

for char in text:
    if char in symbol:
        count += 1

print(f"Кількість речень {count}")
