print("1. Вибрати піцу")
print("2. Вихід")

while True:
    menu = int(input("Ведіть команду (1/2): "))

    if menu == 1:
        pizza_name = input("Яку піцу Ви бажаєте: ")
        pizzas_number = int(input("яку кількість Ви бажаєте: "))
        print(f"Замовлено піцу: {pizza_name}, {pizzas_number} шт")

    else:
        print("До зустрічі!")
        break
