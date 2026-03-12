import random 

#palabras = ["lluvia", "sol", "nublado"]
#palabra_secreta = random.choice(palabras)
palabras = ["lluvia", "sol", "nublado"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
vidas=5

print ("bienvenido al juego del ahorcado")

while vidas > 0:
    mensaje= ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas: 
         mensaje += letra
         #mensaje = mensaje + letra
        else:
           mensaje += "_"

    print (f"palabra actual: {mensaje}")

    if "_" not in mensaje:
         print ("mision cumplida") 
         break 
           
    print (f"tus vidas son {vidas}")
           
    intento = input("ingrese una letra: ").lower()
 
    if intento in letras_adivinadas:           
        print("prueba otra letra") 
    elif intento in palabra_secreta:
     print ("excelente la letra esta en la palabra") 
     letras_adivinadas.append (intento)
    else:
        print ("incorrecto pierde una vida")
        letras_adivinadas.append (intento)
        vidas -=1 