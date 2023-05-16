# # IF
# # if valorBoolean:
# #     bloque_de_código

invitado = False

if invitado:
    print('¡Hola, bienvenido adelante!')


# # # #####################

# # IF-ELSE
# # if valorBoolean:
# #     bloque_de_código_TRUE
# # else:
# #     Bloque_de_código_FALSE

invitado = False

if invitado:
    print('¡Hola, bienvenido adelante!')
else:
    print('Lo siento no puedes ingresar')


# Operadores relacionales: >,<,>=,<=,!=,==

nota = float(input('Ingresa tu nota'))
if nota <= 5:
    print('Desaprobado')
else:
    print('Aprobado')

# Operadores lógicos: not, and, or

aprobado = True
ocupado = True

if aprobado and not ocupado:
    print('¡Debes festejar a tu estilo!')
else:
    print('Lo entiendo, siempre hay algo por hacer...')


# #IF-ELIF-ELSE

nota = float(input('Ingresa tu nota: '))

if nota >= 0 and nota <= 5:
    print('desaprobado')
elif nota >= 6 and nota < 7:
    print('bien')
elif nota >= 7 and nota < 9:
    print('Muy Bien')
elif nota >= 9 and nota <= 10:
    print('Sobresaliente')
else:
    print('Nota fuera de rango')
