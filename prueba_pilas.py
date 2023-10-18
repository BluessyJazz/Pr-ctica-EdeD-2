from dequeues.stack import Stack

# Crear una pila
my_stack = Stack()

# Apilar elementos
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Verificar el elemento superior
assert my_stack.top() == 3

# Desapilar elementos
my_stack.pop()
my_stack.pop()

# Verificar el elemento superior actualizado
assert my_stack.top() == 1

# Verificar si la pila está vacía
assert not my_stack.is_empty()

print("Pruebas de pila exitosas.")
