margarita = 150
pepperoni = 180
four_cheeses = 200
check = 0
goods = ""

print("1. Вибрати піцу")
print("2. Показати вміст заказу")
print("3. Вихід")

while True:
    menu = int(input("Ведіть команду (1, 2 чи 3): "))

    if menu == 1:
        print("Маргарита – 150 грн, \nПепероні – 180 грн, \nЧотири сири – 200 грн")
        pizza_name = input("Яку піцу Ви бажаєте: ")

        if pizza_name == "Маргарита":
            price = margarita

        elif pizza_name == "Пепероні":
            price = pepperoni

        elif pizza_name == "Чотири сири":
            price = four_cheeses

        else:
            price = None
            print("Такої піци нажаль нема")

        if price is not None:
            pizzas_number = int(input("яку кількість Ви бажаєте: "))
            item_total = price * pizzas_number
            check += item_total
            goods += f"• {pizza_name}       {pizzas_number} шт.     {price} грн\n"

            print(
                f"Замовлено піцу: {pizza_name}, {pizzas_number} шт ({item_total} грн)\n"
            )

    elif menu == 2:
        print("========== ВАШЕ ЗАМОВЛЕННЯ ==========")
        print()
        print("Піца     Кількість       Вартість")
        print("--------------------------------------")

        if goods == "":
            print("Ваш кошик порожній.")

        else:
            print(goods.strip())
            print()
            print("--------------------------------------")
            print(f"Загальна вартість: {check} грн")
            print("======================================")
            print("Дякуємо за замовлення!")

    else:
        print("До зустрічі!")
        break
