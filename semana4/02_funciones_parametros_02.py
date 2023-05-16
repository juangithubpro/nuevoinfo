# Parámetros de una función
def imprimir_mensaje_N_veces(N): #Tiene 1 parámetro
    for i in range(N):
        print("Este es el mensaje " + str(i))

# Programa principal
#imprimir_mensaje_N_veces(3) #Ejemplo sin datos ingresados por el usuario

"""
#Datos ingresados por el usuario
veces= int(input("Ingrese la cantidad de veces que desea imprimir: "))
imprimir_mensaje_N_veces(veces) #Ejemplo con datos ingresados por el usuario
"""

# Otro ejemplo

def multiplicar_por_5(numero):
    print(f"{numero} * 5 = {numero * 5}")

# print("Comienzo del programa")
# multiplicar_por_5(4)

# ----------------------------------------
# Con dos parámetros
def mensaje_personalizado_N_veces(N, mje): #Tiene 2 parámetros
    for i in range(N):
        print(mje)

# Programa principal
#mensaje_personalizado_N_veces(4, "Juan Pablo")

# Variante: función con 2 datos de entrada que recibe como parámetros proporcionados por el usuario. 
# Usamos la misma función pero le pasamos valores nosotros.

"""
cant = int(input("¿Cuántas veces se repetirá el valor? "))
mensaje = input("¿Cuál es el mensaje? ")
mensaje_personalizado_N_veces(cant, mensaje)
"""

# Variante validando el código:
"""
cant = int(input("¿Cuántas veces se repetirá el valor? "))
while cant<=0: #Validamos que el número sea positivo
    print("Dato no válido!")
    cant = int(input("¿Cuántas veces se repetirá el valor? "))
mensaje = input("¿Cuál es el mensaje? ")
while len(mensaje)==0: #Validamos que se haya escrito un mensaje
    print("Debes escribir un mensaje!")
    mensaje = input("¿Cuál es el mensaje? ")
mensaje_personalizado_N_veces(cant, mensaje)
"""

# ------------------------------------------------------

# Parámetros opcionales y por defecto

"""
def saludo(nombre, mensaje="encantado de saludarte"):
    print(f"Hola {}, {}")
saludo("Juan Pablo")
saludo("Juan Pablo", "¿cómo estás?")
"""

# Parámetros opcionales (otro ejemplo)

"""
def calcular_raiz(num, raiz=2):  #Si no recibe un segundo parámetro calcula la raiz cuadrada (2)
    print (num**(1/raiz))

# Prog Ppal
calcular_raiz(4)
calcular_raiz(125,3) #Acá tiene dos parámetros, el número y la raíz, que no necesariamente tiene que estar 
                    #y si no está toma por defecto el 2.
"""

# Parámetros posicionales y parámetros con nombre

"""
def saludo(nombre, mensaje="encantado de saludarte"):
    print(f"Hola {}, {}")

saludo(mensaje="¿Cómo estás?", nombre="Juan Pablo")
saludo(nombre="Juan Pablo", mensaje="¿Cómo estás?")
saludo("Juan Pablo", mensaje="¿Cómo estás?")
"""