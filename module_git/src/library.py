print("Вітаємо вас у нашій бібліотеці")
print("Гарного вам дня")

print("1. Отримати книжку")
print("2. Повернути книжку")
print("3. Вихід")

while True:
    menu = int(input("Введіть команду: "))

    if menu == 3:
        print("До нових зустрічей")
        break

    elif menu == 1:
        name = input("Введіть своє і'мя: ")
        book = input("Введіть назву книжки: ")

        if name == "":
            print("Введіть ім'я")

        if book == "":
            print("Введіть назву книги")

        days = int(input("на скільки днів? "))

        if days <= 0:
            print("Ви ввели від’ємну кількість днів ")

        elif days >= 31:
            print("Максимальний термін 30 днів")

        else:
            print(f"Книжку: {book}, видано читачеві: {name}, на {days} днів")

    elif menu == 2:
        name = input("Введіть своє і'мя: ")
        book = input("Введіть назву книжки: ")
        print(f"Читач {name} повернув книжку {book}")

    else:
        print("Виберіть 1, 2 чи 3: ")
