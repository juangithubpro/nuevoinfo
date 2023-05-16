# # Listas []

# # índice    0   1   2   3   4
# vocales = ['a','e','i','o','u']

# print(vocales[0])
# print(vocales[1])
# print(vocales[-1])
# print(vocales[-2])


# # ############################


# factura = ['test@email.com.ar','A', 20, 1550, 8502.9]

# print(f'Factura {factura[1]}-{factura[2]}-{factura[3]} importe ${factura[4]} enviada al email: {factura[0]}')



# Métodos integrados

lista_frutas = ['ciruela', 8, 'manzana', 'pera', 4, 'naranja', 5]

print('append agrega un elemento al final de la lista')
print(lista_frutas)
lista_frutas.append('pera')
print(lista_frutas)
print('------')



# print('index devuelve el índice de un elemento, si no existe da error')
print(lista_frutas.index('pera'))
print()



# print('insert agrega un elemento en un índice')
print(lista_frutas)
lista_frutas.insert(3, 5)
print(lista_frutas)
print()



# print('count cuenta elementos')
# print(lista_frutas.count('ciruela'))

lista_frutas.clear()
print(lista_frutas)
# ############################

