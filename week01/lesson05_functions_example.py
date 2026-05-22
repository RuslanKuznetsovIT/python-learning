# Урок 5 — функции (def)
# Пример: считаем комиссию менеджера разными способами

# --- Пример 1: функция без параметров и без return ---
# Просто блок кода, который можно вызвать несколько раз

def say_hello():
    print("Здравствуйте! Это отдел продаж ARTGK.")

# вызов
say_hello()
say_hello()
say_hello()


# --- Пример 2: функция с параметром, без return ---
# Принимает имя клиента и здоровается по имени

def greet_client(name):
    print(f"Здравствуйте, {name}! Это отдел продаж ARTGK.")

greet_client("Иван")
greet_client("Мария")


# --- Пример 3: функция с параметром и return ---
# Возвращает значение, которое можно сохранить в переменную

def calculate_commission(deal_sum):
    commission = deal_sum * 0.15
    return commission

# вызываем и сохраняем результат
result_1 = calculate_commission(50000)
result_2 = calculate_commission(30000)

print(f"Комиссия с 50000: {result_1}")
print(f"Комиссия с 30000: {result_2}")


# --- Пример 4: функция с двумя параметрами ---
# Считает комиссию с учётом индивидуального процента менеджера

def calculate_commission_v2(deal_sum, percent):
    commission = deal_sum * percent / 100
    return commission

# вызываем с разными процентами
print(f"Топ-менеджер с 50000: {calculate_commission_v2(50000, 20)}")
print(f"Стажёр с 50000: {calculate_commission_v2(50000, 5)}")
