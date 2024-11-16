class Queue:
    def __init__(self):
        self.items = []  # Создаём пустой список для очереди

    def enqueue(self, item):
        self.items.append(item)  # Добавляем элемент в конец очереди

    def is_empty(self) -> bool:
        return len(self.items) == 0  # Проверяем, пуста ли очередь

    def dequeue(self):
        if not self.is_empty():  # Проверяем, есть ли элементы в очереди
            return self.items.pop(0)  # Удаляем и возвращаем первый элемент
        return None  # Если очередь пуста, возвращаем None

    def show_queue(self):
        print(" ".join(map(str, self.items)))  # Выводим элементы через пробел

# Создаём объект класса Queue
q = Queue()

# Добавляем элементы в очередь
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Выводим элементы очереди
q.show_queue()
# Вывод: 1 2 3

# Удаляем элементы из очереди
q.dequeue()
q.dequeue()

# Выводим элементы очереди
q.show_queue()
# Вывод: 3
