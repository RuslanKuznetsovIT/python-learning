deals = [
    {"client": "Иванов", "amount": 50000, "status": "закрыта"},
    {"client": "Петрова", "amount": 120000, "status": "в работе"},
    {"client": "Сидоров", "amount": 80000, "status": "закрыта"},
    {"client": "Орлова", "amount": 30000, "status": "в работе"},
    {"client": "Кузнецов", "amount": 200000, "status": "закрыта"},
]


def total_won(deals):
    total = 0
    for deal in deals:
        if deal['status'] == "закрыта":
            total = total + deal['amount']
    return total


print(f'Сумма закрытых сделок: {total_won(deals)}')

# products = [
#     {"name": "Молоко", "price": 80},
#     {"name": "Ноутбук", "price": 50000},
#     {"name": "Хлеб", "price": 45},
#     {"name": "Телефон", "price": 30000},
#     {"name": "Кофе", "price": 600},
# ]

# def count_cheap(products):
#     count = 0
#     for product in products:
#         if product['price'] < 1000:
#             count += 1
#     return count

# print(f"Дешёвых товаров: {count_cheap(products)}")


products = [
    {"name": "Молоко", "price": 80},
    {"name": "Ноутбук", "price": 50000},
    {"name": "Хлеб", "price": 45},
    {"name": "Телефон", "price": 30000},
    {"name": "Кофе", "price": 600},
]



def average_expensive(products):
    total = 0
    count = 0

    for product in products:
        if product["price"] > 1000:
            total = total + product["price"]
            count += 1

    return float(total / count)

print(f"Средняя цена дорогих: {average_expensive(products)}")


def get_expensive_names(products):
    result = []                              # контейнер — ПУСТОЙ СПИСОК
    for product in products:
        if product["price"] > 1000:
            result.append(product["name"])   # добавляем имя в конец списка
    return result

print(f"Дорогие товары: {get_expensive_names(products)}")
