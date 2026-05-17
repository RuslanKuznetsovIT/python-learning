# Спрашиваем имя и год рождения
name = input("Как тебя зовут? ")
birth_year = int(input("Год рождения? "))

# Считаем возраст
age = 2026 - birth_year

# Считаем сколько лет до пенсии (условно в 65)
years_to_retire = 65 - age

# Выводим результат
print(f"Привет, {name}!")
print(f"Тебе {age} лет.")
print(f"До пенсии осталось {years_to_retire} лет.")
