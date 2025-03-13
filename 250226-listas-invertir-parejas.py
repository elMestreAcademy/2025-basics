from random import randint


def crear_lista_aleatoria(max):
    lista = []
    cantidad = 0
    while cantidad < max:
        lista.append(randint(0, 10))
        cantidad += 1

    return lista


def invierte_posiciones(lista):
    posicion = 0
    while posicion < len(lista):
        print(lista[posicion + 1], lista[posicion])
        posicion += 2


posicion = "delante"

lista = crear_lista_aleatoria(3)
print(lista)
invierte_posiciones(lista)
print(posicion)
