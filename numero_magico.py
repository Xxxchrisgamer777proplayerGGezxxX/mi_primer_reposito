import random

def jugar_numero_magico():
    intentos= 5
    numero= random.randint(0,50)

    while intentos > 0:
        seleccion_usuario= int(input(f"Tienes {intentos} intentos para adivinar. Ingresa el numero: "))

        if seleccion_usuario == numero:
           print(f"Acertaste, el numero elegido es: {numero}")
           return
        elif seleccion_usuario < numero:
             print("El numero es mas alto. Intenta nuevamente")
        else:
            print("El numero es mas bajo. Intenta nuevamente")
        
        intentos -=1

    if intentos == 0:
        print(f"No has adivinado. El numero es {numero}")

if __name__ == "__main__":
    jugar_numero_magico()