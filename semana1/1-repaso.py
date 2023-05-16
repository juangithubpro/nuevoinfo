
# # comentario de una sola línea el intérprete ignora los comentarios.

# '''
# comentario
# multi línea
# '''

# #
# # https://docs.python.org/es/3.10/
# #

# # Tipos de datos                                                 Inmutable crea nuevo objeto

# nulo = None                             # NoneType  Nulo                                        Inmutable
# entero = 2023                           # int       número entero                               Inmutable
# real = 20.23                            # float     número real                                 Inmutable
# complejo = 4 + 3j                       # complex   númer complejo                              Inmutable
# booleano = True                         # bool      booleano                                    Inmutable
# cadena = 'Ahora soy string'             # str       cadena de texto                             Inmutable
# cadena2= '4'
#                                         ## Estructura de datos ##
# conjunto = {'pera', 5, True}            # set       colección de datos ordenados e irrepetibles Mutable

# lista = ['pera',True,'pera',5]          # list      vector con distintos tipos de datos         Mutable

# tupla = ('pera',True,'pera',5)          # tuple

# diccionario = {1: 'pera', 2: 'uva'}     # dict      


# # el código se ejecuta de arriba hacia abajo.
# # case sensitive, distingue entre mayúscula y minúscula en el nombre de variables.

# ###########################
# # Algunas funciones integradas

# print(cadena)                       # Imprime por pantalla
# type(tupla)                         # Devuelve el tipo de datos
# input('Ingresa un texto: ')         # Imprime por pantalla y devuelve lo ingresado por teclado
# len(cadena)                         # Devuelve el tamamaño la variable.

# str(real)                           # Convierte a tipo cadena de texto
# int(cadena2)                        # Convierte a tipo entero
# float(cadena2)                      # Convierte a tipo real
# bool(lista)                         # Convierte a tipo booleano

# # PowerShell

# ########################
# hola = 'Hola '
# mundo = 'mundo'
# hola_mundo = hola + mundo
# print(hola_mundo)
# print('-------')

# # Asignación mútiple
# hola2, mundo2, dos = 'Hola ', 'Mundo ', 2
# print(hola2)
# print(mundo2)
# print(dos)
# print('-------')


# ##################################################################


cadena2 = 'rojo;verde;azul'

lista = cadena2.split(';')
print(type(lista), lista)
print('-------')

color1, color2, color3 = cadena2.split(';')
print(color1)
print(color2)
print(color3)
