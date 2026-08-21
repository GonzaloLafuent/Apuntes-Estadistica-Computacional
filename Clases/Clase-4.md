# CLASE-4
## NOTAS
### MAS DE LA CLASE PASADA
- Varianza: es el valor medio de las distancias cuadraticas al valor medio. 

- TEO 2.3.4: Supongamos que $X$ es variable aleatoria con varianza finita (Esto implica que el valor esperado de esa funcion cuadratica me da algo) entonces la varianza de $VAR(aX + B) = a^{2} * VAR(X)$ con a y b constantes. Sumarle un valor constante no agrega nada, pero si multiplicar. 

### CONSTRUCCION DE DE DISTRIBUCIONES COMUNES
### DISTRIBUCIONES DISCRETAS
**UNIFORME:** $X \sim U(1,N)$ si $P(X=x|N) = \frac{1}{n}$ donde x vale desde el 1 hasta el N. Cual seria el valor esperado de X? Sabemos que $E(X)$ es la suma de todos los posibles valores de la variable por su probabilidad, $E(X) = \sum_{x}^{} x * P(X = x|N)$. Esto a la larga dada el promedio, por que cadad valor es equiprbable. Si la probabilida de cada uno sea distinto, el peso es deistinto para cad numero, y eso por la definicion de $E(X)$ modifca el valor dado. Luego en esta distribucion $E(X) = \frac{N(N+1)}{2} $

A su vez tenemos que: $VAR(X) = \frac{(N+1)(N-1)}{12}$

**DISTRIBUCION DE BERNOULLI:** $x \sim Bernoulli(p)$ si $X$ vale 1 con probabilidad p y $X$ vale 0 con probabilidad (1-p), donde $0 <= p <= 1$. Luego tengo que $E(X) = p$, si lo pensas solo tengo dos valores, 0 o 1, luego si usamos la foumla de esperanza da exactamente p. 
Ademas tenemos que $VAR(X) = p(1-p)$ 

**BINOMIAL:** Supongamos un experimento con $N$ ensayos de bernoulli independientes, Definamos la variable $Y = numero de exitos en N ensayos$ , luego $Y \sim Binomial(N,p)$ si $P(Y = y |N,p) = \binom{n}{y} *p^{n}*(1-p)^{n-y}$. Se lee como la cantidad de formas que tengo de elegir mis y exitos sobre n, por la porbabiliad de que y sean exitos, por la porbabilidad de que el resto no sea un exito. 
Luego $E(X) = n*p$, mas o menos se esperand tener n exitos y sobre esos la probabialida es p. Adenmas, $VAR(X) = p*(1-p)$

Ej:
- Tiramos un dado 4 veces. Calculemos la probabiliad de obtener al menos un 6. Cada tirada lo puedo representar con bernoulli, donde la probabilida de sacar un 6 es $\frac{1}{6}$, tal que todo lo que no quiero obtener esta fuera de eso. De esta forme defino $X = numero de 6s en cuatro tiradas de un dado$, con esto ya se que $X \sim Binomial(4,\frac{1}{6})$. Luego se puede pensar por el complemento $P(por lo menos un 6) = P(X > 0) = 1 - P(X = 0)$.
Luego tenemos que $P(X > 0) = 1 - \binom{4}{0}*(\frac{1}{6})^{0}*(\frac{5}{4})^{4} = 0,518$

**DISTRIBUCION DE POISSON:** Si se define un intervalo fijo de tiempo, el numero de evento independientes que ocurren con una misma tasa y son independients siguen esta distribucion. $X \sim Poisson(\lambda)$ si $P(X = x|\lambda) = \frac{e^{-x}*\lambda^{x}}{x!}$. Donde $\lambda$ es la tasa por unidad de tiempo de que ocurra un evento. Luego tenemos que $E(X) = VAR(X) = \lambda$

EJ:
- Tiempo de espera. Supongamos un operador telefonico que en promedio responde/le entran (Sinifica que le ingresan y tiene que responder) 5 llamadas cada 3 minutos. Cual es la probabilidad de que no haya llamadas en el proximo minuto? Supongamos $X 0 Numero de llamada en un minuto$. luego por lo que vimos antes, podemos decir que $X \sim Poisson(\frac{5}{3})$. Una vez que modelo, lo peor ya paso, el calculo podria ser facil pero una vez que tengo la distribucion la probabilidad es sencilla. La probabiliad del eveneot no llamadas, le vamos a poner A es $P(A) = P(X = 0) = \frac{e^{-\frac{5}{3}}*\frac{5}{3}⁰}{0!} = 0,189$.
Luego cual seria la probabilidad de por lo menos llamdas en el porximo minuto? $P( X > = 2) = 1 - (P(X = 0) + P(X = 1))$, sale mejor por el complemento. 

**DISTRIBUCION DE GEOMETRICA:** Tengo $X = numero de ensayos de bernoulli hasta el primer exito $X \sim Geometrica(p)$ si  $P(X = x|p) = (1-p)^{x-1}* p$, que es la probabilida de $x -1$ casos sin exito, por p que es el caso final donde si tengo exito. $E(X) = \frac{1}{p}$ y $VAR(X) = \frac{1-p}{p^{2}}$. Una propiedad importante de esta distribucion es que no posee memoria, esto se debe a que cumple que:
- $P(X > s| X > t) = P(X > s-t)$. Dado que espere t evento, la propiedad de esperar s eventos, donde s > t, es igual a la porbabildad de esperar esos eventos adicionales desde el comienzo. No importa donde empezas, la probabilidad es igual. 
La probabilidad de obtener una frecuencia de fracasos no depende de la posicion de la tira, solo del largo de la secuencia. 

**DISTRIBUCION HIPERGEOMETRICA:** Supongamos que tenes una urna con $N$ bolitas identicas salvo que $M$ de ellas son rojas y $N-M$ son verdes, seleccion $K$ al azar (Sin reposicion). Defino $X = numero de bolas rojas en la muestra de k bolitas, luego $X \sim Hiper(N,M,K)$ si $P(X = x|N,M,K) = \frac{\binom{M}{x}*\binom{N-M}{K-x}}{\binom{N}{K}}$. $E(X) = \frac{K*M}{N}$ y $VAR(X) \frac{(KM)}{N} * \frac{(N-M)*(N-K)}{N(N-1)}$

EJ:
- Supongamos un negocio compra objetos por lote y cada objeto puede ser aceptable o defectuoso. Digamos que $N = Tamaño del lote$, donde $M = el numero de defectusos$ Y $N-M = el numero de objetos aceptables$. Calculemos la probabilidad de que eligiendo $K$ objetos, haya $X$ defectuosos. En estos enunciados ya dice el modelado, supongamos que el lote es de 25, luego el numero de defectuosos es 6 y elijo 10, entonces la probabilida de que no haya ninguno, es $P(X = 0) = \frac{\binom{6}{0}*\binom{19}{10}}{\binom{25}{10}}$

Esto se suele utilizar para establecer muestras de poblaciones grandes, puedo plantera como cuantos debo agarrar para sersiorar que un experimento de verdad esta bien. Esto me da un grado de confinza de la cantidad de cosas que podria analizar en base a eso. En ese caso el valor $k$ es la incognita (Esto ya es un problem de inferencia).

### RELACIONES DE RECURRENCIA
- Si $X \sim Poisson(\lambda)$ entonces $P(X = x) = \frac{\lambda}{x}* P(X = x-1)$
- Si $Y \sim Binomial(N,p)$ entonces $P(Y = y) = \frac{N - y +1}{y} * \frac{p}{1-p} * p$