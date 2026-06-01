# Урок 8 — списки словарей
# Пример: воронка продаж как реальные данные

deals = [
    {"client": "ООО Ромашка", "amount": 150000, "manager": "Анна"},
    {"client": "ИП Сидоров", "amount": 80000, "manager": "Сергей"},
    {"client": "ООО Альфа", "amount": 250000, "manager": "Анна"},
    {"client": "ИП Петров", "amount": 35000, "manager": "Виктор"}
]

# 1. Простой перебор — все клиенты
print("Сделки в воронке:")
for deal in deals:
    print(f"  - {deal['client']}: {deal['amount']} ₽ (менеджер: {deal['manager']})")

print()

# 2. Общая сумма (накопитель)
total = 0
for deal in deals:
    total += deal["amount"]
print(f"Общая сумма воронки: {total} ₽")

# 3. Сколько сделок больше 100000 (счётчик с условием)
big_count = 0
for deal in deals:
    if deal["amount"] >= 100000:
        big_count += 1
print(f"Крупных сделок (≥ 100000): {big_count}")

# 4. Сумма сделок одного менеджера (накопитель с условием)
anna_total = 0
for deal in deals:
    if deal["manager"] == "Анна":
        anna_total += deal["amount"]
print(f"Сумма сделок Анны: {anna_total} ₽")
