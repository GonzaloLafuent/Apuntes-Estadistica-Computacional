# CLASE - 1
## NOTAS
### Teoria de probabilidad
- **ESPACIO MUESTRAL:** el conjunto de todos los posibles resultados de un experimento se llama **espacio de muestral**. 
    - Por ejemplo, tirar una moneda, el espacio muestral es cara/cruz $S = \{C,X\}$. 
    - Ejemplo, medir el tiempo de reaccion de una persona, el espacio muestral seria $S = (0, + \infty )$
- **EVENTO:** Es una coleccion de posibles resultados de un experimento, osea un subconjunto del espacio muesttral **S** incluyendolo tambien. 
    - EJ, un mazo de cartas, el experimento es sacar una carta y anotar el palo. Luego el espacio muestral es $S=\{basto, espada, copa, oro\}$. Luego algunos eventos posible sson $A = \{copa, espada\}$, $B = \{basto, espada, oro\}$.
Como los eventos son cojunto, aplica la teoria de los mimso sobre ellos:
- $ A U B = \{basto, espada,copa, oro\}$
- $ A interserc B = \{espada\}$
- $ A^{c} = \{basto, oro\}$

Propiedades importantes a tener en cuenta:
- conmutativida: $A \cup B = B \cup A$, $A \cap B = B \cap A$
- Asociatividad: $(A \cup B) \cup C = A \cup (B \cup C)$, $(A \cap B) \cap C = A \cap (B \cap C)$
- Distributiva: $A \cap (B \cup c ) = (A \cap B) \cup (A \cap C)$, $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
- Ley de DeMorag: $(A \cup B)^{c} = A^{c} \cap B^{c}$, $(A \cap B)^{c} = A^{c} \cup B^{c}$.

- **EVENTOS DISJUNTO O MUTUAMENTE EXCLUSIVOS:**  son dos eventos A y B tal que si (A Interseccion B) es vacio. En genral si $A_{1}, A_{i}...$  vale que $A_{i} \cap A_{j} = vacio$, luego la coleccion de cojuntos son disjuntos de a pares.

- **PARTICION DE S**: Si los eventos $A_{1}, A_{2}...$ son disjuntos de a pares y $\cup^{\infty} A_{i} = $ entonces la coleccion de $A_{1}, A_{2}, ...$ es una particion de $S$

#### Hacia un defincion axiomatica de la probabilidad
Para cada evento $A$ del espacio muestral queremos asignarle un numero entre 0 y 1 que le vamos a llamar la **probabilidad**: $P(A)$

Definimos primero el campo de borel o **sigam algebra**: Una coleccion de subcojunto de **S** se llama sigma algebra (B) si satisface:
- El cojunto vacio pertence a la sigma.
- Si un evento $A$ pertence al sigma algebra $B$, luego $A^{c}$ tambien pertenec, es cerrado bajo complmeneto
- Si $A_{1}, A_{2},...$ pertenece al sigma algebra, la union de los mismos tambien. 

Si el espacio muestral es finito y enumerable, entonces esa sigam algebra es todos los subcojuntos de S incluyendolo. esto lo vamos a usar para definir la funcion de probabilidad, El domonio de la funcion probabilidad sera algo del tipo del conjunto de todos los subcojuntos posibles. 

- **FUNCION DE PROBABILIDAD:** dado un espacio muestral **S** y un algebra de Borel **B** asocidada, una funcion de probabilidad **P** es tla que:
    - $P(A) > 0 $ para todo $A$ que pertence a $B$
    - $P(S) = 1$
    - si $A_{1}, A_{2}, ...$ pertence a $B$ son disjuntos de a pares, entonces $P(A_{1} \cup A_{2} \cup ... \cup A_{n}) = P(A_{1}) + P(A_{2})+ ...+ P(A_{n})$ 

- EJ (1.2.5): consideramos el experimentos de tirar una moneda balanceda, donde el espacio mestra es $S = \{C,X\}$. teniendo en cuenta esto podemos proponer que, al ser balanceada entonces, $P({c}) P({x})$. Esto esta fuera de la definicion de porbabilida, esto que proponemos no esta en las condiciones. 
Si analizamos mejor tenemos que $S = \{X\} \cup \{C\}$, por el axioma dos tenemos que $P(\{C\} \cup \{X\}) = 1$. como cara y cru son eventos disjuntos luego teneog que $P(\{X\} \cup \{C\}) = P(\{X\}) +  P(\{C\})$. resolviendo por medio de sistema de ecucaiones, tenemos que $P(\{X\}) = 0.5$ y $P(\{X\}) = 0.5$.
Una vez que decido el espacio de muestral **S**, ahi si puedo poder definir los valores especificos del eventos, nada queda determinado hasta no definir el **S** de mi relidad, lo que se exige es el espacio muestral.

- Teo 1.2.6: Un modo comun de definir una funcion de probabilidad es, supongamos que **S** es un cojunto de eventos $\{S_{1}, .., S_{n} \}$ finito. Sea B un algebra de borel y $p_{1}, ..., p_{n}$  valores no negativo que suman 1. para cualquier evento **A** que pertenece al algebra de borel **B** definimos $P(A) = P_i + ... $ para todo $P_{i}$ tal que $s_{i}$ pertence a $A$.

- Teo 1.2.8: Si $P$ es una funcion de probabilidad y $A$ es un conjunto en $B$:
    - La probabilida de vacio sera 0
    - $P(A) <= 1$
    - $P(A^{c}) = 1 - P(A)$

- Teo 1.2.9: Si $P$ e suna funcion de probailida y $A$ y $B$ son cojuntos que pertencen a $B$ alegbra de borel:
    - $P(A \cap B^{c}) = P(B) - P(A \cap B)$
    - $P(A \cup B) = P(B) + P(A) - P(A \cap B)$
    - Si A esta incluido en B entonces $P(A) <= P(B)$




