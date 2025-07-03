import random
import string

"""Genera una contraseña segura con la longitud especificada.
Args:
longitud (int): Longitud deseada de la contraseña.
Returns:
str: Contraseña generada.
"""
def generar_contrasena(longitud):
    if longitud < 8:
        raise ValueError("La longitud mínima de la contraseña es 8 caracteres.")
    caracteres_mayusculas = string.ascii_uppercase
    caracteres_minusculas = string.ascii_lowercase
    caracteres_digitos = string.digits
    caracteres_especiales = string.punctuation

    todos_caracteres = caracteres_mayusculas + caracteres_minusculas + caracteres_digitos + caracteres_especiales

    contrasena = [
        random.choice(caracteres_mayusculas),
        random.choice(caracteres_minusculas),
        random.choice(caracteres_digitos),
        random.choice(caracteres_especiales)
    ]

    contrasena += [random.choice(todos_caracteres) for _ in range(longitud- 4)]

    random.shuffle(contrasena)
    return ''.join(contrasena)

if  name  == " main ":
    longitud = int(input("Ingrese la longitud deseada para la contraseña (mínimo 8 caracteres): "))
    try:
        print("Contraseña generada:", generar_contrasena(longitud))
    except ValueError as e:\
        print(e)

