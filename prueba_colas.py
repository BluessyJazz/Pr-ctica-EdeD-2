from dequeues.queue import Queue

# Crear una cola
my_queue = Queue()
print(my_queue)

# Encolar elementos
my_queue.enqueue(1)
print(my_queue.first())

my_queue.enqueue(2)
print(my_queue.first())

my_queue.enqueue(3)
print(my_queue.first())



'''# Verificar el primer elemento
assert my_queue.first() == 1

# Desencolar elementos
my_queue.dequeue()
my_queue.dequeue()

# Verificar el primer elemento actualizado
assert my_queue.first() == 3

# Verificar si la cola está vacía
assert not my_queue.is_empty()

print("Pruebas de cola exitosas.")'''