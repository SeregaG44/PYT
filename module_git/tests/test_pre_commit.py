your_rating = "5"
while True:
    exam_grade = input("Введіть оцінку за іспит(від 1 до 5): ")
    if exam_grade == your_rating and exam_grade == "5":
        print("Чудово")
        break

    if exam_grade == your_rating and exam_grade == "1":
        print("Дуже погано")
        break

    if exam_grade == your_rating and exam_grade == "2":
        print("Погано")
        break

    if exam_grade == your_rating and exam_grade == "3":
        print("Задовільно")
        break

    if exam_grade == your_rating and exam_grade == "4":
        print("Добре")

        break
