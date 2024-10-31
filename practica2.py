print(" ")#deja un espacio a la hora de ejecutar
print("oscar alonso reyes yañez 3w_1208:programa de diciionario sobre creditos y materias")
print(" ")#deja un espacio a la hora de ejecutar

# Diccionario con las asignaturas
asignaturas = {
    'Matemáticas': 0,
    'ecosistemas': 0,
    'leoye': 0,
    'programacion 2.1': 0,
    'programacion 2.2': 0
}
print(" ")#deja un espacio a la hora de ejecutar
# Ingresar los créditos para cada asignatura
for asignatura in asignaturas.keys():
    creditos = int(input(f"Ingrese los créditos para {asignatura}: "))
    asignaturas[asignatura] = creditos
print(" ")#deja un espacio a la hora de ejecutar
# se suman y cuentan los créditos totales
total_creditos = 0
print(" ")#deja un espacio a la hora de ejecutar
# Mostrar los créditos de cada asignatura
for asignatura, creditos in asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos")
    total_creditos += creditos
print(" ")#deja un espacio a la hora de ejecutar
# Mostrar el número total de créditos del parcial o unidad
print(f"El total de créditos del curso es {total_creditos}")
print(" ")#deja un espacio a la hora de ejecutar

