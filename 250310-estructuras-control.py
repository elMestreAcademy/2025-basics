from random import randint, choice


def ifelse():
    restos = randint(0, 6)
    cantidad_gente = 4

    if restos >= cantidad_gente:
        print("Todos cenamos restos")
    elif restos > 1:
        print("Algunos cenamos restos")
    else:
        print("Nadie cena restos")

    print("A la cama")


def interrupcion_bucle():
    control = 0
    while control < 100:
        control += 1
        if control == 10:
            break
        print(control)


def ejemplo_break():
    maximo = 10
    while True:
        numero = randint(0, maximo)
        if numero == maximo:
            break
        print(numero)


def ejemplo_continue():
    control = 0
    while control < 10:
        control += 1
        if not (control % 3):  # no imprimas los divisibles entre 3
            continue
        print(control)


# ifelse()
# interrupcion_bucle()
# ejemplo_break()
ejemplo_continue()
