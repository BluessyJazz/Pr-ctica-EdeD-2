import sys

sys.path.append("..")

from listas.list import List

# Crear una lista
my_list = List()

# Agregar elementos a la lista
my_list.add(1)
my_list.add(2)
my_list.add(3)

# Verificar si se agregaron correctamente
assert my_list.size() == 3

# Eliminar elementos de la lista
my_list.remove(2)

# Verificar si se eliminó correctamente
assert my_list.size() == 2

# Verificar si la lista está vacía
assert not my_list.is_empty()

# Buscar elementos en la lista
assert my_list.search(3) is True
assert my_list.search(2) is False

print("Pruebas de lista exitosas.")


