# Material retirado de simetrias.md

<!-- Retirado el 2026-10-03 al reorganizar simetrias.md con la estructura del
documento general (comunicaciones/salientes/documento_general_trabajo.md). Queda fuera según la
propuesta 3: el grupo de Galileo con matrices, los grupos de Lie, los campos vectoriales y los flujos,
las rotaciones con matrices y la derivada total en el teorema de Noether. Se conserva aquí por si
se recupera para un anexo. El contexto histórico largo está en El-contexto-historico.md. -->

## Planteamiento del trabajo (introducción anterior)

Lo primero es precisar qué decimos cuando hablamos de leyes de la física. La cuestión tiene una doble vertiente.

1. **Qué asumimos al plantear una ley física.** Toda ley se formula respecto de un observador, y parte de su contenido es la afirmación de que otros observadores la escriben de la misma forma. En la relatividad de Galileo, el tiempo es el mismo para todos los observadores, lo que la distingue de la relatividad especial, y las coordenadas espaciales de dos observadores inerciales se relacionan mediante una transformación afín de $\mathbb{R}^3$: una rotación, un desplazamiento del origen y un movimiento relativo con velocidad constante. De ahí se obtienen las reglas de transformación de las posiciones, las velocidades, etc. Afirmar que las leyes son las mismas para todos esos observadores lleva implícito que son invariantes bajo traslaciones en el espacio, bajo rotaciones, bajo traslaciones en el tiempo (antes y después) y bajo el paso a otro observador con velocidad constante. Estas transformaciones forman un grupo de Lie de diez parámetros, el grupo de Galileo.

   Todas ellas se reúnen en una sola matriz de entradas constantes si se trabaja en el espacio-tiempo y se añade una coordenada auxiliar igual a 1 (coordenadas homogéneas):

   $$
   \begin{aligned}
   \begin{pmatrix} \vec{x}' \\ t' \\ 1 \end{pmatrix}
   = \begin{pmatrix} R & \vec{v} & \vec{a} \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix}
   \cdot \begin{pmatrix} \vec{x} \\ t \\ 1 \end{pmatrix},
   \qquad \text{es decir,} \qquad
   \vec{x}' = R \cdot \vec{x} + \vec{v} \cdot t + \vec{a}, \quad t' = t + b,
   \end{aligned}
   $$

   donde $R$ es una rotación, $\vec{v}$ la velocidad relativa, $\vec{a}$ el desplazamiento del origen y $b$ el cambio del origen de tiempos. El tiempo solo entra a través del término $\vec{v} \cdot t$, una traslación que crece uniformemente con $t$. Una rotación que dependiera del tiempo, $R(t)$, no cabe en esta forma: correspondería a un observador que gira, que no es inercial. Componer dos transformaciones es multiplicar sus matrices, e invertir una es invertir su matriz; por eso forman un grupo.

   Escrita con todas sus componentes, con $\vec{x} = (x_1, x_2, x_3)$, $\vec{v} = (v_1, v_2, v_3)$, $\vec{a} = (a_1, a_2, a_3)$ y $R = (r_{ij})$, la matriz es:

   $$
   \begin{aligned}
   \begin{pmatrix} x_1' \\ x_2' \\ x_3' \\ t' \\ 1 \end{pmatrix}
   = \begin{pmatrix}
   r_{11} & r_{12} & r_{13} & v_1 & a_1 \\
   r_{21} & r_{22} & r_{23} & v_2 & a_2 \\
   r_{31} & r_{32} & r_{33} & v_3 & a_3 \\
   0 & 0 & 0 & 1 & b \\
   0 & 0 & 0 & 0 & 1
   \end{pmatrix}
   \cdot \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ t \\ 1 \end{pmatrix}.
   \end{aligned}
   $$

   El bloque $3 \times 3$ de arriba a la izquierda es la rotación; la cuarta columna contiene la velocidad relativa, y la quinta, los desplazamientos de los orígenes: $\vec{a}$ en las filas del espacio y $b$ en la del tiempo. Los parámetros se cuentan así:

   * **Rotación: 3 parámetros.** $R$ tiene 9 entradas $r_{ij}$, pero no son independientes. La condición $R^{T} \cdot R = I$ exige que sus columnas tengan longitud 1 y sean perpendiculares entre sí; como $R^{T} \cdot R$ es una matriz simétrica, son 6 ecuaciones ($3$ en la diagonal y $3$ por encima de ella). Quedan $9 - 6 = 3$ parámetros libres. La condición $\det R = 1$ no quita ninguno más: solo excluye las reflexiones, que tienen $\det R = -1$. Esos tres parámetros pueden ser, por ejemplo, tres ángulos de giro. Así, el giro de ángulo $\theta$ alrededor del eje $x_3$ es
     $$
     \begin{aligned}
     R_3(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix},
     \end{aligned}
     $$
     y cualquier rotación se obtiene como producto de tres giros de este tipo alrededor de los ejes coordenados (ángulos de Euler).
   * **Cambio de velocidad: 3 parámetros**, $v_1$, $v_2$ y $v_3$.
   * **Traslación espacial: 3 parámetros**, $a_1$, $a_2$ y $a_3$.
   * **Traslación temporal: 1 parámetro**, $b$.

   En total, $3 + 3 + 3 + 1 = 10$ parámetros.

2. **Cómo formularlo con generalidad.** Lo anterior orienta el camino, pero obliga a comprobar la invariancia ley por ley. Sea, por ejemplo, la ley de Hooke para un muelle, $\vec{F} = -k \cdot \vec{r}$, donde $k > 0$ es la constante elástica del muelle, $\vec{r}$ es la elongación (el desplazamiento del extremo del muelle respecto de su posición de equilibrio) y $\vec{F}$ es la fuerza recuperadora, dirigida en sentido contrario a la elongación. Consideremos dos observadores inerciales: uno con origen en el punto $\vec{0}$ de $\mathbb{R}^3$ y otro cuyo sistema de referencia está girado y desplazado respecto del primero y se mueve con velocidad constante $\vec{v}$. Sus coordenadas se relacionan por

   $$
   \begin{aligned}
   \vec{x}' = R \cdot \vec{x} + \vec{v} \cdot t + \vec{a},
   \end{aligned}
   $$

   donde $R$ es una matriz de rotación constante ($R^{T} \cdot R = I$ y $\det R = 1$) y $\vec{a}$ es el desplazamiento entre los orígenes.

   * La elongación es una diferencia de dos posiciones (la del extremo del muelle y la de su posición de equilibrio), así que $\vec{v} \cdot t$ y $\vec{a}$ se cancelan: $\vec{r}' = R \cdot \vec{r}$.
   * La fuerza es la masa por la aceleración, y la aceleración no cambia al añadir una velocidad constante: $\vec{F}' = R \cdot \vec{F}$.
   * Multiplicando la ley de Hooke por $R$ se obtiene $\vec{F}' = R \cdot \vec{F} = -k \cdot R \cdot \vec{r} = -k \cdot \vec{r}'$. El segundo observador mide la misma ley, con la misma constante $k$: la ley de Hooke es invariante bajo el grupo de Galileo.
   * Es esencial que $R$ no dependa del tiempo. Si el segundo sistema de referencia girase, con una matriz $R(t)$, no sería inercial y aparecerían fuerzas ficticias (centrífuga y de Coriolis), de modo que la ley no conservaría su forma.

Pero este razonamiento hay que repetirlo para cada ley. ¿Se puede expresar con mayor generalidad? Aquí interviene el principio de Hamilton, o principio de acción estacionaria. El formalismo lagrangiano da una forma a la vez muy general y muy precisa de la idea de teoría física, y en él cabe toda la mecánica clásica. Para un sistema de $N$ partículas, la configuración se describe con $3 \cdot N$ coordenadas $q = (q_1, \dots, q_{3 \cdot N})$, y el sistema queda definido por una función, el lagrangiano $L(q, \dot{q}, t)$, que depende de las coordenadas, de las velocidades $\dot{q} = dq/dt$ y del tiempo. Las trayectorias candidatas son las funciones $q : [t_0, t_1] \to \mathbb{R}^{3 \cdot N}$ con segundas derivadas continuas y extremos fijos, $q(t_0) = q_{\mathrm{ini}}$ y $q(t_1) = q_{\mathrm{fin}}$. Sobre ellas se define el funcional de acción

$$
\begin{aligned}
S[q] = \int_{t_0}^{t_1} L(q(t), \dot{q}(t), t)\,dt.
\end{aligned}
$$

La trayectoria física es la que hace estacionaria la acción: $\delta S[q] = 0$ para toda variación $\eta$ con $\eta(t_0) = \eta(t_1) = 0$. Las trayectorias con extremos fijos no forman un espacio vectorial, pero las variaciones sí. Esta condición equivale a las ecuaciones de Euler-Lagrange de $L$, que son las leyes del movimiento del sistema.

En este marco, la pregunta anterior tiene una respuesta general: que las leyes sean las mismas bajo un grupo de transformaciones equivale a que la acción sea invariante bajo ese grupo, salvo un término que es la derivada respecto del tiempo de una función. Esta condición ya no depende del problema particular, y el teorema de Noether asocia a cada simetría continua de la acción una cantidad conservada. Para una partícula libre de masa $m$, con $L = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{x}}|^2$, la invariancia bajo traslaciones en el tiempo da la conservación de la energía; bajo traslaciones en el espacio, la del momento lineal $\vec{p} = m \cdot \dot{\vec{x}}$, y bajo rotaciones, la del momento angular. Bajo un cambio de velocidad, $\dot{\vec{x}} \to \dot{\vec{x}} + \vec{v}$, el lagrangiano cambia justamente en una derivada total,

$$
\begin{aligned}
L' = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{x}} + \vec{v}|^2 = L + \dfrac{d}{dt}\left( m \cdot \vec{v} \cdot \vec{x} + \dfrac{1}{2} \cdot m \cdot |\vec{v}|^2 \cdot t \right),
\end{aligned}
$$

y la cantidad conservada es $m \cdot \vec{x} - \vec{p} \cdot t$, que expresa que el centro de masas se mueve con velocidad constante.

Conviene precisar qué significa que la acción sea invariante, porque aquí intervienen dos variaciones distintas. La condición de estacionariedad, $\delta S = 0$, compara una trayectoria con las que se obtienen deformándola de cualquier manera sin mover sus extremos, y selecciona las trayectorias físicas. Una simetría, en cambio, no es una trayectoria, sino una familia continua de transformaciones $\Phi_\varepsilon$, que depende de un parámetro real $\varepsilon$ y se reduce a la identidad para $\varepsilon = 0$ (por ejemplo, las rotaciones de ángulo $\varepsilon$ alrededor de un eje fijo). Lo que se exige es que no cambie la acción de ninguna trayectoria, sea física o no: $S[\Phi_\varepsilon \circ q] = S[q]$ para toda trayectoria $q$, salvo quizá un término que solo depende de los extremos. De forma equivalente, el lagrangiano cambia como mucho en la derivada total de una función, $\delta L = \varepsilon \cdot \dfrac{dF}{dt}$. La simetría es, por tanto, una propiedad de la ley, es decir, del lagrangiano, y no de una solución particular. Una de sus consecuencias es que transforma soluciones en soluciones, que es la forma general de decir que otro observador ve la misma ley.

El trabajo sigue este camino. Primero se describen las transformaciones continuas mediante los campos vectoriales que las generan y sus flujos. Después se enuncia y demuestra el primer teorema de Noether, que asocia a cada simetría continua de la acción una cantidad conservada, y se aplica al grupo de Galileo: sus diez generadores dan las diez cantidades conservadas de la mecánica clásica, que son la energía, el momento lineal, el momento angular y el movimiento uniforme del centro de masas. Por último, se indica cómo se extiende esta relación a los campos y a la relatividad especial, y cómo se traduce a la mecánica cuántica, donde una cantidad se conserva si su operador conmuta con el hamiltoniano.

## Desarrollo anterior

<!-- Desarrollo, contrastando las ideas de varios autores y, si es posible, con las propias. -->

## Transformaciones continuas, campos vectoriales y flujos

<!-- Familias uniparamétricas Φ_ε (Φ_0 = identidad, Φ_ε ∘ Φ_δ = Φ_{ε+δ}); generador infinitesimal ξ = dΦ_ε/dε en ε = 0; el flujo como solución de dΦ_ε/dε = ξ(Φ_ε); tabla de los generadores del grupo de Galileo. Ideas en BORRADOR.md. -->

## Rotaciones en el espacio

<!-- Pendiente de reubicar en «Simetrías y conservación en mecánica clásica» cuando el grupo acuerde la estructura (comunicaciones/salientes/propuesta_3). Procede de BORRADOR.md, capítulo de rotaciones, puntos 1, 2, 3 y 5. -->

La invariancia bajo rotaciones, que el teorema de Noether asocia a la conservación del momento angular, exige describir las rotaciones con precisión. En este apartado se construye la matriz de una rotación cualquiera y se obtiene su forma infinitesimal, que es la que interviene en el teorema.

### Rotaciones alrededor de los ejes coordenados

Una rotación de ángulo $\theta$ alrededor del eje $z$, en sentido antihorario vista desde el semieje $z$ positivo, deja fija la coordenada $z$ y gira el plano $xy$. Las rotaciones alrededor de los tres ejes son:

$$
\begin{aligned}
R_x(\theta) &= \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix},
\qquad
R_y(\theta) = \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}, \\
R_z(\theta) &= \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}.
\end{aligned}
$$

$R_x$ gira el plano $yz$, de $y$ hacia $z$, y $R_y$ gira el plano $zx$, de $z$ hacia $x$. En $R_y$ el seno negativo aparece en la tercera fila porque el orden cíclico de los ejes es $x \to y \to z \to x$: en el plano $zx$ la primera coordenada es $z$.

Cada una de estas matrices cumple $R^T \cdot R = I$, es decir, conserva longitudes y ángulos. Para $R_z$, el bloque $xy$ del producto es

$$
\begin{aligned}
\begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \cdot \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
&= \begin{pmatrix} \cos^2\theta + \sin^2\theta & 0 \\ 0 & \sin^2\theta + \cos^2\theta \end{pmatrix} \\
&= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},
\end{aligned}
$$

porque los términos fuera de la diagonal, $-\cos\theta \cdot \sin\theta + \sin\theta \cdot \cos\theta$, se anulan. El elemento $(3,3)$ vale $1$. Además, $\det R_z(\theta) = \cos^2\theta + \sin^2\theta = 1$. Las otras dos matrices se comprueban del mismo modo.

### Composición de rotaciones

Aplicar a un vector $\vec{v}$ primero la rotación $R_1$ y después $R_2$ da $R_2 \cdot (R_1 \cdot \vec{v}) = (R_2 \cdot R_1) \cdot \vec{v}$. La composición de rotaciones es, por tanto, el producto de sus matrices, con la primera a la derecha. La suma de rotaciones no es una rotación: con ángulos nulos, $R_x(0) + R_y(0) + R_z(0) = 3 \cdot I$, que multiplica todas las longitudes por $3$.

El orden del producto importa. Con giros de $90^\circ$:

$$
\begin{aligned}
R_x(\pi/2) \cdot R_y(\pi/2) = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix},
\qquad
R_y(\pi/2) \cdot R_x(\pi/2) = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & -1 \\ -1 & 0 & 0 \end{pmatrix}.
\end{aligned}
$$

La primera lleva el vector $\vec{e}_z = (0, 0, 1)$ a $(1, 0, 0)$, y la segunda, a $(0, -1, 0)$. Para describir una rotación cualquiera con tres ángulos hay que fijar, por tanto, un orden. Aquí se gira primero un ángulo $\gamma$ alrededor de $x$, después $\beta$ alrededor de $y$ y por último $\alpha$ alrededor de $z$, siempre respecto de los ejes fijos.

### La matriz de una rotación cualquiera

Con las abreviaturas $c_\alpha = \cos\alpha$ y $s_\alpha = \sin\alpha$ (y lo mismo para $\beta$ y $\gamma$), el producto $R(\alpha, \beta, \gamma) = R_z(\alpha) \cdot R_y(\beta) \cdot R_x(\gamma)$ tiene por columnas

$$
\begin{aligned}
\vec{c}_1 &= \begin{pmatrix} c_\alpha \cdot c_\beta \\ s_\alpha \cdot c_\beta \\ -s_\beta \end{pmatrix},
\qquad
\vec{c}_2 = \begin{pmatrix} c_\alpha \cdot s_\beta \cdot s_\gamma - s_\alpha \cdot c_\gamma \\ s_\alpha \cdot s_\beta \cdot s_\gamma + c_\alpha \cdot c_\gamma \\ c_\beta \cdot s_\gamma \end{pmatrix}, \\
\vec{c}_3 &= \begin{pmatrix} c_\alpha \cdot s_\beta \cdot c_\gamma + s_\alpha \cdot s_\gamma \\ s_\alpha \cdot s_\beta \cdot c_\gamma - c_\alpha \cdot s_\gamma \\ c_\beta \cdot c_\gamma \end{pmatrix}.
\end{aligned}
$$

Esta matriz cumple $R^T \cdot R = I$ sin necesidad de desarrollar los productos. Como la transpuesta de un producto es el producto de las transpuestas en orden inverso, $(A \cdot B)^T = B^T \cdot A^T$:

$$
\begin{aligned}
R^T \cdot R &= R_x^T \cdot R_y^T \cdot \left(R_z^T \cdot R_z\right) \cdot R_y \cdot R_x \\
&= R_x^T \cdot \left(R_y^T \cdot R_y\right) \cdot R_x = R_x^T \cdot R_x = I,
\end{aligned}
$$

donde en cada paso el paréntesis central se ha sustituido por $I$. Del mismo modo, $\det R = \det R_z \cdot \det R_y \cdot \det R_x = 1$.

### Rotaciones infinitesimales

Una rotación próxima a la identidad se escribe $R = I + A$, donde las entradas de $A$ son de primer orden en los ángulos de giro. Sustituyendo en $R^T \cdot R = I$:

$$
\begin{aligned}
(I + A^T) \cdot (I + A) = I + A^T + A + A^T \cdot A = I.
\end{aligned}
$$

El término $A^T \cdot A$ es de segundo orden y se desprecia, de modo que a primer orden $A^T = -A$: la matriz $A$ es antisimétrica. Su diagonal es nula y sus entradas opuestas tienen signos contrarios, así que tiene tres entradas independientes, $a$, $b$ y $c$:

$$
\begin{aligned}
A = \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ -b & a & 0 \end{pmatrix}.
\end{aligned}
$$

Aplicada a un vector $\vec{v}$, con $\vec{\omega} = (a, b, c)$, esta matriz da un producto vectorial:

$$
\begin{aligned}
A \cdot \vec{v} &= (b \cdot v_3 - c \cdot v_2,\ c \cdot v_1 - a \cdot v_3,\ a \cdot v_2 - b \cdot v_1) = \vec{\omega} \times \vec{v}, \\
R \cdot \vec{v} &\approx \vec{v} + \vec{\omega} \times \vec{v}.
\end{aligned}
$$

La rotación infinitesimal desplaza cada vector en $\delta\vec{v} = \vec{\omega} \times \vec{v}$, perpendicular al eje $\vec{\omega}$ y al propio vector. El vector $\vec{\omega}$ reúne el eje de giro (su dirección) y el ángulo (su módulo). Por ejemplo, desarrollando $R_z(\varepsilon)$ con $\cos\varepsilon \approx 1$ y $\sin\varepsilon \approx \varepsilon$, se obtiene $A$ con $a = b = 0$ y $c = \varepsilon$: $\vec{\omega} = (0, 0, \varepsilon)$, un giro de ángulo $\varepsilon$ alrededor del eje $z$. Esta es la forma de la rotación que usa el teorema de Noether para obtener la conservación del momento angular.

A primer orden, además, dos rotaciones infinitesimales conmutan: en el producto $(I + A_1) \cdot (I + A_2) = I + A_1 + A_2 + A_1 \cdot A_2$, el término que depende del orden, $A_1 \cdot A_2$, es de segundo orden. Las rotaciones finitas, en cambio, no conmutan, como se ha visto.

## Simetrías de la acción y primer teorema de Noether

<!-- Definición: S[Φ_ε ∘ q] = S[q] salvo términos de frontera, δL = ε·dF/dt. Diferencia con δS = 0. Enunciado y demostración: Q = Σ p_i·ξ_i − H·τ − F se conserva sobre las soluciones. -->

## El grupo de Galileo y sus diez cantidades conservadas

<!-- Para L = Σ ½·m_a·|ẋ_a|² − V: condición sobre V de cada simetría y cantidad asociada (energía, P, J, G = M·X_cm − P·t). Ejemplo computacional: cuadernos/tema1/noether_galileo.py (repositorio público MCC). -->

## Extensión a campos y a la relatividad especial

<!-- Opcional: grupo de Poincaré (también 10 parámetros) y tensor de energía-momento; el segundo teorema de Noether y la relatividad general, enlazando con el contexto histórico. -->

## Simetrías en mecánica cuántica

<!-- Opcional: una simetría es un operador unitario; su generador es un observable Q̂; se conserva si y solo si [Ĥ, Q̂] = 0. Ejemplos: momento lineal y traslaciones, momento angular y rotaciones. -->
