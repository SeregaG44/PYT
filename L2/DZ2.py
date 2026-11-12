#1
from unittest.result import failfast

#num1 = int(input("перше число: "))
#num2 = int(input("друге число: "))
#sum = num1 + num2
#average = sum / 2
#print("Сума:", sum)
#print("Середнє:", average)

#2 Користувач вводить суму в гривнях та курс долара.
#Переведіть гривні в долари та виведіть на екран

#total = float(input ("введіть суму у гривнях: "))
#currency = float(input("введіть курс долара:  "))
#conversion = total / currency
#print("сума в  доларах: ", conversion )

#3 Користувач вводить ціну товару та відсоток знижки.
# Виведіть суму знижки

#price = float(input("введіть ціну товара: "))
#discount_percentage = int(input ("введіть відсоток знижки: "))
#discounted_amount = (price * (1-discount_percentage/100))
#total_discounts = price - discounted_amount
#print("Сумма знижки: ", total_discounts)



#4 Користувач вводить 3 числа: час повільної/швидкої
#ходьби та бігу.
#Напишіть код який обчислює окремо кількість калорій
#спалених під час цих активностей.
#Також виведіть загальну кількість спалених калорій.

time_slow_walk = float(input ("ввведіть час повільної ходьби: "))
brisk_walking = float(input ("ввведіть час швидкої ходьби: "))
runs = float(input ("ввведіть час бігу: "))

Slow = 3
fast = 4.5
run = 9

calories_Slow = time_slow_walk * Slow
calories_fast = brisk_walking * fast
calories_run = runs * run

total = calories_Slow + calories_fast + calories_run

print("кількість спалених калорій під час повільної ходьби: ", calories_Slow)
print("кількість спалених калорій під час швидкої ходьби: ", calories_fast)
print("кількість спалених калорій під час бігу: ", calories_run,'\nзагальна кількість спалених калорій: ', total)
