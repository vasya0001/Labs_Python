class Node:
    def __init__(self, *args):
        if len(args) == 0:
            self.data = 0
            self.next = None
        elif len(args) == 1:
            self.data = args[0]
            self.next = None
        elif len(args) == 2:
            self.data = args[0]
            self.next = args[1]

    def clear(self):    
        self.data = 0
        self.next = None
    def __str__(self):
        return f"Node({self.data})"


class SinglyLinkedList:
        def __init__(self):
            self.head = None
            self.size = 0

        def prepend(self, data):
            """добавляет элемент в начало списка"""
            new_node = Node(data, self.head)
            self.head = new_node
            self.size = self.size + 1

        def append(self, data):
            """добавляет элемент в конец списка"""
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = new_node
            self.size += 1

        def insert_after(self,index,data):
            """Добавление элемента после элемента с указанным индекссом"""
            if self.head is None:
                raise EmptyStructureError("SinglyLinkedList", "Нельзя вставить в пустой список, нету индекса!")
            if index < 0 or index >= self.size:
                raise IndexError(index, "Index out of range")
            current = self.head
            for i in range(index):
                current = current.next
            new_node = Node(data, current.next)
            current.next = new_node
            self.size = self.size + 1

        def insert_before(self,index,data):
            """Добавление элемента перед элементом с указанным индексом"""
            if self.head is None:
                raise EmptyStructureError("SinglyLinkedList", "Нельзя вставить в пустой список, нету индекса!")
            if index < 0 or index >= self.size:
                raise IndexError(index, "Index out of range")
            if index == 0:
                self.prepend(data)
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node = Node(data, current.next)
            current.next = new_node
            self.size = self.size + 1

        def remove_first(self):
            """Удаляет первый элемент списка"""
            if self.head is None:
                raise EmptyStructureError("SinglyLinkedList", "Нельзя удалить из пустого списка!")
            self.head = self.head.next
            self.size = self.size - 1
        def remove_last(self):
                """Удаляет последний элемент списка"""
                if self.head is None:
                    raise EmptyStructureError("SinglyLinkedList", "Нельзя удалить из пустого списка!")
                if self.size == 1:
                    self.head = None
                else:
                    current = self.head
                    for i in range(self.size - 2):
                        current = current.next
                    current.next = None
                self.size = self.size -1

        def remove_at(self, index):
            if self.head is None:
                raise EmptyStructureError("SinglyLinkedList", "Нельзя удалить из пустого списка!")
            """удаление элемента по индексу"""
            if index < 0 or index >= self.size:
                raise IndexError(index, "Index out of range")
            if index == 0:
                self.head = self.head.next
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next

        def remove_value(self, value):
            """удаление первого вхождения указанного значения"""
            if self.head is None:
                raise EmptyStructureError("SinglyLinkedList", "Нельзя удалить из пустого списка!")
            if self.head.data == value:
                self.head = self.head.next
                self.size = self.size - 1
                return True
            current = self.head
            while current.next is not None:
                if current.next.data == value:
                    current.next = current.next.next
                    self.size = self.size - 1
                    return True
                current = current.next
            raise ValueNotFoundError(value, "Value not found in list")
        def find(self, value):
            """поиск индекса первого вхождения значения (возвращает индекс или -1)"""
            index = 0
            current = self.head
            while current is not None:
                if current.data == value:
                    return index
                current = current.next
                index = index + 1
            return - 1

        def find_all(self, value):
            """поиск индексов всех вхождений значения (возвращает список индексов)"""
            values = []
            index = 0
            current = self.head
            while current is not None:
                if current.data == value:
                    values.append(index)
                current = current.next
                index = index + 1
            return values

        def contains(self, value):
            """проверка наличия значения в списке (возвращает True/False)"""
            current = self.head
            while current is not None:
                if current.data == value:
                    return True
                current = current.next
            return False

        def get(self, index):
            if self.head is None:
                raise EmptyStructureError("SinglyLinkedList", "Нельзя получить элемент из пустого списка!")
            """получение значения элемента по индексу"""
            if index < 0 or index >= self.size:
                raise IndexError(index, "Index out of range")
            current = self.head
            for i in range(index):
                current = current.next
            return current.data

        def __len__(self):
            """возвращает количество элементов"""
            return self.size

        def __str__(self):
            if self.head is None:
                return "None"
            current = self.head
            res = str(current.data)
            while current.next is not None:
                current = current.next
                res = res + " -> " + str(current.data)
            return res + " -> None"
        def __iter__(self):
            """ сделать список итерируемым"""
            current = self.head
            while current is not None:
                yield current.data
                current = current.next
        def clear(self):
            """очистка списка"""
            self.head = None
            self.size = 0

        def __getitem__(self, index):
            """обращение по индексу"""
            if self.head is None:
                raise EmptyStructureError("SinglyLinkedList", "Нельзя получить элемент из пустого списка!")
            if index < 0 or index >= self.size:
                raise IndexError(index, "Index out of range")
            return self.get(index)

        def __setitem__(self, index, value):
            """изменение по индексу"""
            if self.head is None:
                raise  EmptyStructureError("SinglyLinkedList", "Нельзя изменить элемент в пустом списке!")
            if index < 0 or index >= self.size:
                raise IndexError(index, "Index out of range")
            current = self.head
            for i in range(index):
                current = current.next
            current.data = value

        def __contains__(self, value):
            """оператор in"""
            current = self.head
            while current is not None:
                if current.data == value:
                    return True
                current = current.next
            return False

        def __add__(self, other):
            """конкатенация двух списков"""
            if not isinstance(other, (SinglyLinkedList, DoublyLinkedList)):
                raise TypeError(f"Не совпадение типа SinglyLinkedList и  {type(other).__name__}")
            res = SinglyLinkedList()
            for i in self:
                res.append(i)
            for i in other:
                res.append(i)
            return res

        def __mul__(self, other):
            """повторение списка"""
            if not isinstance(other, int):
                raise TypeError(f"невозможно умножить последовательность на значение типа не int, тип:'{type(other).__name__}'")
            if other <=0:
                return SinglyLinkedList
            res = SinglyLinkedList()
            for i in range(other):
                for n in self:
                    res.append(n)
            return res

class DoubleNode(Node):
    """двусвязный узел,наследующий от Node"""
    def __init__(self, data = 0, next = None, prev = None):
        super().__init__(data,next)
        self.prev = prev


class DoublyLinkedList:
    """двусвязный список"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, data):
        """добавление элемента в начало списка"""
        new_node = DoubleNode(data, self.head, None)
        if self.head is None:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.size = self.size + 1

    def append(self, data):
        """добавление элемента в конец списка"""
        new_node = DoubleNode(data,None,self.tail)
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size = self.size + 1

    def insert_after(self, index,data):
        """ добавление элемента после элемента с указанным индексом"""
        if self.head is None:
            raise EmptyStructureError("DoublyLinkedList", "Нельзя вставить в пустой список,нет индекса!")
        if index < 0 or index >= self.size:
            raise IndexError(index, "Index out of range")
        if index == self.size-1:
            self.append(data)
            return
        current = self.head
        for i in range(index):
            current = current.next
        new_node = DoubleNode(data, current.next,current)
        current.next.prev = new_node
        current.next = new_node
        self.size = self.size + 1

    def insert_before(self, index,data):
        """ добавление элемента перед элементом с указанным индексом"""
        if self.head is None:
            raise EmptyStructureError("DoublyLinkedList", "Нельзя вставить в пустой список,нет индекса!")
        if index < 0 or index >= self.size:
            raise IndexError(index, "Index out of range")
        if index == 0:
            self.prepend(data)
            return
        current = self.head
        for i in range(index-1):
            current = current.next
        new_node = DoubleNode(data, current.next,current)
        current.next.prev = new_node
        current.next = new_node
        self.size = self.size + 1

    def remove_first(self):
        """удаление первого элемента"""
        if self.head is None:
            raise EmptyStructureError("DoublyLinkedList", "Нельзя удалить из пустого списка!")
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size = self.size - 1

    def remove_last(self):
        """удаление последнего элемента"""
        if self.head is None:
            raise EmptyStructureError("DoublyLinkedList", "Нельзя удалить из пустого списка")
        if self.size == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size = self.size - 1

    def remove_at(self, index):
        """ удаление элемента по индексу"""
        if self.head is None:
            raise EmptyStructureError("DoublyLinkedList", "Нельзя удалить из пустого списка!")
        if index < 0 or index >= self.size:
            raise IndexError(index, "Index out of range")
        if index == 0:
            self.remove_first()
            return
        if index == self.size - 1:
            self.remove_last()
            return
        current = self.head
        for i in range(index):
            current = current.next
        current.next.prev = current.prev
        current.prev.next = current.next
        self.size = self.size - 1

    def remove_value(self,value):
        """ удаление первого вхождения указанного значения"""
        if self.head is None:
            raise EmptyStructureError("DoublyLinkedList", "Нельзя удалить из пустого списка!")
        current = self.head
        index = 0
        while current is not None:
            if value == current.data:
                self.remove_at(index)
                return True
            current = current.next
            index = index + 1
        raise ValueNotFoundError(value, "Value not found in list")

    def find(self, value):
        """поиск индекса первого вхождения значения (возвращает индекс или -1)"""
        if self.head is None:
            return -1
        current = self.head
        index = 0
        while current is not None:
            if value == current.data:
                return index
            current = current.next
            index = index + 1
        return -1

    def find_all(self,value):
        """поиск индексов всех вхождений значения (возвращает список индексов)"""
        values = []
        if self.head is None:
            return values
        current = self.head
        index = 0
        while current is not None:
            if value == current.data:
                values.append(index)
            current = current.next
            index = index + 1
        return values

    def contains(self, value):
        """ проверка наличия значения в списке (возвращает True/False)"""
        if self.head is None:
            return False
        current = self.head
        while current is not None:
            if value == current.data:
                return True
            current = current.next
        return False

    def get(self, index):
        """получение значения элемента по индексу"""
        if self.head is None:
            raise EmptyStructureError("DoublyLinkedList", "Нельзя получить элемент из пустого списка!")
        if index < 0 or index >= self.size:
            raise IndexError(index, "Index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def __len__(self):
        """возвращает количество элементов"""
        return self.size

    def __str__(self):
        """строковое представление списка"""
        if self.head is None:
            return "None"
        res = []
        current = self.head
        while current is not None:
            res.append(str(current.data))
            current = current.next
        return " <-> ".join(res) + " <-> None"

    def __iter__(self):
        """сделать список итерируемым"""
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def clear(self):
        """очистка списка"""
        self.head = None
        self.tail = None
        self.size = 0

    def __getitem__(self, index):
        """обращение по индексу"""
        if self.head is None:
            raise EmptyStructureError("DoublyLinkedList", "Нельзя получить элемент из пустого списка!")
        if index < 0 or index >= self.size:
            raise IndexError(index, "Index out of range")
        return self.get(index)

    def __setitem__(self, index,value):
        """изменение по индексу"""
        if self.head is None:
            raise EmptyStructureError("DoublyLinkedList", "Нельзя изменить элемент в пустом списке!")
        if index < 0 or index >= self.size:
            raise IndexError(index, "Index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        current.data = value

    def __contains__(self, value):
        """оператор in"""
        if self.head is None:
            return False
        current = self.head
        while current is not None:
            if value == current.data:
                return True
            current = current.next
        return False

    def __add__(self, other):
        """конкатенация двух списков"""
        if not isinstance(other, (SinglyLinkedList, DoublyLinkedList)):
            raise TypeError(f"Не совпадение типа DoublyLinkedList и  {type(other).__name__}")
        res = DoublyLinkedList()
        for item in self:
            res.append(item)
        for item in other:
            res.append(item)
        return res

    def __mul__(self, n):
        """повторение списка"""
        if not isinstance(n, int):
            raise TypeError(f"невозможно умножить последовательность на значение типа, отличное от int, тип:'{type(n).__name__}'")
        res = DoublyLinkedList()
        for i in range(n):
            for p in self:
                res.append(p)
        return res


class Stack:
    def __init__(self):
        self.items = SinglyLinkedList()

    def push(self, data):
        """добавить элемент на вершину стека"""
        self.items.prepend(data)

    def pop(self):
        """удалить и вернуть элемент с вершины стека"""
        if self.items.head is None:
            raise EmptyStructureError("Stack", "Нульзя удалить из пустого стека!")
        data = self.items.head.data
        self.items.remove_first()
        return data

    def peek(self):
        """посмотреть элемент на вершине без удаления"""
        if self.items.head is None:
            raise EmptyStructureError("Stack", "Нельзя простмотреть в пустом стеке!")
        data = self.items.head.data
        return data

    def is_empty(self):
        """проверка, пуст ли стек"""
        if self.items.head is None:
            return True
        else:
            return False

    def size(self):
        """количество элементов"""
        return self.items.size

    @staticmethod
    def from_queue(queue):
        """статический метод, создающий новый стек из очереди (элементы из очереди переносятся в стек)"""
        new = Stack()
        queue_list = []
        while not queue.is_empty():
            queue_list.append(queue.dequeue())
        for i in reversed(queue_list):
            new.push(i)
        return new

    def __str__(self):
        if self.is_empty():
            return "[]"
        all = []
        current = self.items.head
        while current is not None:
            all.append(str(current.data))
            current = current.next
        return f"[{', '.join(all)}]"


class Queue:
    def __init__(self):
        self.items = SinglyLinkedList()

    def enqueue(self, data):
        """Добавляет элемент в конец очереди"""
        self.items.append(data)

    def dequeue(self):
        """ удалить и вернуть элемент из начала очереди"""
        if self.items.head is None:
            raise EmptyStructureError("Queue", "Нельзя удалить из пустой очереди!")
        data = self.items.head.data
        self.items.remove_first()
        return data

    def front(self):
        """посмотреть первый элемент без удаления"""
        if self.items.head is None:
            raise EmptyStructureError("Queue", "Нельзя посмотреть в пустой очереди!")
        data = self.items.head.data
        return data

    def is_empty(self):
        """проверка, пуста ли очередь"""
        if self.items.head is None:
            return True
        else:
            return False

    def size(self):
        """колличество элементов"""
        return self.items.size

    @staticmethod
    def from_stack(stack):
        """статический метод, создающий новую очередь из стека (элементы из стека переносятся в очередь)"""
        new = Queue()
        stack_list = []
        while not stack.is_empty():
            stack_list.append(stack.pop())
        for i in reversed(stack_list):
            new.enqueue(i)
        return new

    def __str__(self):
        """строковое представление очереди"""
        if self.is_empty():
            return "[]"

        all = []
        current = self.items.head
        while current is not None:
            all.append(str(current.data))
            current = current.next
        return f"[{', '.join(all)}]"


class StructureError(Exception):
    """Базовый класс для всех исключений структур данных"""
    pass

class EmptyStructureError(StructureError):
    """ошибка при попытке операции с пустой структурой"""
    def __init__(self, structure_name, message="Structure is empty"):
        self.structure_name = structure_name
        super().__init__(f"{message}: {structure_name}")

class IndexError(StructureError):
    """ошибка при обращении по несуществующему индексу"""
    def __init__(self, index, message="Index out of range"):
        self.index = index
        super().__init__(f"{message}: {index}")

class ValueNotFoundError(StructureError):
    """ошибка при поиске несуществующего значения"""
    def __init__(self, value, message="Value not found"):
        self.value = value
        super().__init__(f"{message}: {value}")




