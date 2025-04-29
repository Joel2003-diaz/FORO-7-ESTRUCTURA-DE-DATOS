"""Forto de la semana VII.
Estudiante JOEL DE JESUS DIAZ TOROCA
FACULTAD DE INGENERIA EN SISTEMAS"""

pila=[]
cantidad = int(input("Cuantas accciones desea registrar?: "))

#Registrar acciones
for i in range(cantidad):
    accion = input(f"Ingrese la accion{i+1}")
    pila.append(accion)

print(pila)

#Eliminar la ultima accion 
deshacer = input("\n Desea deshacer la ultima accion? (s/n)").lower
if deshacer == 's':
    ultima=pila.pop()
    print("Se elimino la accion {ultima}")

#Mostrar la pila final
print("\n Acciones restantes")
for i in reversed(pila):
    print(f"{i}")
