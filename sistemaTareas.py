"""Forto de la semana VII.
Estudiante JOEL DE JESUS DIAZ TOROCA
FACULTAD DE INGENERIA EN SISTEMAS"""

#Una lista, una pila, una cola y un árbol.
tareas = [] #Se utiliza para almacenar las tareas que el usuario agrega.
historial = [] #Se utiliza para llevar un registro de las acciones realizadas (agregar, editar, eliminar tareas, etc.).
tareasUrgentes = []  #Se utiliza para almacenar tareas que el usuario considera urgentes.
arbolTareas = {  #Representa una estructura jerárquica de tareas organizadas por áreas de un proyecto.
    "Proyecto principal": {
        "Fronted": ["Diseño UI", "Revision de estudios"],
        "Backend": ["API Login", "Gestion de BD"]
    }
}
#Funcion para agregar tareas(Funcion principal)//
#Permite al usuario ingresar una nueva tarea, que se agrega a la lista tareas y se registra en el historial.
def agregarTareas():
    tarea = input("Ingrese la nueva tarea: ")
    tareas.append(tarea)
    historial.append(f"Tarea Agregada con exito: {tarea}")

#Funcion para mostrar las tareas ya agregadas.
#Muestra todas las tareas actualmente registradas. Si no hay tareas, informa al usuario.
def mostrarTareas():
    print("\n Tareas actuales")
    if not tareas:
        print("No hay tareas Registradas")
    else:
        for i, t in enumerate(tareas):
            print(f"{i+1}. {t}")

#Funcion para mostrar las tareas ya registradas.
#Permite al usuario editar una tarea existente. Muestra las tareas, solicita el índice de la tarea a editar,
#y si el índice es válido, actualiza la tarea y registra la acción en el historial.
def editarTareas():
    mostrarTareas()
    indice= int(input("Ingrese el numero de la tarea a editar: "))-1
    if  0<= indice <len(tareas):
        nueva= input("Ingrese el nuevo nombre de la tarea: ")
        historial.append(f"tarea Editada: {tareas[indice]} -> {nueva}")
        tareas[indice]=nueva
        print("Tarea Actualizada.")
    else:
        print("Indice fuera de rango")

#Funcion para elimincar la tarea,Permite al usuario eliminar una tarea.
def eliminartareas():
    mostrarTareas()
    indice= int(input("Ingrese el numero de la tarea a eliminar: "))
    if 0<= indice <len(tareas):
        historial.append(f"Tarea Eliminada: {tareas[indice]}")
        tareas.pop(indice)
        print("Tarea eliminada con exito ^_^")
    else:
        print("Indice invalido!!")


#Funcion para tareas urgentes
def urgenciaVital():
    urgente = input("Ingrese una tarea urgente: ")
    tareasUrgentes.append(urgente)
    historial.append (f"Tarea Urgente Agregada : {urgente}")
    print("Tarea urgente registrada")

#Funcion para procesar las tareas urgentes,Procesa la primera tarea en la lista de tareas urgentes
#(simulando que se está trabajando en ella). Si no hay tareas urgentes, informa al usuario.
def procesarUrgente():
    if tareasUrgentes:
        tarea = tareasUrgentes.pop(0)
        print(f"Procesando tarea urgente {tarea}")
        historial.append(f"Tarea urgente procesada: {tarea}")
    else:
        print("No hay tareas urgentes.")

# Muestra la estructura jerárquica del proyecto, listando las áreas y sus respectivas subtareas.
def mostrarArbol():
    print("\n Organizacion Jerarquica del proyecto: ")
    for area, subtareas, in arbolTareas["Proyecto principal"].items():
        print(f"{area}")
        for sub in subtareas:
            print("  ->",sub)
#Funcion para ver la cola de las tareas urgentes,Muestra las tareas urgentes en la cola.
#Indica cuál es la primera y la última tarea en la cola.
def verColaUrgente():
    if tareasUrgentes:
        print("\n Tareas urgentas")
        print(f"primera en la cola {tareasUrgentes}")
        print(f"Ultima en la cola {tareasUrgentes}")
    else:
        print("\n No hay tareas urgentes en la cola")
#Muestra las últimas 10 acciones registradas en el historial, en orden inverso (de más reciente a más antiguo).
def mostrarHistorial():
    print("\n Historial de acciones")
    for i in reversed(historial [-10:]):
        print(f"*, {i}")

def menu():
    while True:
        print("\n 📆MENU DE SISTEMA DE GESTION DE TAREAS") 
        print("1️⃣ Agregar Tarea")
        print("2️⃣ Editar Tarea") 
        print("3️⃣ Eliminar Tarea") 
        print("4️⃣ Mostrar Tareas") 
        print("5️⃣ Agregar Tarea Urgente") 
        print("6️⃣ Procesar Tarea Urgente") 
        print("7️⃣ Mostrar el historial de Cambios") 
        print("8️⃣ Ver estructura del arbol de tareas") 
        print("9️⃣ Ver primera y ultima tarea urgente de la cola") 
        print("🔟 Salir") 
        opcion = int(input("Seleccione una opcion: "))

        if opcion ==1: 
            agregarTareas() 
        elif opcion ==2: 
            editarTareas() 
        elif opcion ==3: 
            eliminartareas() 
        elif opcion ==4: 
            mostrarTareas () 
        elif opcion==5: 
            urgenciaVital() 
        elif opcion ==6: 
            procesarUrgente() 
        elif opcion==7: 
            mostrarHistorial()
        elif opcion ==8:
            mostrarArbol()
        elif opcion ==9:
            verColaUrgente()
        elif opcion ==10:
            print ("Hasta la vista!!")
            break
        else:
            print("Opcion no valida, intente de nuevo")

menu()
        
"""Este El programa permite al usuario gestionar tareas de manera efectiva, proporcionando funcionalidades para agregar,
editar, eliminar y procesar tareas, así como para manejar tareas urgentes y visualizar el historial de acciones.

Referencias:
Open class"""
  

