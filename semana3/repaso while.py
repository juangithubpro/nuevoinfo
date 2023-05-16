personas = [["juan", 1010], ["marcelo", 2324], ["pedro", 5555], ["elias", 6789]]
inicio_sesion = True
while inicio_sesion:
    Usuario = input("ingrese su usuario: ")
    contraseña = int(input("ingrese su contraseña"))

    for persona in personas:
        if Usuario == persona[0] and persona[1]:
            print(f"bienvenido {persona[0]}")
            inicio_sesion = False
            break
    else:
        print("usuario y contraseña incorrrecto")

print("ingresaste al sistema")





   