import datetime
class TypedProperty:
    def __init__(self, type1):
        self.type1 = type1 #запоминаем тип

    def __set_name__(self, owner, name):
        self.name = name #запоминаем имя aттрибута

    def __get__(self, obj, owner):
        if obj is None:
            return self
        return obj.__dict__.get(self.name) #get

    def __set__(self, instance, value):
        if not isinstance(value, self.type1):
            raise TypeError(f"Ожидался тип {self.type1.__name__}, получен {type(value).__name__}")
        instance.__dict__[self.name] = value #set

class ValidatedProperty(TypedProperty):
    def __init__(self, type2, min=None, max=None, allowed_values=None):
        super().__init__(type2)
        self.min = min
        self.max = max
        self.allowed_values = allowed_values #допустимые значения

    def __set__(self, instance, value):
        super().__set__(instance, value)

        if self.allowed_values is not None:
            if value not in self.allowed_values:
                raise ValueError(f"значение должно быть одним из: {self.allowed_values}")

        if isinstance(value, str):
            if self.min is not None and self.max is not None:
                if len(value) < self.min or len(value) > self.max:
                    raise ValueError(f"Длина строки должна быть от {self.min} до {self.max})")

        elif isinstance(value, (int, float)):
            if self.min is not None and self.max is not None:
                if value < self.min or value > self.max:
                    raise ValueError(f"Значение должно быть от {self.min} до {self.max}")

class ReadOnlyProperty:#дескриптор,который не дает изменять параметр
    def __init__(self, private_name):
        self.private_name = private_name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)
    def __set__(self, obj, value):
        if hasattr(obj, self.private_name):
            raise AttributeError("Это свойство только для чтения!")
        setattr(obj, self.private_name, value) #первое присвоение можно,дальше нет
