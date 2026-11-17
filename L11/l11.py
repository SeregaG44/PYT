total = 0
for day in range(1, 6):
    delivery = int(input(f"Введіть кількість доставок за день {day}: "))
    total += delivery
print("Загальна кількість доставок за тиждень:", total)
if total >= 50:
    print("Тижневу норму виконано!")

else:
    print("Тижневу норму не виконано!")
