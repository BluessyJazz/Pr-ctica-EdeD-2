from double_list import DoubleList

# Crear una lista doblemente enlazada
my_list = DoubleList()

# Agregar elementos al principio y al final
my_list.addFirst(5)
my_list.addFirst(10)
my_list.addLast(15)
my_list.addLast(20)

# Imprimir los primeros y últimos elementos
print(f"Primer elemento: {my_list.first()}")
print(f"Último elemento: {my_list.last()}")

# Eliminar el primer y último elemento
my_list.removeFirst()
my_list.removeLast()

# Imprimir el tamaño de la lista
print(f"Tamaño de la lista: {my_list.size}")

# Agregar elementos antes y después de un nodo específico
my_list.addBefore(my_list.tail, 25)
my_list.addAfter(my_list.head, 30)

# Eliminar un nodo específico de la lista
removed_data = my_list.remove(my_list.head.next)

# Imprimir los elementos restantes en la lista
current = my_list.head
while current is not None:
    print(current.get_data())
    current = current.get_next()
