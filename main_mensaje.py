import csv
from datos.direccion import Direccion
from datos.fecha import Fecha
from datos.empleados import Empleado
from datos.sistema import Sistema

txtempleados = "txt/Empleados.txt"
txtpassword = "txt/Password.txt"

sistema = Sistema()
empleados = sistema.empleados

sistema.cargarEmpleados(txtempleados)
sistema.cargarPassword(txtpassword)



#imprime todos los empleados
current = sistema.empleados.head
while current is not None:
    print(current.get_data())  # Aquí asumimos que get_data() devuelve el valor almacenado en el nodo
    current = current.get_next()
    
print(sistema.noEmpleados)

buscado = sistema.buscarUsuario(1001140290)

password = "mAno"

'''if buscado:
    buscado.setPassword(password)
    print(buscado)'''

#imprime direcciones en memoria
'''def imprimir_empleados(double_list):
    current_node = double_list.head
    while current_node is not None:
        print(current_node.__str__())
        current_node = current_node.get_next()
    
imprimir_empleados(sistema.empleados)'''