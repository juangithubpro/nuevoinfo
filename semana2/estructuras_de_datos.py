'''
1-Crear un diccionario con los nombres de tres frutas y sus respectivos precios y mostrar el diccionario completo.
'''

frutas = {"manzana": 519, "banana": 439, "naranja": 669}
print(frutas)


'''
2-Crear una lista con los nombres de tres ciudades y agregar una cuarta ciudad al final de la lista.
'''

ciudades = ["Londres", "París", "Madrid"]
ciudades.append("Roma")
print(ciudades)


'''
3-Crear una lista con los nombres de tres países y mostrar el segundo país de la lista.
'''

paises = ["Argentina", "Francia", "Croacia"]
print(paises[1])


'''
4-Crear un diccionario con los nombres de tres personas y sus respectivas edades. Mostrar la edad de la tercera persona en el diccionario.
'''

personas = {"Juan": 25, "María": 30, "Pedro": 35}
print(personas["Pedro"])


'''
5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número más grande en el conjunto.
'''

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numero_mas_grande = max(numeros)
print(numero_mas_grande)


'''
6-Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número de elementos en el conjunto.
'''

impares = {1, 3, 5, 7, 9}
print(len(impares))


'''
7-Crear un diccionario con los nombres de tres ciudades y sus respectivas poblaciones. Agregar una cuarta ciudad al diccionario con su respectiva población. Mostrar el diccionario resultante.
'''

ciudades = {"Nueva York": 8623000, "Londres": 8982000, "Tokio": 13929286}
ciudades["México"] = 8918653
print(ciudades)


'''
8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_inversos = numeros[::-1]
print(numeros_inversos)


'''
9-Crear una lista con los nombres de tres países y ordenar la lista en orden alfabético. Mostrar la lista resultante.
'''

paises = ["México", "Canadá", "Estados Unidos"]
paises.sort()
print(paises)


'''
10-Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la lista. Mostrar la lista resultante.
'''

frutas = ["manzana", "banana", "naranja"]
del frutas[1]
print(frutas)


'''
11-Crear una lista con los nombres de tres animales y agregar una cuarta animal al principio de la lista. Mostrar la lista resultante.
'''

animales = ["gato", "perro", "ratón"]
animales.insert(0, "conejo")
print(animales)


'''
12-Crear una lista con los nombres de tres países y reemplazar el segundo país de la lista por otro país. Mostrar la lista resultante.
'''

paises = ["Estados Unidos", "México", "Canadá"]
paises[1] = "Argentina"
print(paises)


'''
13-Crear una lista con los nombres de tres colores y agregar dos colores más al final de la lista. Mostrar la lista resultante.
'''

colores = ["azul", "rojo", "verde"]
colores.extend(["amarillo", "naranja"])
print(colores)


'''
14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los elementos de la tupla.
'''

numeros = (1, 2, 3, 4, 5)
suma_numeros = sum(numeros)
print(suma_numeros)

