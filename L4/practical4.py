#1 Користувач вводить час у хвилинах, виведіть скільки це
#секунд. Якщо введено від’ємне число виведіть
#повідомлення “Час має бути додатнім”

#user=int(input("Введіть час у хвилинах: "))

#second=user*60
#if second < 1:
#    print("Час має бути додатнім")
#else:
#    print("вийшло", second, "секунд")


#2 Напишіть програму для перевірки правильності паролю.
#Якщо користувач ввів правильний пароль то виведіть
#“Доступ дозволено” інакше “Доступ заблоковано”
#Правильний пароль secret_password = "OpenSesame123"

#password = str(input("Введіть пароль: "))
#secret_password = "OpenSesame123"
#is_password=False
#if password == "OpenSesame123":
#   is_password = True
#   print("Вірно")
#else:
#    is_password = False
#    print("Не вірний пароль")


#3 Користувач вводить довжину в метрах та в що їх
#перевести(сантиметри(см) чи кілометри(км))
#Напишіть програму яка переводить метри в бажану одиницю вимірювання.
#Якщо користувач ввів не см чи км то повідомте про помилку


#length_meters=int(input("Введіть довжину в метрах: "))
#convert_m = input("перевести у см чи км: ")
#if convert_m == "см":
#    length_sm = length_meters * 100
#    print(f"{length_meters} метрів це {length_sm} см")
#elif convert_m == "км":
#    length_km = length_meters/1000
#    print(f"{length_meters} метрів це {length_km} км")
#else:
#    print("ви ввели не вірну метричну систему ")


#4

#answer = input("Відповідь на Велике Питання Життя, Всесвіту і Всього Іншого: ")
#if answer == "42":
#    print("Правильно")
#elif answer == "сорок-два":
#    print("Правильно")
#elif answer == "сорок два":
#    print("Правильно")
#else:
#    print("Не правильно")


#5

#grade = int(input("Введіть оцінку: "))
#if grade == 2:
#    print("Незадовільно")
#elif grade == 3:
#    print("Задовільно")
#elif grade == 4:
#    print("Добре")
#elif grade == 5:
#    print("Відмінно")
#else:
#    print("Оцінка має бути від 2 до 5")

#6 Ви плануєте замовити піцу для компанії людей.
#Користувач вводить ціну однієї піци, кількість піц та ваш загальний бюджет.
#Перевірте чи вистачає вам грошей. Якщо ні то виведіть скільки саме не вистачає

print("Доброго дня!")
price_pizza = float(input("введіть ціну однієї піци: "))
total_pizza = int(input("введіть бажану кількість піц: "))
budget = float(input("введіть Ваш бюджет: "))

total_sum = price_pizza * total_pizza

remainder = budget - total_sum
if budget < total_sum:
    print(f"У Вас не вистачає: {-remainder} грн")
else:
    print(f"Ви можите замовити {total_pizza} піц")
print("Чекаємо нових замовлень!")