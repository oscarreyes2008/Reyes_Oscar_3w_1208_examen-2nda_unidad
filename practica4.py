print(" ")#deja un espacio a la hora de ejecutar
print("oscar alonso reyes yañez 3w_1208:programa sobre datos personales")
print(" ")#deja un espacio a la hora de ejecutar
# Solicitar información al usuario
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
direccion = input("¿Cuál es tu dirección? ")
telefono = input("¿Cuál es tu número de teléfono? ")
print(" ")#deja un espacio a la hora de ejecutar
# Guardar la información en un diccionario
informacion_usuario = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}
print(" ")#deja un espacio a la hora de ejecutar
# Mostrar la información por pantalla
print(f"{informacion_usuario['nombre']} tiene {informacion_usuario['edad']} años, vive en {informacion_usuario['direccion']} y su número de teléfono es {informacion_usuario['telefono']}.")
print(" ")#deja un espacio a la hora de ejecutar