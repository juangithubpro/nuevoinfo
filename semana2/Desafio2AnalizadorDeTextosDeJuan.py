# analisis de texto 

analisis_texto = input("ingrese 1 texto: ")
letras1 = input("ingresar 1 letras a eleccion: ")
letras2 = input("ingresar 1 letras a eleccion: ")
letras3 = input("ingresar 1 letras a eleccion: ")

analisis_texto = analisis_texto.lower()
letras1 = letras1.lower()
letras2 = letras2.lower()
letras3 = letras3.lower()

conteo_1 = analisis_texto.count(letras1)
conteo_2 = analisis_texto.count(letras2)
conteo_3 = analisis_texto.count(letras3)

palabras = analisis_texto.split()
conteo_palabras = len(palabras)


primera_letra = analisis_texto[0]
ultima_letra = analisis_texto[-1]

texto_inverso = analisis_texto[::-1]

print(f"La letra '{letras1}' aparece {conteo_1} veces en el texto.")
print(f"La letra '{letras2}' aparece {conteo_2} veces en el texto.")
print(f"La letra '{letras3}' aparece {conteo_3} veces en el texto.")
print(f"El texto conitene {conteo_palabras} palabras.")
print(f"La primera letra es: {primera_letra} y la ultima letra es: {ultima_letra}")
print(f"El texto inverso es asi: {texto_inverso}")

aparece_python = "python " in analisis_texto.lower()
if aparece_python:
    print("La palabra python aparece en el texto")
else:
    print("La palabra python no aparece")




