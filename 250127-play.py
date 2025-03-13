cantidad = 288
precio_play = 500
precio_calcetines = 100

if cantidad >= precio_play:
    cantidad -= precio_play
    print("Compro la play")
    if cantidad >= precio_calcetines:
        cantidad -= precio_calcetines
        print("Compro calcetines")

print("nos queda", cantidad)
