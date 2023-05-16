'''
1-Escribir un programa que pida al usuario su edad
y muestre por pantalla si es mayor de edad (18 años o más) o no.
'''

edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


'''
2-Escribir un programa que pida al usuario un número entero
y muestre por pantalla si es positivo, negativo o cero.
'''

num = int(input("Ingresa un número entero: "))
if num > 0:
    print(num, "es un número positivo")
elif num < 0:
    print(num, "es un número negativo")
else:
    print("El número es cero")


'''
3-Escribir un programa que pida al usuario dos números
y muestre por pantalla cuál de ellos es mayor.
'''

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 > num2:
    print(num1, "es mayor que", num2)
elif num1 < num2:
    print(num2, "es mayor que", num1)
else:
    print("Los dos números son iguales")


'''
4-Escribir un programa que pida al usuario una nota del 0 al 10
y muestre por pantalla si está aprobado (5 o más) o no.
'''

nota = float(input("Ingresa una nota del 0 al 10: "))
if nota >= 5:
    print("Estás aprobado")
else:
    print("Estás suspendido")


'''
5-Escribir un programa que pida al usuario un número entero
y muestre por pantalla si es par o impar.
'''

num = int(input("Ingresa un número entero: "))
if num % 2 == 0:
    print(num, "es un número par")
else:
    print(num, "es un número impar")


'''
6-Escribir un programa que pida al usuario un número entero
y muestre por pantalla si es múltiplo de 2 y de 3 a la vez.
'''

num = int(input("Ingresa un número entero: "))
if num % 2 == 0 and num % 3 == 0:
    print(num, "es múltiplo de 2 y de 3 a la vez")
else:
    print(num, "no es múltiplo de 2 y de 3 a la vez")


'''
7-Escribir un programa que pida al usuario un carácter
y muestre por pantalla si es una letra mayúscula, una letra minúscula, un número o un carácter especial.
'''

caracter = input("Ingresa un carácter: ")
if caracter.isupper():
    print("El carácter es una letra mayúscula")
elif caracter.islower():
    print("El carácter es una letra minúscula")
elif caracter.isdigit():
    print("El carácter es un número")
else:
    print("El carácter es un carácter especial")


'''
8- Escribir un programa que pida al usuario una cadena de caracteres
y muestre por pantalla si contiene la letra "a".
'''

cadena = input("Ingresa una cadena de caracteres: ")
if "a" in cadena:
    print(cadena, "contiene la letra 'a'")
else:
    print(cadena, "no contiene la letra 'a'")


'''
9-Escribir un programa que pida al usuario tres números
y muestre por pantalla el mayor de ellos.
'''

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
if num1 > num2 and num1 > num3:
    print(num1, "es el número mayor")
elif num2 > num1 and num2 > num3:
    print(num2, "es el número mayor")
else:
    print(num3, "es el número mayor")



'''
10-Escribir un programa que pida al usuario una letra
y muestre por pantalla si es una vocal o una consonante.
'''

letra = input("Ingresa una letra: ")
if letra in "aeiouAEIOU":
    print(letra, "es una vocal")
else:
    print(letra, "es una consonante")



'''
11-Escribir un programa que pida al usuario dos números
y muestre por pantalla la suma de ellos solo si ambos son pares.
'''

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("La suma de", num1, "+", num2, "=", num1+num2)
else:
    print("Los números no son pares")