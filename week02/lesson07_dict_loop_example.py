# Урок 7 — цикл по словарю

client = {
    "name": "Иванов",
    "phone": "+79991234567",
    "amount": 150000,
    "city": "Уфа"
}

# Только ключи
print("Поля карточки:")
for key in client:
    print(f"  - {key}")

print()

# Только значения
print("Значения:")
for value in client.values():
    print(f"  - {value}")

print()

# Пары
print("Карточка целиком:")
for key, value in client.items():
    print(f"  {key}: {value}")
