from random import randint

z = "patata"

print(z)

for letra in z:
    print(letra)

print("------------------")

def funcion_con_retorno():
    return 10


def funcion_sin_retorno():
    print(99)


a = funcion_con_retorno()
b = funcion_sin_retorno()

msg = f"a: {a * 7} y b = {b}"

print(msg)
