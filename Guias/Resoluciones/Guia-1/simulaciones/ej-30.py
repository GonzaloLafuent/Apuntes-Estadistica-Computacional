import random
import numpy as np
import matplotlib.pyplot as plt

p = 0.5
n = 100000

caras = []
cantidad_caras = 0
cantidad_cruces = 0
secuencia = ''
divisor = 0

for lanzamiento in range(1, n + 1):
    divisor += 1
    if random.random() < p:
        cantidad_caras += 1
        secuencia += 'c'
    else:
        cantidad_cruces += 1
        secuencia += 'x'

    if divisor % 2 == 0:
        secuencia += '#'

apariciones = {}
secuencia = secuencia.split('#')
secuencia.pop()

for s in secuencia:
    if s in apariciones:
        apariciones[s] += 1
    else:
        apariciones[s] = 1

print("p*n:",p*n)
print("Cantidad de caras:", cantidad_caras)
print("n*(1-p):",n*(1-p))
print("Cantidad de cruces:", cantidad_cruces)

print(apariciones.keys())

barras = plt.bar(apariciones.keys(), apariciones.values(), color='skyblue')
plt.bar_label(barras, padding=3)

plt.xlabel('Secuencias')
plt.ylabel('Frecuencia')

plt.show()