from structures import SinglyLinkedList, Stack, Queue, EmptyStructureError,ValueNotFoundError,IndexError,StructureError,DoublyLinkedList,DoubleNode,Node
print("Демонстрация работы программы односвязного списка(SinglyLinkedList):\n")
lst1 = SinglyLinkedList()
print("Начальное состояние:")
print(lst1)
print("\nДобавление элемента спереди(prepend):")
lst1.prepend(5)
lst1.prepend(10)
print(lst1)
print("\nДобавление элемента(20) сзади(append):")
lst1.append(20)
print(lst1)
print("\nДобавление элемента после элемента(7) с указанным индексом(insert_after):")
lst1.insert_after(1, 7)
print(lst1)
print("\nДобавление элемента перед элемента(6) с указанным индексом(insert_before):")
lst1.insert_before(1,6)
print(lst1)
print("\nУдаление первого элемента(remove_first()):")
lst1.remove_first()
print(lst1)
print("\nУдаление последнего элемента(remove_last()):")
lst1.remove_last()
print(lst1)
print("\nУдаление элемента по индексу(1)(remove_at):")
lst1.remove_at(1)
print(lst1)
print("\nУдаление первого вхождения указанного вхождения(6)(remove_value(value)):")
print(lst1.remove_value(6))
print(lst1)

lst1.prepend(20)
lst1.prepend(10)
lst1.prepend(7)
lst1.prepend(50)
print("\nПоиск индекса первого вхождения значения(7) (возвращает индекс или -1, find):")
print(lst1.find(7))
print("Не нашлось значения(100):")
print(lst1.find(100))
print("\nПоиск индексов всех вхождений значения (возвращает список индексов,find_all):")
print(lst1.find_all(7))
print("\nПроверка наличия значения(50) в списке (возвращает True/False, contains):")
print(lst1.contains(50))
print("Не нашлось значения(100, contains):")
print(lst1.contains(100))
print("\nПолучение значения элемента по индексу(get(index)):")
print(lst1.get(1))
print("\nВозвращает количество элементов(len):")
print(len(lst1))
print("\nСтроковое представление списка(str):")
print(str(lst1))
print("\nИтерация списка(iter):")
for i in lst1:
    print(i)
print("\nОбращение по индексу(0,1, __getitem__):")
print(lst1[0], lst1[1])
print("\nОператор in(7), __contains:")
print(7 in lst1)
print("\nКонкатенация двух списков(__add__):")
lst12 = SinglyLinkedList()
lst12.prepend(20)
lst12.prepend(999)
lst12.prepend(888)
print("Первый список:",lst1)
print("Второй список:",lst12)
print("Cумма списков lst1 + lst12:", lst1 + lst12)
print("\nПовторение списка(__mul__):")
print('Список:',lst1)
print("Список, умноженный на 2:",lst1 * 2)
print("\nИзменение по индексу(нулевой индекс заменим на 999), __setitem__")
print("Список:", lst1)
lst1[0] = 999
print("После:", lst1)
print("\nОчистить список(clear):")
lst1.clear()
print("Список:",lst1)
print("\nУдалить первый из пустого списка")
try:
    lst1.remove_first()
except EmptyStructureError as e:
    print(f"ошибка: {e}")
print("\nПолучить элемент из пустого списка")
try:
    value = lst1.get(0)
except EmptyStructureError as e:
    print(f"ошибка: {e}")
print("\nДобавить элемент после индекса в пустом списке")
try:
    lst1.insert_after(0,10)
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst1.prepend(1)
print("\nДобавить элемент после индекса, которого нету в списке")
try:
    lst1.insert_after(5,10)
except IndexError as e:
    print(f"ошибка: {e}")
lst1.clear()
print("\nДобавить элемент перед индексом в пустом списке")
try:
    lst1.insert_before(0,10)
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst1.prepend(10)
print("\nДобавить элемент перед индексом, которого нету в списке")
try:
    lst1.insert_before(30,999)
except IndexError as e:
    print(f"ошибка {e}")
lst1.clear()
print("\nУдалить последний элемент в пустом списке")
try:
    lst1.remove_last()
except EmptyStructureError as e:
    print(f"ошибка {e}")
print("\nУдалить значение из пустого списка")
try:
    lst1.remove_value(13)
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst1.prepend(15)
print("\nУдалить знчание, которого нету в списке")
try:
    lst1.remove_value(100)
except ValueNotFoundError as e:
    print(f"ошибаа: {e}")
print("\nДостать данные по индексу, которого нету")
try:
    lst1.get(10)
except IndexError as e:
    print(f"ошибка: {e}")
lst1.clear()
print("\nУдалить значение по индексу в пустом списке")
try:
    lst1.remove_at(5)
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst1.prepend(10)
print("\nУдалить значение по индексу, которого нету в списке")
try:
    lst1.remove_at(10)
except IndexError as e:
    print(f"ошибка: {e}")
lst1.clear()
print("\nДостать значение по индексу в пустом списке(__getitem__)")
try:
    lst1[4]
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst1.prepend(10)
print("\nДостать значение по индексуб которого нету в списке(__getitem__)")
try:
    lst1[5]
except IndexError as e:
    print(f"ошибка: {e}")
lst1.clear()
print("\nИзменить значение в пустом списке(__setitem__)")
try:
    lst1[5] = 5
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst1.prepend(10)
print("\nИзменить значение в списке у индекса, которого нету в списке(__setitem__)")
try:
    lst1[3] = 10
except IndexError as e:
    print(f"ошибка: {e}")
a = 5
print("\nСумма списка и другого типа данных(int)(__add__)")
try:
    lst1 + a
except TypeError as e:
    print(f"ошибка: {e}")
b = 67.67
print("\nУмножение списка на не целое число b = 67.67(__mul__)")
try:
    lst1 * b
except TypeError as e:
    print(f"ошибка: {e}")



print("\n\nДемонстрация работы двусвязного спика(DoublyLinkedList)")
lst2 = DoublyLinkedList()
print("\nНачальное состояние")
print(lst2)
print("\nДобавление элемента вперед(prepend):")
lst2.prepend(10)
print("lst2.prepend(10):", lst2)
lst2.prepend(5)
print("lst2.prepend(5):", lst2)
print("\nДобавление элемента назад(append):")
lst2.append(15)
print("lst2.append(15):", lst2)
print("\nДобавление перед индексом(insert_before):")
lst2.insert_before(1, 7)
print("lst2.insert_before(1, 7):", lst2)
print("\nДобавление после индекса(nsert_after)")
lst2.insert_after(2,13)
print("lst2.insert_after(2,13):", lst2)
print("\nУдаление первого элемента(remove_first):")
lst2.remove_first()
print(lst2)
print("\nУдаление последнего элемента(remove_last)")
lst2.remove_last()
print(lst2)
print("\nУдаление элемента по индексу(1)(remove_at):")
lst2.remove_at(1)
print("lst2.remove_at(1):",lst2)
print("\nУдаление первого вхождения указанного значения(13)(remove_value(value):")
lst2.remove_value(13)
print("lst2.remove_value(13):", lst2)
print("\nПоиск индекса первого вхождения значения(7) (возвращает индекс или -1, find)")
print(lst2.find(7))
print("Если значения нету:")
print(lst2.find(999))
lst2.prepend(6)
lst2.prepend(1)
lst2.append(7)
print(f"\nДвусвязный список: {lst2}")
print("\nНайти индексы всех вхождений(7)(find_all):")
print(lst2.find_all(7))
print("\nПроверка наличия числа в списке(contains):")
print("lst2.contains(7):",lst2.contains(7))
print("lst2.contains(99):",lst2.contains(99))
print("\nПолучение значения по индексу(get):")
print("lst2.get(2):",lst2.get(2))
print(f"\nДвусвязный список lst2: {lst2}")
print("Количесиво элементов(len): len(lst2):", len(lst2))
print("\nСтроковое представление списка lst2:", str(lst2))
print("\nИтерация списка(iter):")
for i in lst2:
    print(i)
print("\nОбращение по индексу(__getitem__):")
print('lst2[1]:', lst2[1])
print("\nИзменение по идексу(__setitem__):")
lst2[1] = 8
print("lst2[1] = 8, lst2 =", lst2)
print("\nОператор in(__contains__):")
print("8 in lst2:", 8 in lst2)
lst22 = DoublyLinkedList()
lst22.prepend(1)
lst22.prepend(7)
print("\nВторой двусвязный спискок lst22:", lst22)
print("Конкатенация двух списков(__add__) lst2 + lst22:",lst2+lst22)
print("\nПовторение списка(__mul__):")
print("lst2 =", lst2)
print("lst2 * 2:", lst2 * 2)

print("\nОчистка списка")
lst2.clear()
print("lst2.clear() = ", lst2)

print("\n==Обработка ошибок в двусвязном списке==")
print("\nДобавление элемента после индекса в пустом списке(insert_after):")
try:
    lst2.insert_after(2,4)
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst2.prepend(10)
print("\nДобавление элемента после индекса, которого нету в списке(insert_after):")
try:
    lst2.insert_after(3,5)
except IndexError as e:
    print(f"ошибка: {e}")
lst2.clear()
print("\nДобавление элемента перед индексом в пустом списке(insert_before):")
try:
    lst2.insert_before(3,6)
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst2.prepend(15)
print("\nДобавление элемента перед индекссом, которого нету в списке(insert_before):")
try:
    lst2.insert_before(5,15)
except IndexError as e:
    print(f"ошибка: {e}")
lst2.clear()
print("\nУдаление первого элемента из пустого списка(remove_first):")
try:
    lst2.remove_first()
except EmptyStructureError as e:
    print(f"ошибка: {e}")
print("\nУдаление последнего элемента из пустого списка(emove_last)Ж")
try:
    lst2.remove_last()
except EmptyStructureError as e:
    print(f"ошибка: {e}")
print("\nУдаление элемента по индексу из пустого списка(remove_at):")
try:
    lst2.remove_at(5)
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst2.prepend(10)
print("\nУдаление элемента по индексу, которого нету в списке(remove_at):")
try:
    lst2.remove_at(10)
except IndexError as e:
    print(f"ошибка: {e}")
lst2.clear()
print("\nУдаление элемента по значению из пустого списка(remove_value):")
try:
    lst2.remove_value(15)
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst2.prepend(10)
print("\nУдаление значения из списка, в котором нету этого значения(remove_value):")
try:
    lst2.remove_value(13)
except ValueNotFoundError as e:
    print(f"ошибка: {e}")
lst2.clear()
print("\nПолучение занчения по индексу в пустом списке(get):")
try:
    lst2.get(4)
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst2.prepend(10)
print("\nПолучение значения по индексу, которого нету в списке(get):")
try:
    lst2.get(4)
except IndexError as e:
    print(f"ошибка: {e}")
lst2.clear()
print("\nОбращение к индексу в пустом списке(__getitem__):")
try:
    lst2[5]
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst2.prepend(10)
print("\nОбращение к индексу, которого нету в списке(__getitem__):")
try:
    lst2[10]
except IndexError as e:
    print(f"ошибка: {e}")
lst2.clear()
print("\nИзменение ао индексу в пустом списке(__setitem):")
try:
    lst2[5] = 10
except EmptyStructureError as e:
    print(f"ошибка: {e}")
lst2.prepend(7)
print("\nИзменение по индексу в списке, в котором отсутствует этот индекс(__setitem__):")
try:
    lst2[5] = 10
except IndexError as e:
    print(f"ошибка: {e}")
t = 15
print("\nСложение списка и другого типа данных, t(int),(__add__):")
try:
    lst2 + t
except TypeError as e:
    print(f"ошибка: {e}")
e = 11.1
print("\nУмножение списка на тип данных,отличный от int, e = 11,1 ,(__mul__):")
try:
    lst2 * e
except TypeError as e:
    print(f"ошибка: {e}")

print("\n\n==Демонстрация работы стека==\n")
stk = Stack()
print("Начальное состояние:", stk)
print("\nДобавление элемента в стек(push):")
stk.push(10)
print("stk.push(10):",stk)
stk.push(5)
print("stk.push(5):", stk)
print("\nУдалить и вернуть элемент с вершины стека(pop):")
print("stk.pop():", stk.pop())
print("stk =", stk)
print("\nПросмотреть элемент на вершине стека без удаления(pewk):")
print("stk.peek():",stk.peek()    )
print(stk)
print("\nПроверить пустой ли стек(is_empty):")
print("Стек:", stk)
print('stk.is_empty:', stk.is_empty())
print("\nРазмер стека(size):")
print("Стек:", stk)
print("stk.size:", stk.size())
print("\n==Ошибки в стеке==")
stk.pop()
print("\nУдалить элемент из пустого стека(pop):")
try:
    stk.pop()
except EmptyStructureError as e:
    print(f"ошибка: {e}")
print("\nПросмотреть первый элемент в пустом стеке(peek):")
try:
    stk.peek()
except EmptyStructureError as e:
    print(f"ошибка: {e}")
print("\n\n==Демонстрация работы очереди==")
que = Queue()
print("\nНачальное положение:",que)
print("\nДобавление элемента в конец очереди(enqueue):")
que.enqueue(5)
print("que.enqueue(5) :",que)
que.enqueue(15)
print("que.enqueue(15) :",que)
print("\nУдалить и вернуть элемент из начала очереди(dequeue):")
print("que.dequeue()", que.dequeue())
print("\nПосмотреть первый элемент без удаления(front()):")
print("Очередь сейчас:", que)
print("que.front():", que.front())
print("\nпроверка, пуста ли очередь(is_empty()):")
print("Очередь сейчас:", que)
print("que.is_empty():", que.is_empty())
print("\nРазмер очереди(size):")
print(que.size())
print("\n==Ошибки в очереди==")
que.dequeue()
print("очередь:", que)
print("\nУдалить элемент из пустой очереди(dequeue):")
try:
    que.dequeue()
except EmptyStructureError as e:
    print(f"ошибка: {e}")
print("\nПросмотреть элемент в пустой очереди(front):")
try:
    que.front()
except EmptyStructureError as e:
    print(f"ошибка: {e}")
print("\n\nПереход между структурами:")
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
stack = Stack.from_queue(queue)
print("В используя метод стека:",stack.pop())
new_queue = Queue.from_stack(stack)
print("В очереди:", new_queue.front())