""" desafio semana """ 
""" juego adivina el numero """ 


import random 


Player = input("Bienvenido al juego de juan Ingrese un Nombre/Apodo/Alias: ")
print("######################################################################")
print(f"Hola {Player} ¿te animarias a adivinar un numero del 1 al 100? ")
print("######################################################################")
print(f"No tan rapido, {Player} no te lo vamos a dejar tan facil")
print(f"Solo tienes 8 vidas")
print(f"No desperdicies ninguna vida")
print("######################################################################")
print(f"¡Suerte joven!")

numero_correcto = random.randint(1, 100)

intentos = 8

while intentos > 0:
    print(f"vidas restantes: {intentos} ")
    numero = input("ingresa un numero joven: ")

    if not numero.isdigit():
        print("Debes ingresar un numero chamaco")
        continue


    numero = int(numero)

    if numero < numero_correcto:
        print("¡Incorrecto! el numero es mayor")
        print("###############################")
    elif numero > numero_correcto:
        print("¡fallaste! es menor")
        print("###############################")
    else:
        print("¡Eres un crack! acertaste el numero")
        print("###################################")
        break

    intentos -= 1 

if intentos == 0:
    print("Se te agotaron los intentos chamaco: ")