name_product = input("Название товара? ")
cost_product = float(input("Цена товара "))
quantity_product = int(input("Введите количество штук "))
price = cost_product * quantity_product
print(f"Товар: {name_product}, количество: {quantity_product}, итого: {price} руб.")