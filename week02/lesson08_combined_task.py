# Урок 8 — комбинированная задача: функция + список словарей + цикл + if
#
# Дан список сотрудников:
employees = [
    {"name": "Анна", "department": "продажи", "salary": 80000},
    {"name": "Сергей", "department": "разработка", "salary": 120000},
    {"name": "Виктор", "department": "продажи", "salary": 75000},
    {"name": "Мария", "department": "маркетинг", "salary": 90000},
    {"name": "Дмитрий", "department": "разработка", "salary": 150000},
    {"name": "Светлана", "department": "продажи", "salary": 85000}
]
#
# Задание:
#
# 1. Опиши функцию department_total(employees, department), которая:
#    - принимает список сотрудников и название отдела
#    - возвращает СУММУ зарплат сотрудников этого отдела
#
# 2. Опиши функцию department_count(employees, department), которая:
#    - возвращает КОЛИЧЕСТВО сотрудников этого отдела
#
# 3. Вызови обе функции для трёх отделов и выведи отчёт:
#    Отдел продаж: 3 чел., ФОТ 240000 ₽
#    Отдел разработки: 2 чел., ФОТ 270000 ₽
#    Отдел маркетинга: 1 чел., ФОТ 90000 ₽
#
# Подсказка: внутри функции — тот же паттерн что в ДЗ выше,
# только обёрнутый в def и с return.
#
# Дисциплина: запусти → сверь посимвольно → потом сдавай.

# Пиши код ниже (список employees уже создан):

def department_total(employees, department):
    total_salary = 0
    for employee in employees:
        if employee["department"] == department:
            total_salary = total_salary + employee["salary"]
    return total_salary


def department_count(employees, department):
    count_employee = 0
    for employee in employees:
        if employee["department"] == department:
            count_employee += 1
    return count_employee

sales_department = department_total(employees, "продажи")
count_sales_department = department_count(employees, "продажи")

dev_team = department_total(employees, "разработка")
count_dev_team = department_count(employees, "разработка")

marketing_department = department_total(employees, "маркетинг")
count_marketing_department = department_count(employees, "маркетинг")

print(f"Отдел продаж: {count_sales_department} чел., ФОТ {sales_department} ₽")
print(f"Отдел разработки: {count_dev_team} чел., ФОТ {dev_team} ₽")
print(f"Отдел маркетинга: {count_marketing_department} чел., ФОТ {marketing_department} ₽")
