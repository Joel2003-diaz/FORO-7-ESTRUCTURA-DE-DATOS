"""Forto de la semana VII.
Estudiante JOEL DE JESUS DIAZ TOROCA
FACULTAD DE INGENERIA EN SISTEMAS"""

cola= []

cantidad = int(input("Cuantas tareas urgentes desea guardar?: ")) 

for i in range(cantidad): 
    tarea = input(f"Ingrese la accion {i+1}: ") 
    cola.append(tarea)

print (cola) 

print("\n Tarea urgentes en la cola") 
for i in cola: 
    print(i) 

#Mostrar primer y ultimo elemento 
print("\n Primero en la cola", cola [0]) 
print("\n Ultimo en la cola", cola [-1])

#Procesar tareas
atender= input("\n Desea atender la primera tarea (s/n): ").lower()
if atender =='s':
    tareaAtendida = cola.pop(0)
    print(f"La tarea atendida fue {tareaAtendida}")

print (cola)