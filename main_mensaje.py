import csv
from datos.direccion import Direccion
from datos.fecha import Fecha
from datos.empleados import Empleado
from datos.mensajeria import Mensajeria

txtempleados = "txt/Empleados.txt"
txtpassword = "txt/Password.txt"

sistema = Mensajeria()

sistema.cargarEmpleados(txtempleados)
'''sistema.cargarPassword(txtpassword)'''
current = sistema.empleados.head
print(current.item)
'''while current is not None:
    print(current.get_data())  # Aquí asumimos que get_data() devuelve el valor almacenado en el nodo
    current = current.get_next()'''
print(sistema.noEmpleados)

