cantidad = 288
precio_play = 500
precio_calcetines = 100
tengo_la_play = False
cantidad_para_caprichos = 3
mes = 0

while not tengo_la_play:
    mes += 1
    cantidad += cantidad_para_caprichos
    if cantidad >= precio_play:
        cantidad -= precio_play
        tengo_la_play = True
        if cantidad >= precio_calcetines:
            cantidad -= precio_calcetines
            print("Compro calcetines")

    print("mes: ", mes, " nos queda", cantidad)

print("SAN SE ACABO")
print("ACABAMOS EN EL MES ", mes)
print("NOS QUDA EN EL BOTE: ", cantidad)