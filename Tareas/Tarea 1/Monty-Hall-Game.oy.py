#Grupo: Estefany Clara, Gonzalo Paz y Juan Pérez
""" Monty Hall Game, es un juego de azar en el que se debe elegir una puerta de tres,
una de ellas tiene un premio y las otras dos no tienen nada.
El juego consiste en que el presentador de un programa de televisión abre una de las puertas
que no tiene premio, y te da la opción de cambiar de puerta o no.
El objetivo es ganar el premio."""
def monty_hall():
    import random
    """ La variable repeticiones es la cantidad de veces que se va a repetir el juego.
    La variable cambiar es la respuesta del usuario si quiere cambiar de puerta o no.
    La variable aciertos es la cantidad de veces que el usuario gana el premio.
    La variable perdidos es la cantidad de veces que el usuario pierde el premio."""

    repeticiones = int(input("Cuantas veces quieres jugar? "))
    cambiarStr = input("S por si/N por no: ").lower()
    if cambiarStr == "s":
        cambiar = True
    elif cambiarStr == "n":
        cambiar = False
    else:
        print("Respuesta no valida")
    
    aciertos = 0
    perdidos = 0
    for i in range(repeticiones):
        puertas = [1, 2, 3]
        premio = random.choice(puertas)
        #eleccion = int(input("Elije una puerta: "))
        eleccion = random.choice(puertas)
        if eleccion == premio:
            """ Si la eleccion del usuario es igual al premio, se le pregunta si quiere cambiar de puerta.
            Si la respuesta es "s" se le cambia la puerta y se le dice que perdió el premio.
            Si la respuesta es "n" se le dice que ganó el premio."""
            print("vacia", [x for x in puertas if x != premio and x != eleccion][0])
            print("Quiere cambiar de puerta?")
            #cambiar = input("S por si/N por no: ").lower()
            if cambiar:
                eleccion = [x for x in puertas if x != premio and x != eleccion][0]
                
                print("Perdiste!\nTu premio consuelo es un pendrive de 512MB")
                perdidos += 1
            else:
                print("Ganaste un auto!")
                aciertos += 1
        else:
            """ Si la eleccion del usuario es diferente al premio, se le pregunta si quiere cambiar de puerta.
            Si la respuesta es "s" se le cambia la puerta y se le dice que ganó el premio.
            Si la respuesta es "n" se le dice que perdió el premio."""
            print("Quiere cambiar de puerta?")
            #cambiar = input("S por si/N por no: ").lower()
            if cambiar:
                eleccion = premio
                print("Ganaste un auto!")
                aciertos += 1
            else:
                print("Perdiste!\nTu premio consuelo es un pendrive de 512MB")
                perdidos += 1
        print("El premio se encuentra tras la puerta", premio)
        print("Abriste la puerta", eleccion)
        print("La otra puerta es", [x for x in puertas if x != premio and x != eleccion][0])
    
    print("Quiere volver a jugar?")
    """ Si la respuesta es "s" se vuelve a repetir el juego.
    Si la respuesta es "n" se imprime la cantidad de veces que se ganó y se perdió el premio,
    el porcentaje de veces que se ganó y se perdió el premio y se agradece al usuario por jugar."""
    respuesta = input("S por si/N por no: ").lower()
    if respuesta == "s":
        monty_hall()
    else:
        print("Aciertos:", aciertos)
        print("Perdidos:", perdidos)
        print("Porcentaje de aciertos:", (aciertos/repeticiones)*100, "%" )
        print("Porcentaje de perdidos:", (perdidos/repeticiones)*100, "%" )
        print("Gracias por jugar!")

monty_hall()        #Llamada a la función monty_hall() para que se ejecute el juego.
