# Додати один файл
git add main.py

# Додати всю папку
git add src/

# Додати всі зміни в поточній папці
git add .


# 1. Перевірити стан
git status

# 2. Додати зміни в індекс
git add .

# 3. Зберегти коміт
git commit -m "Опис змін"
pre-commit run --all-files

# 4. Відправити на GitHub
git push