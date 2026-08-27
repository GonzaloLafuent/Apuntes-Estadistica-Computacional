# CLASE-6
## NOTAS
### DESIGUALDAD DE CHEBYSHEV TEO 3.6.1
Sea X una V.A, $g(x)$ unatranformacion no negativa, entoncespara $r > 0$ se cumple que $P(g(x) >= r) <= \frac{E(g(x))}{r}$.
$g(x)$ puede ser cualquier cosa mientras nos e negativo. Se puede leer como la porbabilidad de una tranofmracion acotado por una cota r, es menor o igual a el valor esperado de la transformacion sobre la cota.

Sabemos que el $E(g(X))$ es la intrgral etre menos infito y mas infito de g(x) mutiplicado por su porbabilidad puntual. Eso lo puedo acotar tomando una integral que se define sobre todos los x tal que g(x)>= r. se la acota por abajo. Luego por la cota, puedo sacar de adentro de la indeitdad g(x) como una contsnate r, por la cota establcecidad. Luego la el resultado que nos queda es que $E(g(x)) >= r* P(g(x) >= r)$. Graficamente se puede ver lo que quier graficar. luego tenemos que $P(g(x) >=r) <= \frac{E(g(x))}{r}$

### COTAS PARA UNA VARIBALE NORMALIZADA, ej 3.612
Supongamos que tenemos $g(x) = \frac{(x-\mu)^{2}}{\sigma^{2}}$, donde $\mu = E(x)$ y $\sigma^{2} = VAR(X)$. tomemos $P(\frac{(x-\mu)^{2}}{\sigma^{2}} >= t^{2})$, por la desiguladad anterior tomando $r = t^{2}$, tenemos que todo es menor a $\frac{1}{t^{2}}*E(\frac{(x-\mu)^{2}}{\sigma^{2}})$, donde la esperanza me da 1, tal que puedo sacar la contsate y luego lo que queda es igual a la deifncion de varianza.

Podemos seguir moviemnto y tener que $P(|x-\mu| >= t*\simga) <= \frac{1}{t^{2}}$. A su vez puedo obtener el complemento como $P(|x-\mu| <> t*\simga) >= 1 - \frac{1}{t^{2}}$. Esto vale para cualquier X. 
esto nos define un monton de cosas que podes pensar sobre disitrbucion para todo t y para toda distribucion de X, $P(|x - \mu| >= 2 \simga) <= 2.5$.Por ejemplo esto vale cualquier disibtrucin, que dice que la porbabilidad de que la distincia entre x y la media sea mayor o igual a 2 veces la varianz,a es un 25 por ciento, y esto de nuevo vale para toda distribucion. 

(Pregunta, que se puede decir si r <= 0?)

Esta desigualdad se va a usar para 

### DISTRIBUCIONES CONJUNTA
**DEF 4.1.1**: Un **VECTOR ALEATORIA** de deminsion n, es una funcion del espacio muestral en $R^{n}$

EJ:
- Arrojar dos dados equilibrados. El espacio muestral $S = (1,1), ...., (6,6)$,son 36 elementos equiprobables. Para cada uno de estso resultados definimos la V.A X = 'suma de ambos resultados', Y = 'el modulo de la diferencia netre resultados'. Vamos a definir la porbabilidad de cada par. La suma sabemos que nos puede dar hasta 12, mientras que la diferencia nos da entre 0 y 5. A las combinaciones que no son posibles le vamos a dar 0. Para la tabla ver el ejemplo en el libro, es contar igual que siempre resultados posibles sobre opciones totales. 

Definimos: funcion de probabilidad puntual conjunta, a la $f(x,y) = P(X = x, Y = y)$, que la primera tenag el valor dadao, y que la segunda tenga el otor valor dado.Se puede escribir como $f_{x}{y}(x,y)$. La funcion de probabilidad conjunta define complmentamente la tabla dada antes. La porbabilidad de $P((x,y) \in A) = \sum_{(x,y) \in A}f(x,y)$

Para esta conjunto tenemos que $E(g(x,y)) = \sum_{(x,y)\in R^{2}}g(x,y)*f(x,y)$

EJ:
- $g(x) = x*y$, como obtengo $E(x*y)?$ habria que calcula el producto de cada par, multiplicarlo por su probabilidad y sumarlo. Seria como recorrer la tabla vista antes y a partir de eso realizar la operacion que definimos. 

### PROPIEDADES
$G_{1}(x,y), G_{2}(x,y), a,b,c $ seran las premisas:
- $E(ag_{1}(x,y) + b(g_{2}(x,y)) + c) = E(ag_{1}(x,y)) + E(b(g_{2}(x,y))) + c$, es lineal
- $f(x,y,) >= 0$
- $\sum_{(x,y)\in R^{2}}f(x,y) = 1$, esto se interpreta como la porbabilidad de que sa alguna valor. 

### Una funcion de dsitribucion conjunta, muchos espacios muestrales
Supongamos que tenemos $f(x,y)$ que valoe $\frac{1}{6}$ si es igual a (0,0) o (0,1), o vale un $\frac{1}{3}$ si vale (1,0) o (1,1). En otro caos da 0. Podriamos calcular $P(X = Y) = f(0,0) + f(1,1) = \frac{1}{2}$. Un espacio muestral posible en el fondo de esto es "dos daodos, mimo experimento", definiendo x = 0 si un dado es como maximo 2, x = 1 si el dado es mayor que 2, Y = 0 si el segundo dado es impar, Y = 1 si el segundo dado es par. 

### DISTRIBUCION MARGINAL DE PROBABILIDAD TEO 4.1.6
Lo que quiero aca es por ejemplo la chance de los valores de X, independiente de Y. Sea (X,Y)  un vector aleatorio de dimnesion 2, con funcion de distribucion cobjunta puntula (fpp conjunta) f_{x}{y}(x,y) , definimos las distribuciones marginales como:
- $f_{x}(x) = P(X = x) = \sum_{y \in R}f_{x,y}(x,y)$
- $f_{y}(y) = P(Y = y) = \sum_{x \in R}f_{x,y}(x,y)$
Para el primero es, para cada x, sumas todos los pares en y. Luego para el segundo, para cada y, sumas todos los pares con x. Sobre cualquiera de las dos hay una condicion implicita que es que x o y valgan cualquier cosa, dependiendo el caso en el que estamos:
- $f_{x}(x) =  P(X = x, -\infty <y< \infty)$, es como tomar la porbabildad del conjunto $A_{x}= {(x,y): -\infty <y< \infty}$, tal que lo que busco es $P((x,y) \in A_{x}) = \sum_{(x,y):A_{x}} f_{x,y}(x,y) = \sum_{y\in R} f_{x,y}(x,y)$

Si tengo las probabilidades marginales por separado, eso me define una unica probabilidad conjunta? A partir de la tabla si altero distintos valores de la misma puedo llegar a las funciones de marginalidades, por lo que la cojunta no es unica. Esto rompe el espacio muestral, pero muestra que las marginales no definen a la conjunta, las conjuntas tienen mas informacion que las marginales. 

### VECTORES ALEATORIOS CONTINUOS
- **DEF:** (X,Y) es un vector alatorio de dos dimension continuo, si $f(x,y): R^{2} -> R$ es la distriucion conjunta de densidad de probabilidad si al calcular la probabildad de $P((x,y) \in A) = \int \int_{A} f(x,y) dx dy$

- Sea $g(x,y) \in R$, luego $E(g(x,y)) = \int \int_{-\infty}^{\infty} g(x,y)f(x,y) dxdy$

### DISTRIBUCIONES MARGINALES CONTINUAS
- $f_x(x) = \int_{-\infty}^{\infty} f_{x,y}(x,y)dy$ 
- $f_y(y) = \int_{-\infty}^{\infty} f_{x,y}(x,y)dx$

Por definicion de probabilidad sabemos que $f(x,y) > 0$ y que $\int \int_{-\infty}^{\infty} f(x,y) dxdy = $

### DISTRIBUCION CONJUNTA ACUMULADA
Se define como $F(x,y) = P(x<=x, y<=y)$, se define igual que antes. En terminos de integrales tengo que $F(x,y) = \int_{-\infty}^{x}\int_{-\infty}^{y} f(s,t) ds dt$. A su vez tenemos que $f(x,y) = \frac_{\alpha^{2}F(x,y)}{\alpha x \alpha y}$, es una derivada parcial. Si las variables fueran independientes seria lo mimso poner parcial o total. 

### PROBABILIDAD CONDICIONAL
Tomemos un vector (x,y) el cual es aleatorio discrteo, que posee una $f(x,y)$ como funcion de distribucion puntutal, las funciones marginales de la forma $f_{x}(x) > 0$ y $f_{y}(y) > 0$, la funcion de distribucion condicional de probabilidad puntual de y dado x es:
- $f(y|x) = P(Y= y | X= x) = \frac{f(x,y)}{f_{x}(x)}$
- $f(x|y) = P(X= X | Y= y) = \frac{f(x,y)}{f_{y}(y)}$
Son distribuciones de probabilidad: 
- $f(x|y) >= 0$
- $\sum_{x} f(x,y) = \frac{\sum_{x}f(x,y)}{f_{y}(y)} = \frac{f_{y}(y)}{f_{y}(y)} = 1$

Para variables continuas es lo mismo, lo que pasa es que no pasamos por la puntual. Para vectores continuos:
- $f(y|x) = \frac{f(x,y)}{f_{x}(x)}$
- $f(x|y) = \frac{f(x,y)}{f_{y}(y)}$

### VALOR ESPERADO CONDICIONAL
- $E(g(y)|x) = \sum_{y} g(y)* f(y|x)$
- $E(g(y)|x) = \int_{-\infty}{\infty}g(y)f(y|x) dy$

### VARIABLES INDEPENDIENTES
Sea (X,Y) un vector aleatorio, con distribucion conjunta $f(x,y)$ y marginales $f_{x}(x), f_{y}(y)$. Se dice que X e Y son independientes si:
- $f(x,y) = f_{x}(x) * f_{y}(y)$

A partir de esto tenemos que $f(y|x) = \frac{f(x,y)}{f_{x}(x)}$, si fueran independientes tenemos que $f(y|x) = \frac{f_{x}(x)f_{y}(y)}{f_{x}(x)} = f_{y}(y)$, la probabilidad condicional no depende de X. 

### LEMA 4.2.7
Supongamos que tenemos una distribucion conjunta, donde dado (X,Y) con una distribucion conjunta $f(x,y)$, donde X e Y son independientes  si y solo si existen $g(x)$ y $h(y)$ tales que $f(x,y) = g(x)*h(y)$. Significa que si tambien puedo ayer una descompoision dada por una funcion para X y otra para Y, puedo decir que son independientes. 

### VALOR ESPERADO DE UN PRODDUCTO DE FUNCIONES 4.1.11
Si g(x) solo depende de x y h(y) solo depende de y, entonces tenemos que:
- $E(g(x)* h(y)) = E(g(x)) * E(h(y))$
tenemos que:
- $E[g(x)h(y)] = \int \int g(x)h(y) f(x,y) dx dy =  \int \int g(x)h(y) f_{x}(x) f_{y}(y) dx dy = \int_{y} h(y)f_{y}(y) \int_{x} g(x) f_{x}(x) dx dy =  \int_{y} h(y)f_{y}(y)dy  \int_{x} g(x) f_{x}(x) dx = E(g(x)) E(h(y))$

### TEO 4.2.14
La suma de dos normales es normal. Supongamos que $X \sim normal(\mu, \simga^{2})$ y tengo $Y \sim normal(a,b^{2})$ y ademas tengo $Z = X +Y$ donde $X \sim N(\mu + A, \sigma^{2} + b^{2})$. Esto permite definir al difrencia entre tranformacion y distribuccion. La distirbucion que me de no va a ser la suma de ambas campanas, eso no sera la dsitribucion de la variable suma, por que si lo fuera, desde el punto grafico el valor promedio de la suma no pude ser el punto medio entre ambas medias, tiene que estar mas lejos. 