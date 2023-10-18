from dequeues.queue import Queue

# Crear una cola
my_queue = Queue()

# Encolar elementos
my_queue.enqueue(1)
print(my_queue.first())
my_queue.enqueue(2)
print(my_queue.first())
my_queue.enqueue(3)
print(my_queue.first())

# Verificar el primer elemento
assert my_queue.first() == 1

# Desencolar elementos
my_queue.dequeue()
print(my_queue.first())
print(my_queue.dequeue())
print(my_queue.first())

# Verificar el primer elemento actualizado
assert my_queue.first() == 3

# Verificar que la cola no está vacía
assert not my_queue.is_empty()

print("Pruebas de cola exitosas.")
