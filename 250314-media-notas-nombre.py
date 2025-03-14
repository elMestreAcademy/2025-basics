def introducir_nota(abajo, arriba, asignatura):
    nota = None
    equivocado = False
    while nota is None or nota < abajo or nota > arriba:
        if equivocado:
            print("Introduce un número comprendido entre " + str(abajo) + " y " + str(arriba))
        nota = float(input("Nota de " + asignatura + ": "))
        equivocado = True

    return nota


def calculos(datos_fuente):
    cantidad = len(datos_fuente)
    suma = sum(datos_fuente)
    media = suma / cantidad

    return [media, suma, cantidad]


def mostrar_resumen(lista):
    datos = calculos(lista)

    print()
    print("Lista de num introducidos: ", lista)
    print("Cantidad de elementos:     ", datos[2])
    print("Suma total:                ", datos[1])
    print("Media final:               ", datos[0])


def main():
    lista = []
    asignaturas = [
        "Mates",
        "Lengua",
        "Historia",
        "Inglés"
    ]

    nota_minima = 0
    nota_maxima = 10

    for asignatura in asignaturas:
        lista.append(introducir_nota(nota_minima, nota_maxima, asignatura))

    mostrar_resumen(lista)


main()
