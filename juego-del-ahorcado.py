import random


def obtenerPalabraSecreta() -> str:
    palabras = ['python', 'javascript', 'java', 'angular', 'django', 'tenserflow', 'react', 'typescript', 'git', 'flask']
    return random.choice(palabras)

def mostrarProgreso(palabraSecreta, letrasAdivinadas):
    adivinado = ''

    for letra in palabraSecreta:
        if letra in letrasAdivinadas:
            adivinado += letra
        else: 
            adivinado += '_'
    
    return adivinado

def juegoAhorcado():
    palabraSecreta = obtenerPalabraSecreta()
    letrasAdivinadas = []
    intentos = 7
    juegoTerminado = False

    print('¡Bienvenido al juego del ahorcado!')
    print(f'Tienes {intentos} instentos para adivinar la palabra secreta')
    print(mostrarProgreso(palabraSecreta, letrasAdivinadas), "La cantidad de letras de la palabra es : ", len(palabraSecreta))

    while not juegoTerminado and intentos > 0:
        adivinanza = input('Introduce una letra: ').lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print('Por favor introduce una letra válida (sólo escribir una letra)')
        elif adivinanza in letrasAdivinadas:
            print('Ya has utilizado esa letra, prueba con otra letra')
        else:
            letrasAdivinadas.append(adivinanza)

            if adivinanza in palabraSecreta:
                print(f'Muy bien has acertado, la letra {adivinanza} está en la palabra')
            else:
                intentos -= 1
                print(f'Lo siento, la letra "{adivinanza}", no se encuentra en la palabra, cuentas con {intentos} intentos')
        progresoActual = mostrarProgreso(palabraSecreta, letrasAdivinadas)
        print(progresoActual)

        if '_' not in progresoActual:
            juegoTerminado = True
            palabraSecreta = palabraSecreta.capitalize()
            print(f"¡Felicitaciones has ganado! La palabra completa es: '{palabraSecreta}'")

    if intentos == 0:
        palabraSecreta = palabraSecreta.capitalize()
        print(f"Lo sentimos se te han terminado los intentos, la palabra secreta es '{palabraSecreta}'")

juegoAhorcado()