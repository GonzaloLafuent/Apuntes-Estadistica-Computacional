# CLASE - 2 
## NOTAS
### REPASO PROPIEDADES
Recordemos esto:
- **Teo 1.2.9:** Si $P$ es una funcion de probabilidad y $A$ y $B$ son conjuntos que pertenecen a $B$ algebra de borel:
    - $P(A \cap B^{c}) = P(B) - P(A \cap B)$
    - $P(A \cup B) = P(B) + P(A) - P(A \cap B)$
    - Si A esta incluido en B entonces $P(A) <= P(B)$

En base a la propiedad 2, donde esta establece la probabilidad de A union B, podemos llegar a la desigualdad de bonferroni.

Prueba de la propiedad 2:
- Reescribimos la union tal $A \cup B = A \cup (B\cap A^{c})$. Notemos a partir de esto a $A$ y $B \cap A^{c}$  son disjuntos. Si son disjuntos la interseccion es vacia, $A \cap(B \cap A^{c}) = vacio \cap B = vacio$, dado que permutando y conmutando tenngo que $A \cap A^{C}$ es vacio.
Si sos disjuntos entonces tenemos $P(A \cup B) = P(A \cup (B \cap A^{c})) = P(A) + P(B \cap A^{c})$
Luego si aplico la propiedad a. donde $P(A) + P(B \cap A^{c}) = P(A) + P(B) - P(A \cap B)$ 

### DESIGUALDAD DE BONFERRONI
A partir de lo anterior tenemos que $P(A \cap B) = P(A) + P(B) - P(A \cup B)$. Por los axiomas de probabilidad sabemos que cada $P$ de la expresion anterior es menor a uno. Mas aun, vamos a pedir que $P(A \cup B) <= 1$. Reemplazando la union por 1 llegamos a:
- $P(A \cap B ) >=  P(A) + P(B) - 1$

Se le da una cota a la suma de $P(A) + P(B)$. Hay casos donde nos da mucha informacion. a veces es complicado calcular la interseccion, pero sabemos las probabilidad de los eventos por separado. Los observe separados, pero nunca los observe juntos, no tengo ese dato. Esta desigudaldad me permite generar una cota para la probabilidad de que los eventos ocurrean juntos.

EJ:
- Supongamos  $P(A) = P(B) = 0.95$, luego podemos decir que $P(A \cap B) >= 2*0,95 -1 = 0,9$. Estamos diciendo que la probabilidad de que ocurran jutnos es al menos de 90%.

Ej:
- No siempre ocurre, supongamos  $P(A) = P(B) = 0.1$, luego la probabilidad de que ocurra juntos es $P(A \cap B) >= 2*0,1 -1 = -0,8$. No hay nada malo, pero no aporta nada, porque ya sabemos que la probabilidad va a ser mayor o igual a 0.

Por que se debe esto? Si lo pensamos como diagramas de vennn se ve todo mas claro. Supongamos que la chance de A es 95, de todas la cosas que podian ocurrir A es el 95 por ciento de chances. B tambien tiene 95 porciento de chances. dentro del digrama podria hacer concidir con A, podriamos hacerlo concidir desde el costado. pero dentro del diagrama no hay forma de ubicar a B sin tomar mas del 90, por es que la cota por debajo nos daba esto. No forma de achicarlo. 

En el segundo caso, si tomo con A con 0,1 de proabbilidad, tengo muchas formas de ubicar B para que no coincida, hasta dando probabilidad 0.

### MAS TEOREMAS
- $P(A) = \sum^{\infty}_{i=1} P(A \cap C_{i})$ donde $C_i$ es una particion del espacio muestral **S**. La probabilidad de A es la suma de las probabilidad de las particiones de A.
- $P(\cup^{\infty}_{i=1}A_{i}) <= \sum^{\infty}_{i=1} P(A_{i})$ para cualquier $A_{i}$.Esto se denomina como la **Desigualdad de Boole**

Demostracion de la primer propiedad:
- $C_{1}, C_{2},...$ son una particion , esto implica que $C_{i} \cap C_{j} = vacio$ y $S$ es igual a la union de todos los $C_{i}$. Tomemos $S = A \cap S$. Luego tenemos que:
- $A = A \cap S$
- $A = A \cap (\cup^{\infty}_{i=1} c_{i}) = (\cup^{\infty}_{i=1} A \cap c_{i})$

Luego tenemos que
- $P(A) = P(\cup^{\infty}_{i=1}(A \cap C_{i}))$ 

Como $C_{i}$ son disjuntos entonces $A \cap C_i$ es disjunto:
- $P(A) = P(\cup^{\infty}_{i=1}(A \cap C_{i})) = P(\sum^{\infty}_{i = 1} A \cap C_{i})$ 

Nota: la dessigualdad de Boole es una generalizacion de la desigualdad de Bonferroni. Demostracion:
- Apliquemos Boole al conjunto $A^{c}$. Luego $P(\cup^{n}_{i=1} A^{c}_{i}) <= \sum^{n}_{i= 1}P(A^{c}){i}$, esto vale por boole.
Luego usamos que $\cup A^{c}_{i} = (\cap A_{i})^{c}$ esto vale por de morgan. Adema $P(A^{c}_{i}) = 1 - P(A_{i})$. Entonces podemos decir que $1 - P(\cap^{n}_{i=1} A_{i}) <= n - \sum^{n}_{i=1} P(A_{i})$. Luego coo ultimo paso, $P(\cap^{n}_{i = 1}A_{i}) >= \sum^{n}_{i = 1} P(A_{i}) - n -1$. Generalizacion de bonferroni para $n = 2$.

Notar que en uno aparece el n porque esta aplicanod la propiedad del complemtno dentro de la sumatoria, mientras que para el otro caso lo saca de afuera.

### CONTEO DE CASOS
**Teorema fundamental del conteo:** Si un trabajo consta de K tareas, de las cuales la i-esima se puede resolver de $n_i$ formas, entonces la tarea entera se puede resolver de $n_{1} * n_{2} * ... *  n_{k}$ formas. 

Hay distintas formas de establecer conteo, por ejemplo, con reemplazo o sin reemplazo. Supongamos que tenemos un Loto, donde hay que elegir 6 numeros del  1 al 36. Se puede elegir dos veces el mismo numero? Si la respuesta es si hay un numero de casos, si la repuesta es no hay otra. 
Si podes repertir la cantidad de forma de elegir es $36 * 36 * 36 * 36 *36 * 36 $ tal que siemprem puedo eleggir los mismos numeros.
Sino, si no puedo repetir, tengo $36 * 35 * 34 * 33 * 32  * 31$.

la otra pregunta es, importa el orden o no? En el caso anterior, si si importa el orden, importa cual sale primero y cual segundo. Este caso es mas dificil de calcular. Si no importa el orden, tengo mas chances de ganar. 

cuando decimos sin reposicion decimos que las opciones no se devuelven al conjunto de posibilidades. 

Tipos de conteo:
- El primer caso es importa el orden, sin reposicion o reemplazo, sea $n$ el numero total de casos entonces se define como $\frac{n!}{(n-r)!}$, donde $r$ es el numero de casos seleccionados.
- El segundo caso es importa el orden, con reposicion. En este caso sea $n$ el numero total de casos y $r$ el numero de casos seleccionados, entonces es $n^r$
- Tercer caso, no importa el orden, sin reemplazo. Hay que corregir el primer casos para resolver esto. Agarremos el numero de casos del primer tipo, $\frac{n!}{(n-r)!}$, lo corregimos por todas las formas que tenemos de reordenar los casos seleccionados, es decir tengo $r$ chances para corregir el primero, $r-1$ para corregir el segundo, y asi. Luego queda como: $\frac{n!}{r!(n-r)!}$. Y esto es el combianatorio, $\binom{n}{r}$, se suele interpretar como tomo $r$ de $n$
- Cuarto tipo, no importa el orden, con reposicion. En este caso hay que hacer una correcion sobre el segundo. este es el cobinatorio: $\binom{n+r+1}{r}$

De esta forma el numero de elegir $r$ entre $n$, depende de si tengo repo, no repo, o si importa o no el orden. 

### PROBABILIDAD CONDICIONAL
Supongamos que elijo 4 cartas de un mazo, cual es la probabilidad de que las 4 sean ases?? En este caso estamos en la parte de sin repo y sin orden. por lo tanto se puede resolver con $\binom{n}{4}$, siendo $ n = 52$. Luego la probabilidad de recibir 4 ases es $\frac{1}{270725}$. 

Cual es la probabilida de un as? es $\frac{4}{52}$, hay 4 ases y 52 cartas, por lo tanto de ahi se deduce. 

Cual es la probabilida de que la segunda sea un as? Aca va a importar que fue lo primero que saque, si es que primero saque un as o no. El numero de chances cambia dado que ya saque una carta. sabemos que la $P(4 ases ) = \frac{4}{52} * \frac{3}{51} * \frac{2}{50} * \frac{1}{49}$, esto da exactamente lo que calculamos antes por medio de la formula. La idea de esto es realizar una actualizacion del espacio muestral disponible. esto es **probailidad condicional** se cambia la probabilidad de lo que calculo frente a algo que observe. 

**Probabilidad Condiconal:** Si A y B son evento en el espacio muestral y $P(B) > 0$, entonces definimos a la probabilidad condicional de A dado B como:
- $P(A|B) = \frac{P(A \cap B)}{P(B)}$

es la probabilidad de que ocurran juntos, relativo a que ocurra B. se produce una renormalizacion del espacio muestral. 

Nuevamente el diagrama de veen ayuda. Sabemos que la interesecciones la area en comun con B y A. Si sabemos que estamos en B, A todavia podria ocurrir o no, pero probablemnte sea distinto al saber B, tal que las chances de A las voy a medir relativas al nuevo universo. Por lo tanto es define como la interseccion sobre la nueva area. Tengo que actualizar los nuevos casos totales. 

De la definicion anterior pordemos definir una expression alternativa para calcular una interseccion. donde:
- $P(A \cap B) = P(A|B) * P(B)$
- $P(B \cap A) = P(B|A) * P(A)$
Estos deberian ser los mismo, dado que la interseccion es conmutativa. Apartir de eso tenemos que:
- $P(A|B) = P(B|A) * \frac{P(A)}{P(B)}$

Esto es lo que se determina como regla de bayes. posee la siguiente generalizacion, sean $A_{1}, A_{2}, ....$ una particion de $S$ y $B$ cualquier evento, entonces bayer dice que:
- $P(A_{i}|B) = \frac{P(B|A_{i})* P(A_{i})}{\sum^{\infty}_{i=1}P(B|A_{i})*P(A_{i})}$

La parte del numerador aplica lo que se conoce como probabilidad total. La probabilidad del evento $B$, dado un particion $A_{1}, .., A_{n}$ del espacio muestral $S$ se define como:
$\sum^{n}_{i=1}P(B|A_{i})*P(A_{i})$

A la hora de usar porbabilidad total esta bueno pensar el espacio muestral como un evento y su completo, para solo tener dos particiones. 

### INDEPENDENCIA ESTADISTICA
Supongamos que la ocurrencia de B no tiene efecto en al probabilidad de A. Entonces:
- $P(A|B) = P(A)$

que haya ocurrido B, no me cambia la informacion. Si esto ocurre, puedo agarrar bayes donde $P(B|A) = P(A|B) \frac{P(B)}{P(A)}$. Luego como la $P(A|B)$ no depende de B, entonces $P(B|A) = P(A) \frac{P(B)}{P(A)} = P(B)$. Entonces $A$ no tiene efecto en $P(B)$, entonces si volvemos a la nocion de probabilidad condicional que nos llevo a bayers, tenemos que $P(A \cap B) = P(A) * P(B)$. Esto ultimo es la mejor definicion de lo que decimos **independencia estadistica**.

La independecia no esta vinculada a que los eventos sean disjuntos. La independecia bsuca ver como se relaciona dos espacio $A$ y $B$, y estos como se relacionan con el espacio muestral $S$. La la independencia se da si la ocurrencia de $B$ no afecta a la aparicion del evento $A$. La independecia nos dice que el evento $A$ tiene la misma probabilidad en $S$ que en $B$.

### TEOREMA DE INDEPENDENCIA DE COMPLEMENTO
Si $A$ y $B$ son eventos independientes, entonces los siguientes tambien:
- $A$ y $B^{c}$
- $A^{c}$ Y $B$
- $A^{c}$ y $B^{c}$
La segunda sale por siemtria de la primera. 

### EJEMPLO DE INDEPENDENCIA
para dos eventos es sencillo, pero que pasa para mas eventos?? Hay varias generalizaciones, pero solo una sirve y es mas larga de ver. Necesitamos una definicion que tambien incluya para cuando son dos eventos. 

**Experimento:** tira una vez dos dados. el espacio muestral $S$ sera todas las posibilidades de pares de numeros combinando los valores que puedne sacar ambos dados. Tomemos los siguientes eventos, A son los pares los que tiene mismo valor de cada dado, B es la suma entre 7 y 10, y el evento C es la suma entre 2,7 u 8. Pensemolos primero calculando las probabilidad:
- $P(A) = \frac{1}{6}$
- $P(B) = \frac{1}{2}$
- $P(C) = \frac{1}{3}$

luego la probabilidad de la interseccion triple es de que salga un par, de que la suma sea  entre 7 y 10,  y la suma es 2,7,8.Esto nos da 1/36, tal que solo un par cumple, el (4,4).

Con esto vale que $P(A \cap B \cap C) = P(A) * P(B) *P(C)$. Luego son indendientes? pensemos lo siguientes:
- $P(B \cap C) = 11/36$, lo que no es P(B) * P(C)
Entonces que esa intersecion triple sea factorizble, no es una buena defincion de independencia.

**Alternativa:** que sean todos independientes de a pares. Si cuando testeo de a dos todos los posibles pares sean independientes, que todo se independiente. Pero no vale, se puede ver que aun que cuando cumplan eso los tres al mismo tiempo no son necesariamente independientes. 

Lo que hay que pedir es mas fuerte, hay que pedir ambas cosas al mismo tiempo: 

**GENERALIZACION DE INDEPENDECIA ESTADISTICA PARA N EVENTOS:**
- Los eventos $A_{1}, ..., A_{n}$ son mutuamente independientes si para cualquier subconjunto $A_{i}{1}, ..., A_{i}{k}$ se cumple que la probabilidad de  $P(\cap^{k}_{j = 1} A_{i}{j}) = P(A_{i}{j})$
la idea es que hay que pedir que sean independientes de a ternas, de pares, de cuaternas etc. 
