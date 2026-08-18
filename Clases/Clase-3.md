# CLASE - 3
## NOTAS
### VARIABLES ALEATORIAS
Supongamos que hacemos una encuesta sobre un tema, donde la respuesta de la gente es si o no. Si muestramos 50 personas, el espacio muestral es 2 a la 50, esa es la cantidad de posibles respuestas. Ahora bien, quizas no me intersa quien respondio que, sino el porcentaje de personas que respondio algo.
Por ejemplo podemos tomar X = 'numero de personas que respondio si', donde X ahora forma un espacio muestal de 50 numeros.

De esta forma puedo definir un mapeo del espacio muestral a la variable que me interesa, de forma tal de reducir el espacio de lo que analizo. 

**VARIABLE ALEATORIA 1.4.1:** una variable aleatoria (v.a) es una funcion del espacio muestral a los reales. Es una reeinterpretacion del espacio muestral. EJ:
- Arrojar dos dados, luego la v.a puede ser X = 'suma de los dados'. 
- Arrojar una moneda 25 veces, luego la v.a puede ser X = 'Numero de caras'
- Aplicar fertilizante en diferentes niveles a un cultivo, luego la v.a puede ser X = 'rendimiento en toneladas por hectarea'
Es como si se definiera un nuevo espacio muesral donde se mueve la varibale aleatoria. 

Supongamos que tenemos un espacio muestral $S = \{S_1, ...., S_n\}$, mas una funcion de porbabilidad $P$ y una variable aleatoria, $X = \{X_1, ..., X_m\}$. Definimos la funcion de probabilidad como $P_x$ ,donde X es la variable, de la siguinete manera: 
- Observamos el valor $X = x_{i}$ (En mayuscula habbo de la vairble, en minuscula del valor), si y solo si el resultado del experimento es $S_{j} \in S$ tal que $X(S_{j}) = x_{i}$. Luego $P_{X}(X = x_{i}) = P(\{ S_{j} \in S : X(S_{j}) = x_{i}\})$. A esto se lo llama **porbabilidad inducida**.
El valor de la varibale aletoria, queda determinada por lo eventos del espacio muestral que cumpla con su valor. 
- $P_{X}(X = X_{i})$ se suele contar como $P(X = x_{i})$ o $P(X = x_{i})$. Lo que expresaes la funcion de probabilida asociada a una variable aleatoria $X$,asociada a un vaolor determinados $x_{i}$. 

Ej mas dificil (1.4.4): En este vamos a definir una v.a $X$ donde no se pueden definir todos sus $x_{i}$. Supongamos el espacio de tamaño 2 a la 50 de la encuesta, donde $S = \{ (10000...00), (0100..000),..... ,(1111.....11111)\}$. Por simplicidad, supongamos que todos los resultados son igualmente probables. Calculemos, por ejemplo, la probabilidad de obtener $X = 27$. Luego tenemos que:
- $P_{x}(X = 27) = frac_{\binom{50}{27}}{2^{50}}$, tomar de 50, las 27 personas que pueden poner que si, sobre los escenatios totales. 
En general:
- $P_{x}(X = i) = frac_{\binom{50}{i}}{2^{50}}$

Si $X$ es inumerable ya no tengo eventos discretos para numerar, luego tengo que:
- $P_{x}(X \in A) = P(\{s \in S : X(s) \in A \})$

### FUNCION DE DISTRIBUCION DE PROBABILIDAD ACUMULADA 1.5.1:
Dada $X$ variable aleatoria, su **fda** $F_{x}$ es $F_{X}(x) = P(X <= x)$. Es la probabilidad acumulada para todos los valores menores que $x$. Ej:
1.5.2: Arrojamos tres monedas equilibradas. Definimos la variable aleatoria $X = 'numero de caras'$. 
Para $P_{X = 0} = 1/8$, luego $P(X = 1) = 3/8$, luego $P(X = 2) = 3/8$ y $P(X = 3) = 1/8$, luego acumuladno tenemos la $fda$:
Luego la $fda$ sera: 
- $F_X(x) = 0 si -\infty < x <0 $  
- $F_X(x) = 1/8 si 0 <= x <1 $, esta es la probabilidad de que no salga ninguna cara, sobre 8 resultados posibles hay uno valido
- $F_X(x) = 1/2 si 1 <= x <2 $, esta es la probabilidad de que salga una cara
- $F_X(x) = 7/8 si 2 <= x <3 $, esta es la probabilidad de que salgan dos caras
- $F_X(x) = 1 si 3 <= x <\infty $, esta es la probabilidad de que salgan dos caras

Si graficamos la funcion, podemos ver que no es continua. Ya por el simple hecho de su definicion podemos ver que no es continua. 

**PROPIEDADES DE LA FDA: (Teo 1.5.3)**
Una funcion $F(x)$ es una $fda$ si y solo si: 
- El limite cuando x tiende a menos infinito es igual a cero y limite de x cuando tiende a mas infinito es igual a 1
- F es nos decreciente (Tiene sentido por acumula valores positivos)
- F es continua a la derecha, Esto implica que cuando el limite de X tiene a un valor $x_{0}^{+}$, entonces tiende a $F(x_{0})$

Ejemeplo 1.54: Arrojamos una moneda hasta que salga una cara. Supongamos $p = probabilidad de cara en cualquier tirada individual$ y definimos la varibale aleatoria $X = numero de tiradas necesrias para obtener una cara$. Si pensamos con esto ya saemos que $P(X = 1) = p$, para la longitud de una tirada. Si tengo $P(X = 2) = (1-p)*p$, la primera es la porbabilidad de no ser cara y la ultima de serlo. Y asi podemos seguir $P(X = 3) = (1-p)^{2}*p$. En forma general tenemos que:
- $P(X = x) = (1-p)^{x-1}*p$, esta sera la funcion de probabilida puntual.
- Calculemos la $fda$ donde $F_{x}(X = x) = P_{X}(X <= x) = \sum_{i=1}^{x}P_{x}(X = i) = \sum_{i=1}^{x} (1-p)^{i-1}*p$
Usandos la formula de la geometrica:
- $F_{X}(x) = \frac{1-(1-p)^{x}}{1-(1-p)} * p = 1-(1-p)^{x}$
Y esta es la llamada **distribucion geometrica***.Cualquier problema que se pueda mapear con cuantas tiradas hacen falta para encontrar un elemento bsucado al final, se puede resover con esto. Template: numero de ensayos hasta cosneguir el primer exito.

## VARIABLE ALEATORIAS DISCRTES VS CONTINUAS
**V.A CONTINUA:** X V.A es continua si $F_X(x)$ es una funcion continua de $X$
**V.A DISCRETA:** X V.A es discreta si $F_X(x)$ es una funcion con escalones.

Esto nos lleva a que puede haber variables aleatorias que tengan la misma distribucion y no ser la misma variable. Esto implica que variables que tengan la misma distribucion no implica que sean la misma variable. Esto se denomina como **varibale identicamente distribuida (def 1.5.8)**. X e Y son **indenticamente distribuidas** si para cada conjunto $A \in Algebra B$ se ve que verifica que $P(X \in A) = P(Y \in A)$. Ej:
- Experimento, arrojar una moneda equilibrada 3 veces. Definimos la varibale $X = numero de caras$, $Y = numero de cruces$. Si analizamos las probabilidades puntales vistas antes, podian aplicar los mimso valores para la cantidad de cruces. Luego eso verifica que $P(X = k) = P(Y = k)$ para todo valor $k$, y sin embargo no existe un resultado s tal que $X(s) = Y(s)$. No tienen los mismos valores, pero si la misma distribucion. 

### FUNCION DE DISTRIBUCION DE PROBABILIDAD PUNTUAL 1.6.1:
la $fdp$ de una varibla aleatoria discreta $X$ es:
- $f_{X}(x) = P(X = x)$
Posee una relacion con la $fda$:
-$F_{X}(x) = P_{X}(X <= x) = \sum_{x}^{i =1} P_{X}(X = i) = \sum_{x}^{i =1} f_{X}(X = i)$

Para la continua tenemos:
### FUNCION DE DENSIDAD DE PROBABILIDAD 1.6.3
la $fdp$ de una varibale continua $X$ es:
- $f_{X}(x) = \int_{-\infty}^{x} f_{x}(t) \, dt$
Cuando la varibale es continua lo que hago es integrar densidad. t seran los posibles valores de x, definidos sobre el intervalo dado por x. 

Notacion: la varibale aleatoria $X$ tiene funcion de distribucion de probabilidad $F_{X}(x)$ se nota $X \sim F_{X}(X)$, X tiene distribucion en la fda. Lo mismo vale para $X \sim f_{X}(X)$. A su vez se usa $X \sim Y$ para decir que son identicamente distribuidas. 

En varibales continuas, si quiero preguntar por la porbabilida de un valor exacto es 0. Es decir la porbabilidad de un valor puntual sera 0, mas alla de que el intervalo tenga un valor cerrado o abierto. De esta forma, para v.a continuas, la porbabilidad de $P(a < x < b) = P(a <= x <= b) = P(a <= x < b) = P(a < x <= b)$.

### PROBABILIDAD COMO AREA BAJO LA CURVA
Ej, 1.6.4: En este ejemplo se me da una fda, de la forma $F_{X}(x) = \frac{1}{1+e^{-x}}$. A partir de la defincion de contnua tenemos que $F_{X}(x) =  \int_{-\infty}^{x} f_{X}(t) \, dt$ si y solo si $f_{X}(x) = \frac{d F_{X}(x)}{dx}$. Si quisiera calcular $P(a < x < b)$ seria el area bajo la curva entre los valores a y b, $P(a < x < b) = F_{X}(b) - F_{X}(a) = \int_{-\infty}^{b} f_{x}(t) \, dt - \int_{-\infty}^{a} f_{x}(t) \, dt = \int_{a}^{b} f_{x}(t) \, dt$

### CONDICIONES PARA FDP O FPP (teo 1.6.5)
Una funcion $f(x)$ es fdp/fpp de $X$ variable aleatoria, si y solo si:
- $f_{X}(x) >= 0 para todo x$
- $\sum_{x}^{} f_{X}(x) = 1$ (fpp)
- $\int_{-\infty}^{+\infty} f_{X}(x) dx = 1$ (fdp)

### VALOR ESPERADO
Una forma de resumir los valores de una varibale aleatoria, es condensarlo mediante un valor. Una forma de conseguir esto es por medio de la esperanza o valor esperado. El valor esperado de una variable aleatoria $X$ llamado $E(X)$ es:
- $E(X) = \sum_{x}^{} x * f_X{x}$  para X discreta. Es cada valor por su probabilidad
- $E(X) = \int_{-\infty}^{+\infty} x * f_X{x} \ dx$  para X continua

En general, valor esperado de $g(X)$, la cual de define una nueva varibale sobre la variable anterior, temeos que:
- $E[g(x)] = \int_{-\infty}^{\infty} g(x)*f(x)dx$ para la variable continuas 
- $E[g(x)] = \int_{-\infty}^{+\infty} g(x) * f_X{x} \ dx$  para X continua

Dos valores esperados muy habituales:
- Donde $g(x) = x$, luego $E(X) = promedio (ponderado)$
- Donde $g(x) = x - E(X)$ Donde este valor que utilizo en la formula es por ejemplo el promedio, algo que calcule antes. Esto representa por ejemplos distnacias al pormedio o valores medios. La idea es realizar un promedio con esto, pero que no se compenesen entre las positivas y negtaivas. Quiero ver cuanto se aparta cada valor de su propio medio. Para evitar esto de los positivos negativos lo pienso como $g(x) = (x -  E(X))^{2}$. El valor esperado de esta expresesion $E[(x - E(X))²] = varianza$. Lo que nos interesa saber es que distancia promedio hay entre los valores y su medio. Se suele nomeclar como $VAR(X)$, que temina siendo el valor esperado de la funcion que definimos. 

si analizamos la esperanza, $f_{x}(X)$ no posee unidad, por lo tatnto loq eu determina la unidad sera la expresion de $g(x)$. Lo mimso para la varianza, sera la unidad de la fncion $g(x)$ al cuadrado. A partir de esto diremos que $\sqrt VAR(X) = la desviacion estandar$

Propiedades:
Sea $X$ v.a y a,b,c constantes y $g_{1}(x), ...., g_{n}(x)$ con valor esperado finito. Luego:
- $E[ag_{1}(x) + bg_{2}(x) + c] = aE[g_{1}(x)] + bE[g_{2}(x)] + c$
- Si $g_{i}(x) >= 0$ para todo  entonces $E[g_{i}(x)] >= 0$
- Si $g_{1}(x) >= g_{2}(x)$ para todo x entonces $E[g_{1}(x) ] > = E[g_{2}(x)]$
- Si $a <= g_{1}(x) <= b$  para todo x entonces $a <= E[g_{1}(x)] <= b$ 