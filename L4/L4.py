#print("start")
#temp=20
#if temp<15:
#    print("Вдягни куртку!")
#elif temp==15:
#    print("куртку на усмотрение")
#else:
#    print("на улице тепло")
#print("end")





product = input("віедіть назву товару: ")
print("Доброго дня")
is_purchased = False
if product == "пиріжок":
    is_purchased = True
    print("Є з вишнею або з шоколадом")

elif product == "морозиво":
    is_purchased = True
    print("залишився лише пломбір")

else:
    is_purchased = True
    print(f"можливо ви знайдите {product} в іншому магазині")

print("Бажаємо Вам гарного дня")