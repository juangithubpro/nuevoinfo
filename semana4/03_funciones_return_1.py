def contar_letras(texto):
    contador = 0
    for caracter in texto:
        if caracter == " ":
            continue
        else:
            contador = contador + 1
    return contador

def contar_palabras(texto):
    listaPalabras = texto.split()
    cantidadPalabras = len(listaPalabras)
    return cantidadPalabras

def contar_palabra(texto,palabra):
    cuentaPalabra = texto.count(palabra)
    return cuentaPalabra