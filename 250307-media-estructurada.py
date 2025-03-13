
def introducir_numero():
    return int(input("dame un numero: "))


def calculos(datos_fuente):
    cantidad = len(datos_fuente)
    suma = sum(datos_fuente)
    media = suma / cantidad

    return [media, suma, cantidad]


def mostrar_paso(lista):
    datos = calculos(lista)
    print("La media de los ultimos n numeros: ", datos[0])


def mostrar_resumen(lista):
    datos = calculos(lista)

    print("Lista de num introducidos: ", lista)
    print("Cantidad de elementos:     ", datos[2])
    print("Suma total:                ", datos[1])
    print("Media final:               ", datos[0])


def main():
    lista = []
    while True:
        nuevo_numero = introducir_numero()
        if nuevo_numero == 0:
            break

        lista.append(nuevo_numero)
        mostrar_paso(lista)

    mostrar_resumen(lista)


main()
