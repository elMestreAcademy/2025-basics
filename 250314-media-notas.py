def introducir_numero(abajo, arriba):
    nota = None
    equivocado = False
    while nota is None or nota < abajo or nota > arriba:
        if equivocado:
            print("Introduce un número comprendido entre " + abajo " y " + arriba)
        nota = float(input("dame un numero: "))
        equivocado = True

    return nota


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
    cantidad_asignaturas = 14
    nota_minima = -100
    nota_maxima = 100

    while len(lista) < cantidad_asignaturas:
        nuevo_numero = introducir_numero(nota_minima, nota_maxima)
        lista.append(nuevo_numero)
        mostrar_paso(lista)

    mostrar_resumen(lista)


main()
