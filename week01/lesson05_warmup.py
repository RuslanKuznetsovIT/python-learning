# Урок 5 — разогрев
# Задание:
# 1. Создать функцию calculate_commission(deal_sum, percent) — возвращает комиссию
#    Формула: deal_sum * percent / 100
# 2. Вызвать функцию для трёх менеджеров и вывести результат
#
# Ожидаемый вывод:
# Комиссия Анны: 12000.0
# Комиссия Сергея: 45000.0
# Комиссия Дмитрия: 8000.0

# Сначала описываем функцию:


# Потом вызываем её три раза с разными данными:


def calculate_commission(deal_sum, percent):
    salary = deal_sum * percent / 100
    return salary

result_anna = calculate_commission (100000,12)
result_sergey = calculate_commission (250000,18)
result_dmitriy = calculate_commission (80000,10)

print(f"Комиссия Анны: {result_anna}")
print(f"Комиссия Сергея: {result_sergey}")
print(f"Комиссия Дмитрия: {result_dmitriy}")