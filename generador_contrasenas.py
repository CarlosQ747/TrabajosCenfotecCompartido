import random
import string

def generar_contrasena(longitud, usar_especiales=True, evitar_ambiguos=True):
    if longitud < 8:
        raise ValueError("La longitud mínima de la contraseña es 8 caracteres.")

    # Caracteres base
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
    
    if usar_especiales:
        caracteres += string.punctuation

    if evitar_ambiguos:
        caracteres_ambiguos = "O0oIl1|"
        caracteres = ''.join(c for c in caracteres if c not in caracteres_ambiguos)

    # Asegurar al menos un carácter de cada tipo
    seleccion = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits)
    ]
    if usar_especiales:
        seleccion.append(random.choice(string.punctuation))

    while len(seleccion) < longitud:
        seleccion.append(random.choice(caracteres))

    random.shuffle(seleccion)
    return ''.join(seleccion)

# Menú de prueba interactivo
if __name__ == "__main__":
    try:
        print("\n Generador de Contraseñas Personalizado\n")
        longitud = int(input(" Longitud deseada (mínimo 8): "))
        usar_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'
        evitar_ambiguos = input("¿Evitar caracteres ambiguos como 'O', '0', 'l'? (s/n): ").lower() == 's'

        contrasena = generar_contrasena(longitud, usar_especiales, evitar_ambiguos)
        print(f"\n Contraseña generada:\n{contrasena}\n")

    except ValueError as e:
        print(f" Error: {e}")
