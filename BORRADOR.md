Empezaré a dar ideas sueltas sobre este primer trabajo. El trabajo se titulará «Las simetrías en la física».

PLATEANDO EL PROBLEMA

Lo primero es saber que decimos cuando hablamos de leyes de la física.
Tenemos una doble vertiente:

1. Qué es lo que asumimos cuando planteamos una ecuación de la física, que decimos que es verdadera. Un ejemplo es la relatividad de Galileo. El tiempo de cualquier observador es el mismo (que lo distingue de la relatividad especial). Pero el marco espacial depende de forma lineal (como en un álgebra lineal sobre $\mathbb{R}$ de dimensión 3). De aquí vienen las transformaciones de las coordenadas, de las velocidades, etc. afirmando que las leyes son las mismas. Esto lleva implícito que en el espacio tridimensional, las leyes son las mismas bajo traslaciones, bajo rotaciones, antes y después (traslaciones temporales). Con esas aclaraciones ya se ve algo de lo que tenemos que hacer.
2. Pero aún queda un problema. El marco general. Lo que he puesto en el punto 1. nos pone en la ruta, pero el problema es que esas leyes siempre habría que verlas de forma particular. Si hablamos de la ley de Hook del comportamiento de muelles y deformaciones elásticas, $\vec{F} = -k \cdot \vec{r}$, dónde $k$ es una constante propia del medio elástico, y $\vec{r}$ es la elongación producida con dirección, $\vec{F}$ es la fuerza que el elástico produce en dirección contraria a la elongación. Si tenemos dos observadores colocado uno en la posición $0$ de $\mathbb{R}^3$, y otro en otra posición con velocidad constante respecto al $0$, deben poder medirse con la mediación de una matriz $A_{3\times 3}(t)$ que indique el movimiento del segundo observador contra el observador que está en $0$. A lo medido por el obsevador central, debemos poder multiplicar su fuerza y su elongación por esta matriz, y el resultado debe ser conforme a la ley de Hook. ¿¿?? Pero todo esto nos obliga siempre a mirar problemas particulares. ¿Podemos dar este tipo de resultados con mayor generalidad? Aquí es dónde entra el Principio de Acción Estacionaria de Hamilton. El formalismo langrangiano da una forma muy general y muy precisa ala vez de la idea de teoría física. Toda la mecánica clásica parece caber en esta formulación. Damos un funcional para un sistema de $N$ partículas discretas, para cada función $f : \mathbb{R}^{3 \cdot N + 1} \to \mathbb{R}$ tal que tenga determinadas propiedades, como tener segundas derivadas parciales continuas en todas las variables, esto formará un espacio vectorial de funciones que llamaremos $\mathcal{C}^2 = \{f : \mathbb{R}^{3 \cdot N + 1} \to \mathbb{R} | \forall i < 3\cdot N+1, \forall j < 3, \exists \dfrac {\partial^j f} {\partial x_i^j} \text{ continua }, f(\infty)=f(-\infty)=0, \int_{-\infty}^{+\infty} f(x)\,dt \in \mathbb{R}\}$ y definimos $\mathcal{L}: \mathcal{C}^2 \to \mathbb{R}$, terminamos obteniendo la acción $S[f] = \int_{t_0}^{t_1} \mathcal{L}(f) \,dt$, si $f$ es tal que $\delta S[f] = 0$, entonces la ley dada por $f$ es físicamente correcta.

IDEAS PARA EL DESARROLLO (conversación con la IA, 25-09-2026)

Material de trabajo para el capítulo «Desarrollo del trabajo» de simetrias.md. El planteamiento ya recoge la definición de simetría y el camino; aquí van los detalles.

1. Transformaciones continuas, campos vectoriales y flujos

El teorema de Noether no trabaja con una transformación suelta, sino con familias de un parámetro $\Phi_\varepsilon$ que dependen de forma continua de $\varepsilon$ y cumplen

$$
\begin{aligned}
\Phi_0 = \text{identidad}, \qquad \Phi_{\varepsilon} \circ \Phi_{\delta} = \Phi_{\varepsilon + \delta}.
\end{aligned}
$$

Por ejemplo, las rotaciones de ángulo $\varepsilon$ alrededor de un eje fijo, o las traslaciones de longitud $\varepsilon$ en una dirección fija. Cada una es un subgrupo uniparamétrico del grupo de Galileo.

Derivando respecto de $\varepsilon$ en $\varepsilon = 0$ se obtiene en cada punto un vector, la dirección en que la transformación empieza a moverlo. Es el campo vectorial generador (generador infinitesimal):

$$
\begin{aligned}
\xi(q) = \left.\dfrac{d}{d\varepsilon}\Phi_\varepsilon(q)\right|_{\varepsilon = 0}.
\end{aligned}
$$

A la inversa, dado el campo $\xi$, la familia se recupera resolviendo $\dfrac{d}{d\varepsilon}\Phi_\varepsilon(q) = \xi(\Phi_\varepsilon(q))$: es el flujo del campo. «Transformación continua» y «campo vectorial» son dos caras de lo mismo, y Noether solo necesita el campo, que es lo lineal.

Generadores del grupo de Galileo, para partículas en posiciones $\vec{x}_a$:

| Transformación | Flujo $\Phi_\varepsilon$ | Generador |
| --- | --- | --- |
| Traslación temporal | $t \to t + \varepsilon$ | $\tau = 1$ (mueve el tiempo, no las posiciones) |
| Traslación espacial en la dirección $\vec{e}$ | $\vec{x}_a \to \vec{x}_a + \varepsilon \cdot \vec{e}$ | $\vec{\xi}_a = \vec{e}$ |
| Rotación alrededor del eje $\vec{n}$ | $\vec{x}_a \to R_{\vec{n}}(\varepsilon) \cdot \vec{x}_a$ | $\vec{\xi}_a = \vec{n} \times \vec{x}_a$ |
| Cambio de velocidad $\vec{u}$ | $\vec{x}_a \to \vec{x}_a + \varepsilon \cdot \vec{u} \cdot t$ | $\vec{\xi}_a = \vec{u} \cdot t$ (depende del tiempo) |

Son 1 + 3 + 3 + 3 = 10 generadores independientes, tantos como parámetros del grupo.

2. Qué es una simetría y en qué se distingue de la estacionariedad

- Estacionariedad ($\delta S = 0$): se varía la trayectoria de cualquier manera sin mover sus extremos y se busca la trayectoria cuya acción no cambia en primer orden. Selecciona las soluciones.
- Simetría: se fija una transformación $\Phi_\varepsilon$ y se exige que no cambie la acción de ninguna trayectoria, física o no, $S[\Phi_\varepsilon \circ q] = S[q]$ para toda $q$, salvo un término de frontera. Equivale a $\delta L = \varepsilon \cdot \dfrac{dF}{dt}$.
- La simetría la tiene la transformación (su campo $\xi$), no una trayectoria, y es una propiedad del lagrangiano, es decir, de la ley. Transforma soluciones en soluciones.

3. Primer teorema de Noether en mecánica: la cuenta

Sea $q_i \to q_i + \varepsilon \cdot \xi_i(q, t)$ con $\delta L = \varepsilon \cdot \dfrac{dF}{dt}$. Por la regla de la cadena,

$$
\begin{aligned}
\dfrac{\delta L}{\varepsilon} = \sum_i \left( \dfrac{\partial L}{\partial q_i} \cdot \xi_i + \dfrac{\partial L}{\partial \dot{q}_i} \cdot \dot{\xi}_i \right).
\end{aligned}
$$

Sobre una solución vale la ecuación de Euler-Lagrange, $\dfrac{\partial L}{\partial q_i} = \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_i}\right) = \dot{p}_i$, y los dos términos forman la derivada de un producto:

$$
\begin{aligned}
\dfrac{\delta L}{\varepsilon} = \dfrac{d}{dt}\left( \sum_i p_i \cdot \xi_i \right) = \dfrac{dF}{dt}
\quad \Longrightarrow \quad
Q = \sum_i p_i \cdot \xi_i - F \ \text{ se conserva.}
\end{aligned}
$$

Si la transformación mueve también el tiempo ($t \to t + \varepsilon \cdot \tau$), aparece un término más: $Q = \sum_i p_i \cdot \xi_i - H \cdot \tau - F$, con $H$ el hamiltoniano. De ahí sale que $H$ se conserva cuando $L$ no depende explícitamente del tiempo (Tema 1, sección 7).

4. Aplicación al grupo de Galileo

Para $N$ partículas con $L = \sum_a \dfrac{1}{2} \cdot m_a \cdot |\dot{\vec{x}}_a|^2 - V$, cada simetría impone una condición sobre $V$ (la física del problema):

| Simetría | Condición sobre $V$ | Cantidad conservada |
| --- | --- | --- |
| Traslación temporal | $V$ no depende de $t$ | Energía $E = T + V$ |
| Traslaciones espaciales | $V$ solo depende de las diferencias $\vec{x}_a - \vec{x}_b$ | Momento total $\vec{P} = \sum_a m_a \cdot \dot{\vec{x}}_a$ |
| Rotaciones | además, solo de las distancias $\lvert \vec{x}_a - \vec{x}_b \rvert$ | Momento angular $\vec{J} = \sum_a \vec{x}_a \times \vec{p}_a$ |
| Cambios de velocidad | se cumple si se cumple la de las traslaciones; $L$ cambia en $\dfrac{d}{dt}\left(\sum_a m_a \cdot \vec{u} \cdot \vec{x}_a\right)$ | $\vec{G} = M \cdot \vec{X}_{\mathrm{cm}} - \vec{P} \cdot t$ |

El grupo de Galileo tiene 10 parámetros: 1 desplazamiento en el tiempo, 3 desplazamientos en el espacio (uno por coordenada), 3 componentes de la velocidad relativa y 3 ángulos de rotación (alrededor de los ejes $x$, $y$ y $z$). Cada parámetro es una simetría independiente y da una cantidad conservada: la energía $E$ (1), las 3 componentes del momento lineal $\vec{P}$, las 3 de $\vec{G}$ y las 3 del momento angular $\vec{J}$. En total, $1 + 3 + 3 + 3 = 10$ cantidades conservadas. Comprobado con SymPy para tres partículas en cuadernos/tema1/noether_galileo.py (16 comprobaciones: invariancia de L bajo cada generador, cantidades de Noether y su conservación sobre las soluciones).

5. Posibles extensiones (opcionales)

- Campos y relatividad especial: grupo de Poincaré (también 10 parámetros) y tensor de energía-momento; segundo teorema de Noether y relatividad general, enlazando con el contexto histórico.
- Mecánica cuántica (la asignatura es Fundamentos de Mecánica Cuántica): una simetría es un operador unitario; su generador es un observable $\hat{Q}$; se conserva si y solo si $[\hat{H}, \hat{Q}] = 0$. Ejemplos: momento lineal y traslaciones, momento angular y rotaciones.


ROTACIONES EN TRES DIMENSIONES (26-09-2026)

Capítulo de trabajo: la matriz de una rotación cualquiera en 3D, con tres ángulos, construida de tres maneras (producto de rotaciones alrededor de los ejes, a partir de $R^T \cdot R = I$ y como composición de rotaciones infinitesimales). Todas las afirmaciones están comprobadas con SymPy. Abreviaturas: $c_\alpha = \cos\alpha$, $s_\alpha = \sin\alpha$, y lo mismo para $\beta$ y $\gamma$.

1. Rotaciones alrededor de cada eje

Una rotación de ángulo $\theta$ alrededor del eje $z$, en sentido antihorario vista desde el semieje $z$ positivo, deja fija la coordenada $z$ y gira el plano $xy$. Las tres rotaciones alrededor de los ejes son:

$$
\begin{aligned}
R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix},
\qquad
R_x(\theta) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix},
\qquad
R_y(\theta) = \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}.
\end{aligned}
$$

$R_x$ gira el plano $yz$ (de $y$ hacia $z$) y $R_y$ gira el plano $zx$ (de $z$ hacia $x$). En $R_y$ el signo menos aparece abajo y no arriba porque el orden cíclico de los ejes es $x \to y \to z \to x$: en el plano $zx$ la primera coordenada es $z$, que en la matriz ocupa la tercera fila.

Cada una cumple $R^T \cdot R = I$. Para $R_z$, el producto de la transpuesta por la matriz da en el bloque $xy$:

$$
\begin{aligned}
\begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \cdot \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
&= \begin{pmatrix} \cos^2\theta + \sin^2\theta & -\cos\theta \cdot \sin\theta + \sin\theta \cdot \cos\theta \\ -\sin\theta \cdot \cos\theta + \cos\theta \cdot \sin\theta & \sin^2\theta + \cos^2\theta \end{pmatrix} \\
&= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},
\end{aligned}
$$

y el elemento $(3,3)$ vale $1$. Las otras dos se comprueban igual. Además, $\det R_z(\theta) = \cos^2\theta + \sin^2\theta = 1$, y lo mismo para $R_x$ y $R_y$.

2. Las rotaciones se componen multiplicando, no sumando

Aplicar primero $R_x$ y después $R_y$ a un vector $\vec{v}$ da $R_y \cdot (R_x \cdot \vec{v}) = (R_y \cdot R_x) \cdot \vec{v}$: la composición es el producto de matrices, con la primera rotación a la derecha. La suma no es una rotación. Por ejemplo, con los tres ángulos nulos cada matriz es la identidad, y

$$
\begin{aligned}
S = R_x(0) + R_y(0) + R_z(0) = 3 \cdot I
\quad \Longrightarrow \quad
S^T \cdot S = 9 \cdot I \neq I:
\end{aligned}
$$

$S$ multiplica todas las longitudes por $3$.

El orden del producto importa. Con giros de $90°$:

$$
\begin{aligned}
R_x(\pi/2) \cdot R_y(\pi/2) = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix},
\qquad
R_y(\pi/2) \cdot R_x(\pi/2) = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & -1 \\ -1 & 0 & 0 \end{pmatrix}.
\end{aligned}
$$

La primera lleva el vector $\vec{e}_z = (0, 0, 1)$ a $(1, 0, 0)$, y la segunda a $(0, -1, 0)$. Por eso, para describir una rotación cualquiera con tres ángulos, hay que fijar un orden. Aquí se usa: primero el ángulo $\gamma$ alrededor de $x$, después $\beta$ alrededor de $y$ y por último $\alpha$ alrededor de $z$, todos respecto de los ejes fijos. Hay otros convenios (los ángulos de Euler clásicos usan $z$, $x$, $z$), y todos usan tres ángulos.

3. La matriz de una rotación cualquiera

$$
\begin{aligned}
R(\alpha, \beta, \gamma) &= R_z(\alpha) \cdot R_y(\beta) \cdot R_x(\gamma) \\
&= \begin{pmatrix}
c_\alpha \cdot c_\beta & c_\alpha \cdot s_\beta \cdot s_\gamma - s_\alpha \cdot c_\gamma & c_\alpha \cdot s_\beta \cdot c_\gamma + s_\alpha \cdot s_\gamma \\
s_\alpha \cdot c_\beta & s_\alpha \cdot s_\beta \cdot s_\gamma + c_\alpha \cdot c_\gamma & s_\alpha \cdot s_\beta \cdot c_\gamma - c_\alpha \cdot s_\gamma \\
-s_\beta & c_\beta \cdot s_\gamma & c_\beta \cdot c_\gamma
\end{pmatrix}.
\end{aligned}
$$

Cumple $R^T \cdot R = I$ sin necesidad de desarrollar los productos. Como la transpuesta de un producto es el producto de las transpuestas en orden inverso, $(A \cdot B)^T = B^T \cdot A^T$:

$$
\begin{aligned}
R^T \cdot R &= R_x^T \cdot R_y^T \cdot \left(R_z^T \cdot R_z\right) \cdot R_y \cdot R_x \\
&= R_x^T \cdot \left(R_y^T \cdot R_y\right) \cdot R_x \\
&= R_x^T \cdot R_x = I,
\end{aligned}
$$

donde en cada paso se ha sustituido el paréntesis central por $I$. Del mismo modo, $\det R = \det R_z \cdot \det R_y \cdot \det R_x = 1$.

4. Derivación a partir de $R^T \cdot R = I$

El elemento $(i, j)$ de $R^T \cdot R$ es el producto escalar de la columna $i$ de $R$ por la columna $j$. Si las columnas son $\vec{c}_1$, $\vec{c}_2$ y $\vec{c}_3$, la condición $R^T \cdot R = I$ equivale a:

- $\vec{c}_1 \cdot \vec{c}_1 = \vec{c}_2 \cdot \vec{c}_2 = \vec{c}_3 \cdot \vec{c}_3 = 1$ (cada columna es unitaria: 3 ecuaciones);
- $\vec{c}_1 \cdot \vec{c}_2 = \vec{c}_1 \cdot \vec{c}_3 = \vec{c}_2 \cdot \vec{c}_3 = 0$ (columnas perpendiculares dos a dos: 3 ecuaciones).

Son $6$ ecuaciones para $9$ entradas, así que quedan $9 - 6 = 3$ parámetros libres. La matriz se construye columna a columna, contando los parámetros:

- **Primera columna: 2 ángulos.** Un vector unitario de $\mathbb{R}^3$ queda fijado por dos ángulos, como un punto de la esfera por su longitud y su latitud. Con $\alpha$ como longitud y $-\beta$ como latitud: $\vec{c}_1 = (c_\alpha \cdot c_\beta,\ s_\alpha \cdot c_\beta,\ -s_\beta)$, que cumple $|\vec{c}_1|^2 = c_\beta^2 \cdot (c_\alpha^2 + s_\alpha^2) + s_\beta^2 = 1$.
- **Segunda columna: 1 ángulo.** $\vec{c}_2$ es unitario y perpendicular a $\vec{c}_1$, luego está en la circunferencia unidad del plano perpendicular a $\vec{c}_1$. Ese plano tiene como base ortonormal $\vec{u} = (-s_\alpha,\ c_\alpha,\ 0)$ y $\vec{w} = \vec{c}_1 \times \vec{u} = (c_\alpha \cdot s_\beta,\ s_\alpha \cdot s_\beta,\ c_\beta)$. Se comprueba que $\vec{u} \cdot \vec{c}_1 = -s_\alpha \cdot c_\alpha \cdot c_\beta + c_\alpha \cdot s_\alpha \cdot c_\beta = 0$, y $\vec{w}$ es perpendicular a los dos por ser un producto vectorial. Un punto de esa circunferencia queda fijado por un ángulo: $\vec{c}_2 = c_\gamma \cdot \vec{u} + s_\gamma \cdot \vec{w}$.
- **Tercera columna: ningún parámetro.** $\vec{c}_3$ es unitario y perpendicular a $\vec{c}_1$ y a $\vec{c}_2$, así que solo puede ser $\vec{c}_1 \times \vec{c}_2$ o $-\vec{c}_1 \times \vec{c}_2$. La condición $\det R = +1$ elige el signo positivo, porque $\det(\vec{c}_1, \vec{c}_2, \vec{c}_3) = (\vec{c}_1 \times \vec{c}_2) \cdot \vec{c}_3$.

En total, $2 + 1 + 0 = 3$ parámetros, y la matriz $(\vec{c}_1, \vec{c}_2, \vec{c}_1 \times \vec{c}_2)$ coincide entrada a entrada con la del punto 3: los dos caminos llevan al mismo resultado.

Sobre el determinante: de $R^T \cdot R = I$ se deduce $\det(R^T) \cdot \det R = (\det R)^2 = 1$, así que $\det R = \pm 1$. Las matrices con $\det R = -1$ incluyen una reflexión, como $\mathrm{diag}(1, 1, -1)$, que cambia $z$ por $-z$. No se pueden alcanzar desde la identidad variando los ángulos de forma continua, porque el determinante varía de forma continua y solo puede tomar los valores $\pm 1$. Las rotaciones son las de $\det R = +1$.

5. Rotaciones infinitesimales

Una rotación próxima a la identidad se escribe $R = I + A$, con $A$ pequeña (sus entradas son de primer orden en los ángulos). Sustituyendo en $R^T \cdot R = I$:

$$
\begin{aligned}
(I + A^T) \cdot (I + A) = I + A^T + A + A^T \cdot A = I.
\end{aligned}
$$

$A^T \cdot A$ es de segundo orden y se desprecia. A primer orden queda $A^T = -A$: $A$ es antisimétrica. Su diagonal es nula y cada entrada de un lado es la opuesta de la simétrica, así que tiene $3$ entradas libres, $a$, $b$ y $c$ (los tres parámetros de nuevo):

$$
\begin{aligned}
A = 
\begin{pmatrix} 0 & -c & b \\ 
c & 0 & -a \\ 
-b & a & 0 
\end{pmatrix}
= a \cdot J_x + b \cdot J_y + c \cdot J_z,
\qquad
J_z = 
\begin{pmatrix} 
0 & -1 & 0 \\ 
1 & 0 & 0 \\ 
0 & 0 & 0 
\end{pmatrix}
\end{aligned}
$$

y análogamente $J_x$ y $J_y$ (un $1$ y un $-1$ en el plano que gira cada eje). Son las derivadas de las rotaciones finitas en el ángulo cero. Por ejemplo, con $\cos\varepsilon = 1 - \dfrac{\varepsilon^2}{2} + \dots \approx 1$ y $\sin\varepsilon = \varepsilon - \dfrac{\varepsilon^3}{6} + \dots \approx \varepsilon$:

$$
\begin{aligned}
R_z(\varepsilon) \approx \begin{pmatrix} 1 & -\varepsilon & 0 \\ \varepsilon & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I + \varepsilon \cdot J_z.
\end{aligned}
$$

Aplicada a un vector, la rotación infinitesimal lo desplaza en un producto vectorial. Con $\vec{\omega} = (a, b, c)$:

$$
\begin{aligned}
A \cdot \vec{v} &= (b \cdot v_3 - c \cdot v_2,\ c \cdot v_1 - a \cdot v_3,\ a \cdot v_2 - b \cdot v_1) = \vec{\omega} \times \vec{v}, \\
R \cdot \vec{v} &\approx \vec{v} + \vec{\omega} \times \vec{v}.
\end{aligned}
$$

El desplazamiento es perpendicular al eje $\vec{\omega}$ y al propio $\vec{v}$, como corresponde a un giro alrededor de $\vec{\omega}$ de ángulo $|\vec{\omega}|$.

A primer orden, las rotaciones infinitesimales conmutan:

$$
\begin{aligned}
(I + \varepsilon \cdot J_x) \cdot (I + \delta \cdot J_y) &= I + \varepsilon \cdot J_x + \delta \cdot J_y + \varepsilon \cdot \delta \cdot J_x \cdot J_y \\
&\approx I + \varepsilon \cdot J_x + \delta \cdot J_y,
\end{aligned}
$$

y el resultado es el mismo en el orden inverso. La diferencia entre los dos órdenes está en el término $\varepsilon \cdot \delta$, de segundo orden. Las rotaciones finitas no conmutan (punto 2).

6. Rotación finita como composición de rotaciones infinitesimales

Las rotaciones alrededor de un mismo eje se componen sumando los ángulos: $R_z(\alpha) \cdot R_z(\beta) = R_z(\alpha + \beta)$. En el bloque $xy$, la entrada $(1,1)$ del producto es $\cos\alpha \cdot \cos\beta - \sin\alpha \cdot \sin\beta = \cos(\alpha + \beta)$, y las demás salen igual con las fórmulas del seno y del coseno de la suma. Por tanto, una rotación de ángulo $\theta$ es exactamente la composición de $N$ rotaciones de ángulo $\theta/N$:

$$
\begin{aligned}
R_z(\theta) = \left(R_z\left(\dfrac{\theta}{N}\right)\right)^N.
\end{aligned}
$$

Si en cada paso se sustituye la rotación por su aproximación de primer orden, $I + \dfrac{\theta}{N} \cdot J_z$, el producto de los $N$ pasos tiende a la rotación exacta cuando $N \to \infty$. La forma más directa de verlo es con números complejos. En el plano $xy$, $J_z$ lleva $(x, y)$ a $(-y, x)$, que es multiplicar $x + i \cdot y$ por $i$. Cada paso es, entonces, multiplicar por $1 + i \cdot \dfrac{\theta}{N}$, y $N$ pasos:

$$
\begin{aligned}
\left(1 + \dfrac{i \cdot \theta}{N}\right)^N \xrightarrow[N \to \infty]{} e^{i \cdot \theta} = \cos\theta + i \cdot \sin\theta,
\end{aligned}
$$

por el mismo límite que $\left(1 + \dfrac{x}{N}\right)^N \to e^x$, que vale también para $x$ complejo. Multiplicar por $\cos\theta + i \cdot \sin\theta$ es girar un ángulo $\theta$:

$$
\begin{aligned}
(x + i \cdot y) \cdot (\cos\theta + i \cdot \sin\theta) = (x \cdot \cos\theta - y \cdot \sin\theta) + i \cdot (x \cdot \sin\theta + y \cdot \cos\theta),
\end{aligned}
$$

que son las dos primeras filas de $R_z(\theta)$.

Por qué se pueden rechazar los órdenes superiores: cada paso de primer orden no conserva exactamente la longitud, porque $\left|1 + \dfrac{i \cdot \theta}{N}\right| = \sqrt{1 + \dfrac{\theta^2}{N^2}}$, con un error de segundo orden, $\dfrac{\theta^2}{2 \cdot N^2}$. Tras $N$ pasos, el logaritmo del factor acumulado es

$$
\begin{aligned}
\ln\left(1 + \dfrac{\theta^2}{N^2}\right)^{N/2} = \dfrac{N}{2} \cdot \ln\left(1 + \dfrac{\theta^2}{N^2}\right) \approx \dfrac{N}{2} \cdot \dfrac{\theta^2}{N^2} = \dfrac{\theta^2}{2 \cdot N} \xrightarrow[N \to \infty]{} 0.
\end{aligned}
$$

Los $N$ errores de orden $1/N^2$ suman un error de orden $1/N$, que desaparece en el límite. Con el ángulo el error es aún menor: cada paso gira $\arctan(\theta/N) = \dfrac{\theta}{N} - \dfrac{\theta^3}{3 \cdot N^3} + \dots$, con un error de orden $1/N^3$, y $N$ pasos acumulan un error de orden $1/N^2$.

En forma matricial, el mismo límite es la serie exponencial, $\sum_k \dfrac{\theta^k}{k!} \cdot J_z^k$. Como $J_z^2 = -\mathrm{diag}(1, 1, 0)$ y $J_z^3 = -J_z$, las potencias se repiten con periodo $2$ salvo el signo. Agrupando las impares y las pares:

$$
\begin{aligned}
R_z(\theta) &= I + \left(\theta - \dfrac{\theta^3}{3!} + \dots\right) \cdot J_z + \left(\dfrac{\theta^2}{2!} - \dfrac{\theta^4}{4!} + \dots\right) \cdot J_z^2 \\
&= I + \sin\theta \cdot J_z + (1 - \cos\theta) \cdot J_z^2.
\end{aligned}
$$

Comprobación de la entrada $(1,1)$: $1 + (1 - \cos\theta) \cdot (-1) = \cos\theta$.

7. Las rotaciones forman un grupo

Componer rotaciones es multiplicar sus matrices, así que se escribe $A \cdot B$ para $A \circ B$. El conjunto de las matrices $3 \times 3$ con $R^T \cdot R = I$ y $\det R = 1$ cumple las cuatro propiedades de grupo bajo la composición:

- **La composición de dos rotaciones es una rotación.** Con $(A \cdot B)^T = B^T \cdot A^T$:

  $$
  \begin{aligned}
  (A \cdot B)^T \cdot (A \cdot B) = B^T \cdot (A^T \cdot A) \cdot B = B^T \cdot B = I,
  \end{aligned}
  $$

  y $\det(A \cdot B) = \det A \cdot \det B = 1$.
- **La identidad es una rotación** (la de ángulo cero): $I^T \cdot I = I$ y $\det I = 1$.
- **La inversa de una rotación es una rotación, y es su transpuesta: $A^{-1} = A^T$.** $A^T \cdot A = I$ dice que $A^T$ es inversa de $A$ por la izquierda; en matrices cuadradas, una inversa por la izquierda lo es también por la derecha, así que $A \cdot A^T = I$. Por tanto, $A \cdot A^{-1} = A^{-1} \cdot A = I$. Además, $A^T$ es una rotación: $(A^T)^T \cdot A^T = A \cdot A^T = I$ y $\det A^T = \det A = 1$.
- **Asociatividad:** $(A \cdot B) \cdot C = A \cdot (B \cdot C)$, porque el producto de matrices (como toda composición de aplicaciones) es asociativo.

Este grupo se llama $SO(3)$, grupo especial ortogonal de orden $3$. Dos precisiones:

- **No es conmutativo:** en general, $A \cdot B \neq B \cdot A$ (el ejemplo de los giros de $90°$ del punto 2).
- **La condición $\det R = +1$ es necesaria.** Las matrices ortogonales con $\det R = -1$ (una rotación seguida de una reflexión) no forman un grupo por sí solas: el producto de dos de ellas tiene determinante $(-1) \cdot (-1) = +1$, y la identidad no está entre ellas. Junto con las rotaciones forman el grupo ortogonal $O(3)$.

El mismo razonamiento se aplica a las matrices $5 \times 5$ del grupo de Galileo del planteamiento: componer transformaciones es multiplicar sus matrices e invertir una transformación es invertir su matriz, así que también cumplen las cuatro propiedades.


EL GRUPO DE GALILEO (26-09-2026)

Capítulo de trabajo: las transformaciones de Galileo, escritas como matrices $5 \times 5$, forman un grupo, y su producto dice cómo se componen los parámetros. Todas las afirmaciones están comprobadas con SymPy.

1. La matriz y su acción

Una transformación de Galileo queda dada por una rotación $R$ (matriz $3 \times 3$ con $R^T \cdot R = I$ y $\det R = 1$), una velocidad $\vec{v}$, un desplazamiento espacial $\vec{a}$ y un desplazamiento temporal $b$:

$$
\begin{aligned}
\vec{x}' &= R \cdot \vec{x} + \vec{v} \cdot t + \vec{a}, \\
t' &= t + b.
\end{aligned}
$$

Con los vectores escritos como columnas, se reúne en una sola matriz que actúa sobre la columna $(\vec{x}, t, 1)$:

$$
\begin{aligned}
G(R, \vec{v}, \vec{a}, b) = 
\begin{pmatrix} 
R & \vec{v} & \vec{a} \\ 
\vec{0}^T & 1 & b \\ 
\vec{0}^T & 0 & 1 
\end{pmatrix},
\qquad
\begin{pmatrix} 
\vec{x}' \\ 
t' \\ 
1 
\end{pmatrix} 
= G(R, \vec{v}, \vec{a}, b) \cdot 
\begin{pmatrix} \vec{x} 
\\ t 
\\ 1 
\end{pmatrix}.
\end{aligned}
$$

$\vec{0}^T = (0, 0, 0)$ es una fila de tres ceros. La matriz es $5 \times 5$: el bloque $R$ ocupa las tres primeras filas y columnas, $\vec{v}$ y $\vec{a}$ son la cuarta y la quinta columna de esas filas, y las dos últimas filas son $(0, 0, 0, 1, b)$ y $(0, 0, 0, 0, 1)$. El $1$ final de la columna $(\vec{x}, t, 1)$ es el que permite escribir los desplazamientos $\vec{a}$ y $b$ como un producto de matrices.

2. La composición: cómo se combinan los parámetros

Aplicar primero $G_1 = G(R_1, \vec{v}_1, \vec{a}_1, b_1)$ y después $G_2 = G(R_2, \vec{v}_2, \vec{a}_2, b_2)$ es multiplicar $G_2 \cdot G_1$. El producto se calcula por bloques, igual que el de matrices ordinarias, porque los tamaños de los bloques encajan (el bloque $3 \times 3$ multiplica a columnas de $3$ entradas):

$$
\begin{aligned}
G_2 \cdot G_1
&= \begin{pmatrix} R_2 & \vec{v}_2 & \vec{a}_2 \\ \vec{0}^T & 1 & b_2 \\ \vec{0}^T & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} R_1 & \vec{v}_1 & \vec{a}_1 \\ \vec{0}^T & 1 & b_1 \\ \vec{0}^T & 0 & 1 \end{pmatrix} \\
&= \begin{pmatrix} R_2 \cdot R_1 & R_2 \cdot \vec{v}_1 + \vec{v}_2 & R_2 \cdot \vec{a}_1 + \vec{v}_2 \cdot b_1 + \vec{a}_2 \\ \vec{0}^T & 1 & b_1 + b_2 \\ \vec{0}^T & 0 & 1 \end{pmatrix}.
\end{aligned}
$$

Por ejemplo, la entrada de arriba a la derecha es la fila de bloques $(R_2,\ \vec{v}_2,\ \vec{a}_2)$ por la columna de bloques $(\vec{a}_1,\ b_1,\ 1)$: $R_2 \cdot \vec{a}_1 + \vec{v}_2 \cdot b_1 + \vec{a}_2 \cdot 1$. El resultado tiene otra vez la forma de una matriz de Galileo, con los parámetros:

$$
\begin{aligned}
R &= R_2 \cdot R_1, \\
\vec{v} &= R_2 \cdot \vec{v}_1 + \vec{v}_2, \\
\vec{a} &= R_2 \cdot \vec{a}_1 + \vec{v}_2 \cdot b_1 + \vec{a}_2, \\
b &= b_1 + b_2.
\end{aligned}
$$

Comprobación aplicando las transformaciones una tras otra. La primera da $\vec{x}' = R_1 \cdot \vec{x} + \vec{v}_1 \cdot t + \vec{a}_1$ y $t' = t + b_1$. La segunda, aplicada a ese resultado:

$$
\begin{aligned}
\vec{x}'' &= R_2 \cdot \vec{x}' + \vec{v}_2 \cdot t' + \vec{a}_2 \\
&= R_2 \cdot (R_1 \cdot \vec{x} + \vec{v}_1 \cdot t + \vec{a}_1) + \vec{v}_2 \cdot (t + b_1) + \vec{a}_2 \\
&= (R_2 \cdot R_1) \cdot \vec{x} + (R_2 \cdot \vec{v}_1 + \vec{v}_2) \cdot t + (R_2 \cdot \vec{a}_1 + \vec{v}_2 \cdot b_1 + \vec{a}_2), \\
t'' &= t' + b_2 = t + (b_1 + b_2).
\end{aligned}
$$

Son los mismos parámetros. Significado de cada uno:

- **Desplazamientos temporales: se suman**, $b = b_1 + b_2$. Retrasar el reloj $b_1$ y después $b_2$ es retrasarlo $b_1 + b_2$.
- **Rotaciones: se multiplican**, $R = R_2 \cdot R_1$. Los ángulos solo se suman cuando las dos rotaciones son alrededor del mismo eje, $R_z(\alpha) \cdot R_z(\beta) = R_z(\alpha + \beta)$. Con ejes distintos no hay una regla de suma de ángulos: el producto no es conmutativo (capítulo de rotaciones, punto 2).
- **Velocidades: se suman después de girar la primera**, $\vec{v} = R_2 \cdot \vec{v}_1 + \vec{v}_2$. Es la ley de adición de velocidades de Galileo. $R_2$ aparece porque la segunda transformación también gira la velocidad que dejó la primera. Sin rotaciones, $\vec{v} = \vec{v}_1 + \vec{v}_2$.
- **Desplazamientos espaciales: se suman, girando el primero, más un término cruzado**, $\vec{a} = R_2 \cdot \vec{a}_1 + \vec{v}_2 \cdot b_1 + \vec{a}_2$. El término $\vec{v}_2 \cdot b_1$ aparece porque el cambio de velocidad $\vec{v}_2$ actúa sobre el tiempo ya desplazado $t + b_1$: durante ese tiempo adicional $b_1$, el movimiento con velocidad $\vec{v}_2$ recorre $\vec{v}_2 \cdot b_1$.

3. Las cuatro propiedades de grupo

- **Composición.** El producto de dos matrices de Galileo es una matriz de Galileo: tiene la misma forma por bloques, y $R_2 \cdot R_1$ es una rotación por ser producto de rotaciones (capítulo de rotaciones, punto 7).
- **Identidad.** $G(I, \vec{0}, \vec{0}, 0)$ es la matriz identidad $5 \times 5$: no gira, no cambia la velocidad y no desplaza.
- **Inversa.** Se obtiene despejando $\vec{x}$ y $t$. De $t' = t + b$ sale $t = t' - b$. De $\vec{x}' = R \cdot \vec{x} + \vec{v} \cdot t + \vec{a}$, multiplicando por $R^T = R^{-1}$ y sustituyendo $t$:

  $$
  \begin{aligned}
  \vec{x} &= R^T \cdot (\vec{x}' - \vec{v} \cdot t - \vec{a}) = R^T \cdot \left(\vec{x}' - \vec{v} \cdot (t' - b) - \vec{a}\right) \\
  &= R^T \cdot \vec{x}' - R^T \cdot \vec{v} \cdot t' - R^T \cdot (\vec{a} - \vec{v} \cdot b).
  \end{aligned}
  $$

  Es otra transformación de Galileo:

  $$
  \begin{aligned}
  G(R, \vec{v}, \vec{a}, b)^{-1} = G\left(R^T,\ -R^T \cdot \vec{v},\ -R^T \cdot (\vec{a} - \vec{v} \cdot b),\ -b\right).
  \end{aligned}
  $$

  Con la ley de composición del punto 2 se comprueba que el producto en cualquiera de los dos órdenes da la identidad. Por ejemplo, $G^{-1} \cdot G$ tiene $R = R^T \cdot R = I$, $\vec{v} = R^T \cdot \vec{v} - R^T \cdot \vec{v} = \vec{0}$, $b = b - b = 0$ y $\vec{a} = R^T \cdot \vec{a} + (-R^T \cdot \vec{v}) \cdot b - R^T \cdot (\vec{a} - \vec{v} \cdot b) = \vec{0}$.
- **Asociatividad.** Se hereda del producto de matrices.

Por tanto, las transformaciones de Galileo forman un grupo de $3 + 3 + 3 + 1 = 10$ parámetros: 3 de la rotación, 3 de la velocidad, 3 del desplazamiento espacial y 1 del temporal.

4. El grupo no es conmutativo

Dos ejemplos en los que el orden cambia el resultado, obtenidos con la ley del punto 2:

- **Desplazamiento temporal $b$ y cambio de velocidad $\vec{u}$.** Si primero se desplaza el tiempo y después se cambia la velocidad, $\vec{a} = \vec{u} \cdot b$. En el orden inverso, $\vec{a} = \vec{0}$. La diferencia es el término cruzado del punto 2: el cambio de velocidad aplicado después actúa sobre un tiempo ya desplazado.
- **Rotación $R$ y desplazamiento espacial $\vec{u}$.** Si primero se desplaza y después se gira, $\vec{a} = R \cdot \vec{u}$: el desplazamiento también gira. En el orden inverso, $\vec{a} = \vec{u}$.

5. Subgrupos de un parámetro y flujos

Si se fija una dirección y se deja libre un solo parámetro $s$, la ley de composición se reduce a una suma:

- traslaciones espaciales en la dirección $\vec{e}$: $G(I, \vec{0}, s \cdot \vec{e}, 0)$, con $s_1 + s_2$;
- cambios de velocidad en la dirección $\vec{e}$: $G(I, s \cdot \vec{e}, \vec{0}, 0)$, con $s_1 + s_2$;
- traslaciones temporales: $G(I, \vec{0}, \vec{0}, s)$, con $s_1 + s_2$;
- rotaciones alrededor de un eje fijo: $G(R_{\vec{e}}(s), \vec{0}, \vec{0}, 0)$, con $s_1 + s_2$, porque los ángulos alrededor del mismo eje se suman.

En los cuatro casos, $\Phi_s = G(\dots s \dots)$ cumple $\Phi_0 = I$ y $\Phi_{s_2} \circ \Phi_{s_1} = \Phi_{s_1 + s_2}$: es un flujo en el sentido del Tema 1, apartado 4.4 (apuntes públicos). Son las familias de un parámetro que usa el teorema de Noether, una por cada una de las 10 direcciones del grupo.


LA EXPONENCIAL DE UNA MATRIZ Y LAS ROTACIONES (26-09-2026)

Capítulo de trabajo: definir $e^M$ para una matriz cuadrada $M$ y demostrar que las rotaciones son exactamente las matrices $R = e^A$ con $A$ antisimétrica. Se usa $A$ para el exponente (como en el punto 5 del capítulo de rotaciones) porque $G$ ya designa la matriz de Galileo. Todas las afirmaciones están comprobadas con SymPy.

1. Definición

Para un número real, $e^x = \sum_{k=0}^{\infty} \dfrac{x^k}{k!}$. Para una matriz cuadrada $M$ se define igual, con las potencias de la matriz ($M^0 = I$, $M^1 = M$, $M^2 = M \cdot M$...):

$$
\begin{aligned}
e^M = \sum_{k=0}^{\infty} \dfrac{M^k}{k!} = I + M + \dfrac{M^2}{2!} + \dfrac{M^3}{3!} + \dots
\end{aligned}
$$

Cada entrada de $e^M$ es la suma de una serie numérica. Es la misma serie que apareció en el punto 6 del capítulo de rotaciones como límite de $N$ rotaciones infinitesimales.

La serie converge para toda matriz. Se usa la norma $\|M\| = \sqrt{\sum_{i,j} M_{ij}^2}$ (la raíz de la suma de los cuadrados de las entradas), que cumple $\|M \cdot N\| \le \|M\| \cdot \|N\|$. En efecto, $(M \cdot N)_{ij} = \sum_l M_{il} \cdot N_{lj}$ y, por la desigualdad de Cauchy-Schwarz, $|(M \cdot N)_{ij}|^2 \le \left(\sum_l M_{il}^2\right) \cdot \left(\sum_l N_{lj}^2\right)$; sumando en $i$ y en $j$ se obtiene $\|M \cdot N\|^2 \le \|M\|^2 \cdot \|N\|^2$. Aplicándolo $k$ veces, $\|M^k\| \le \|M\|^k$, y cada entrada cumple $|(M^k)_{ij}| \le \|M^k\|$. Por tanto, la serie de cada entrada está acotada término a término por $\sum_k \dfrac{\|M\|^k}{k!} = e^{\|M\|}$, que es finita: la serie converge absolutamente.

2. Propiedades

- **$e^0 = I$**, porque todas las potencias $0^k$ con $k \ge 1$ son nulas.
- **$(e^M)^T = e^{M^T}$**, porque la transpuesta de una suma es la suma de las transpuestas y $(M^k)^T = (M^T)^k$.
- **Si $M \cdot N = N \cdot M$, entonces $e^{M+N} = e^M \cdot e^N$.** La condición hace falta para desarrollar las potencias con el binomio de Newton. Por ejemplo, $(M + N)^2 = M^2 + M \cdot N + N \cdot M + N^2$, que solo es $M^2 + 2 \cdot M \cdot N + N^2$ si $M \cdot N = N \cdot M$. Con esa condición, $(M + N)^k = \sum_{j=0}^{k} \dfrac{k!}{j! \cdot (k-j)!} \cdot M^j \cdot N^{k-j}$, y

  $$
  \begin{aligned}
  e^{M+N} = \sum_{k=0}^{\infty} \sum_{j=0}^{k} \dfrac{M^j}{j!} \cdot \dfrac{N^{k-j}}{(k-j)!} = \left(\sum_{j=0}^{\infty} \dfrac{M^j}{j!}\right) \cdot \left(\sum_{l=0}^{\infty} \dfrac{N^l}{l!}\right) = e^M \cdot e^N,
  \end{aligned}
  $$

  donde reordenar los términos está permitido porque las series convergen absolutamente. Sin la condición, la igualdad falla en general (punto 6).
- **Consecuencias.** $s \cdot M$ y $r \cdot M$ conmutan, así que $e^{s \cdot M} \cdot e^{r \cdot M} = e^{(s+r) \cdot M}$: la familia $e^{s \cdot M}$ se compone sumando el parámetro. Con $r = -s$: $e^{s \cdot M} \cdot e^{-s \cdot M} = e^0 = I$. Por tanto, $e^M$ siempre es invertible y su inversa es $e^{-M}$.
- **Derivada respecto de un parámetro.** Derivando la serie término a término (está permitido, porque es una serie de potencias en $s$ que converge para todo $s$):

  $$
  \begin{aligned}
  \dfrac{d}{ds} e^{s \cdot M} = \sum_{k=1}^{\infty} \dfrac{k \cdot s^{k-1} \cdot M^k}{k!} = M \cdot \sum_{k=1}^{\infty} \dfrac{s^{k-1} \cdot M^{k-1}}{(k-1)!} = M \cdot e^{s \cdot M}.
  \end{aligned}
  $$

  Así, $\vec{x}(s) = e^{s \cdot M} \cdot \vec{x}_0$ es la solución de $\dfrac{d\vec{x}}{ds} = M \cdot \vec{x}$ con $\vec{x}(0) = \vec{x}_0$: $e^{s \cdot M}$ es el flujo del campo vectorial lineal $M \cdot \vec{x}$ (Tema 1, apartado 4.4, de los apuntes públicos).

3. La exponencial de una matriz antisimétrica es una rotación

Sea $A$ antisimétrica, $A^T = -A$. Como $-A$ y $A$ conmutan, las propiedades del punto 2 dan:

$$
\begin{aligned}
(e^A)^T \cdot e^A = e^{A^T} \cdot e^A = e^{-A} \cdot e^A = e^{-A+A} = e^0 = I.
\end{aligned}
$$

Falta ver que $\det e^A = +1$ y no $-1$. La función $f(s) = \det e^{s \cdot A}$ es continua en $s$ (las entradas de $e^{s \cdot A}$ son series de potencias en $s$, y el determinante es un polinomio en las entradas). Por lo anterior, aplicado a $s \cdot A$, que también es antisimétrica, solo toma los valores $\pm 1$. Como $f(0) = \det I = 1$ y una función continua no puede saltar de $1$ a $-1$, $f(1) = \det e^A = 1$. Por tanto, $e^A$ es una rotación.

4. Fórmula cerrada: rotación de ángulo $\theta$ alrededor de un eje $\vec{n}$

Toda matriz antisimétrica es $A = a \cdot J_x + b \cdot J_y + c \cdot J_z$ y actúa como $A \cdot \vec{v} = \vec{\omega} \times \vec{v}$, con $\vec{\omega} = (a, b, c)$ (capítulo de rotaciones, punto 5). Si $\vec{\omega} \neq \vec{0}$, se escribe $\vec{\omega} = \theta \cdot \vec{n}$, con $\theta = |\vec{\omega}|$ y $\vec{n}$ unitario, y $A = \theta \cdot K$, donde $K$ es la matriz que cumple $K \cdot \vec{v} = \vec{n} \times \vec{v}$. Las potencias de $K$ se repiten:

- $K \cdot \vec{n} = \vec{n} \times \vec{n} = \vec{0}$.
- $K^2 \cdot \vec{v} = \vec{n} \times (\vec{n} \times \vec{v}) = \vec{n} \cdot (\vec{n} \cdot \vec{v}) - \vec{v}$, por la fórmula del doble producto vectorial y $\vec{n} \cdot \vec{n} = 1$. En matrices, $K^2 = \vec{n} \cdot \vec{n}^T - I$.
- $K^3 = K \cdot (\vec{n} \cdot \vec{n}^T - I) = (K \cdot \vec{n}) \cdot \vec{n}^T - K = -K$.

Por tanto, $K^3 = -K$, $K^4 = -K^2$, $K^5 = K$... Las potencias impares son $\pm K$ y las pares, $\pm K^2$. Agrupándolas en la serie:

$$
\begin{aligned}
e^{\theta \cdot K} &= I + \left(\theta - \dfrac{\theta^3}{3!} + \dfrac{\theta^5}{5!} - \dots\right) \cdot K + \left(\dfrac{\theta^2}{2!} - \dfrac{\theta^4}{4!} + \dots\right) \cdot K^2 \\
&= I + \sin\theta \cdot K + (1 - \cos\theta) \cdot K^2.
\end{aligned}
$$

Es la fórmula de Rodrigues. Su significado geométrico:

- **El eje queda fijo:** como $K \cdot \vec{n} = \vec{0}$, $e^{\theta \cdot K} \cdot \vec{n} = \vec{n}$.
- **El plano perpendicular gira un ángulo $\theta$:** para $\vec{v}$ perpendicular a $\vec{n}$, $K^2 \cdot \vec{v} = -\vec{v}$, y queda $e^{\theta \cdot K} \cdot \vec{v} = \cos\theta \cdot \vec{v} + \sin\theta \cdot (\vec{n} \times \vec{v})$. Es el giro de ángulo $\theta$ en el plano de base $\vec{v}$ y $\vec{n} \times \vec{v}$.
- **Con $\vec{n} = \vec{e}_z$** ($K = J_z$) se recupera $R_z(\theta)$ (capítulo de rotaciones, punto 6). Igualmente, $R_x(\theta) = e^{\theta \cdot J_x}$ y $R_y(\theta) = e^{\theta \cdot J_y}$.

En resumen: $e^A$ es la rotación de ángulo $|\vec{\omega}|$ alrededor del eje $\vec{\omega}$. Los tres parámetros de la rotación son las tres componentes de $\vec{\omega}$.

5. Recíproco: toda rotación es una exponencial

Sea $R$ una rotación. Primero se ve que tiene un eje, es decir, un vector $\vec{n}$ con $R \cdot \vec{n} = \vec{n}$ (teorema de Euler). Como $R - I = R \cdot (I - R^T) = R \cdot (I - R)^T$ y $\det R = 1$:

$$
\begin{aligned}
\det(R - I) = \det R \cdot \det\left((I - R)^T\right) = \det(I - R) = (-1)^3 \cdot \det(R - I) = -\det(R - I),
\end{aligned}
$$

donde se ha usado que cambiar el signo de una matriz $3 \times 3$ multiplica su determinante por $(-1)^3$. Por tanto, $\det(R - I) = 0$: el sistema $(R - I) \cdot \vec{n} = \vec{0}$ tiene solución no nula, que se toma unitaria.

$R$ conserva los productos escalares: $(R \cdot \vec{v}) \cdot (R \cdot \vec{w}) = \vec{v}^T \cdot R^T \cdot R \cdot \vec{w} = \vec{v} \cdot \vec{w}$. Así, si $\vec{v}$ es perpendicular a $\vec{n}$, $(R \cdot \vec{v}) \cdot \vec{n} = (R \cdot \vec{v}) \cdot (R \cdot \vec{n}) = \vec{v} \cdot \vec{n} = 0$: $R$ lleva el plano perpendicular a $\vec{n}$ a sí mismo. En ese plano conserva longitudes y ángulos, y su determinante es $1$ (el de $R$, porque sobre $\vec{n}$ actúa como la identidad). Una transformación del plano con esas propiedades es un giro de un ángulo $\theta$ (el mismo razonamiento por columnas del capítulo de rotaciones, punto 4, en dos dimensiones). Según el punto 4, $e^{\theta \cdot K}$ hace exactamente lo mismo: deja fijo $\vec{n}$ y gira $\theta$ el plano perpendicular. Por tanto:

$$
\begin{aligned}
R = e^{\theta \cdot K} = e^A, \qquad A = \theta \cdot K \text{ antisimétrica}.
\end{aligned}
$$

Las rotaciones son exactamente las exponenciales de las matrices antisimétricas. La correspondencia no es única: $\theta$ y $\theta + 2 \cdot \pi$ dan la misma rotación, y también el ángulo $\theta$ alrededor de $\vec{n}$ y el ángulo $2 \cdot \pi - \theta$ alrededor de $-\vec{n}$.

6. Dos formas de dar una rotación con tres parámetros

- **Tres ángulos respecto de los ejes fijos** (capítulo de rotaciones): $R = R_z(\alpha) \cdot R_y(\beta) \cdot R_x(\gamma) = e^{\alpha \cdot J_z} \cdot e^{\beta \cdot J_y} \cdot e^{\gamma \cdot J_x}$.
- **Un vector eje-ángulo** $\vec{\omega} = (a, b, c)$: $R = e^{a \cdot J_x + b \cdot J_y + c \cdot J_z}$.

No son lo mismo: en general, $e^{\alpha \cdot J_z} \cdot e^{\beta \cdot J_y} \cdot e^{\gamma \cdot J_x} \neq e^{\alpha \cdot J_z + \beta \cdot J_y + \gamma \cdot J_x}$, porque las matrices $J$ no conmutan. Por ejemplo, $J_x \cdot J_y - J_y \cdot J_x = J_z \neq 0$. Se puede ver sin calcular ninguna exponencial. Si fuera $e^{M+N} = e^M \cdot e^N$ para $M = \dfrac{\pi}{2} \cdot J_x$ y $N = \dfrac{\pi}{2} \cdot J_y$, como $M + N = N + M$ se tendría $e^M \cdot e^N = e^{M+N} = e^N \cdot e^M$, es decir, $R_x(\pi/2) \cdot R_y(\pi/2) = R_y(\pi/2) \cdot R_x(\pi/2)$. Pero esos dos productos son distintos (capítulo de rotaciones, punto 2).

7. Las familias de Galileo como exponenciales

Lo mismo vale para las familias de un parámetro del grupo de Galileo (capítulo del grupo de Galileo, punto 5): cada una es $e^{s \cdot M}$ para una matriz $5 \times 5$ fija $M$.

- **Rotación alrededor de $\vec{n}$:** $M$ tiene $K$ en el bloque $3 \times 3$ y ceros en el resto, y $e^{s \cdot M}$ tiene $e^{s \cdot K}$ en ese bloque.
- **Cambio de velocidad en la dirección $x$:** $M$ tiene un $1$ en la fila $1$, columna $4$. **Traslación en $x$:** un $1$ en la fila $1$, columna $5$. **Traslación temporal:** un $1$ en la fila $4$, columna $5$. En los tres casos $M^2 = 0$: el único $1$ de $M$ está en una fila $i$ y una columna $j$ distintas, y $(M^2)_{ik} = M_{ij} \cdot M_{jk}$ necesitaría otro $1$ en la fila $j$, que no existe. La serie se corta en el segundo término: $e^{s \cdot M} = I + s \cdot M$, que es exactamente $G(I, s \cdot \vec{e}_x, \vec{0}, 0)$, $G(I, \vec{0}, s \cdot \vec{e}_x, 0)$ o $G(I, \vec{0}, \vec{0}, s)$.

Por el punto 2, $\dfrac{d}{ds} e^{s \cdot M} = M \cdot e^{s \cdot M}$ y $e^{s \cdot M} \cdot e^{r \cdot M} = e^{(s+r) \cdot M}$: cada familia es el flujo de un campo vectorial lineal, y $M$ es su generador.


LAS TRANSFORMACIONES DE GALILEO COMO EXPONENCIALES (26-09-2026)

Capítulo de trabajo: completar el formalismo escribiendo cualquier transformación de Galileo $G(R, \vec{v}, \vec{a}, b)$ en forma exponencial. Se hace de dos maneras (como producto de cuatro exponenciales y como una sola exponencial) y se termina con el campo vectorial que genera cada exponente y su cantidad conservada. Usa los capítulos «El grupo de Galileo» y «La exponencial de una matriz y las rotaciones». Todas las afirmaciones están comprobadas con SymPy.

1. Los diez generadores

$E_{ij}$ es la matriz $5 \times 5$ con un $1$ en la fila $i$, columna $j$, y ceros en el resto. Cada familia de un parámetro del grupo (capítulo del grupo de Galileo, punto 5) tiene como generador la derivada de la familia en $s = 0$:

| Familia de un parámetro | Generador | Matriz |
| --- | --- | --- |
| Rotación alrededor de $x$, $y$, $z$ | $\mathcal{J}_x$, $\mathcal{J}_y$, $\mathcal{J}_z$ | $J_x$, $J_y$, $J_z$ en el bloque $3 \times 3$; ceros en el resto |
| Cambio de velocidad en $x$, $y$, $z$ | $\mathcal{K}_x$, $\mathcal{K}_y$, $\mathcal{K}_z$ | $E_{14}$, $E_{24}$, $E_{34}$ |
| Traslación espacial en $x$, $y$, $z$ | $\mathcal{P}_x$, $\mathcal{P}_y$, $\mathcal{P}_z$ | $E_{15}$, $E_{25}$, $E_{35}$ |
| Traslación temporal | $\mathcal{T}$ | $E_{45}$ |

Para la traslación temporal se usa $\mathcal{T}$ y no $\mathcal{H}$, para no confundirla con el hamiltoniano. Con la notación $\vec{u} \cdot \vec{\mathcal{K}} = u_1 \cdot \mathcal{K}_x + u_2 \cdot \mathcal{K}_y + u_3 \cdot \mathcal{K}_z$ (y lo mismo para $\vec{\mathcal{J}}$ y $\vec{\mathcal{P}}$), un generador general es una combinación de los diez, con diez coeficientes $\vec{\omega}$, $\vec{u}$, $\vec{d}$ y $\tau$:

$$
\begin{aligned}
\Lambda = \vec{\omega} \cdot \vec{\mathcal{J}} + \vec{u} \cdot \vec{\mathcal{K}} + \vec{d} \cdot \vec{\mathcal{P}} + \tau \cdot \mathcal{T}
= \begin{pmatrix} A & \vec{u} & \vec{d} \\ \vec{0}^T & 0 & \tau \\ \vec{0}^T & 0 & 0 \end{pmatrix},
\end{aligned}
$$

donde $A$ es la matriz antisimétrica $3 \times 3$ con $A \cdot \vec{x} = \vec{\omega} \times \vec{x}$.

2. Qué generadores conmutan

Los productos de las matrices $E_{ij}$ siguen una regla sencilla: $E_{ij} \cdot E_{kl} = E_{il}$ si $j = k$, y es nulo si $j \neq k$. Con ella:

- $\mathcal{K}_i \cdot \mathcal{K}_j = E_{i4} \cdot E_{j4} = 0$, porque $4 \neq j$. Del mismo modo, $\mathcal{P}_i \cdot \mathcal{P}_j = 0$, $\mathcal{K}_i \cdot \mathcal{P}_j = 0$, $\mathcal{P}_i \cdot \mathcal{K}_j = 0$, $\mathcal{T} \cdot \mathcal{T} = 0$, $\mathcal{P}_i \cdot \mathcal{T} = 0$, $\mathcal{T} \cdot \mathcal{P}_i = 0$ y $\mathcal{T} \cdot \mathcal{K}_i = 0$.
- La excepción: $\mathcal{K}_i \cdot \mathcal{T} = E_{i4} \cdot E_{45} = E_{i5} = \mathcal{P}_i$, mientras que $\mathcal{T} \cdot \mathcal{K}_i = 0$.

Entre los siete generadores que no son rotaciones, el único par que no conmuta es un cambio de velocidad con la traslación temporal. Es el origen del término cruzado $\vec{v}_2 \cdot b_1$ de la ley de composición y de los factores que aparecen en los puntos 3 y 4.

3. Primera forma: producto de cuatro exponenciales

Como $(\vec{v} \cdot \vec{\mathcal{K}})^2 = 0$, $(\vec{a} \cdot \vec{\mathcal{P}})^2 = 0$ y $\mathcal{T}^2 = 0$ (punto 2), sus exponenciales se reducen a los dos primeros términos de la serie y son matrices de Galileo sencillas:

$$
\begin{aligned}
e^{\vec{a} \cdot \vec{\mathcal{P}}} &= I + \vec{a} \cdot \vec{\mathcal{P}} = G(I, \vec{0}, \vec{a}, 0), \\
e^{\vec{v} \cdot \vec{\mathcal{K}}} &= I + \vec{v} \cdot \vec{\mathcal{K}} = G(I, \vec{v}, \vec{0}, 0), \\
e^{b \cdot \mathcal{T}} &= I + b \cdot \mathcal{T} = G(I, \vec{0}, \vec{0}, b).
\end{aligned}
$$

La rotación es $e^{\vec{\omega} \cdot \vec{\mathcal{J}}} = G(e^A, \vec{0}, \vec{0}, 0)$, con $e^A = R$ (capítulo de la exponencial, puntos 4 y 5). Se componen con la ley del capítulo del grupo de Galileo, punto 2, empezando por la derecha:

- $G(I, \vec{0}, \vec{0}, b) \cdot G(R, \vec{0}, \vec{0}, 0) = G(R, \vec{0}, \vec{0}, b)$;
- $G(I, \vec{v}, \vec{0}, 0) \cdot G(R, \vec{0}, \vec{0}, b) = G(R,\ \vec{v},\ \vec{v} \cdot b,\ b)$, donde $\vec{v} \cdot b$ es el término cruzado;
- $G(I, \vec{0}, \vec{a}', 0) \cdot G(R, \vec{v}, \vec{v} \cdot b, b) = G(R,\ \vec{v},\ \vec{v} \cdot b + \vec{a}',\ b)$.

Para obtener el desplazamiento $\vec{a}$ hay que elegir $\vec{a}' = \vec{a} - \vec{v} \cdot b$, que compensa el término cruzado. Por tanto, toda transformación de Galileo es

$$
\begin{aligned}
G(R, \vec{v}, \vec{a}, b) 
= e^{(\vec{a} - \vec{v} \cdot b) \cdot \vec{\mathcal{P}}} \cdot e^{\vec{v} \cdot \vec{\mathcal{K}}} \cdot e^{b \cdot \mathcal{T}} \cdot e^{\vec{\omega} \cdot \vec{\mathcal{J}}}.
\end{aligned}
$$

Cada factor es una familia de un parámetro, y el orden importa: con otro orden, el vector que multiplica a $\vec{\mathcal{P}}$ sería distinto.

4. Segunda forma: una sola exponencial

**Potencias del generador.** Multiplicando por bloques (la fila de bloques $(A,\ \vec{u},\ \vec{d})$ por cada columna de bloques):

$$
\begin{aligned}
\Lambda^2 = 
\begin{pmatrix} A^2 & A \cdot \vec{u} & A \cdot \vec{d} + \tau \cdot \vec{u} \\ 
\vec{0}^T & 0 & 0 \\ 
\vec{0}^T & 0 & 0 \end{pmatrix}.
\end{aligned}
$$

Las dos últimas filas se anulan a partir de $\Lambda^2$. Multiplicando otra vez por $\Lambda$ por la izquierda, cada potencia añade un factor $A$ en la primera fila de bloques. Por inducción, para $k \ge 2$:

$$
\begin{aligned}
\Lambda^k = \begin{pmatrix} A^k & A^{k-1} \cdot \vec{u} & A^{k-1} \cdot \vec{d} + \tau \cdot A^{k-2} \cdot \vec{u} \\ \vec{0}^T & 0 & 0 \\ \vec{0}^T & 0 & 0 \end{pmatrix}.
\end{aligned}
$$

**La exponencial.** Sumando la serie $\sum_k \dfrac{\Lambda^k}{k!}$ bloque a bloque:

$$
\begin{aligned}
e^{\Lambda} = G\left(e^A,\ V \cdot \vec{u},\ V \cdot \vec{d} + \tau \cdot W \cdot \vec{u},\ \tau\right),
\qquad
V = \sum_{j=0}^{\infty} \dfrac{A^j}{(j+1)!},
\qquad
W = \sum_{j=0}^{\infty} \dfrac{A^j}{(j+2)!}.
\end{aligned}
$$

Por ejemplo, la columna de la velocidad es $\sum_{k \ge 1} \dfrac{A^{k-1} \cdot \vec{u}}{k!}$, que con $j = k - 1$ es $V \cdot \vec{u}$.

**Sin rotación** ($A = 0$): $V = I$ y $W = \dfrac{1}{2} \cdot I$, y queda

$$
\begin{aligned}
e^{\vec{u} \cdot \vec{\mathcal{K}} + \vec{d} \cdot \vec{\mathcal{P}} + \tau \cdot \mathcal{T}} = G\left(I,\ \vec{u},\ \vec{d} + \dfrac{\tau}{2} \cdot \vec{u},\ \tau\right).
\end{aligned}
$$

Los coeficientes del exponente no coinciden con los parámetros de la transformación: aparece $\dfrac{\tau}{2} \cdot \vec{u}$. La razón es que la exponencial aplica a la vez el cambio de velocidad y la traslación temporal, cada uno creciendo desde $0$ con el parámetro $s$ del flujo (punto 5). El punto con $t = 0$ se mueve según $\dfrac{d\vec{x}}{ds} = \vec{u} \cdot t(s) + \vec{d}$, con $t(s) = \tau \cdot s$, y entre $s = 0$ y $s = 1$ recorre $\int_0^1 (\vec{u} \cdot \tau \cdot s + \vec{d})\,ds = \dfrac{\tau}{2} \cdot \vec{u} + \vec{d}$: el tiempo desplazado vale, en promedio, $\tau/2$.

**Con rotación** ($A = \theta \cdot K$, con $\theta = |\vec{\omega}|$ y $K \cdot \vec{x} = \vec{n} \times \vec{x}$ para el eje unitario $\vec{n}$). Como $K^3 = -K$, las series se agrupan como en la fórmula de Rodrigues:

$$
\begin{aligned}
V &= I + \dfrac{1 - \cos\theta}{\theta} \cdot K + \dfrac{\theta - \sin\theta}{\theta} \cdot K^2, \\
W &= \dfrac{1}{2} \cdot I + \dfrac{\theta - \sin\theta}{\theta^2} \cdot K + \dfrac{\theta^2/2 - 1 + \cos\theta}{\theta^2} \cdot K^2.
\end{aligned}
$$

Por ejemplo, en $V$ las potencias impares dan $\sum_{m \ge 0} \dfrac{(-1)^m \cdot \theta^{2 \cdot m + 1}}{(2 \cdot m + 2)!} \cdot K = \dfrac{1 - \cos\theta}{\theta} \cdot K$, porque $\sum_{m \ge 0} \dfrac{(-1)^m \cdot \theta^{2 \cdot m + 2}}{(2 \cdot m + 2)!} = 1 - \cos\theta$.

**Toda transformación de Galileo es una sola exponencial.** Dada $G(R, \vec{v}, \vec{a}, b)$, se elige $A$ con $e^A = R$ y ángulo $\theta \in [0, \pi]$ (siempre es posible; capítulo de la exponencial, punto 5), $\tau = b$, y se despejan $\vec{u}$ y $\vec{d}$ de

$$
\begin{aligned}
V \cdot \vec{u} = \vec{v},
\qquad
V \cdot \vec{d} + b \cdot W \cdot \vec{u} = \vec{a}.
\end{aligned}
$$

Hace falta que $V$ sea invertible. Sobre el eje, $K \cdot \vec{n} = \vec{0}$ y $V \cdot \vec{n} = \vec{n}$. En el plano perpendicular, $K$ actúa como multiplicar por $i$ y $K^2$ como multiplicar por $-1$ (capítulo de rotaciones, punto 6), así que $V$ actúa como el número complejo

$$
\begin{aligned}
\dfrac{\sin\theta}{\theta} + i \cdot \dfrac{1 - \cos\theta}{\theta} = \dfrac{e^{i \cdot \theta} - 1}{i \cdot \theta},
\qquad
\left|\dfrac{e^{i \cdot \theta} - 1}{i \cdot \theta}\right|^2 = \dfrac{2 \cdot (1 - \cos\theta)}{\theta^2}.
\end{aligned}
$$

Por tanto, $\det V = \dfrac{2 \cdot (1 - \cos\theta)}{\theta^2}$, que no se anula para $0 < \theta \le \pi$. Con $\theta = 0$, $V = I$. En ambos casos $V$ es invertible, y $\vec{u} = V^{-1} \cdot \vec{v}$, $\vec{d} = V^{-1} \cdot (\vec{a} - b \cdot W \cdot \vec{u})$.

5. El campo vectorial de cada generador y su cantidad conservada

Por el capítulo de la exponencial, punto 2, $\dfrac{d}{ds} e^{s \cdot \Lambda} = \Lambda \cdot e^{s \cdot \Lambda}$: la familia $e^{s \cdot \Lambda}$ es el flujo del campo lineal que $\Lambda$ define sobre la columna $(\vec{x}, t, 1)$. Multiplicando:

$$
\begin{aligned}
\dfrac{d\vec{x}}{ds} &= \vec{\omega} \times \vec{x} + \vec{u} \cdot t + \vec{d}, \\
\dfrac{dt}{ds} &= \tau.
\end{aligned}
$$

Es el generador infinitesimal de «Ideas para el desarrollo», punto 1, con las diez direcciones a la vez: $\vec{\xi} = \vec{\omega} \times \vec{x} + \vec{u} \cdot t + \vec{d}$ para cada partícula y $\xi^t = \tau$. La cantidad de Noether $Q = \sum_a \vec{p}_a \cdot \vec{\xi}_a - H \cdot \tau - F$ (punto 3 de ese capítulo), con $F = \sum_a m_a \cdot \vec{u} \cdot \vec{x}_a$ para el cambio de velocidad, es lineal en los diez coeficientes:

$$
\begin{aligned}
Q = \vec{\omega} \cdot \vec{J} - \vec{u} \cdot \vec{G} + \vec{d} \cdot \vec{P} - \tau \cdot H.
\end{aligned}
$$

Término a término:

- $\sum_a \vec{p}_a \cdot (\vec{\omega} \times \vec{x}_a) = \vec{\omega} \cdot \sum_a \vec{x}_a \times \vec{p}_a = \vec{\omega} \cdot \vec{J}$, por la propiedad cíclica del producto mixto;
- $\sum_a \vec{p}_a \cdot (\vec{u} \cdot t) - \sum_a m_a \cdot \vec{u} \cdot \vec{x}_a = -\vec{u} \cdot \left(\sum_a m_a \cdot \vec{x}_a - \vec{P} \cdot t\right) = -\vec{u} \cdot \vec{G}$;
- $\sum_a \vec{p}_a \cdot \vec{d} = \vec{d} \cdot \vec{P}$.

Aquí $\vec{G} = M \cdot \vec{X}_{\mathrm{cm}} - \vec{P} \cdot t$ es la cantidad del cambio de velocidad, no una matriz de Galileo. Como $Q$ se conserva para cualquier elección de los diez coeficientes, se conserva cada una de las diez cantidades por separado.

6. Resumen

| Generador | Familia $e^{s \cdot (\dots)}$ | Campo $(\vec{\xi},\ \xi^t)$ | Cantidad conservada |
| --- | --- | --- | --- |
| $\vec{n} \cdot \vec{\mathcal{J}}$ | $G(e^{s \cdot K}, \vec{0}, \vec{0}, 0)$ | $(\vec{n} \times \vec{x},\ 0)$ | $\vec{n} \cdot \vec{J}$ (momento angular) |
| $\vec{e} \cdot \vec{\mathcal{K}}$ | $G(I, s \cdot \vec{e}, \vec{0}, 0)$ | $(\vec{e} \cdot t,\ 0)$ | $-\vec{e} \cdot \vec{G}$ (centro de masas) |
| $\vec{e} \cdot \vec{\mathcal{P}}$ | $G(I, \vec{0}, s \cdot \vec{e}, 0)$ | $(\vec{e},\ 0)$ | $\vec{e} \cdot \vec{P}$ (momento lineal) |
| $\mathcal{T}$ | $G(I, \vec{0}, \vec{0}, s)$ | $(\vec{0},\ 1)$ | $-H$ (energía) |

Toda transformación de Galileo se obtiene como producto de estas familias (punto 3) o como una sola exponencial $e^{\Lambda}$ (punto 4). Cada generador define un campo vectorial en el espacio-tiempo (punto 5) y, por el teorema de Noether, una cantidad conservada.
