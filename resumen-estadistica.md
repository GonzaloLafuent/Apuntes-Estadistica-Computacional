# TEORIA SOBRE PROBABILIDAD
Son los fundamentos sobre los que se construye toda la estadistica. Dando mecanismo para poder mdeolar pobaliciones o experimientos ubicados dentro de lo que se consideran como fenomenos aleatorios. 
A partir de esto se busca realizar inferencias sobre poblaciones enteras.

## CNJUNTO DE TEORIAS
**ESPACIO MUESTRAL o ESPACIO DE SAMPLEO:** Es el conjunto **S** de posibles resultados de un experimento. 
El espacio muestral puede ser contable, si tiene una correspondencia 1 a 1 con los enteros, o en caso contrario puede ser considerado como incontable. Siempre que se finito va a ser contable. 
La idea de contable o incontable solo va a tener peso cuando hablemos de asignacion de probabilidades. 
 
**SUCESO o EVENTO:** es una coleccion de posibles salidas de un experimento, siendo algun subconjunto de **S**.
Se suele estudiar la probabilidad de un **suceso**. Decimos que un **suceso** ocurre si la salida de un experimento esta dentro del **suceso**.

Los sets son conjuntos, por lo tanto aplican las operaciones de union, interseccion y complemento, entre otras. Sobre esto tambien valen propiedades de distribucion, asocitaivdad, distribucion y leyes de de morgan.

**EVENTOS DISJUNTOS**: Se dice que dos sucesos A y B son disjuntos si su interseccion es igual a el conjunto vacio. Esto se puede extender para una cantidad finita de conjuntos.

**PARTICION**: Si tengo una sucesion de conjuntos disjuntos tal que su union forma el espacio muestral **S**, entonces tenemos una particion de **S**.

## TEORIA DE PROBABILIDAD
La frecuencia con la que ocurre un resultado producto de una experiemntacion se puede considerar como una probabilidad. No se suele definir probabilidad en terminso de frecuencia, sino desde un punto de vista matematico. Se busca hacer que la probabilidad se defina por medio de una funcion que cumple ciertos axiomas. 

Para cada suceso **A** es un espacio muestral **S** queremos asociarle un numero entre 0 y 1. esto se lo llamara probabilidad de **A**, P(A).

**SIGMA ALGEBRA:** Es una coleccion de subconjuntos del espacio muestral **S**. satisface las siguientes propiedades:
- El conjunto vacio pertenece al **Sigma Algebra**.
- Si el sucesos **A** pertecene al **Sigma Algebra**, su complemento tambien
- Si un conjunto $A_i$ de sucesos pertenece al **Sigma Algebra**, su union tambien.
Por lo general nos focalizamos en el **Sigma Algebra** mas pequeño.

Si el espacio muestral **S** es finito o contable, entonces el **Sigma Algebra** sera todos los subcojuntos de **S** incluido **S**.
De ser finito el **Sigma algebra** sera el cojunto de partes.

**FUNCION DE PROBABILIDAD:** dada un espacio muestral **S** y un **Sigma algebra** asociado, una **funcion de probabilidad** es una funcion **P** con dominion sobre el **Sigma Algebra** que satisface:
- P(A) >= 0 para todo A
- P(S) = 1
- Si $A_i$ pertenece a **Sigma Algebra** y son disjuntos, luego la sumatoria de $P(A_1 U ... U A_N)$ = $\sum_{i=1}^{n} P(A_i)$

**TEOREMA:** sea **S** un espacio muestral finito. Suponiendo que tengo un **Sigma algebra** de subojuntos de **S**. Se $p_1, ...., p_n$ numeros no negativos que suman 1. Para todo **A** perteneciente a el **Sigma Algebra**, define $P(A)$ como: 
- $P(A) = \sum_{s_i pertence a A} P_i$

## AXIOMAS DE PROBABILIDAD
De la defincion de estos podemos genera distintis propiedades de las funciones de probabilidad:

![Texto alternativo](Axioma-1.png)
![Texto alternativo](Propiedades-1.png)
![Texto alternativo](Propiedades-2.png)

**INECUACION DE BOFERRONI:** es uitl para cuando es imposible calcular la probabilidad de interseccion, pero se necesita alguna valor estimado. La idea es dar una cota tal que :
- $ P(A \cap B) \geq P(A) + P(B) - 1 $

## TEOREMAS UTILES
![Texto alternativo](Teorema-1.png)

## CONTEO
Se utilizan distintos metodos de conteno para construir asignacion de probabilidades en espacio de muestreo finitos. Para resolver esto suele ser utili dividirlos en tareas mas pequeñas y aplicar reglas conocidas para combinarlos. 

**TEOREMA FUNDAMENTAL DE CONTEO:**  Si un trabajo de **K** tareas, donde cada tarea$ $T_i$ puede hacerce en $N_i$ maneras, entonces el trabajo entero puede hacerce en 
$N_1 X N_2 X...X N_K$ maneras.

El problema de conteo se puede dividir en:
- Conteo con reemplazo
- Conteo sin reemplazo.
A su vez tambien se debe tener en cuenta si el orden es o no importante.

A la hora de elegir una formula debo hacerme dos preguntas:
- Importa el orden?
- Se pueden repetir elementos?

### DIFERENTES CASOS DE CONTEO
![Texto alternativo](Casos-Conteo.png)

Operacion a tener en cuenta al leer la tabla:

![Texto alternativo](Operacion-importante.png)


Si dice **without replacement**, implica que se puede reeptir. En caso contrario indica que no se puede repetir el elemento.

Estas tecnicas de conteo son utiles para espacio de muestro **S** que son finitos y todos sus resultados tienen la misma probabilidad de que ocurran.

## PROBABILIDAD CONDICIONAL E INDEPENDENCIA
Hasta ahora todos los casos que vimos son de **probabilidad incondicional**, todas las probabilidades fueron calculadas sobre el espacio de muestro definido. Si queremos que la misma cambie de acuerdo a nueva informacion, estamos hablando de **probabilidad condicional**.

Si **A** y **B** son eventos de **S** y $P(B) > 0$, entonces la **probabilidad condicional** de **A** dado **B**, escrito como $P(A|B)$ sera:

- $P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(B|A) P(A)}{P(B)}$

$P(A)$ es nuestra creencia inicial, luego llega el evento $B$ y tenemos una nueva creencia representada por $P(A|B)$

cada simbolo representa:
- P(A|B): La probabilidad posterior. la probabilidad de que ocurrio A, dado el evento B.
- P(B|A): La probabilidad previa, antes de la evidencia. es la probabilidad de que ocurra B dada que la hipotesis A es verdadera. probabilidad de B dado A.
- P(A): probabilidad de la evidencia, dado que la creencia es verdadera
- P(B): probabilidad marginal, probabilidad de la evidencia bajo cualquier circunstancia. ver cual es la probabilidad de que ocurra mas alla de cualquier condicion.

La probabilidad de **B** se puede pensar como, $P(B) = P(B|A)P(A) + P(B|A^c)P(A^c)$, donde:
$P(B|A)P(A) = $ la probabilidad de ver B en el mundo donde ocurre A
$P(B|A)P(A) = $ la probabilidad de ver B en el mundo donde no ocurre B.

la idea es que nuestro espacio muestral es actualizaco a **B**, es decir estamos actualizando el espacio muestral usando lo que ocurrio en **B**. 
La idea de condicionar es ver como cambia el espacio muestral luego de un evento sucedido.

**TEOREMA DE BAYES:** sea $A_1,A_2...$ una particion del espacio de muestreo, y sea **B** cualquier conjunto. luego para cada $i = 1,2,...$ tengo que:

- $P(A_i | B) = \frac{P(B|A_i)P(A_i)}{\sum_{j=1}^{\inf} P(B|A_j)P(A_j)}$

Donde tengo que:
- $P(A_i)$ representa la probabilidad de cada evento $A_i$
- $P(A_i|b)$ representa la probabilidad de cada evento $A_i$ dado el evento **B**.
- EL denominador representa la probabilidad de $B$.

**INDEPENDENCIA DE EVENTOS:** dos eventos son independientes si $P(A \cap B) = P(A) P(B)$

a partir de esto podemos decir que, si **A** y **B** son eventos independientes, entonces los siguientes pares tambien lo son:
- $A$ y $B^c$
- $A^c$ y $B$
- $A^c$ y $B^c$

- Una coleccion de eventos $A_1,A_2,..$ son independientes entre ellos si para toda subcoleccion $A_{i}_{1},...,A_{i}_{k}$ tenemos que:

# VARIABLES ALEATORIAS
**VARIABLE ALEATORIA:** es una funcion de un espacio de sampleo a numeros reales. Es decir sera una funcion que le asigna un valor numerico a cada resultado posible de un experimento aleatorio. Nos permite cuantificar los resultados de un evento o suceso aletario.

Al definir esto estamos obteniendo un nuevo espacio de sampleo. Podemos chequear que nuestra funcion de probabilidad tambien funcione sobre este nuevo espacio.
En algunos casos, cuando los eventos ocurridos son numeros, los valores coinciden con los de la variable aletoria.

Ver ejemplos 1.4.4, 1.4.3.

para cada valor aleatoria **X**, asociamos una funcion llamada la funcion de distribucion acumulativa:

**FUNCION ACUMULATIVA O FUNCION DE DISTRIBUCION**: Para una variable independiente **X**, la funcion acumulativa (cdf), la cual se denota como $F_x(X)$, se define como:
- $F_x(x) = P_x(X \leq x)$ para todo x.

Veamos el siguiente ejemplo de DM:

La funcion de distribucion describe el comportamiento probabilistico de una variable aleatoria **X** asociada a un experimento aleatorio. Representa la probabilidad de que una variable aleatoria tome un valor menor o igual a un cierto valor definido.

![Texto alternativo](Ejemplo-Variable-Aleatoria-DM.png)

Se define en base a la funcion de probabilidad de X.
ver definicion de 1.5.2

Se puede pensar que $F_x$ puede ser discontinua. Pero de acuerdo a como fue definida, al producirse un salto, toma el valor del tope de ese salto. Esto se conoce como **Continuidad a derecha**, la funcion es continua cuando un punto se aproxima desde la derecha.

![Texto alternativo](Funcion-Acumulativa-Propiedades.png)

**CONTINUIDAD:** Una variable aleatoria **X** es continua si $F_x(x)$ es una funcion continua de x. En este caso, decimos que sera continua cuando el conjunto de valores posibles son todos los valores de un intervalo o de una union de intervalos de numeros reales.
Por ejemplo, si consideramos el experimento aleatoria
consistente en medir el nivel de agua en un embalse y tomamos la variable aleatoria X=”nivel de agua”, esta puede tomar valores entre 0 y más infinito

**DISCRETA:** Una variable aleatoria **X** es discreta si $F_x(x)$ es una funcion a pasos de x. Por lo general lo que nos quiere decir es que una variable aleatoria sera discreta si su resultado es finiro o infinito numerable.
Por ejemplo, supongamos el experimento consistente en lanzar tres veces una moneda no trucada; si consideramos la variable aleatoria X=”número de caras obtenidas en los tres lanzamientos”, los valores que puede tomar esta variable aleatoria son finitos (0,1,2,3).

**DISTRIBUCION IDENTICA:** Decimos que dos varibale aleatorias **X** e **Y** son distribuidas identicamente su, para cada cojunto A perteneciente al sigma algebra, entonces $P(X \in A) = P(Y \in A)$. Esto no implica que sean iguales. 

**TEOREMA:** los siguiente oraciones son equivalentes:
- Las variables aleatorias **X** e **Y** son distribuidas identicamente.
- $F_x(x) = F_y(x)$ para todo x.

**FUNCION DE MASA DE PROBABILIDAD:** la funcion de masa de probabilidad se define sobre una variable aleatoria **X** como:
- $f_x(x) = P(X = x)$ para todo x.

Notar que para hablar de estad funciones le ponemos una letra f en minuscula.
En este caso define la probabilidad de que una variable aleatoria **X** tome un valor exacto x. Solo aplica a variables aleatorias discretas. 
Para la defincion de esta funcion en el caso de las varibales independientes discretas, podemos sumar los valores de la pmf para obtener la cdf.

para el caso de las variables aletorias continuas usamos otro nombre.

**FUNCION DE DENSIDAD DE PROBABILIDAD:** la funcion de densidad de la probabilidad $f_x(x)$, sera aquella que satisface que:
- $F_x(x) = \int_{-\infty}^{x} f_x(t) \mathrm{d}x $

Esto a su vez quiere decir que:

- $\frac{\partial }{\partial x} F_x(x)= f_x(x)$ 

La función de densidad de probabilidad (PDF) es la probabilidad que toma una variable aleatoria continua en un intervalo específico. Se evalua en intervaloes especificos.

En parte esto nos define que tanto la pdf como al pmf contienen la misma informacion que la cdf, por lo tanto debemos elegir la mas sencilla para resolver el problema.

![Texto alternativo](Propiedades-pdf-pmf.png)

Por le genearl la funcion de acumulativa de porbabilidad se usa cuando necesitamos hallar la probabilidad de que una variable aleatoria sea menor o igual a un valor especifico.
Por el otro lado, la pdf o pmf, se usa cuando necesitamos obtener la probabilidad sobre un valor especifico.

A la hora de definir un fenomeno en terminos de una varibale alteatorias con uan cdf $F_x(x)$, preocupara el comportamiento de la misma. 

# VAlORES ESPERADOS
A la hora de definir un fenomeno en terminos de una varibale alteatorias con uan cdf $F_x(x)$, preocupara el comportamiento de la misma.

**DISTRIBUCION DE FUNCION DE UNA VARIBALE ALEATORIA:** Si **X** es una variable aleatoria con una cdf $F_x(x)$, luego cualquier funcion **X**, por ejemplo $g(X)$ es tambien una variable aleatoria. Por lo general decimos que $Y = g(X)$ para denotar una nueva varibale aleatoria. 

**VALOR ESPERADO o ESPERANZA**: Dado una variable aleatoria, el valor esperado de la misma es casi el promedio de su valor, donde cuando decimos promedio nos referimos a un valor que es medido de acuerdo a la probabilidad de distribucion. 
Por medio de pesar los valores de una variable aleatoria, de acuerdo a la dsitrbucion de probabilidad, esperamos obyener un numero que resuman un valor tipico y esperado de uan observacion sobre una varibale aleatoria.

Dado una variable aleatoria $g(X)$, denotada como $Eg(x)$, la esperanza sera:

![Texto alternativo](Esperanza-Ecuacion.png)

$g(X)$ representa la posibilidad de utilizar alguna tranformacion de una varibale independiente $X$, pero se puede tomar tambien a $g(X) = X$.

En resumen en la esperanza sera un valor que nos indica el valor promedio que se espera obtener de una variable aleatoria a largo plazo. Es decir, si repito el experimento muchas veces, la esperanza nos dice cual sera el resultado promedio. Nos da una idea de un comportamiento general a largo plazo.

![Texto alternativo](Propiedades-Esperanza.png)