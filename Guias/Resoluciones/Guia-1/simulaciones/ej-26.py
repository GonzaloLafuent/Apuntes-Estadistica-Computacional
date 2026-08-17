import random
import numpy as np
import matplotlib.pyplot as plt

p = 0.03
n = 100000

caras = []
cantidad_caras = 0

for lanzamiento in range(1, n + 1):

    if random.random() < p:
        cantidad_caras += 1

    proporcion = cantidad_caras / lanzamiento
    caras.append(proporcion)

plt.plot(range(1, n + 1), caras)
plt.axhline(p, linestyle="--", label=f"p = {p}")

plt.xlabel("Número de lanzamientos")
plt.ylabel("Proporción de caras")
plt.title("Proporción de caras en función del número de lanzamientos")
plt.legend()
plt.grid()

plt.show()