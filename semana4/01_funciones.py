#####################################################

#                    FUNCIONES

#####################################################

# definición de una función
def saludar():
    ''' Esta función imprime un saludo --- DocString (cadena de documentación)'''
    print('Hola comisión 3 --- Hola Mundo desde una función')


# La definición de la función no ejecuta el cuerpo de la misma.
# para ejecurarla debemos realizar una llamada a la función

# saludar()





# Definición los valores recibidos se llaman parámetros
def saludo_lugar(nombre, localidad):
    ''' Esta función imprime un saludo con el nombre y localidad que son pasados como parámetros'''
    print(f'{nombre} nos saluda desde {localidad}')



# Llamada de la función los valores que se envían se llaman argumentos
# Parámetros por posición
# saludo_lugar('Miguel', 'Charata')


# Parámetros por nombre
#saludo_lugar(localidad='Charata', nombre='Miguel')

# Llamada sin argumentos TypeError- Parámetros por defecto

def saludo_lugar(nombre = None, localidad = None):
    ''' Esta función imprime un saludo con el nombre y localidad que son pasados como parámetros'''
    if not nombre and not localidad:
        print('Debe enviar los parámetros de nombre y localidad')
    elif not nombre:
        print('También debe enviar el parámetro nombre')
    elif not localidad:
        print('También debe enviar el parámetro localidad')
    else:
        print(f'{nombre} nos saluda desde {localidad}')

# saludo_lugar(localidad='Charata')


#######################################################
# Argumentos indeterminados
# Por posición

def saludo_lugar(*args):
    ''' Esta función imprime un saludo con los nombres y localidades que son pasados como parámetros'''
    for arg in args:
        print(f'{arg[0]} nos saluda desde {arg[1]}')

# saludo_lugar(('Miguel', 'Charata'), ('Roque', 'Tandil'), ('Nara', 'Resistencia'))


# Por nombre

def usuario(**kwargs):
    ''' Esta función imprime un saludo con los nombres y localidades que son pasados como parámetros'''
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')



# usuario(nombre='Miguel', localidad='Charata', profesion='Desarrollador')

# Por posición y nombre
def por_posicion_nombre(*args, **kwargs):
    compras = 0
    for arg in args:
        compras += arg
        print(f'Argumentos posicionales: subtotal - {arg}')
    print(f'Argumentos posicionales: total comprado {compras}')

    for clave, valor in kwargs.items():
        print(f'Argumento por nombre: {clave} : {valor}')

# por_posicion_nombre(5500, 3400, 25000, id = 93, nombre='Miguel', pago='Contado')


