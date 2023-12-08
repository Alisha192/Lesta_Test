class CircularBuffer1:
	def __init__(self, capacity):
		self.capacity = capacity
		self.buffer = [None] * capacity
		self.size = 0
		self.head = 0
		self.tail = 0

	def append(self, item):
		if self.size < self.capacity:
		self.buffer[self.tail] = item
		self.tail = (self.tail + 1) % self.capacity
		self.size += 1
		else:
		print("Buffer is full, item cannot be added.")

	def pop(self):
		if self.size > 0:
		item = self.buffer[self.head]
		self.buffer[self.head] = None
		self.head = (self.head + 1) % self.capacity
		self.size -= 1
		return item
		else:
		print("Buffer is empty, no item to pop.")
		
### Плюсы реализации:
- Простота реализации: Использование списка позволяет легко определить циклическое поведение буфера и управлять индексами.
- Относительная эффективность дополнения и извлечения:** Обычно, дополнение и извлечение элементов выполняются за O(1) времени.

### Минусы реализации:
- Непроизводительные операции: При удалении элементов возникает необходимость в сдвиге всех оставшихся элементов, что приводит к неэффективным операциям.
