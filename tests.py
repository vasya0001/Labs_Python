import datetime


from models import Product
from models import Customer
from models import OrderItem
from models import Order
product = Product("Ноутбук",50000.0,2,"Техника","MAI-001", 0.5)
print("Создание объекта")
print(f"Имя:{product.name}\n")
print(f"Цена:{product.price}\n")
print(f"Колличество:{product.quantity}\n")
print(f"Катыегория:{product.category}\n")
print(f"SKU:{product.sku}\n")
print(f"Скидка:{product.discount}\n")
print("Проверка данных товара:")
try:
    product.name = 15
except TypeError as e:
    print(e)
print("\n")
try:
    product.name = 'R'
except ValueError as e:
    print(e)
print("\n")
try:
    product.price = "12000"
except TypeError as e:
    print(e)
print("\n")
try:
    product.price = -50000.0
except ValueError as e:
    print(e)
print("\n")
try:
    product.quantity = "1"
except TypeError as e:
    print(e)
print("\n")
try:
    product.quantity = -10
except ValueError as e:
    print(e)
print("\n")
try:
    product.category = [1,2,3,4]
except TypeError as e:
    print(e)
print("\n")
try:
    product.sku = "MAI-002"
except AttributeError as e:
    print(e)
print("\n")
try:
    product.discount = 50000.0
except ValueError as e:
    print(e)
print("\n")
print(f"Финальная цена:{product.final_price()}")
print("\n")
print(product.total_value)
print("\n")
del product.name
del product.price
del product.quantity
del product.category
del product.discount
print(f"Создание клиента!")
customer = Customer("Vasya", "Kalinnikov",18,"vasenkak2008@gmail.com","+79105839637", "VASYA-001", 50000.0)
print(customer.first_name)
print(customer.last_name)
print(customer.age)
print(customer.email)
print(customer.phone)
print(customer.balance)
print("\n")
try:
    customer.first_name = 12
except TypeError as e:
    print(e)
print("\n")
try:
    customer.first_name = "Vasya12"
except ValueError as e:
    print(e)
try:
    customer.last_name = 11
except TypeError as e:
    print(e)
print("\n")
try:
    customer.last_name = "Kalinnikov13"
except ValueError as e:
    print(e)
print("\n")
try:
    customer.age = '11'
except TypeError as e:
    print(e)
print("\n")
try:
    customer.age = -14
except ValueError as e:
    print(e)
print("\n")
try:
    customer.email = 12
except TypeError as e:
    print(e)
print("\n")
try:
    customer.email = "vasenkak2008gmail.com"
except ValueError as e:
    print(e)
print("\n")
try:
    customer.phone = 12
except TypeError as e:
    print(e)
print("\n")
try:
    customer.id = 12
except TypeError as e:
    print(e)
print("\n")
try:
    customer.id = "Vasya - 003"
except AttributeError as e:
    print(e)
print("\n")
print(f"Полное имя:{customer.full_name}")
print("\n")
print(f"Проверка на совершеннолетие:{customer.is_adult}")
print("\n")
print("Проверка класса OrderItem")

first = OrderItem()
first.product = Product(name="Ноутбук", price=10000.0, quantity=10, category="Ноутбуки", sku="VASYA001", discount=0.1)
first.quantity = 10
first.discount = 0.3
subtotal = first.subtotal()

print(f"Объект:{first.product}")
print(f"колличество:{first.quantity}")
print(f"Цена за единицу:{first.product.price}")
print(f"Скидка:{first.discount * 100}%")
print(f"Имя объекта:{first.product.name}")
print(f"Сумма без скидки: {first.product.price * first.quantity}")
print(f"Сумма со скидкой: {subtotal}")
print("\n")
print("Проверка ошибок!")
try:
    first.quantity = 0
except ValueError as e:
    print(e)
print("\n")
try:
    first.discount = "0.4"
except TypeError as e:
    print(e)
print("\n")
try:
    first.discount = 0.6
except ValueError as e:
    print(e)
print("\n")
try:
    first.product = "Ноутбук"
except TypeError as e:
    print(e)


print("\n")
"""Класс ORDER реаоизация"""
customer1 = Customer("Vasya", "Kalinniko",18, "oaoavasa128@gmai.com", "+79105839637", "VASYA-001", 100000.0)
item1 = OrderItem()
item1.product = Product("Клавиатура",4000.0, quantity=5,category="Техника", sku="KEYBORAD-001", discount = 0.5)
item1.quantity = 1
item1.discount = 0.5
item2 = OrderItem()
item2.product = Product("Монитор",20000.0, quantity=10,category="Техника", sku="DISPLAy-001", discount = 0.5)
item2.quantity = 2
item2.discount = 0.5
item3 = OrderItem()
item3.product = Product("Кресло",10000.0, quantity=50,category="Техника", sku="CHAIR-001", discount = 0.5)
item3.quantity = 1
item3.discount = 0.5



order = Order(order_id='ORD-1',customer=customer1)
print(order.order_id)
print("\n")
print(order.status)
print("\n")
print(order.created_at)
print("\n")

order.add_item(item1)
order.add_item(item2)
order.add_item(item3)
try:
    order.add_item("Phone")
except TypeError as e:
    print(e)
print(order.items)
order.remove_item("CHAIR-001")
print(order.items)
print(f"Общая цена закаpа:{order.total_price()}")
print(f"Количество позиций в заказе:{order.total_quantity()}")
order.change_status("PAID")
print(order.status)
try:
    order.change_status("DELIVERED")
except ValueError as e:
    print(e)
