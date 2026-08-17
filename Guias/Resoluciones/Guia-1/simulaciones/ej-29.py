import random
import numpy as np

p = 0.5
n = 100

secuencia = ""

for lanzamiento in range(n):
    if random.random() < p:
        secuencia += 'x'
    else:
        secuencia += 'o'

    if(lanzamiento + 1) % 5 == 0:
        secuencia += '#'

secuencia = secuencia.split('#')
secuencia.pop()  

print("secuencia:", secuencia)