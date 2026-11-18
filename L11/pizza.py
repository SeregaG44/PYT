margarita = 150
pepperoni = 180
four_cheeses = 200
check = 0
goods = ""

print("1. Вибрати піцу")
print("2. Вихід")

while True:
    menu = int(input("Ведіть команду (1/2): "))

    if menu == 1:
        print("Маргарита – 150 грн, \nПепероні – 180 грн, \nЧотири сири – 200 грн")
        pizza_name = input("Яку піцу Ви бажаєте: ")

        if (
            pizza_name == "Маргарита"
            or pizza_name == "Пепероні"
            or pizza_name == "Чотири сири"
        ):
            pizzas_number = int(input("яку кількість Ви бажаєте: "))
            print(f"Замовлено піцу: {pizza_name}, {pizzas_number} шт")

        else:
            print("Такої піци нажаль нема")

    else:
        print("До зустрічі!")
        break
