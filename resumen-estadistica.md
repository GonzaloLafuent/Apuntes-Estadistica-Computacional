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
- P(B|A): La probabilidad previa, antes de la evidencia.
- P(A): probabilidad de la evidencia, dado que la creencia es verdadera
- P(B): probabilidad marginal, probabilidad de la evidencia bajo cualquier circunstancia. ver cual es la probabilidad de que ocurra mas alla de cualquier condicion.

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

- Una coleccion de eventos $A_1,A_2,..$ son independientes entre ellos si para toda subcoleccion $A_i_1,...,A_i_k$ tenemos que:

