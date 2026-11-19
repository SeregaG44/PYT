text = input("ведіть текст: ")
symbol = input("Введіть символ: ")
count = 0
# count = text.count(symbol)

# print(f"символ зустрічається {symbol} разів {count}")

for char in text:
    if char == symbol:
        count += 1
print(f"символ зустрічається {symbol} разів {count}")
