import random

p = 0.3
repeticiones = 10000

for n in [10, 100, 1000]:

    suma_caras = 0

    for simulacion in range(repeticiones):

        cantidad_caras = 0

        for lanzamiento in range(n):
            if random.random() < p:
                cantidad_caras += 1

        suma_caras += cantidad_caras

    promedio = suma_caras / repeticiones

    print("n =", n)
    print("Promedio de X:", promedio)
    print("n*p:", n * p)
    print()