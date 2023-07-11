#Grupo: Estefany Clara, Gonzalo Paz y Juan Pérez

""" Monty Hall Game, es un juego de azar en el que se debe elegir una puerta de tres,
una de ellas tiene un premio y las otras dos no tienen nada.
El juego consiste en que el presentador de un programa de televisión abre una de las puertas
que no tiene premio, y te da la opción de cambiar de puerta o no.
El objetivo es ganar el premio."""

def monty_hall():
    import random
    """ Inicializamos las variables que vamos a utilizar:
        repeticiones: cantidad de veces que se va a repetir el juego.
        cambiar: respuesta del usuario si quiere cambiar de puerta o no, en True o False respectivamente.
        salir_cambio: variable que nos permite salir del bucle de cambiar de puerta.
        salir_modalidad: variable que nos permite salir del bucle de modalidad.
        puertas: lista con las puertas.
        premio: puerta que tiene el premio.
        eleccion: puerta que elige el usuario.
        aciertos: cantidad de veces que el usuario gana el premio.
        perdidos: cantidad de veces que el usuario pierde el premio."""

    aciertos = 0
    perdidos = 0
    cambio_si = 0
    cambio_no = 0
    cambio_sim = 0
    salir_modalidad = False 

    while salir_modalidad == False:
        modalidad = input("Desea jugar manualmente o en simulación? \nPulsa M para manual y S para simulación: ").lower()
        if modalidad == "m":
            puertas = [1, 2, 3]
            premio = random.choice(puertas)
            print("Las posibilidades son: puerta 1, puerta 2 y puerta 3")
            eleccion = int(input("Elije una puerta: "))
            """ Validamos que la elección sea válida. Si no es válida, se le vuelve a preguntar al usuario. 
                Si es válida, se sale del bucle."""            
            while eleccion not in puertas:
                print("Respuesta no válida, intente nuevamente.")
                eleccion = int(input("Elije una puerta: "))
            if eleccion == premio:
                """Si la elección es igual al premio, se abre una puerta vacia y
                se le pregunta al usuario si quiere cambiar de puerta."""
                print("El presentador abre la puerta ", [x for x in puertas if x != premio and x != eleccion][0])
                puertas.remove([x for x in puertas if x != premio and x != eleccion][0])
                print("Las posibilidades son: puerta ", puertas[0], " y puerta ", puertas[1])
                salir_cambio = False
                while salir_cambio == False:
                    #Validamos que la respuesta sea válida. Si no es válida, se le vuelve a preguntar al usuario.
                    cambiar_str = input("¿Desea cambiar de puerta? S/N: ").lower()
                    if cambiar_str == "s":
                        salir_cambio = True
                        print("El usuario cambia de puerta")
                        eleccion = [x for x in puertas if x != eleccion][0]
                        #Imprimimos la elección del usuario y el premio.
                        print("La elección del usuario es la puerta ", eleccion)
                        print("Perdiste! El premio estaba en la puerta ", premio)
                        print("Te llevas un premio consuelo: un abrazo")
                        perdidos += 1
                        cambio_si += 1
                    elif cambiar_str == "n":
                        salir_cambio = True
                        print("El usuario no cambia de puerta")
                        print("Ganaste un AUTO 0km! El premio estaba tras la puerta ", premio)
                        aciertos += 1
                        cambio_no += 1
                    else:
                        print("Respuesta no válida, intente nuevamente.")
            else:
                """ Si la elección es diferente al premio, se abre una puerta vacia y
                    se le pregunta al usuario si quiere cambiar de puerta."""
                print("El presentador abre la puerta ", [x for x in puertas if x != premio and x != eleccion][0])
                puertas.remove([x for x in puertas if x != premio and x != eleccion][0])
                print("Las posibilidades son: puerta ", puertas[0], " y puerta ", puertas[1])
                salir_cambio = False
                while salir_cambio == False:
                    cambiar = input("¿Desea cambiar de puerta? S/N: ").lower()
                    if cambiar == "s":
                        salir_cambio = True
                        print("El usuario cambia de puerta")
                        eleccion = [x for x in puertas if x != eleccion][0]
                        print("La elección del usuario es la puerta ", eleccion)
                        print("Ganaste un AUTO 0km! El premio estaba tras la puerta ", premio)
                        aciertos += 1
                        cambio_si
                    elif cambiar == "n":
                        salir_cambio = True
                        print("El usuario no cambia de puerta")
                        print("Perdiste! El premio estaba en la puerta ", premio)
                        print("Te llevas un premio consuelo: un abrazo")
                        perdidos += 1
                        cambio_no += 1
                    else:
                        print("Respuesta no válida, intente nuevamente.")
            respuesta = input("¿Desea volver a jugar? S/N: ").lower()
            if respuesta == "s":
                salir_modalidad = False
            elif respuesta == "n":
                salir_modalidad = True
            
        elif modalidad == "s":
            repeticiones = int(input("Ingrese la cantidad de veces que desea repetir el juego: "))
            salir_cambio = False
            
            cambiarStr = input("Desea jugar cambiando de puertas?\nS por si/N por no: ").lower()
            if cambiarStr == "s":
                cambiar = True
                cambio_sim += 1
            elif cambiarStr == "n":
                cambiar = False
            else:
                print("Respuesta no valida")

            for i in range(repeticiones):
                puertas = [1, 2, 3]
                premio = random.choice(puertas)
                eleccion = random.choice(puertas)
                
                if eleccion == premio:
                    puertas.remove([x for x in puertas if x != premio and x != eleccion][0])                    
                    if cambiar == True:
                        eleccion = [x for x in puertas if x != eleccion][0]
                        perdidos += 1
                    else :
                        aciertos += 1
                else:
                    puertas.remove([x for x in puertas if x != premio and x != eleccion][0])
                    if cambiar == True:
                        eleccion = [x for x in puertas if x != eleccion][0]
                        aciertos += 1
                    else :
                        perdidos += 1
            respuesta = input("¿Desea volver a jugar? S/N: ").lower()
            if respuesta == "s":
                salir_modalidad = False
            elif respuesta == "n":
                salir_modalidad = True

        else:
            print("Respuesta no válida, intente nuevamente.")

    if cambio_no == 0 and cambio_si == 0:
        if cambio_sim == 0:
            print("El jugador respondio que NO queria cambiar la puerta.")
        else:
            print("El jugador respondio que SI queria cambiar la puerta.")
    else:
        print("El jugador cambio de puerta ", cambio_si, " veces y no cambio de puerta ", cambio_no, " veces.")

    print(f"Jugadas totales: {aciertos+perdidos} Aciertos: {aciertos} y Perdidos: {perdidos}")
    print("Las frecuencia relativas son: Ganar:", "{:.2f}".format(aciertos/(aciertos+perdidos)),"y Perder:", "{:.2f}".format(perdidos/(aciertos+perdidos)))
    print("La probabilidad de ganar el auto es de:", "{:.2f}".format((aciertos/(aciertos+perdidos))*100), "%")
    print("La probabilidad de perder el auto es de:", "{:.2f}".format((perdidos/(aciertos+perdidos))*100), "%")
    
    
monty_hall()
terminar = input("\nPulse ENTER para terminar ")
    