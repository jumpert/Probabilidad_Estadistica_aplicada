import random

# Definimos las opciones (puertas) del juego
opciones = [1, 2, 3]

# Función para seleccionar una puerta al azar
def seleccionar_puerta():
    return random.choice(opciones)

# Función para elegir la puerta ganadora al azar
def seleccionar_ganadora():
    return random.choice(opciones)

# Función que revela una puerta no ganadora
def revelar_puerta(puertas, seleccion, ganadora):
    for puerta in puertas:
        if puerta != seleccion and puerta != ganadora:
            return puerta

# Función que cambia de puerta
def cambiar_puerta(puertas, seleccion, revelada):
    for puerta in puertas:
        if puerta != seleccion and puerta != revelada:
            return puerta

# Función que simula el juego
def jugar(cambiar):
    print("____________________________________________________________________________")
    # Seleccionamos una puerta al azar
    seleccion = seleccionar_puerta()
    print("Seleccionamos la puerta", seleccion)

    # Seleccionamos la puerta ganadora al azar
    ganadora = seleccionar_ganadora()

    # Revelamos una puerta no ganadora
    puertas_restantes = [puerta for puerta in opciones if puerta != seleccion]
    print("Puertas restantes:", puertas_restantes)
    revelada = revelar_puerta(puertas_restantes, seleccion, ganadora)
    print("Revelamos la puerta", revelada)

    if cambiar:
        # Cambiamos de puerta
        puertas_restantes = [puerta for puerta in opciones if puerta != seleccion and puerta != revelada]
        seleccion = cambiar_puerta(puertas_restantes, seleccion, revelada)
        print("Cambiando de puerta, seleccionamos la", seleccion)

    # Comprobamos si hemos ganado
    return seleccion == ganadora

ganadas = 0
for i in range(100):
    if jugar(True):
        ganadas += 1
print("Ganadas cambiando:", ganadas)
