class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularBuffer2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        
    def append(self, item):
        if self.size < self.capacity:
            new_node = Node(item)
            if self.size == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
                new_node.prev = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                new_node.next = self.head
                self.head.prev = new_node
                self.tail = new_node
            self.size += 1
        else:
            print("Buffer is full, item cannot be added.")
    
    def pop(self):
        if self.size > 0:
            item = self.head.value
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            self.size -= 1
            return item
        else:
            print("Buffer is empty, no item to pop.")

    ### Плюсы реализации:
    - Эффективность добавления и удаления элементов: Использование двусвязного списка позволяет обходить операции сдвига, значительно повышая производительность при добавлении и удалении элементов.
    - Производительность с использованием больших буферов: При больших буферах вставка и удаление элементов будут выполняться быстрее, чем в реализации с использованием массива.

    ### Минусы реализации :
    - Больший объем занимаемой памяти: Двусвязный список требует больше памяти для хранения указателей на предыдущий и следующий элементы, что может привести к излишнему использованию памяти.


