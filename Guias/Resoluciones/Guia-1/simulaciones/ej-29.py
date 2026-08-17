import random
import numpy as np

p = 0.5
n = 1000000

primer_secuencia = "ccccc"
segund_secuencia = "cxccx"

secuencia = ""

for lanzamiento in range(n):
    if random.random() < p:
        secuencia += 'c'
    else:
        secuencia += 'x'

    if(lanzamiento + 1) % 5 == 0:
        secuencia += '#'

secuencia = secuencia.split('#')
secuencia.pop()  

cant_primer_secuencia = 0
cant_segund_secuencia = 0

for s in secuencia:
    if s == primer_secuencia:
        print("Se encontró la primera secuencia:", primer_secuencia)
        cant_primer_secuencia += 1
    elif s == segund_secuencia:
        print("Se encontró la segunda secuencia:", segund_secuencia)
        cant_segund_secuencia += 1

print("Cantidad de veces que se encontró la primera secuencia:", cant_primer_secuencia)
print("Cantidad de veces que se encontró la segunda secuencia:", cant_segund_secuencia)