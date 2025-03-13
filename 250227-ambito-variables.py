variable_global = "Esto es global"


def funcion():
    def funcion_dentro_de_funcion():
        variable = "99x"
        print(variable)
        print(variable_global)

    variable = 3
    print(variable)
    funcion_dentro_de_funcion()


def otra_funcion():
    variable = 1
    print(variable)
    print(variable_global)


variable = "patata"

otra_funcion()
funcion()
print(variable)
