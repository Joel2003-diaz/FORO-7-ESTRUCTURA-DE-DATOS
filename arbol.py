"""Forto de la semana VII.
Estudiante JOEL DE JESUS DIAZ TOROCA
FACULTAD DE INGENERIA EN SISTEMAS"""


#Arbol basico con diccionario de diccionario.
arbol= {
    "Proyecto principal: ":{
        "fase 1": ["Analisis", "Diseño"],
        "fase 2": ["Desarrolo", "pruebas"]
    }
}

print(arbol)
print("Estructura del proyecto")
for fase in arbol ["Proyecto principal: "]:
    print(f"-> {fase}")
    for tarea in arbol["Proyecto principal: "][fase]:
        print("  -", tarea)