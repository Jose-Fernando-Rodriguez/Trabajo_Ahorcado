import random

def elegir_palabra():
    # Lista de palabras para elegir al azar
    lista_palabras = ["HOLA", "LUISA", "EMILYS", "JULIETH", "FERNANDO", "ESTEFANIA"]
    return random.choice(lista_palabras)

def ocultar_palabra(palabra):
    # Crear una lista de guiones para ocultar las letras
    return ["_"] * len(palabra)

def mostrar_palabra(palabra_oculta):
    # Mostrar la palabra oculta con guiones y letras
    return ' '.join(palabra_oculta)

def main():
    palabra = elegir_palabra()
    palabra_oculta = ocultar_palabra(palabra)
    intentos = 6

    print(f"¡Bienvenido!!!!!!! \nAdivina una Palabra!")
    print(f"La palabra contiene {len(palabra)} letras: {mostrar_palabra(palabra_oculta)}")

    while intentos > 0:
        letra = input("INGRESA UNA LETRA o ESCRIBE LA PALABRA COMPLETA: ").upper()  # Convertir a mayúsculas

        if len(letra) == 1:
            if letra in palabra:
                print(f"La letra '{letra}' está en la palabra.")
                # Reemplazar la letra en la lista de guiones
                for i, c in enumerate(palabra):
                    if c == letra:
                        palabra_oculta[i] = letra
                print(f"Palabra oculta con guiones y letras: {mostrar_palabra(palabra_oculta)}")

                # Verificar si se ha adivinado la palabra completa
                if "".join(palabra_oculta) == palabra:
                    print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
                    break
            else:
                print(f"La letra '{letra}' no está en la palabra.")
                intentos -= 1
                print(f"Intentos restantes: {intentos}")
        else:
            if letra == palabra:
                print(f"¡Felicidades! ¡Has adivinado la palabra correctamente!")
                break
            else:
                print(f"La palabra '{letra}' no es correcta.")
                intentos -= 1
                print(f"Intentos restantes: {intentos}")

    if intentos == 0:
        print(f"¡Lo siento! Has agotado tus intentos. La palabra era '{palabra}'. ¡Mejor suerte la próxima vez!")

    jugar_nuevamente = input("¿Deseas empezar con otra palabra? (Sí/No): ").lower()
    if jugar_nuevamente == "si":
        main()
    else:
        print("¡Gracias por jugar!")

if __name__ == "__main__":
    main()
