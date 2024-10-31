print(" ")#deja un espacio a la hora de ejecutar
print("oscar alonso reyes yañez 3w_1208:programa sobre materias a repetir")
print(" ")#deja un espacio a la hora de ejecutar

asignaturas = ["matematicas", "programacion 2.1", "ecosistemas", "humanidades", "leoye"]
asignaturas_repetir = []# Lista para almacenar las materias que vas a repetir
print(" ")#deja un espacio a la hora de ejecutar
for asignatura in asignaturas:
    nota = float(input(f"¿Cuál es tu nota en {asignatura}? "))#solicita que ingreses la nota
    
    # Comprobar si la asignatura está aprobada (considerando un 6 como el límite)
    if nota < 6:
        asignaturas_repetir.append(asignatura)
print(" ")#deja un espacio a la hora de ejecutar
if asignaturas_repetir:# Mostrar las asignaturas que se deben repetir
    print("Tienes que repetir las siguientes asignaturas:")#mensaje que te da si tienes que repetir
    for asignatura in asignaturas_repetir:
        print(asignatura)
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")
    #mensaje que se muestra si pasaste tdo
print(" ")#deja un espacio a la hora de ejecutar