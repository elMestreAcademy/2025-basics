# Ejemplo 1: Sentencia con múltiples funciones y operadores

resultado = round(sum([abs(x) for x in range(-10, 10) if x % 2 == 0]) / len([i for i in range(1, 20) if i % 3 == 0]), 2) + max(min(a, b), c)


# Ejemplo 2: Sentencia con funciones recursivas y operaciones lógicas

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


valores = [fibonacci(i) for i in range(10) if fibonacci(i) % 2 == 0]
total = sum(valores) * min(valores)


# Ejemplo 3: Sentencia con múltiples estructuras condicionales

if all(isinstance(x, int) for x in lista) and any(x > 10 for x in lista):
    suma = sum([math.sqrt(x) for x in lista if x > 0])
    maximo = max(lista)
    if maximo > suma:
        resultado = maximo / suma
    else:
        resultado = suma / maximo


# Ejemplo 4: Sentencia con funciones y manejo de excepciones

try:
    data = [int(x) for x in input_data.split(",")]
    if len(data) > 5:
        promedio = sum(data) / len(data)
        print("Promedio:", promedio)
    else:
        raise ValueError("Lista demasiado corta")
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Error desconocido:", e)


# Ejemplo 5: Sentencia con operaciones sobre diccionarios y listas

def procesar_datos(datos):
    return {k: sum(v) for k, v in datos.items() if isinstance(v, list)}


info = {"A": [1, 2, 3], "B": [4, 5], "C": "texto"}
resultados = procesar_datos(info)
filtered_results = {k: v for k, v in resultados.items() if v > 5}
print(filtered_results)


# Ejemplo 6: Sentencia con funciones lambda y operaciones complejas

filtro = lambda x: x * 2 if x > 0 else x - 2
resultados = list(map(filtro, [i for i in range(-5, 5)]))
producto = functools.reduce(lambda x, y: x * y, resultados)


# Ejemplo 7: Sentencia con operaciones matemáticas complejas y funciones incorporadas

import math

valores = [math.log(abs(x)) for x in range(-10, 0) if x != 0]
suma = sum(valores)
promedio = suma / len(valores)
resultado_final = math.exp(promedio) + min(valores)


# Ejemplo 8: Sentencia con múltiples funciones, listas y manejo de errores

def procesar_lista(lst):
    if not lst:
        raise ValueError("La lista está vacía")
    return [i ** 2 for i in lst if i % 2 == 0]


try:
    data = [int(x) for x in input().split(",")]
    processed = procesar_lista(data)
    print("Resultado:", sum(processed) / len(processed))
except ValueError as e:
    print("Error:", e)


# Ejemplo 9: Sentencia con múltiples expresiones y listas anidadas

resultados = [
    sum([x for x in range(1, 10) if x % 2 != 0]) * max([y for y in range(5, 15) if y % 3 == 0]),
    min([abs(z) for z in range(-20, 0)]) + max([a * b for a, b in zip(range(1, 6), range(6, 11))])
]


# Ejemplo 10: Sentencia con combinaciones de funciones y estructuras condicionales

def procesar_entrada(entrada):
    if entrada > 10:
        return math.sqrt(entrada)
    elif entrada > 5:
        return math.pow(entrada, 2)
    else:
        return abs(entrada)


datos = [1, 4, 9, 16, 25]
resultados = [procesar_entrada(x) for x in datos if x % 2 == 0]
resultado_final = max(resultados) - min(resultados)
