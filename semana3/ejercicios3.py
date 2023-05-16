# ejercicio 1

""" palabra = input("ingrese una palabra: ")
for letra in palabra:
    print("las letras son: ", letra) """

# ejercicio 2

""" numero = int(input("ingrese un numero: "))

suma = 0

for i in range(1, numero + 1):
    suma += i 

print(f"la suma de todos los numero naturales hasta {numero} es: {suma}") """


# ejercicio 3 

""" numero = int(input("ingrese un numero para la tabla: "))
i = 1
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")  
    i += 1 """

# ejercicio 4 

""" for i in range(1, 101):
    if i % 2 == 0:
        print(i) """ 

# ejercicio 5 

""" for i in range(1, 101):
    if i % 2 == 1:
        print(i) """

# ejercicio 5 

""" sumar = 0 

for i in range(1, 101, 2):
    sumar += i
print("la suma de todos los numeros del 1 al 100 es: ", sumar) """


# ejercicio 6

""" palabra = input("ingrese una palabra: ")

palabra_inversa = palabra[::-1]

print("la palabra en forma inversa es: ", palabra_inversa) """


# ejercicio 7

""" palabra = input("ingrese una palabra: ")

palabra_inversa = palabra [::-1]

if palabra == palabra_inversa:
    print("es un palíndromo")
else:
    print("no es un palíndromo") """ 


# ejercicio 8

""" frase = input("ingrese una frase: ")

palabra = frase.split()
conteo = len(palabra)

print(f"la frase tiene {conteo} palabras") """

# ejercicio 10

""" texto = input("ingrese un texto: ")

vocales = "aeiouAEIOU"
resultado = ""

for letra in texto:
    if letra.lower() in vocales:
        letra = letra.upper()
    resultado += letra    
print("el texto con las vocales mayuscula es: ", resultado) """

# ejercicio 13

""" asterisco = int(input("ingrese un numero: "))

for i in range(1, asterisco + 1):
    print((asterisco - i) * "", end="")
    print((i - 1) * "*") """

# ejercicio 14

""" triangulo = int(input("ingrese un numero: "))

for i in range(1, triangulo + 1):
    for j in range(i):
        print(i, end=" ")
    print() """ 

# ejercicio 15

texto = input("ingresar un texto: ")

letras = "abcdefghijklmopqrstuvwxyz"

for letras in texto:
    if letra.lower() 



