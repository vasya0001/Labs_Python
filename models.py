import datetime
from descriptions import *  
class Product:
    def __init__(self,name,price,quantity,category,sku,discount=0.0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self._sku = sku
        self.discount = discount
        """"name"""
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) == False:
            raise TypeError("Имя должно быть строкой!")
        elif len(value) < 2 or len(value) > 100:
            raise ValueError("Длинна имени может быть от 2 до 100 символов!")
        else:
            self._name = value
    @name.deleter
    def name(self):
        self._name = None

        """"price"""
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if isinstance(value,float) == False:
            raise TypeError("Цена должна быть указана в вещественном типе!")
        elif value <= 0:
            raise ValueError("Цена должна быть больше нуля!")
        else:
            self._price = value
    @price.deleter
    def price(self):
        self._price = None

    """"quantity"""
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self,value):
        if isinstance(value, int) == False:
            raise TypeError("Колличество может быть только целым числом!")
        elif value < 0:
            raise ValueError("Колличество не может быть отрицательным!")
        else:
            self._quantity = value
    @quantity.deleter
    def quantity(self):
        self._quantity = None

    """"category"""
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if isinstance(value, str) == False:
            raise TypeError("Категория обозначается строкой!")
        else:
            self._category = value
    @category.deleter
    def category(self):
        self._category = None

    """"sku"""
    @property
    def sku(self):
        return self._sku
    @sku.setter
    def sku(self, value):
        raise AttributeError("SKU нельзя изменить")
    @sku.deleter
    def sku(self):
        raise AttributeError("Нельзя удалить SKU товара")

    """discount"""
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, value):
        if isinstance(value, float) == False:
            raise TypeError("Скидка должна быть вещественным числом!")
        elif value < 0 or value > 0.9:
            raise ValueError("Скидка не может быть больше 0.9 или меньше 0!")
        else:
            self._discount = value
    @discount.deleter
    def discount(self):
        self._discount = 0.0

    """Итоговая цена с учетом скидки"""
    def final_price(self):
        if self._price is None:
            return 0.0
        return self._price * (1 - self._discount)

    """"Стоимость всех единиц товара на складе товара на складе"""
    @property
    def total_value(self):
        if self._price is None or self._quantity is None:
            return 0.0
        return self._price * self._quantity

class Customer:
    def __init__(self,first_name,last_name,age,email,phone,customer_id,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone = phone
        self._customer_id = customer_id
        self.balance = balance

    def __setattr__(self,name,value):
        if name == "first_name":
            if isinstance(value, str) == False:
                raise TypeError("имя может быть только строкой!")
            if value.isalpha() == False:
                raise ValueError("Имя может состоять только из букв!")


        elif name == "last_name":
            if isinstance(value, str) == False:
                raise TypeError("Фамилия должна быть строкой!")
            if not value.isalpha():
                raise ValueError("Фамилия должна содержать только буквы!")

        elif name == "age":
            if isinstance(value, int) == False:
                raise TypeError("Возрастом может быть только целое число!")
            if value < 1 or value > 120:
                raise ValueError("аозраст должен быть от 1 до 120 лет!")

        elif name == "email":
            if isinstance(value, str) == False:
                raise TypeError("Электронная почта обозначается строкой!")
            if not "@" in value:
                raise ValueError("невозможно распознать почту!нету символа \"@\"")
        elif name == "phone":
            if isinstance(value, str) == False:
                raise TypeError("Телефон обозначается строко!")

        elif name == "customer_id":
            if not isinstance(value, str):
                raise TypeError("customer_id должен быть строкой!")
            if hasattr(self, "_customer_id"): #если аттрибут существует,то мы не можем его изменить
                raise AttributeError("Нельзя изменить customer_id")
            super().__setattr__("_customer_id", value) #при первом присвоении разрешаем
            return

        elif name == "balance":
            if isinstance(value, float) == False:
                raise TypeError("Баланс пользователя может быть записан только в дробном виде!")
            if value < 0:
                raise ValueError("баланс не может быть отрицательным!")

        return super().__setattr__(name,value)

    @property
    def customer_id(self):
        return self._customer_id

    def __getattribute__(self, name):
        """Логирование доступа к атрибутам"""
        print(f"[LOG {datetime.datetime.now()}] Accessing attribute: {name}")
        return super().__getattribute__(name) #аозвращение аттрибута

    def __getattr__(self, name):
        """обработка несуществующих атрибутов"""
        return f"Атрибут '{name}' не существует"

    @property
    def full_name(self):
        """Полное имя"""
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self):
        """"проверка на аовершеннолетие"""
        return self.age >= 18

class OrderItem:
    product = TypedProperty(Product)
    quantity = ValidatedProperty(int, 1, 10000000000000000000)
    discount = ValidatedProperty(float, 0, 0.5)

    def subtotal(self):
        """стоимость позиции заказа"""
        x = self.product.price * self.quantity * (1 - self.discount)
        return x

class Order:
    rightstatus = ["NEW", "PAID", "SHIPPED", "DELIVERED","CANCELED"]

    status_transition = {'NEW': ['PAID', 'CANCELLED'],'PAID': ['SHIPPED', 'CANCELLED'],'SHIPPED': ['DELIVERED', 'CANCELLED'],'DELIVERED': [],'CANCELLED': []}

    order_id = ReadOnlyProperty('_order_id')
    customer = TypedProperty(Customer)
    status = ValidatedProperty(str, allowed_values=rightstatus)
    created_at = TypedProperty(datetime.datetime)

    def __init__(self, order_id:str, customer:Customer):
        self.order_id = order_id
        self.customer = customer
        self.status = "NEW"
        self.created_at = datetime.datetime.now()
        self._items = []
    @property
    def items(self) -> list[OrderItem]:
        return self._items.copy()

    def add_item(self, item:OrderItem):
        """"Добавление позиции в заказ"""
        if not isinstance(item, OrderItem):
            raise TypeError("Можно добавлять только объекты OrderItem")
        for i in self._items:
            if i.product.sku == item.product.sku:
                i.quantity += item.quantity
                print(f"Товар '{item.product.name}' уже в заказе. Количество увеличено до {i.quantity}")
                return
        self._items.append(item)

    def remove_item(self, sku: str):
        """Удаление позиции заказа по sku"""
        for i, item in enumerate(self._items):
            if item.product.sku == sku:
                self._items.pop(i)
                return
        raise ValueError(f"Товар с sku {sku} не найден в заказе!")

    def total_price(self) -> float:
        """"Общая стоимость заказа!"""
        return sum(item.subtotal() for item in self.items)

    def total_quantity(self) -> int:
        """Общее количество товаров в заказе"""
        return sum(item.quantity for item in self.items)

    def change_status(self, new_status: str):
        """Изменение статуса заказа с проверкой корректности переходов"""
        if new_status not in self.rightstatus:
            raise ValueError(f"Недопустимый статус")

        # Проверяем, возможен ли переход
        allowed_next = self.status_transition.get(self.status, [])
        if new_status not in allowed_next:
            raise ValueError(f"Невозможно перейти из статуса '{self.status}' в '{new_status}'")
        old = self.status
        self.status = new_status
        print(f"статус заказа изменен: '{old}' на  '{new_status}'")
