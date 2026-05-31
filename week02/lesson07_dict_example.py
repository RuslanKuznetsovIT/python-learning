# Урок 7 — словари (dict)
# Пример: карточка клиента из CRM

client = {
    "name": "Иванов Иван",
    "phone": "+79991234567",
    "amount": 150000,
    "status": "квалифицирован",
    "manager": "Анна"
}

# Доступ к полям
print(f"Клиент: {client['name']}")
print(f"Сумма: {client['amount']}")
print(f"Менеджер: {client['manager']}")

# Изменение
client["amount"] = 200000
print(f"Новая сумма: {client['amount']}")

# Добавление нового поля
client["city"] = "Уфа"
print(f"Город: {client['city']}")

# Проверка
print(f"Есть телефон? {'phone' in client}")
print(f"Есть email? {'email' in client}")

# Количество полей
print(f"Всего полей: {len(client)}")
