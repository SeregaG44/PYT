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

text = input("ведіть текст: ")
word = input("Введіть слово: ")
count = 0

count = text.count(word)

print(f"Cлово: {word} \nзустрічається: {count} разів")
