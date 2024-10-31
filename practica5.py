print(" ")#deja un espacio a la hora de ejecutar
print("oscar alonso reyes yañez 3w_1208:programa sobre clases")
print(" ")#deja un espacio a la hora de ejecutar
# Lista de materias
asignaturas = ['Matemáticas', 'ecosistemas', 'por 2.1', 'pro 2.1', 'Leoye']
print(" ")#deja un espacio a la hora de ejecutar
# Diccionario para almacenar las calificaciones
notas = {}
print(" ")#deja un espacio a la hora de ejecutar
# Preguntar al usuario por la nota en cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota que has sacado en {asignatura}: "))
    notas[asignatura] = nota
print(" ")#deja un espacio a la hora de ejecutar
# Mostrar las notas por pantalla
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")
print(" ")#deja un espacio a la hora de ejecutar