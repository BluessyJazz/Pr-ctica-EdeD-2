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

# Pedir al usuario que ingrese su cedula y contraseña
cedula_ingresada = int(input("Ingrese su número de identificación (cedula): "))
contraseña_ingresada = str(input("Ingrese su contraseña: "))

# Verificar el acceso y obtener el rol del usuario
rol_usuario = sistema.verificarAcceso(cedula_ingresada, contraseña_ingresada)

if rol_usuario is not None:
    print(f"Bienvenido, usted es un {rol_usuario}.")  
else:
    print("Acceso denegado. Verifique sus datos.")

#imprime todos los empleados
'''current = sistema.empleados.head
while current is not None:
    print(current.get_data())  # Aquí asumimos que get_data() devuelve el valor almacenado en el nodo
    current = current.get_next()'''

