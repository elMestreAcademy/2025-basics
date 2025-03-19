import random
"""
    Esta es una forma habitual de
    escribir comentarios en Python
    Comentarios que ocupan multiples lineas
"""
# Este es un comentario sencillo


def escribir_centrado(texto):
    mitad = int(len(texto) / 2)
    cantidad_espacios = 40 - mitad
    pre = " " * cantidad_espacios

    print(pre + texto)
    print(pre + "=" * len(texto))


def main():
    print("_" * 80)
    escribir_centrado(random.choice([
        "patata",
        "papa",
        "La Perra de las Galaxias",
        "Estofado de Xampiñones",
        "El Chakacha de tren",
        "·Sayonara, Baby·",
        ">> Aquí <<"
    ]))
    print("_" * 80)


main()
