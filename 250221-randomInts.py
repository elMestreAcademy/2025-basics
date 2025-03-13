import random

def generaNumero(min, max):
    min = 99
    max = 100
    numeroInventado = random.randint(min, max)
    print("por", numeroInventado, "canicas que me he comido")

    return numeroInventado

deuda = generaNumero(1000, 2000) 
mes = generaNumero(1, 12)
print("______")
print( "mes : ", mes)
print( "debe: ", deuda)

