# Paso por valor y paso por referencia

"""
• Paso por valor: el paso por valor de los argumentos, hace una copia del valor de las 
variables en los respectivos parámetros. Cualquier modificación del valor del 
parámetro, no afecta a la variable externa correspondiente porque estamos 
modificando la copia.
Tradicionalmente, los tipos simples se pasan por valor: Enteros (Int), flotantes (float), cadenas (string), lógicos (bool)
"""

"""
Ejemplo de paso por valor
Como ya sabemos los números se pasan por valor y crean una copia dentro de la 
función, por eso no les afecta externamente lo que hagamos con ellos:
"""

# def doblar_valor(numero):
#     numero = numero * 2
# n = 10
# doblar_valor(n)
# print(n) #10

#########################################################################################

"""
• Paso por referencia: el paso por referencia copia en los parámetros la dirección de 
memoria de las variables que se usan como argumento. Esto implica que realmente 
hagan referencia al mismo objeto/elemento y cualquier modificación del valor en el 
parámetro afectará a la variable externa correspondiente.
Tradicionalmente, los tipos compuestos se pasan por referencia: Listas, diccionarios, 
conjuntos
"""

"""
Ejemplo de paso por referencia
Sin embargo las listas u otras colecciones, al ser tipos compuestos se pasan por 
referencia, y si las modificamos dentro de la función estaremos modificándolas también 
fuera:
"""

# def cubo(coleccion):
#     for indice in range(len(coleccion)):
#         coleccion[indice]=coleccion[indice] ** 3
#     print(coleccion)


# lista = [2,5,8]

# Ejemplo 1
"""
Creo una copia de mi lista para no modificarla con el metodo .copy()
"""
# lista_2=[2,4,8]
# def cubo(coleccion):
#     coleccion_a_modificar = coleccion.copy()
    
#     for indice in range(len(coleccion_a_modificar)):
#         coleccion_a_modificar[indice]=coleccion_a_modificar[indice]**3
#     print(coleccion_a_modificar)

# cubo(lista_2)
# print(lista_2)













