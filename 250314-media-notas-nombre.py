def introducir_nota(abajo, arriba, concepto):
    nota = None
    equivocado = False

    while (nota is None) or (nota < abajo) or (nota > arriba):
        if equivocado:
            print("Introduce un número comprendido entre " + str(abajo) + " y " + str(arriba))
        nota = float(input("Nota de " + concepto + ": "))
        equivocado = True

    return nota


def calculos(datos_fuente):
    cantidad = len(datos_fuente)
    suma = sum(datos_fuente)
    media = suma / cantidad

    return [cantidad, suma, media]


def mostrar_resumen(lista):
    datos = calculos(lista)

    print()
    print("Lista de num introducidos: ", lista)
    print("Cantidad de elementos:     ", datos[0])
    print("Suma total:                ", datos[1])
    print("Media final:               ", datos[2])


def main():
    notas = []
    asignaturas = [
        "Mates",
        "Lengua",
        "Historia",
        "Inglés"
    ]

    nota_minima = 0
    nota_maxima = 10

    for elemento in asignaturas:
        notas.append(introducir_nota(nota_minima, nota_maxima, elemento))

    mostrar_resumen(notas)


main()
