print(" ")#deja un espacio a la hora de ejecutar
print("oscar alonso reyes yañez 3w_1208:programa sobre materias")
print(" ")#deja un espacio a la hora de ejecutar
# Lista de materias del parcial
asignaturas = ['Matemáticas', 'ecosistemas', 'pro 2.1', 'pro 2.2', 'Leoye']
print(" ")#deja un espacio a la hora de ejecutar
# Diccionario para almacenar las calificaciones
notas = {}
print(" ")#deja un espacio a la hora de ejecutar
# Preguntar al usuario por la calificacion en cada parcial
for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota que has sacado en: {asignatura}: "))
    notas[asignatura] = nota
print(" ")#deja un espacio a la hora de ejecutar
# Mostrar las calificaciones por pantalla
for asignatura, nota in notas.items():
    print(f"En {asignatura} tu calificacion fue de: {nota}")
print(" ")#deja un espacio a la hora de ejecutar