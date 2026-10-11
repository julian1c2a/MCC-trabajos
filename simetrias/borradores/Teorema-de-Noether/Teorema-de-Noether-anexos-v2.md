---
author: "Julián Calderón Almendros"
---

# El teorema de Noether: anexos (versión 2)

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-11
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

Resultados matemáticos sobre los grupos de transformaciones que usa la parte física de la serie: las rotaciones del espacio, la exponencial de una matriz, el grupo de Galileo, el grupo de Lorentz y el de Poincaré, todos en forma de matrices, y la relación entre los dos últimos y el primero. Responden a preguntas que la parte física da por sabidas: por qué el generador de un giro es $\vec{n} \times \vec{q}$, por qué las diez transformaciones de Galileo y las diez de Poincaré forman grupos de diez parámetros cuyas familias de un parámetro son flujos, y por qué la masa aparece en la mecánica cuántica como un término adicional en las relaciones del grupo de Galileo.

La versión 2 de la serie consta de cinco documentos:

* «El teorema de Noether: parte matemática (versión 2)»: la teoría, con una función, varias funciones y varias variables, los flujos, las derivadas de Fréchet y de Lie, y una guía de dimensión infinita.
* «El teorema de Noether: ejemplos matemáticos (versión 2)»: el camino más corto, como gráfica y en forma paramétrica, las ecuaciones con la estructura de las de Newton y la ecuación de Laplace.
* «El teorema de Noether: parte física (versión 2)»: los sistemas de partículas, el grupo de Galileo, el grupo de Lorentz y el de Poincaré, y la mecánica cuántica no relativista.
* «El teorema de Noether: ejemplos físicos (versión 2)»: los casos de la parte física con la comprobación sobre la solución explícita, la cuerda con el cambio de velocidad de Lorentz, la partícula relativista y la partícula cuántica en un potencial central.
* «El teorema de Noether: anexos (versión 2)», este documento.

Las citas «parte matemática» y «parte física» se refieren a la versión 2. Todas las afirmaciones de este documento están comprobadas con SymPy en Teorema-de-Noether-anexos-v2-comprobaciones.py, en el mismo directorio.

**Diferencias con la versión 1**, cuyo documento se conserva:

* los apartados 1 a 3 proceden de la versión 1, con la notación de la parte física de la versión 2: coordenadas $(q_1, q_2, q_3)$ en lugar de $(x, y, z)$, ángulos $\theta_1$, $\theta_2$, $\theta_3$, matriz de Galileo $\Gamma$ y generador general $X$;
* la exponencial de una matriz va antes de los grupos, y añade el determinante de una exponencial, la fórmula de las potencias que se repiten con signo positivo y el producto de dos exponenciales hasta segundo orden;
* la forma de producto de una transformación de Galileo usa un orden de los factores que no necesita corrección;
* los apartados 4 a 6 son nuevos: el grupo de Lorentz y el de Poincaré en forma de matrices, la contracción de Poincaré a Galileo y la carga central.

**Avisos de notación.**

* **Matrices de los grupos:** $R$ es una rotación; $\Gamma(R, \vec{v}, \vec{a}, b)$, una transformación de Galileo; $\Lambda$, una transformación de Lorentz; $\Pi(\Lambda, a)$, una de Poincaré; $X$, un generador. $\vec{G}$, con flecha, es la cantidad conservada de los cambios de velocidad de la parte física, no una matriz.
* **Generadores de los grupos:** $\mathcal{J}_k$ (giros), $\mathcal{K}_k$ (cambios de velocidad), $\mathcal{P}_k$ (traslaciones) y $\mathcal{T}$ o $\mathcal{P}_0$ (traslación en el tiempo). Las mismas letras designan los de Galileo (apartado 3) y los de Lorentz y Poincaré (apartados 4 y 5), que son matrices distintas; el apartado 6 muestra que los segundos tienden a los primeros. $J_k$, sin caligrafía, son las matrices $3 \times 3$ de las rotaciones infinitesimales.
* **Numeración de filas y columnas:** de $1$ a $5$ en las matrices de Galileo, que actúan sobre $(\vec{q}, t, 1)$; de $0$ a $3$ en las de Lorentz y de $0$ a $4$ en las de Poincaré, que actúan sobre $(c \cdot t, \vec{q})$ y $(c \cdot t, \vec{q}, 1)$. $E_{ij}$ es la matriz con un $1$ en la fila $i$ y la columna $j$ y ceros en el resto, con la numeración de cada caso.
* $\eta$ es la métrica de Minkowski del apartado 4 (en la parte matemática, $\eta$ es otra cosa); $\zeta$, la rapidez; $\beta = \dfrac{v}{c}$; $\gamma$, el factor de Lorentz.
* $A_{\vec{n}}$ es la matriz antisimétrica con $A_{\vec{n}} \cdot \vec{v} = \vec{n} \times \vec{v}$ (en la versión 1, $K$). $V$ y $W$ son las series de los apartados 3.8 y 5.3, no energías potenciales.
* $\{f, g\}$ es el corchete de Poisson del apartado 6.3.
* $\varepsilon$ es un parámetro pequeño, como en el resto de la serie.

## 1. Rotaciones en tres dimensiones

La matriz de una rotación cualquiera en tres dimensiones, con tres ángulos, construida de tres maneras: producto de rotaciones alrededor de los ejes, a partir de $R^{\mathsf{T}} \cdot R = I$ y como composición de rotaciones infinitesimales. $R^{\mathsf{T}}$ es la matriz traspuesta e $I$ la identidad. Abreviaturas: $c_k := \cos\theta_k$ y $s_k := \sin\theta_k$, para $k = 1, 2, 3$.

### 1.1. Rotaciones alrededor de cada eje

Una rotación de ángulo $\theta$ alrededor del eje $q_3$, en sentido antihorario vista desde el semieje $q_3$ positivo, deja fija la coordenada $q_3$ y gira el plano $q_1 q_2$. Las tres rotaciones alrededor de los ejes son:

$$
\begin{aligned}
R_3(\theta) &= \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix},
\qquad
R_1(\theta) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}, \\
R_2(\theta) &= \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}.
\end{aligned}
$$

$R_1$ gira el plano $q_2 q_3$ (de $q_2$ hacia $q_3$) y $R_2$ gira el plano $q_3 q_1$ (de $q_3$ hacia $q_1$). En $R_2$ el signo menos aparece abajo y no arriba porque el orden cíclico de los ejes es $1 \to 2 \to 3 \to 1$: en el plano $q_3 q_1$ la primera coordenada es $q_3$, que en la matriz ocupa la tercera fila.

Cada una cumple $R^{\mathsf{T}} \cdot R = I$. Para $R_3$, el producto de la traspuesta por la matriz da en el bloque $q_1 q_2$:

$$
\begin{aligned}
\begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \cdot \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},
\end{aligned}
$$

porque las dos entradas de la diagonal valen $\cos^2\theta + \sin^2\theta = 1$, y las otras dos, $-\cos\theta \cdot \sin\theta + \sin\theta \cdot \cos\theta = 0$. El elemento $(3, 3)$ vale $1$. Las otras dos se comprueban igual. Además, $\det R_3(\theta) = \cos^2\theta + \sin^2\theta = 1$, y lo mismo para $R_1$ y $R_2$.

### 1.2. Las rotaciones se componen multiplicando, no sumando

Aplicar primero $R_1$ y después $R_2$ a un vector $\vec{v}$ da $R_2 \cdot (R_1 \cdot \vec{v}) = (R_2 \cdot R_1) \cdot \vec{v}$: la composición es el producto de matrices, con la primera rotación a la derecha. La suma no es una rotación. Por ejemplo, con los tres ángulos nulos cada matriz es la identidad, y

$$
\begin{aligned}
S = R_1(0) + R_2(0) + R_3(0) = 3 \cdot I
\quad \Longrightarrow \quad
S^{\mathsf{T}} \cdot S = 9 \cdot I \neq I:
\end{aligned}
$$

$S$ multiplica todas las longitudes por $3$.

El orden del producto importa. Con giros de $90^\circ$:

$$
\begin{aligned}
R_1(\pi/2) \cdot R_2(\pi/2) = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix},
\qquad
R_2(\pi/2) \cdot R_1(\pi/2) = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & -1 \\ -1 & 0 & 0 \end{pmatrix}.
\end{aligned}
$$

La primera lleva el vector $\vec{e}_3 = (0, 0, 1)$ a $(1, 0, 0)$, y la segunda a $(0, -1, 0)$. Por eso, para describir una rotación cualquiera con tres ángulos, hay que fijar un orden. Aquí se usa: primero el ángulo $\theta_1$ alrededor de $q_1$, después $\theta_2$ alrededor de $q_2$ y por último $\theta_3$ alrededor de $q_3$, todos respecto de los ejes fijos. Hay otros convenios (los ángulos de Euler clásicos usan los ejes $3$, $1$, $3$), y todos usan tres ángulos.

### 1.3. La matriz de una rotación cualquiera

$$
\begin{aligned}
R(\theta_1, \theta_2, \theta_3) &= R_3(\theta_3) \cdot R_2(\theta_2) \cdot R_1(\theta_1) \\
&= \begin{pmatrix}
c_3 \cdot c_2 & c_3 \cdot s_2 \cdot s_1 - s_3 \cdot c_1 & c_3 \cdot s_2 \cdot c_1 + s_3 \cdot s_1 \\
s_3 \cdot c_2 & s_3 \cdot s_2 \cdot s_1 + c_3 \cdot c_1 & s_3 \cdot s_2 \cdot c_1 - c_3 \cdot s_1 \\
-s_2 & c_2 \cdot s_1 & c_2 \cdot c_1
\end{pmatrix}.
\end{aligned}
$$

Cumple $R^{\mathsf{T}} \cdot R = I$ sin necesidad de desarrollar los productos. Como la traspuesta de un producto es el producto de las traspuestas en orden inverso, $(A \cdot B)^{\mathsf{T}} = B^{\mathsf{T}} \cdot A^{\mathsf{T}}$:

$$
\begin{aligned}
R^{\mathsf{T}} \cdot R &= R_1^{\mathsf{T}} \cdot R_2^{\mathsf{T}} \cdot \left(R_3^{\mathsf{T}} \cdot R_3\right) \cdot R_2 \cdot R_1 \\
&= R_1^{\mathsf{T}} \cdot \left(R_2^{\mathsf{T}} \cdot R_2\right) \cdot R_1 \\
&= R_1^{\mathsf{T}} \cdot R_1 = I,
\end{aligned}
$$

donde en cada paso se ha sustituido el paréntesis central por $I$. Del mismo modo, $\det R = \det R_3 \cdot \det R_2 \cdot \det R_1 = 1$.

### 1.4. Derivación a partir de $R^{\mathsf{T}} \cdot R = I$

El elemento $(i, j)$ de $R^{\mathsf{T}} \cdot R$ es el producto escalar de la columna $i$ de $R$ por la columna $j$. Si las columnas son $\vec{r}_1$, $\vec{r}_2$ y $\vec{r}_3$, la condición $R^{\mathsf{T}} \cdot R = I$ equivale a:

* $\vec{r}_1 \cdot \vec{r}_1 = \vec{r}_2 \cdot \vec{r}_2 = \vec{r}_3 \cdot \vec{r}_3 = 1$ (cada columna es unitaria: 3 ecuaciones);
* $\vec{r}_1 \cdot \vec{r}_2 = \vec{r}_1 \cdot \vec{r}_3 = \vec{r}_2 \cdot \vec{r}_3 = 0$ (columnas perpendiculares dos a dos: 3 ecuaciones).

Son $6$ ecuaciones para $9$ entradas, así que quedan $9 - 6 = 3$ parámetros libres. La matriz se construye columna a columna, contando los parámetros:

* **Primera columna: 2 ángulos.** Un vector unitario de $\mathbb{R}^3$ queda fijado por dos ángulos, como un punto de la esfera por su longitud y su latitud. Con $\theta_3$ como longitud y $-\theta_2$ como latitud: $\vec{r}_1 = (c_3 \cdot c_2,\ s_3 \cdot c_2,\ -s_2)$, que cumple $|\vec{r}_1|^2 = c_2^2 \cdot (c_3^2 + s_3^2) + s_2^2 = 1$.
* **Segunda columna: 1 ángulo.** $\vec{r}_2$ es unitario y perpendicular a $\vec{r}_1$, luego está en la circunferencia unidad del plano perpendicular a $\vec{r}_1$. Ese plano tiene como base ortonormal $\vec{w}_1 = (-s_3,\ c_3,\ 0)$ y $\vec{w}_2 = \vec{r}_1 \times \vec{w}_1 = (c_3 \cdot s_2,\ s_3 \cdot s_2,\ c_2)$. Se comprueba que $\vec{w}_1 \cdot \vec{r}_1 = -s_3 \cdot c_3 \cdot c_2 + c_3 \cdot s_3 \cdot c_2 = 0$, y $\vec{w}_2$ es perpendicular a los dos por ser un producto vectorial. Un punto de esa circunferencia queda fijado por un ángulo: $\vec{r}_2 = c_1 \cdot \vec{w}_1 + s_1 \cdot \vec{w}_2$.
* **Tercera columna: ningún parámetro.** $\vec{r}_3$ es unitario y perpendicular a $\vec{r}_1$ y a $\vec{r}_2$, así que solo puede ser $\vec{r}_1 \times \vec{r}_2$ o $-\vec{r}_1 \times \vec{r}_2$. La condición $\det R = +1$ elige el signo positivo, porque $\det(\vec{r}_1, \vec{r}_2, \vec{r}_3) = (\vec{r}_1 \times \vec{r}_2) \cdot \vec{r}_3$.

En total, $2 + 1 + 0 = 3$ parámetros, y la matriz $(\vec{r}_1, \vec{r}_2, \vec{r}_1 \times \vec{r}_2)$ coincide entrada a entrada con la del apartado 1.3: los dos caminos llevan al mismo resultado.

Sobre el determinante: de $R^{\mathsf{T}} \cdot R = I$ se deduce $\det(R^{\mathsf{T}}) \cdot \det R = (\det R)^2 = 1$, así que $\det R = \pm 1$. Las matrices con $\det R = -1$ incluyen una reflexión, como $\mathrm{diag}(1, 1, -1)$, que cambia $q_3$ por $-q_3$. No se pueden alcanzar desde la identidad variando los ángulos de forma continua, porque el determinante varía de forma continua y solo puede tomar los valores $\pm 1$. Las rotaciones son las de $\det R = +1$.

### 1.5. Rotaciones infinitesimales

Una rotación próxima a la identidad se escribe $R = I + A$, con $A$ pequeña (sus entradas son de primer orden en los ángulos). Sustituyendo en $R^{\mathsf{T}} \cdot R = I$:

$$
\begin{aligned}
(I + A^{\mathsf{T}}) \cdot (I + A) = I + A^{\mathsf{T}} + A + A^{\mathsf{T}} \cdot A = I.
\end{aligned}
$$

$A^{\mathsf{T}} \cdot A$ es de segundo orden y se desprecia. A primer orden queda $A^{\mathsf{T}} = -A$: $A$ es **antisimétrica**. Su diagonal es nula y cada entrada de un lado es la opuesta de la simétrica, así que tiene $3$ entradas libres, $\omega_1$, $\omega_2$ y $\omega_3$ (los tres parámetros de nuevo):

$$
\begin{aligned}
A =
\begin{pmatrix} 0 & -\omega_3 & \omega_2 \\
\omega_3 & 0 & -\omega_1 \\
-\omega_2 & \omega_1 & 0
\end{pmatrix}
= \omega_1 \cdot J_1 + \omega_2 \cdot J_2 + \omega_3 \cdot J_3, \\
J_3 =
\begin{pmatrix}
0 & -1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix},
\end{aligned}
$$

y análogamente $J_1$ y $J_2$ (un $1$ y un $-1$ en el plano que gira cada eje). Son las derivadas de las rotaciones finitas en el ángulo cero. Por ejemplo, con $\cos\varepsilon = 1 - \dfrac{\varepsilon^2}{2} + \dots$ y $\sin\varepsilon = \varepsilon - \dfrac{\varepsilon^3}{6} + \dots$,

$$
\begin{aligned}
R_3(\varepsilon) = \begin{pmatrix} 1 & -\varepsilon & 0 \\ \varepsilon & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} + O(\varepsilon^2) = I + \varepsilon \cdot J_3 + O(\varepsilon^2).
\end{aligned}
$$

Aplicada a un vector, la rotación infinitesimal lo desplaza en un producto vectorial. Con $\vec{\omega} = (\omega_1, \omega_2, \omega_3)$:

$$
\begin{aligned}
A \cdot \vec{v} &= (\omega_2 \cdot v_3 - \omega_3 \cdot v_2,\ \omega_3 \cdot v_1 - \omega_1 \cdot v_3,\ \omega_1 \cdot v_2 - \omega_2 \cdot v_1) = \vec{\omega} \times \vec{v}, \\
R \cdot \vec{v} &= \vec{v} + \vec{\omega} \times \vec{v} + O(|\vec{\omega}|^2).
\end{aligned}
$$

El desplazamiento es perpendicular al eje $\vec{\omega}$ y al propio $\vec{v}$, como corresponde a un giro alrededor de $\vec{\omega}$ de ángulo $|\vec{\omega}|$. Es el generador $\vec{n} \times \vec{q}$ de la parte física, apartado 3, con $\vec{\omega} = \varepsilon \cdot \vec{n}$.

**A primer orden, las rotaciones infinitesimales conmutan; a segundo orden, no.** Con dos parámetros pequeños, $\varepsilon$ y $\varepsilon'$,

$$
\begin{aligned}
(I + \varepsilon \cdot J_1) \cdot (I + \varepsilon' \cdot J_2) - (I + \varepsilon' \cdot J_2) \cdot (I + \varepsilon \cdot J_1) = \varepsilon \cdot \varepsilon' \cdot (J_1 \cdot J_2 - J_2 \cdot J_1).
\end{aligned}
$$

La diferencia es de segundo orden, y su coeficiente es el **conmutador** de las dos matrices, $[J_1, J_2] := J_1 \cdot J_2 - J_2 \cdot J_1$. Multiplicando las matrices,

$$
\begin{aligned}
{[J_1, J_2]} = J_3, \qquad [J_2, J_3] = J_1, \qquad [J_3, J_1] = J_2:
\end{aligned}
$$

la diferencia entre girar alrededor de $q_1$ y de $q_2$ en un orden o en el otro es, a segundo orden, un giro alrededor de $q_3$. El apartado 2.7 generaliza esta observación.

### 1.6. Rotación finita como composición de rotaciones infinitesimales

Las rotaciones alrededor de un mismo eje se componen sumando los ángulos: $R_3(\alpha) \cdot R_3(\beta) = R_3(\alpha + \beta)$. En el bloque $q_1 q_2$, la entrada $(1, 1)$ del producto es $\cos\alpha \cdot \cos\beta - \sin\alpha \cdot \sin\beta = \cos(\alpha + \beta)$, y las demás salen igual con las fórmulas del seno y del coseno de la suma. Por tanto, una rotación de ángulo $\theta$ es exactamente la composición de $N$ rotaciones de ángulo $\theta/N$:

$$
\begin{aligned}
R_3(\theta) = \left(R_3\left(\dfrac{\theta}{N}\right)\right)^N.
\end{aligned}
$$

Si en cada paso se sustituye la rotación por su aproximación de primer orden, $I + \dfrac{\theta}{N} \cdot J_3$, el producto de los $N$ pasos tiende a la rotación exacta cuando $N \to \infty$. La forma más directa de verlo es con números complejos. En el plano $q_1 q_2$, $J_3$ lleva $(q_1, q_2)$ a $(-q_2, q_1)$, que es multiplicar $q_1 + i \cdot q_2$ por la unidad imaginaria $i$. Cada paso es, entonces, multiplicar por $1 + i \cdot \dfrac{\theta}{N}$, y $N$ pasos:

$$
\begin{aligned}
\left(1 + \dfrac{i \cdot \theta}{N}\right)^N \xrightarrow[N \to \infty]{} e^{i \cdot \theta} = \cos\theta + i \cdot \sin\theta,
\end{aligned}
$$

por el mismo límite que $\left(1 + \dfrac{x}{N}\right)^N \to e^x$, que vale también para $x$ complejo. Multiplicar por $\cos\theta + i \cdot \sin\theta$ es girar un ángulo $\theta$:

$$
\begin{aligned}
(q_1 + i \cdot q_2) \cdot (\cos\theta + i \cdot \sin\theta) &= (q_1 \cdot \cos\theta - q_2 \cdot \sin\theta) \\
&\qquad + i \cdot (q_1 \cdot \sin\theta + q_2 \cdot \cos\theta),
\end{aligned}
$$

que son las dos primeras filas de $R_3(\theta)$.

Por qué se pueden despreciar los órdenes superiores: cada paso de primer orden no conserva exactamente la longitud, porque $\left|1 + \dfrac{i \cdot \theta}{N}\right| = \sqrt{1 + \dfrac{\theta^2}{N^2}}$, con un error de segundo orden, $\dfrac{\theta^2}{2 \cdot N^2}$. Tras $N$ pasos, el logaritmo del factor acumulado es

$$
\begin{aligned}
\ln\left(1 + \dfrac{\theta^2}{N^2}\right)^{N/2} = \dfrac{N}{2} \cdot \ln\left(1 + \dfrac{\theta^2}{N^2}\right) = \dfrac{\theta^2}{2 \cdot N} + O\!\left(\dfrac{1}{N^3}\right) \xrightarrow[N \to \infty]{} 0.
\end{aligned}
$$

Los $N$ errores de orden $1/N^2$ suman un error de orden $1/N$, que desaparece en el límite. Con el ángulo el error es aún menor: cada paso gira $\arctan(\theta/N) = \dfrac{\theta}{N} - \dfrac{\theta^3}{3 \cdot N^3} + \dots$, con un error de orden $1/N^3$, y $N$ pasos acumulan un error de orden $1/N^2$.

En forma matricial, el mismo límite es la serie exponencial del apartado 2, $\sum_k \dfrac{\theta^k}{k!} \cdot J_3^k$. Como $J_3^2 = -\mathrm{diag}(1, 1, 0)$ y $J_3^3 = -J_3$, las potencias se repiten con periodo $2$ salvo el signo. Agrupando las impares y las pares:

$$
\begin{aligned}
R_3(\theta) &= I + \left(\theta - \dfrac{\theta^3}{3!} + \dots\right) \cdot J_3 + \left(\dfrac{\theta^2}{2!} - \dfrac{\theta^4}{4!} + \dots\right) \cdot J_3^2 \\
&= I + \sin\theta \cdot J_3 + (1 - \cos\theta) \cdot J_3^2.
\end{aligned}
$$

Comprobación de la entrada $(1, 1)$: $1 + (1 - \cos\theta) \cdot (-1) = \cos\theta$.

### 1.7. Las rotaciones forman un grupo

Componer rotaciones es multiplicar sus matrices. Un **grupo** es un conjunto con una operación que cumple cuatro propiedades: la composición de dos elementos está en el conjunto, hay un elemento neutro, cada elemento tiene inverso y la operación es asociativa. El conjunto de las matrices $3 \times 3$ con $R^{\mathsf{T}} \cdot R = I$ y $\det R = 1$ las cumple:

* **La composición de dos rotaciones es una rotación.** Con $(A \cdot B)^{\mathsf{T}} = B^{\mathsf{T}} \cdot A^{\mathsf{T}}$:

  $$
  \begin{aligned}
  (A \cdot B)^{\mathsf{T}} \cdot (A \cdot B) = B^{\mathsf{T}} \cdot (A^{\mathsf{T}} \cdot A) \cdot B = B^{\mathsf{T}} \cdot B = I,
  \end{aligned}
  $$

  y $\det(A \cdot B) = \det A \cdot \det B = 1$.
* **La identidad es una rotación** (la de ángulo cero): $I^{\mathsf{T}} \cdot I = I$ y $\det I = 1$.
* **La inversa de una rotación es una rotación, y es su traspuesta: $A^{-1} = A^{\mathsf{T}}$.** $A^{\mathsf{T}} \cdot A = I$ dice que $A^{\mathsf{T}}$ es inversa de $A$ por la izquierda; en matrices cuadradas, una inversa por la izquierda lo es también por la derecha, así que $A \cdot A^{\mathsf{T}} = I$. Además, $A^{\mathsf{T}}$ es una rotación: $(A^{\mathsf{T}})^{\mathsf{T}} \cdot A^{\mathsf{T}} = A \cdot A^{\mathsf{T}} = I$ y $\det A^{\mathsf{T}} = \det A = 1$.
* **Asociatividad:** $(A \cdot B) \cdot C = A \cdot (B \cdot C)$, porque el producto de matrices, como toda composición de aplicaciones, es asociativo.

Este grupo se llama $SO(3)$, grupo especial ortogonal de orden $3$. Dos precisiones:

* **No es conmutativo:** en general, $A \cdot B \neq B \cdot A$ (el ejemplo de los giros de $90^\circ$ del apartado 1.2).
* **La condición $\det R = +1$ es necesaria.** Las matrices ortogonales con $\det R = -1$ (una rotación seguida de una reflexión) no forman un grupo por sí solas: el producto de dos de ellas tiene determinante $(-1) \cdot (-1) = +1$, y la identidad no está entre ellas. Junto con las rotaciones forman el grupo ortogonal $O(3)$.

El mismo razonamiento se aplica a las matrices de los grupos de Galileo, de Lorentz y de Poincaré de los apartados 3 a 5: componer transformaciones es multiplicar sus matrices e invertir una transformación es invertir su matriz.

## 2. La exponencial de una matriz

Se define $e^M$ para una matriz cuadrada $M$, se calculan dos familias de exponenciales en forma cerrada y se ve qué dice el conmutador sobre el producto de dos exponenciales. Se usa $A$ para el exponente cuando es antisimétrico, como en el apartado 1.5.

### 2.1. Definición

Para un número real, $e^x = \sum_{k=0}^{\infty} \dfrac{x^k}{k!}$. Para una matriz cuadrada $M$ se define igual, con las potencias de la matriz ($M^0 = I$, $M^1 = M$, $M^2 = M \cdot M$...):

$$
\begin{aligned}
e^M = \sum_{k=0}^{\infty} \dfrac{M^k}{k!} = I + M + \dfrac{M^2}{2!} + \dfrac{M^3}{3!} + \dots
\end{aligned}
$$

Cada entrada de $e^M$ es la suma de una serie numérica. Es la misma serie que apareció en el apartado 1.6 como límite de $N$ rotaciones infinitesimales.

La serie converge para toda matriz. Se usa la norma $\lVert M \rVert = \sqrt{\sum_{i,j} M_{ij}^2}$ (la raíz de la suma de los cuadrados de las entradas), que cumple $\lVert M \cdot N \rVert \leq \lVert M \rVert \cdot \lVert N \rVert$. En efecto, $(M \cdot N)_{ij} = \sum_l M_{il} \cdot N_{lj}$ y, por la desigualdad de Cauchy–Schwarz, $|(M \cdot N)_{ij}|^2 \leq \left(\sum_l M_{il}^2\right) \cdot \left(\sum_l N_{lj}^2\right)$; sumando en $i$ y en $j$ se obtiene $\lVert M \cdot N \rVert^2 \leq \lVert M \rVert^2 \cdot \lVert N \rVert^2$. Aplicándolo $k$ veces, $\lVert M^k \rVert \leq \lVert M \rVert^k$, y cada entrada cumple $|(M^k)_{ij}| \leq \lVert M^k \rVert$. Por tanto, la serie de cada entrada está acotada término a término por $\sum_k \dfrac{\lVert M \rVert^k}{k!} = e^{\lVert M \rVert}$, que es finita: la serie converge absolutamente.

### 2.2. Propiedades

* **$e^0 = I$**, porque todas las potencias $0^k$ con $k \geq 1$ son nulas.
* **$(e^M)^{\mathsf{T}} = e^{M^{\mathsf{T}}}$**, porque la traspuesta de una suma es la suma de las traspuestas y $(M^k)^{\mathsf{T}} = (M^{\mathsf{T}})^k$. Del mismo modo, si $C$ es invertible, $e^{C \cdot M \cdot C^{-1}} = C \cdot e^M \cdot C^{-1}$, porque $(C \cdot M \cdot C^{-1})^k = C \cdot M^k \cdot C^{-1}$.
* **Si $M \cdot N = N \cdot M$, entonces $e^{M+N} = e^M \cdot e^N$.** La condición hace falta para desarrollar las potencias con el binomio de Newton. Por ejemplo, $(M + N)^2 = M^2 + M \cdot N + N \cdot M + N^2$, que solo es $M^2 + 2 \cdot M \cdot N + N^2$ si $M \cdot N = N \cdot M$. Con esa condición, $(M + N)^k = \sum_{j=0}^{k} \dfrac{k!}{j! \cdot (k-j)!} \cdot M^j \cdot N^{k-j}$, y

  $$
  \begin{aligned}
  e^{M+N} = \sum_{k=0}^{\infty} \sum_{j=0}^{k} \dfrac{M^j}{j!} \cdot \dfrac{N^{k-j}}{(k-j)!} = \left(\sum_{j=0}^{\infty} \dfrac{M^j}{j!}\right) \cdot \left(\sum_{l=0}^{\infty} \dfrac{N^l}{l!}\right) = e^M \cdot e^N,
  \end{aligned}
  $$

  donde reordenar los términos está permitido porque las series convergen absolutamente. Sin la condición, la igualdad falla en general (apartados 2.6 y 2.7).
* **Consecuencias.** $s \cdot M$ y $r \cdot M$ conmutan, así que $e^{s \cdot M} \cdot e^{r \cdot M} = e^{(s+r) \cdot M}$: la familia $e^{s \cdot M}$ se compone sumando el parámetro. Con $r = -s$: $e^{s \cdot M} \cdot e^{-s \cdot M} = e^0 = I$. Por tanto, $e^M$ siempre es invertible y su inversa es $e^{-M}$.
* **Derivada respecto de un parámetro.** Derivando la serie término a término (está permitido, porque es una serie de potencias en $s$ que converge para todo $s$):

  $$
  \begin{aligned}
  \dfrac{d}{ds} e^{s \cdot M} = \sum_{k=1}^{\infty} \dfrac{k \cdot s^{k-1} \cdot M^k}{k!} = M \cdot \sum_{k=1}^{\infty} \dfrac{s^{k-1} \cdot M^{k-1}}{(k-1)!} = M \cdot e^{s \cdot M}.
  \end{aligned}
  $$

  Así, $\vec{y}(s) = e^{s \cdot M} \cdot \vec{y}_0$ es la solución de $\dfrac{d\vec{y}}{ds} = M \cdot \vec{y}$ con $\vec{y}(0) = \vec{y}_0$: $e^{s \cdot M}$ es el flujo del campo vectorial lineal $M \cdot \vec{y}$ (parte matemática, apartado 9.1). Por la unicidad de las soluciones de ese sistema, una familia de matrices $U(s)$ con $\dfrac{dU}{ds} = M \cdot U$ y $U(0) = I$ es $e^{s \cdot M}$.
* **El determinante: $\det e^M = e^{\operatorname{tr} M}$**, donde $\operatorname{tr} M = \sum_i M_{ii}$ es la **traza**. Sea $f(s) := \det e^{s \cdot M}$. Como $e^{(s+h) \cdot M} = e^{s \cdot M} \cdot e^{h \cdot M}$ y el determinante de un producto es el producto de los determinantes, $f(s + h) = f(s) \cdot \det e^{h \cdot M}$. Además, $e^{h \cdot M} = I + h \cdot M + O(h^2)$, y el determinante, que es una suma de productos de entradas, una de cada fila y de cada columna (fórmula de Leibniz), cumple

  $$
  \begin{aligned}
  \det(I + h \cdot M) = \prod_i (1 + h \cdot M_{ii}) + O(h^2) = 1 + h \cdot \operatorname{tr} M + O(h^2),
  \end{aligned}
  $$

  porque cualquier producto distinto del de la diagonal contiene al menos dos factores fuera de la diagonal, de la forma $h \cdot M_{ij}$. Por tanto, $f'(s) = \operatorname{tr} M \cdot f(s)$ con $f(0) = 1$, cuya única solución es $f(s) = e^{s \cdot \operatorname{tr} M}$. En particular, **si $\operatorname{tr} M = 0$, $\det e^M = 1$**.

### 2.3. Potencias que se repiten: dos fórmulas cerradas

Cuando las potencias de una matriz se repiten, la serie se agrupa en funciones conocidas.

* **Si $A^3 = -A$**, las potencias impares son $\pm A$ y las pares, $\pm A^2$, y con las series del seno y del coseno,

  $$
  \begin{aligned}
  e^{\theta \cdot A} &= I + \left(\theta - \dfrac{\theta^3}{3!} + \dfrac{\theta^5}{5!} - \dots\right) \cdot A + \left(\dfrac{\theta^2}{2!} - \dfrac{\theta^4}{4!} + \dots\right) \cdot A^2 \\
  &= I + \sin\theta \cdot A + (1 - \cos\theta) \cdot A^2.
  \end{aligned}
  $$

* **Si $K^3 = K$**, todas las potencias impares son $K$ y todas las pares, $K^2$, y con las series del seno y del coseno hiperbólicos, $\sinh\zeta = \zeta + \dfrac{\zeta^3}{3!} + \dots$ y $\cosh\zeta = 1 + \dfrac{\zeta^2}{2!} + \dots$,

  $$
  \begin{aligned}
  e^{\zeta \cdot K} = I + \sinh\zeta \cdot K + (\cosh\zeta - 1) \cdot K^2.
  \end{aligned}
  $$

La primera da las rotaciones (apartado 2.4); la segunda, los cambios de velocidad de Lorentz (apartado 4.3).

**La fórmula de Rodrigues.** Toda matriz antisimétrica es $A = \omega_1 \cdot J_1 + \omega_2 \cdot J_2 + \omega_3 \cdot J_3$ y actúa como $A \cdot \vec{v} = \vec{\omega} \times \vec{v}$ (apartado 1.5). Si $\vec{\omega} \neq \vec{0}$, se escribe $\vec{\omega} = \theta \cdot \vec{n}$, con $\theta = |\vec{\omega}|$ y $\vec{n}$ unitario, y $A = \theta \cdot A_{\vec{n}}$, donde $A_{\vec{n}} \cdot \vec{v} = \vec{n} \times \vec{v}$. Las potencias de $A_{\vec{n}}$ se repiten:

* $A_{\vec{n}} \cdot \vec{n} = \vec{n} \times \vec{n} = \vec{0}$;
* $A_{\vec{n}}^2 \cdot \vec{v} = \vec{n} \times (\vec{n} \times \vec{v}) = \vec{n} \cdot (\vec{n} \cdot \vec{v}) - \vec{v}$, por la fórmula del doble producto vectorial y $\vec{n} \cdot \vec{n} = 1$; en matrices, $A_{\vec{n}}^2 = \vec{n} \cdot \vec{n}^{\mathsf{T}} - I$;
* $A_{\vec{n}}^3 = A_{\vec{n}} \cdot (\vec{n} \cdot \vec{n}^{\mathsf{T}} - I) = (A_{\vec{n}} \cdot \vec{n}) \cdot \vec{n}^{\mathsf{T}} - A_{\vec{n}} = -A_{\vec{n}}$.

Por la primera fórmula,

$$
\begin{aligned}
e^{\theta \cdot A_{\vec{n}}} = I + \sin\theta \cdot A_{\vec{n}} + (1 - \cos\theta) \cdot A_{\vec{n}}^2.
\end{aligned}
$$

Su significado geométrico:

* **El eje queda fijo:** como $A_{\vec{n}} \cdot \vec{n} = \vec{0}$, $e^{\theta \cdot A_{\vec{n}}} \cdot \vec{n} = \vec{n}$.
* **El plano perpendicular gira un ángulo $\theta$:** para $\vec{v}$ perpendicular a $\vec{n}$, $A_{\vec{n}}^2 \cdot \vec{v} = -\vec{v}$, y queda $e^{\theta \cdot A_{\vec{n}}} \cdot \vec{v} = \cos\theta \cdot \vec{v} + \sin\theta \cdot (\vec{n} \times \vec{v})$. Es el giro de ángulo $\theta$ en el plano de base $\vec{v}$ y $\vec{n} \times \vec{v}$.
* **Con $\vec{n} = \vec{e}_3$** ($A_{\vec{n}} = J_3$) se recupera $R_3(\theta)$ (apartado 1.6). Igualmente, $R_1(\theta) = e^{\theta \cdot J_1}$ y $R_2(\theta) = e^{\theta \cdot J_2}$.

$e^A$ es la rotación de ángulo $|\vec{\omega}|$ alrededor del eje $\vec{\omega}$. Los tres parámetros de la rotación son las tres componentes de $\vec{\omega}$.

### 2.4. La exponencial de una matriz antisimétrica es una rotación

Sea $A$ antisimétrica, $A^{\mathsf{T}} = -A$. Como $-A$ y $A$ conmutan, las propiedades del apartado 2.2 dan

$$
\begin{aligned}
(e^A)^{\mathsf{T}} \cdot e^A = e^{A^{\mathsf{T}}} \cdot e^A = e^{-A} \cdot e^A = e^{-A+A} = e^0 = I.
\end{aligned}
$$

Además, la diagonal de $A$ es nula, $\operatorname{tr} A = 0$ y $\det e^A = e^0 = 1$. Por tanto, $e^A$ es una rotación.

### 2.5. Recíproco: toda rotación es una exponencial

Sea $R$ una rotación. Primero se ve que tiene un eje, es decir, un vector $\vec{n}$ con $R \cdot \vec{n} = \vec{n}$ (teorema de Euler). Como $R - I = R \cdot (I - R^{\mathsf{T}}) = R \cdot (I - R)^{\mathsf{T}}$ y $\det R = 1$:

$$
\begin{aligned}
\det(R - I) &= \det R \cdot \det\left((I - R)^{\mathsf{T}}\right) = \det(I - R) \\
&= (-1)^3 \cdot \det(R - I) = -\det(R - I),
\end{aligned}
$$

donde se ha usado que cambiar el signo de una matriz $3 \times 3$ multiplica su determinante por $(-1)^3$. Por tanto, $\det(R - I) = 0$: el sistema $(R - I) \cdot \vec{n} = \vec{0}$ tiene solución no nula, que se toma unitaria.

$R$ conserva los productos escalares: $(R \cdot \vec{v}) \cdot (R \cdot \vec{w}) = \vec{v}^{\mathsf{T}} \cdot R^{\mathsf{T}} \cdot R \cdot \vec{w} = \vec{v} \cdot \vec{w}$. Así, si $\vec{v}$ es perpendicular a $\vec{n}$, $(R \cdot \vec{v}) \cdot \vec{n} = (R \cdot \vec{v}) \cdot (R \cdot \vec{n}) = \vec{v} \cdot \vec{n} = 0$: $R$ lleva el plano perpendicular a $\vec{n}$ a sí mismo. En ese plano conserva longitudes y ángulos, y su determinante es $1$ (el de $R$, porque sobre $\vec{n}$ actúa como la identidad). Una transformación del plano con esas propiedades es un giro de un ángulo $\theta$ (el razonamiento por columnas del apartado 1.4, en dos dimensiones). Según el apartado 2.3, $e^{\theta \cdot A_{\vec{n}}}$ hace exactamente lo mismo: deja fijo $\vec{n}$ y gira $\theta$ el plano perpendicular. Por tanto,

$$
\begin{aligned}
R = e^{\theta \cdot A_{\vec{n}}} = e^A, \qquad A = \theta \cdot A_{\vec{n}} \text{ antisimétrica}.
\end{aligned}
$$

Las rotaciones son exactamente las exponenciales de las matrices antisimétricas. La correspondencia no es única: $\theta$ y $\theta + 2 \cdot \pi$ dan la misma rotación, y también el ángulo $\theta$ alrededor de $\vec{n}$ y el ángulo $2 \cdot \pi - \theta$ alrededor de $-\vec{n}$.

### 2.6. Dos formas de dar una rotación con tres parámetros

* **Tres ángulos respecto de los ejes fijos** (apartado 1.3): $R = R_3(\theta_3) \cdot R_2(\theta_2) \cdot R_1(\theta_1) = e^{\theta_3 \cdot J_3} \cdot e^{\theta_2 \cdot J_2} \cdot e^{\theta_1 \cdot J_1}$.
* **Un vector eje-ángulo** $\vec{\omega}$: $R = e^{\omega_1 \cdot J_1 + \omega_2 \cdot J_2 + \omega_3 \cdot J_3}$.

No son lo mismo: en general, $e^{\theta_3 \cdot J_3} \cdot e^{\theta_2 \cdot J_2} \cdot e^{\theta_1 \cdot J_1} \neq e^{\theta_3 \cdot J_3 + \theta_2 \cdot J_2 + \theta_1 \cdot J_1}$, porque las matrices $J_k$ no conmutan. Se puede ver sin calcular ninguna exponencial. Si fuera $e^{M+N} = e^M \cdot e^N$ para $M = \dfrac{\pi}{2} \cdot J_1$ y $N = \dfrac{\pi}{2} \cdot J_2$, como $M + N = N + M$ se tendría $e^M \cdot e^N = e^{M+N} = e^N \cdot e^M$, es decir, $R_1(\pi/2) \cdot R_2(\pi/2) = R_2(\pi/2) \cdot R_1(\pi/2)$. Pero esos dos productos son distintos (apartado 1.2).

### 2.7. El producto de dos exponenciales y el conmutador

**Hasta segundo orden.** Para dos matrices cuadradas $M$ y $N$ cualesquiera y $s$ pequeño,

$$
\begin{aligned}
e^{s \cdot M} \cdot e^{s \cdot N} &= e^{s \cdot (M + N) + (s^2/2) \cdot [M, N] + O(s^3)}, \\
e^{s \cdot M} \cdot e^{s \cdot N} \cdot e^{-s \cdot M} \cdot e^{-s \cdot N} &= I + s^2 \cdot [M, N] + O(s^3).
\end{aligned}
$$

Para la primera, se desarrollan los dos lados hasta $s^2$. El izquierdo es $\left(I + s \cdot M + \dfrac{s^2}{2} \cdot M^2\right) \cdot \left(I + s \cdot N + \dfrac{s^2}{2} \cdot N^2\right) + O(s^3) = I + s \cdot (M + N) + s^2 \cdot \left(\dfrac{M^2}{2} + M \cdot N + \dfrac{N^2}{2}\right) + O(s^3)$. El derecho, con $C := s \cdot (M + N) + s^2 \cdot Z$, es $I + C + \dfrac{C^2}{2} + O(s^3) = I + s \cdot (M + N) + s^2 \cdot \left(Z + \dfrac{(M + N)^2}{2}\right) + O(s^3)$. Los coeficientes de $s^2$ coinciden si y solo si $Z = M \cdot N - \dfrac{M \cdot N + N \cdot M}{2} = \dfrac{1}{2} \cdot [M, N]$. La segunda igualdad se obtiene del mismo modo. (La serie completa del exponente es la fórmula de Baker–Campbell–Hausdorff; Hall, 2015, cap. 5.)

**Qué dicen.** Si $M$ y $N$ conmutan, se recupera $e^{s \cdot M} \cdot e^{s \cdot N} = e^{s \cdot (M + N)}$. Si no, recorrer dos flujos en un orden y después deshacerlos en el otro no devuelve al punto de partida: el defecto es, a segundo orden, la exponencial del conmutador. Es la versión con exponenciales de la observación del apartado 1.5. Por eso las relaciones de conmutación de los generadores de un grupo contienen, cerca de la identidad, su ley de composición.

**Álgebra de Lie.** Un **álgebra de Lie de matrices** es un espacio vectorial de matrices cerrado bajo el conmutador: si $M$ y $N$ están en él, también $[M, N]$. Para cada uno de los grupos de este documento, los generadores, es decir, las matrices $X$ con $e^{s \cdot X}$ en el grupo para todo $s$, forman un álgebra de Lie (Hall, 2015, cap. 3); en cada caso, la tabla de conmutadores de los generadores lo muestra directamente.

## 3. El grupo de Galileo

Las transformaciones de Galileo, escritas como matrices $5 \times 5$, forman un grupo, su producto dice cómo se componen los parámetros y sus generadores dan las diez cantidades conservadas de la parte física, apartado 8.

### 3.1. La matriz y su acción

Una transformación de Galileo queda dada por una rotación $R$, una velocidad $\vec{v}$, un desplazamiento espacial $\vec{a}$ y un desplazamiento temporal $b$:

$$
\begin{aligned}
\vec{q}^{\,\prime} &= R \cdot \vec{q} + \vec{v} \cdot t + \vec{a}, \\
t' &= t + b.
\end{aligned}
$$

Con los vectores escritos como columnas, se reúne en una sola matriz que actúa sobre la columna $(\vec{q}, t, 1)$:

$$
\begin{aligned}
\Gamma(R, \vec{v}, \vec{a}, b) =
\begin{pmatrix}
R & \vec{v} & \vec{a} \\
\vec{0}^{\mathsf{T}} & 1 & b \\
\vec{0}^{\mathsf{T}} & 0 & 1
\end{pmatrix},
\qquad
\begin{pmatrix}
\vec{q}^{\,\prime} \\
t' \\
1
\end{pmatrix}
= \Gamma(R, \vec{v}, \vec{a}, b) \cdot
\begin{pmatrix} \vec{q}
\\ t
\\ 1
\end{pmatrix}.
\end{aligned}
$$

$\vec{0}^{\mathsf{T}} = (0, 0, 0)$ es una fila de tres ceros. La matriz es $5 \times 5$: el bloque $R$ ocupa las tres primeras filas y columnas, $\vec{v}$ y $\vec{a}$ son la cuarta y la quinta columna de esas filas, y las dos últimas filas son $(0, 0, 0, 1, b)$ y $(0, 0, 0, 0, 1)$. El $1$ final de la columna $(\vec{q}, t, 1)$ es el que permite escribir los desplazamientos $\vec{a}$ y $b$ como un producto de matrices. Las transformaciones son activas, como en la parte física (apartado 2).

### 3.2. La composición: cómo se combinan los parámetros

Aplicar primero $\Gamma_1 = \Gamma(R_1, \vec{v}_1, \vec{a}_1, b_1)$ y después $\Gamma_2 = \Gamma(R_2, \vec{v}_2, \vec{a}_2, b_2)$ es multiplicar $\Gamma_2 \cdot \Gamma_1$. El producto se calcula por bloques, igual que el de matrices ordinarias, porque los tamaños de los bloques encajan:

$$
\begin{aligned}
\Gamma_2 \cdot \Gamma_1
&= \begin{pmatrix} R_2 & \vec{v}_2 & \vec{a}_2 \\ \vec{0}^{\mathsf{T}} & 1 & b_2 \\ \vec{0}^{\mathsf{T}} & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} R_1 & \vec{v}_1 & \vec{a}_1 \\ \vec{0}^{\mathsf{T}} & 1 & b_1 \\ \vec{0}^{\mathsf{T}} & 0 & 1 \end{pmatrix} \\
&= \begin{pmatrix} R_2 \cdot R_1 & R_2 \cdot \vec{v}_1 + \vec{v}_2 & R_2 \cdot \vec{a}_1 + \vec{v}_2 \cdot b_1 + \vec{a}_2 \\ \vec{0}^{\mathsf{T}} & 1 & b_1 + b_2 \\ \vec{0}^{\mathsf{T}} & 0 & 1 \end{pmatrix}.
\end{aligned}
$$

Por ejemplo, la entrada de arriba a la derecha es la fila de bloques $(R_2,\ \vec{v}_2,\ \vec{a}_2)$ por la columna de bloques $(\vec{a}_1,\ b_1,\ 1)$. El resultado tiene otra vez la forma de una matriz de Galileo, con los parámetros

$$
\begin{aligned}
R &= R_2 \cdot R_1, \qquad \vec{v} = R_2 \cdot \vec{v}_1 + \vec{v}_2, \\
\vec{a} &= R_2 \cdot \vec{a}_1 + \vec{v}_2 \cdot b_1 + \vec{a}_2, \qquad b = b_1 + b_2.
\end{aligned}
$$

Comprobación aplicando las transformaciones una tras otra. La primera da $\vec{q}^{\,\prime} = R_1 \cdot \vec{q} + \vec{v}_1 \cdot t + \vec{a}_1$ y $t' = t + b_1$. La segunda, aplicada a ese resultado:

$$
\begin{aligned}
\vec{q}^{\,\prime\prime} &= R_2 \cdot \vec{q}^{\,\prime} + \vec{v}_2 \cdot t' + \vec{a}_2 \\
&= R_2 \cdot (R_1 \cdot \vec{q} + \vec{v}_1 \cdot t + \vec{a}_1) + \vec{v}_2 \cdot (t + b_1) + \vec{a}_2 \\
&= (R_2 \cdot R_1) \cdot \vec{q} + (R_2 \cdot \vec{v}_1 + \vec{v}_2) \cdot t + (R_2 \cdot \vec{a}_1 + \vec{v}_2 \cdot b_1 + \vec{a}_2), \\
t'' &= t' + b_2 = t + (b_1 + b_2).
\end{aligned}
$$

Significado de cada parámetro:

* **Desplazamientos temporales: se suman**, $b = b_1 + b_2$.
* **Rotaciones: se multiplican**, $R = R_2 \cdot R_1$. Los ángulos solo se suman cuando las dos rotaciones son alrededor del mismo eje (apartado 1.6).
* **Velocidades: se suman después de girar la primera**, $\vec{v} = R_2 \cdot \vec{v}_1 + \vec{v}_2$. Es la ley de adición de velocidades de Galileo. $R_2$ aparece porque la segunda transformación también gira la velocidad que dejó la primera. Sin rotaciones, $\vec{v} = \vec{v}_1 + \vec{v}_2$.
* **Desplazamientos espaciales: se suman, girando el primero, más un término cruzado**, $\vec{a} = R_2 \cdot \vec{a}_1 + \vec{v}_2 \cdot b_1 + \vec{a}_2$. El término $\vec{v}_2 \cdot b_1$ aparece porque el cambio de velocidad $\vec{v}_2$ actúa sobre el tiempo ya desplazado $t + b_1$.

### 3.3. Las cuatro propiedades de grupo

* **Composición.** El producto de dos matrices de Galileo es una matriz de Galileo: tiene la misma forma por bloques, y $R_2 \cdot R_1$ es una rotación por ser producto de rotaciones (apartado 1.7).
* **Identidad.** $\Gamma(I, \vec{0}, \vec{0}, 0)$ es la matriz identidad $5 \times 5$.
* **Inversa.** Se obtiene despejando $\vec{q}$ y $t$. De $t' = t + b$ sale $t = t' - b$. De $\vec{q}^{\,\prime} = R \cdot \vec{q} + \vec{v} \cdot t + \vec{a}$, multiplicando por $R^{\mathsf{T}} = R^{-1}$ y sustituyendo $t$:

  $$
  \begin{aligned}
  \vec{q} &= R^{\mathsf{T}} \cdot (\vec{q}^{\,\prime} - \vec{v} \cdot t - \vec{a}) = R^{\mathsf{T}} \cdot \left(\vec{q}^{\,\prime} - \vec{v} \cdot (t' - b) - \vec{a}\right) \\
  &= R^{\mathsf{T}} \cdot \vec{q}^{\,\prime} - R^{\mathsf{T}} \cdot \vec{v} \cdot t' - R^{\mathsf{T}} \cdot (\vec{a} - \vec{v} \cdot b).
  \end{aligned}
  $$

  Es otra transformación de Galileo:

  $$
  \begin{aligned}
  \Gamma(R, \vec{v}, \vec{a}, b)^{-1} = \Gamma\left(R^{\mathsf{T}},\ -R^{\mathsf{T}} \cdot \vec{v},\ -R^{\mathsf{T}} \cdot (\vec{a} - \vec{v} \cdot b),\ -b\right).
  \end{aligned}
  $$

  Con la ley de composición del apartado 3.2 se comprueba que el producto en cualquiera de los dos órdenes da la identidad.
* **Asociatividad.** Se hereda del producto de matrices.

Las transformaciones de Galileo forman un grupo de $3 + 3 + 3 + 1 = 10$ parámetros: 3 de la rotación, 3 de la velocidad, 3 del desplazamiento espacial y 1 del temporal.

### 3.4. El grupo no es conmutativo

Dos ejemplos en los que el orden cambia el resultado, obtenidos con la ley del apartado 3.2:

* **Desplazamiento temporal $b$ y cambio de velocidad $\vec{u}$.** Si primero se desplaza el tiempo y después se cambia la velocidad, $\vec{a} = \vec{u} \cdot b$. En el orden inverso, $\vec{a} = \vec{0}$. La diferencia es el término cruzado de la ley de composición.
* **Rotación $R$ y desplazamiento espacial $\vec{a}$.** Si primero se desplaza y después se gira, el desplazamiento resultante es $R \cdot \vec{a}$: también gira. En el orden inverso, es $\vec{a}$.

### 3.5. Familias de un parámetro y flujos

Si se fija una dirección $\vec{e}$ (un vector unitario) y se deja libre un solo parámetro $s$, la ley de composición se reduce a una suma:

* traslaciones espaciales en la dirección $\vec{e}$: $\Gamma(I, \vec{0}, s \cdot \vec{e}, 0)$;
* cambios de velocidad en la dirección $\vec{e}$: $\Gamma(I, s \cdot \vec{e}, \vec{0}, 0)$;
* traslaciones temporales: $\Gamma(I, \vec{0}, \vec{0}, s)$;
* rotaciones alrededor de un eje fijo: $\Gamma(e^{s \cdot A_{\vec{e}}}, \vec{0}, \vec{0}, 0)$, porque los ángulos alrededor del mismo eje se suman.

En los cuatro casos, $\Phi_s$ cumple $\Phi_0 = I$ y $\Phi_{s_2} \circ \Phi_{s_1} = \Phi_{s_1 + s_2}$: es un flujo (parte matemática, apartado 9.1). Cada una es $e^{s \cdot M}$ para una matriz $5 \times 5$ fija $M$:

* **rotación alrededor de $\vec{e}$:** $M$ tiene $A_{\vec{e}}$ en el bloque $3 \times 3$ y ceros en el resto, y $e^{s \cdot M}$ tiene $e^{s \cdot A_{\vec{e}}}$ en ese bloque;
* **cambio de velocidad, traslación espacial y traslación temporal** en la dirección del eje $q_1$: $M$ es $E_{14}$, $E_{15}$ o $E_{45}$. En los tres casos $M^2 = 0$, porque $E_{ij} \cdot E_{kl} = E_{il}$ si $j = k$ y es nula si $j \neq k$, y aquí $j \neq i$. La serie se corta en el segundo término: $e^{s \cdot M} = I + s \cdot M$, que es exactamente $\Gamma(I, s \cdot \vec{e}_1, \vec{0}, 0)$, $\Gamma(I, \vec{0}, s \cdot \vec{e}_1, 0)$ o $\Gamma(I, \vec{0}, \vec{0}, s)$.

Por el apartado 2.2, cada familia es el flujo de un campo vectorial lineal, y $M$ es su generador.

### 3.6. Los diez generadores y sus conmutadores

Cada familia de un parámetro tiene como generador la derivada de la familia en $s = 0$:

| Familia de un parámetro | Generador | Matriz |
| ------------------------------------ | ---------------- | ---------------------------------------------- |
| Rotación alrededor de $q_1$, $q_2$, $q_3$ | $\mathcal{J}_1$, $\mathcal{J}_2$, $\mathcal{J}_3$ | $J_1$, $J_2$, $J_3$ en el bloque $3 \times 3$; ceros en el resto |
| Cambio de velocidad en $q_1$, $q_2$, $q_3$ | $\mathcal{K}_1$, $\mathcal{K}_2$, $\mathcal{K}_3$ | $E_{14}$, $E_{24}$, $E_{34}$ |
| Traslación espacial en $q_1$, $q_2$, $q_3$ | $\mathcal{P}_1$, $\mathcal{P}_2$, $\mathcal{P}_3$ | $E_{15}$, $E_{25}$, $E_{35}$ |
| Traslación temporal | $\mathcal{T}$ | $E_{45}$ |

Table: Los diez generadores del grupo de Galileo.

Para la traslación temporal se usa $\mathcal{T}$ y no $\mathcal{H}$, para no confundirla con el hamiltoniano. Con la notación $\vec{u} \cdot \vec{\mathcal{K}} = u_1 \cdot \mathcal{K}_1 + u_2 \cdot \mathcal{K}_2 + u_3 \cdot \mathcal{K}_3$, y lo mismo para $\vec{\mathcal{J}}$ y $\vec{\mathcal{P}}$, un generador general es una combinación de los diez, con diez coeficientes $\vec{\omega}$, $\vec{u}$, $\vec{d}$ y $\tau$:

$$
\begin{aligned}
X = \vec{\omega} \cdot \vec{\mathcal{J}} + \vec{u} \cdot \vec{\mathcal{K}} + \vec{d} \cdot \vec{\mathcal{P}} + \tau \cdot \mathcal{T}
= \begin{pmatrix} A & \vec{u} & \vec{d} \\ \vec{0}^{\mathsf{T}} & 0 & \tau \\ \vec{0}^{\mathsf{T}} & 0 & 0 \end{pmatrix},
\end{aligned}
$$

donde $A$ es la matriz antisimétrica $3 \times 3$ con $A \cdot \vec{y} = \vec{\omega} \times \vec{y}$. Se usa $\vec{d}$ y no $\vec{a}$ porque $\vec{a}$ es el desplazamiento de la transformación finita.

**Conmutadores.** Con la regla de los productos de las matrices $E_{ij}$, y para $(i, j, k)$ igual a $(1, 2, 3)$, $(2, 3, 1)$ o $(3, 1, 2)$:

$$
\begin{aligned}
{[\mathcal{J}_i, \mathcal{J}_j]} &= \mathcal{J}_k, \qquad [\mathcal{J}_i, \mathcal{K}_j] = \mathcal{K}_k, \qquad [\mathcal{J}_i, \mathcal{P}_j] = \mathcal{P}_k, \qquad [\mathcal{K}_i, \mathcal{T}] = \mathcal{P}_i,
\end{aligned}
$$

y son nulos $[\mathcal{J}_i, \mathcal{K}_i]$, $[\mathcal{J}_i, \mathcal{P}_i]$, $[\mathcal{J}_i, \mathcal{T}]$, $[\mathcal{K}_i, \mathcal{K}_j]$, $[\mathcal{K}_i, \mathcal{P}_j]$, $[\mathcal{P}_i, \mathcal{P}_j]$ y $[\mathcal{P}_i, \mathcal{T}]$, para todos los índices.

* **Los de las rotaciones entre sí** son los del apartado 1.5, en el bloque $3 \times 3$.
* **Los de una rotación con un cambio de velocidad o una traslación.** $\mathcal{J}_i \cdot E_{j4} = \sum_l (J_i)_{lj} \cdot E_{l4}$, porque $J_i$ solo ocupa las tres primeras filas y columnas, y $E_{j4} \cdot \mathcal{J}_i = 0$, porque la cuarta fila de $\mathcal{J}_i$ es nula. Los números $(J_i)_{lj}$ son las componentes de $J_i \cdot \vec{e}_j = \vec{e}_i \times \vec{e}_j$, que vale $\vec{e}_k$ para $(i, j, k)$ cíclico y $\vec{0}$ si $i = j$. Por tanto, $[\mathcal{J}_i, \mathcal{K}_j] = \mathcal{K}_k$, y lo mismo con $E_{j5}$.
* **Entre los siete que no son rotaciones**, $E_{i4} \cdot E_{j4} = 0$ porque $4 \neq j$, y del mismo modo se anulan los demás productos, salvo uno: $\mathcal{K}_i \cdot \mathcal{T} = E_{i4} \cdot E_{45} = E_{i5} = \mathcal{P}_i$, mientras que $\mathcal{T} \cdot \mathcal{K}_i = 0$. El único par que no conmuta es un cambio de velocidad con la traslación temporal: es el origen del término cruzado $\vec{v}_2 \cdot b_1$ de la ley de composición.

Los conmutadores de dos generadores son generadores: los diez forman un álgebra de Lie (apartado 2.7), el **álgebra de Galileo**.

### 3.7. Forma de producto

Como $(\vec{a} \cdot \vec{\mathcal{P}} + b \cdot \mathcal{T})^2 = 0$ y $(\vec{v} \cdot \vec{\mathcal{K}})^2 = 0$ (apartado 3.6), sus exponenciales se reducen a los dos primeros términos de la serie:

$$
\begin{aligned}
e^{\vec{a} \cdot \vec{\mathcal{P}} + b \cdot \mathcal{T}} = \Gamma(I, \vec{0}, \vec{a}, b), \qquad e^{\vec{v} \cdot \vec{\mathcal{K}}} = \Gamma(I, \vec{v}, \vec{0}, 0),
\end{aligned}
$$

y la rotación es $e^{\vec{\omega} \cdot \vec{\mathcal{J}}} = \Gamma(e^A, \vec{0}, \vec{0}, 0)$, con $e^A = R$ (apartados 2.3 y 2.5). Con la ley de composición del apartado 3.2, empezando por la derecha, $\Gamma(I, \vec{v}, \vec{0}, 0) \cdot \Gamma(R, \vec{0}, \vec{0}, 0) = \Gamma(R, \vec{v}, \vec{0}, 0)$ y $\Gamma(I, \vec{0}, \vec{a}, b) \cdot \Gamma(R, \vec{v}, \vec{0}, 0) = \Gamma(R, \vec{v}, \vec{a}, b)$, porque el término cruzado $\vec{v}_2 \cdot b_1$ es nulo cuando la transformación de la derecha no desplaza el tiempo. Por tanto, toda transformación de Galileo es

$$
\begin{aligned}
\Gamma(R, \vec{v}, \vec{a}, b) = e^{\vec{a} \cdot \vec{\mathcal{P}} + b \cdot \mathcal{T}} \cdot e^{\vec{v} \cdot \vec{\mathcal{K}}} \cdot e^{\vec{\omega} \cdot \vec{\mathcal{J}}}.
\end{aligned}
$$

Cada factor es una familia de un parámetro (el primero, de cuatro parámetros que conmutan entre sí). La versión 1 usaba el orden $e^{(\vec{a} - \vec{v} \cdot b) \cdot \vec{\mathcal{P}}} \cdot e^{\vec{v} \cdot \vec{\mathcal{K}}} \cdot e^{b \cdot \mathcal{T}} \cdot e^{\vec{\omega} \cdot \vec{\mathcal{J}}}$, en el que la traslación temporal va a la derecha del cambio de velocidad y hay que compensar el término cruzado con $-\vec{v} \cdot b$.

### 3.8. Una sola exponencial

**Potencias del generador.** Multiplicando por bloques:

$$
\begin{aligned}
X^2 =
\begin{pmatrix} A^2 & A \cdot \vec{u} & A \cdot \vec{d} + \tau \cdot \vec{u} \\
\vec{0}^{\mathsf{T}} & 0 & 0 \\
\vec{0}^{\mathsf{T}} & 0 & 0 \end{pmatrix}.
\end{aligned}
$$

Las dos últimas filas se anulan a partir de $X^2$. Multiplicando otra vez por $X$ por la izquierda, cada potencia añade un factor $A$ en la primera fila de bloques. Por inducción, para $k \geq 2$:

$$
\begin{aligned}
X^k = \begin{pmatrix} A^k & A^{k-1} \cdot \vec{u} & A^{k-1} \cdot \vec{d} + \tau \cdot A^{k-2} \cdot \vec{u} \\ \vec{0}^{\mathsf{T}} & 0 & 0 \\ \vec{0}^{\mathsf{T}} & 0 & 0 \end{pmatrix}.
\end{aligned}
$$

**La exponencial.** Sumando la serie $\sum_k \dfrac{X^k}{k!}$ bloque a bloque:

$$
\begin{aligned}
e^{X} &= \Gamma\left(e^A,\ V \cdot \vec{u},\ V \cdot \vec{d} + \tau \cdot W \cdot \vec{u},\ \tau\right), \\
V &= \sum_{j=0}^{\infty} \dfrac{A^j}{(j+1)!},
\qquad
W = \sum_{j=0}^{\infty} \dfrac{A^j}{(j+2)!}.
\end{aligned}
$$

Por ejemplo, la columna de la velocidad es $\sum_{k \geq 1} \dfrac{A^{k-1} \cdot \vec{u}}{k!}$, que con $j = k - 1$ es $V \cdot \vec{u}$. Derivando las series término a término, $\dfrac{d}{ds}\big(s \cdot V(s \cdot A)\big) = e^{s \cdot A}$ y $\dfrac{d}{ds}\big(s^2 \cdot W(s \cdot A)\big) = s \cdot V(s \cdot A)$, donde $V(s \cdot A)$ es la serie $V$ con $s \cdot A$ en lugar de $A$.

**Sin rotación** ($A = 0$): $V = I$ y $W = \dfrac{1}{2} \cdot I$, y queda

$$
\begin{aligned}
e^{\vec{u} \cdot \vec{\mathcal{K}} + \vec{d} \cdot \vec{\mathcal{P}} + \tau \cdot \mathcal{T}} = \Gamma\left(I,\ \vec{u},\ \vec{d} + \dfrac{\tau}{2} \cdot \vec{u},\ \tau\right).
\end{aligned}
$$

Los coeficientes del exponente no coinciden con los parámetros de la transformación: aparece $\dfrac{\tau}{2} \cdot \vec{u}$. La razón es que la exponencial aplica a la vez el cambio de velocidad y la traslación temporal, cada uno creciendo desde $0$ con el parámetro $s$ del flujo (apartado 3.9). El punto con $t = 0$ se mueve según $\dfrac{d\vec{q}}{ds} = \vec{u} \cdot t(s) + \vec{d}$, con $t(s) = \tau \cdot s$, y entre $s = 0$ y $s = 1$ recorre $\int_0^1 (\vec{u} \cdot \tau \cdot s + \vec{d}) \,ds = \dfrac{\tau}{2} \cdot \vec{u} + \vec{d}$: el tiempo desplazado vale, en promedio, $\dfrac{\tau}{2}$.

**Con rotación** ($A = \theta \cdot A_{\vec{n}}$, con $\theta = |\vec{\omega}|$). Como $A_{\vec{n}}^3 = -A_{\vec{n}}$, las series se agrupan como en la fórmula de Rodrigues:

$$
\begin{aligned}
V &= I + \dfrac{1 - \cos\theta}{\theta} \cdot A_{\vec{n}} + \dfrac{\theta - \sin\theta}{\theta} \cdot A_{\vec{n}}^2, \\
W &= \dfrac{1}{2} \cdot I + \dfrac{\theta - \sin\theta}{\theta^2} \cdot A_{\vec{n}} + \dfrac{\theta^2/2 - 1 + \cos\theta}{\theta^2} \cdot A_{\vec{n}}^2.
\end{aligned}
$$

Por ejemplo, en $V$ las potencias impares dan $\sum_{l \geq 0} \dfrac{(-1)^l \cdot \theta^{2 \cdot l + 1}}{(2 \cdot l + 2)!} \cdot A_{\vec{n}} = \dfrac{1 - \cos\theta}{\theta} \cdot A_{\vec{n}}$, porque $\sum_{l \geq 0} \dfrac{(-1)^l \cdot \theta^{2 \cdot l + 2}}{(2 \cdot l + 2)!} = 1 - \cos\theta$.

**Toda transformación de Galileo es una sola exponencial.** Dada $\Gamma(R, \vec{v}, \vec{a}, b)$, se elige $A$ con $e^A = R$ y ángulo $\theta \in [0, \pi]$ (siempre es posible; apartado 2.5), $\tau = b$, y se despejan $\vec{u}$ y $\vec{d}$ de

$$
\begin{aligned}
V \cdot \vec{u} = \vec{v},
\qquad
V \cdot \vec{d} + b \cdot W \cdot \vec{u} = \vec{a}.
\end{aligned}
$$

Hace falta que $V$ sea invertible. Sobre el eje, $A_{\vec{n}} \cdot \vec{n} = \vec{0}$ y $V \cdot \vec{n} = \vec{n}$. En el plano perpendicular, $A_{\vec{n}}$ actúa como multiplicar por $i$ y $A_{\vec{n}}^2$ como multiplicar por $-1$ (apartado 1.6), así que $V$ actúa como el número complejo

$$
\begin{aligned}
\dfrac{\sin\theta}{\theta} + i \cdot \dfrac{1 - \cos\theta}{\theta} = \dfrac{e^{i \cdot \theta} - 1}{i \cdot \theta},
\qquad
\left|\dfrac{e^{i \cdot \theta} - 1}{i \cdot \theta}\right|^2 = \dfrac{2 \cdot (1 - \cos\theta)}{\theta^2}.
\end{aligned}
$$

Por tanto, $\det V = \dfrac{2 \cdot (1 - \cos\theta)}{\theta^2}$, que no se anula para $0 < \theta \leq \pi$. Con $\theta = 0$, $V = I$. En ambos casos $V$ es invertible, y $\vec{u} = V^{-1} \cdot \vec{v}$, $\vec{d} = V^{-1} \cdot (\vec{a} - b \cdot W \cdot \vec{u})$.

### 3.9. El campo vectorial de cada generador y su cantidad conservada

Por el apartado 2.2, $\dfrac{d}{ds} e^{s \cdot X} = X \cdot e^{s \cdot X}$: la familia $e^{s \cdot X}$ es el flujo del campo lineal que $X$ define sobre la columna $(\vec{q}, t, 1)$. Multiplicando:

$$
\begin{aligned}
\dfrac{d\vec{q}}{ds} = \vec{\omega} \times \vec{q} + \vec{u} \cdot t + \vec{d}, \qquad
\dfrac{dt}{ds} = \tau.
\end{aligned}
$$

Es el generador de la parte física, apartado 8, con las diez direcciones a la vez y $\vec{d}$ en lugar de $\vec{a}$: $\vec{\xi}_i = \vec{\omega} \times \vec{q}_i + \vec{u} \cdot t + \vec{d}$ para cada partícula y el desplazamiento del tiempo $\tau$. Para $N$ partículas sin campo exterior, la cantidad conservada, $Q = \sum_i \vec{p}_i \cdot \vec{\xi}_i - \tau \cdot \bsH - F$, con $F = \sum_i m_i \cdot \vec{u} \cdot \vec{q}_i$ por el cambio de velocidad, es lineal en los diez coeficientes:

$$
\begin{aligned}
Q = \vec{\omega} \cdot \vec{J} - \vec{u} \cdot \vec{G} + \vec{d} \cdot \vec{P} - \tau \cdot \bsH.
\end{aligned}
$$

Término a término:

* $\sum_i \vec{p}_i \cdot (\vec{\omega} \times \vec{q}_i) = \vec{\omega} \cdot \sum_i \vec{q}_i \times \vec{p}_i = \vec{\omega} \cdot \vec{J}$, por la propiedad cíclica del producto mixto;
* $\sum_i \vec{p}_i \cdot (\vec{u} \cdot t) - \sum_i m_i \cdot \vec{u} \cdot \vec{q}_i = -\vec{u} \cdot \left(\sum_i m_i \cdot \vec{q}_i - \vec{P} \cdot t\right) = -\vec{u} \cdot \vec{G}$;
* $\sum_i \vec{p}_i \cdot \vec{d} = \vec{d} \cdot \vec{P}$.

Aquí $\vec{G} = M \cdot \vec{X} - \vec{P} \cdot t$ es la cantidad del cambio de velocidad de la parte física. Como $Q$ se conserva para cualquier elección de los diez coeficientes, se conserva cada una de las diez cantidades por separado.

| Generador | Familia $e^{s \cdot (\dots)}$ | Campo $(\tau,\ \vec{\xi})$ | Cantidad conservada |
| ---------------------- | ------------------------------------ | ---------------------------- | ---------------------------- |
| $\vec{n} \cdot \vec{\mathcal{J}}$ | $\Gamma(e^{s \cdot A_{\vec{n}}}, \vec{0}, \vec{0}, 0)$ | $(0,\ \vec{n} \times \vec{q})$ | $\vec{n} \cdot \vec{J}$ |
| $\vec{e} \cdot \vec{\mathcal{K}}$ | $\Gamma(I, s \cdot \vec{e}, \vec{0}, 0)$ | $(0,\ \vec{e} \cdot t)$ | $-\vec{e} \cdot \vec{G}$ |
| $\vec{e} \cdot \vec{\mathcal{P}}$ | $\Gamma(I, \vec{0}, s \cdot \vec{e}, 0)$ | $(0,\ \vec{e})$ | $\vec{e} \cdot \vec{P}$ |
| $\mathcal{T}$ | $\Gamma(I, \vec{0}, \vec{0}, s)$ | $(1,\ \vec{0})$ | $-\bsH$ |

Table: Los generadores de Galileo, sus campos y sus cantidades conservadas.

## 4. El grupo de Lorentz en forma de matrices

El grupo de Lorentz de la parte física, apartado 9.1, escrito como un grupo de matrices $4 \times 4$, con la misma estructura que las rotaciones del apartado 1: una condición del tipo $R^{\mathsf{T}} \cdot R = I$, generadores que la cumplen a primer orden y exponenciales que dan los elementos del grupo.

### 4.1. Coordenadas y métrica

Un suceso se escribe como la columna $x = (x_0, x_1, x_2, x_3) := (c \cdot t, q_1, q_2, q_3)$, con $c$ la velocidad de la luz. Las cuatro componentes tienen unidades de longitud, y las matrices que actúan sobre ellas son adimensionales. Las filas y columnas se numeran de $0$ a $3$. La **métrica de Minkowski**, con la signatura $(+, -, -, -)$, es

$$
\begin{aligned}
\eta := \mathrm{diag}(1, -1, -1, -1), \qquad x^{\mathsf{T}} \cdot \eta \cdot x = c^2 \cdot t^2 - |\vec{q}|^2:
\end{aligned}
$$

el intervalo de la parte física, apartado 9.1. Además, $\eta^{\mathsf{T}} = \eta$ y $\eta^2 = I$.

### 4.2. Definición y propiedades de grupo

**Definición.** Una matriz real $4 \times 4$ $\Lambda$ es una **transformación de Lorentz** si conserva el intervalo de todo suceso: $(\Lambda \cdot x)^{\mathsf{T}} \cdot \eta \cdot (\Lambda \cdot x) = x^{\mathsf{T}} \cdot \eta \cdot x$ para todo $x$. Como dos matrices simétricas que dan la misma forma cuadrática son iguales (se recupera cada entrada evaluando en $x = e_\mu$ y $x = e_\mu + e_\nu$, con $e_\mu$ los vectores de la base), la condición es

$$
\begin{aligned}
\Lambda^{\mathsf{T}} \cdot \eta \cdot \Lambda = \eta.
\end{aligned}
$$

Es el análogo de $R^{\mathsf{T}} \cdot R = I$, con $\eta$ en lugar de $I$.

**Consecuencias.**

* **Inversa:** $\Lambda^{-1} = \eta \cdot \Lambda^{\mathsf{T}} \cdot \eta$, porque $(\eta \cdot \Lambda^{\mathsf{T}} \cdot \eta) \cdot \Lambda = \eta \cdot \eta = I$. Multiplicando $\Lambda \cdot \Lambda^{-1} = I$ por $\eta$ por la derecha se obtiene también $\Lambda \cdot \eta \cdot \Lambda^{\mathsf{T}} = \eta$.
* **Determinante:** $\det(\Lambda^{\mathsf{T}}) \cdot \det \eta \cdot \det \Lambda = \det \eta$, así que $(\det \Lambda)^2 = 1$ y $\det \Lambda = \pm 1$.
* **El elemento $(0, 0)$:** el elemento $(0, 0)$ de $\Lambda^{\mathsf{T}} \cdot \eta \cdot \Lambda = \eta$ es $\Lambda_{00}^2 - \sum_{k=1}^{3} \Lambda_{k0}^2 = 1$, así que $\Lambda_{00}^2 \geq 1$: o $\Lambda_{00} \geq 1$, o $\Lambda_{00} \leq -1$. Del mismo modo, con $\Lambda \cdot \eta \cdot \Lambda^{\mathsf{T}} = \eta$, $\sum_{k=1}^{3} \Lambda_{0k}^2 = \Lambda_{00}^2 - 1$.

**El grupo de Lorentz propio y ortócrono.** Las transformaciones con $\det \Lambda = 1$ (**propias**: no invierten la orientación del espacio) y $\Lambda_{00} \geq 1$ (**ortócronas**: no invierten el sentido del tiempo) forman un grupo, que se escribe $SO^+(1, 3)$ y es el que la parte física llama grupo de Lorentz:

* **Composición.** $(\Lambda_2 \cdot \Lambda_1)^{\mathsf{T}} \cdot \eta \cdot (\Lambda_2 \cdot \Lambda_1) = \Lambda_1^{\mathsf{T}} \cdot (\Lambda_2^{\mathsf{T}} \cdot \eta \cdot \Lambda_2) \cdot \Lambda_1 = \Lambda_1^{\mathsf{T}} \cdot \eta \cdot \Lambda_1 = \eta$, y el determinante del producto es $1$. Queda ver que el elemento $(0, 0)$ sigue siendo positivo. Con $\lambda_2 := (\Lambda_2)_{00} \geq 1$ y $\lambda_1 := (\Lambda_1)_{00} \geq 1$,
  $$
  \begin{aligned}
  (\Lambda_2 \cdot \Lambda_1)_{00} &= \lambda_2 \cdot \lambda_1 + \sum_{k=1}^{3} (\Lambda_2)_{0k} \cdot (\Lambda_1)_{k0} \\
  &\geq \lambda_2 \cdot \lambda_1 - \sqrt{\lambda_2^2 - 1} \cdot \sqrt{\lambda_1^2 - 1} > 0,
  \end{aligned}
  $$
  por la desigualdad de Cauchy–Schwarz y las dos sumas del punto anterior; la última desigualdad se debe a que $(\lambda_2 \cdot \lambda_1)^2 - (\lambda_2^2 - 1) \cdot (\lambda_1^2 - 1) = \lambda_2^2 + \lambda_1^2 - 1 > 0$. Como su cuadrado es al menos $1$, $(\Lambda_2 \cdot \Lambda_1)_{00} \geq 1$.
* **Identidad:** $I^{\mathsf{T}} \cdot \eta \cdot I = \eta$, con $\det I = 1$ e $I_{00} = 1$.
* **Inversa:** $\Lambda^{-1} = \eta \cdot \Lambda^{\mathsf{T}} \cdot \eta$ cumple la condición, tiene determinante $1$ y su elemento $(0, 0)$ es $\Lambda_{00}$.
* **Asociatividad:** la del producto de matrices.

Quedan fuera la reflexión del espacio, $\mathrm{diag}(1, -1, -1, -1)$, con determinante $-1$, y la inversión del tiempo, $\mathrm{diag}(-1, 1, 1, 1)$, con $\Lambda_{00} = -1$: como en el apartado 1.4, no se alcanzan desde la identidad de forma continua, porque $\det \Lambda$ y el signo de $\Lambda_{00}$ no pueden cambiar de forma continua.

### 4.3. Giros y cambios de velocidad

**Giros.** Si $R$ es una rotación, $\mathrm{diag}(1, R)$, la matriz con $1$ en el elemento $(0, 0)$ y $R$ en el bloque espacial, es de $SO^+(1, 3)$: no cambia $c \cdot t$ y conserva $|\vec{q}|$.

**Cambio de velocidad en la dirección de $q_1$.** Con las fórmulas de la parte física, apartado 9.1, y $v$ cambiada de signo (la forma activa, como en el resto de la serie), $t' = \gamma \cdot \left(t + \dfrac{v \cdot q_1}{c^2}\right)$ y $q_1' = \gamma \cdot (q_1 + v \cdot t)$. En las coordenadas $(c \cdot t, q_1)$, con $\beta := \dfrac{v}{c}$ y $\gamma = \dfrac{1}{\sqrt{1 - \beta^2}}$,

$$
\begin{aligned}
\begin{pmatrix} c \cdot t' \\ q_1' \end{pmatrix} = \begin{pmatrix} \gamma & \gamma \cdot \beta \\ \gamma \cdot \beta & \gamma \end{pmatrix} \cdot \begin{pmatrix} c \cdot t \\ q_1 \end{pmatrix},
\end{aligned}
$$

con $q_2$ y $q_3$ sin cambiar. Como $\gamma^2 - (\gamma \cdot \beta)^2 = \gamma^2 \cdot (1 - \beta^2) = 1$ y $\gamma \geq 1$, hay un único número real $\zeta$, la **rapidez**, con $\cosh\zeta = \gamma$ y $\sinh\zeta = \gamma \cdot \beta$; es decir, $\tanh\zeta = \beta$. La matriz completa es

$$
\begin{aligned}
B_1(\zeta) = \begin{pmatrix} \cosh\zeta & \sinh\zeta & 0 & 0 \\ \sinh\zeta & \cosh\zeta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} = e^{\zeta \cdot \mathcal{K}_1}, \qquad \mathcal{K}_1 := E_{01} + E_{10}.
\end{aligned}
$$

La segunda igualdad es la fórmula de las potencias que se repiten con signo positivo (apartado 2.3): $\mathcal{K}_1^2 = E_{00} + E_{11}$ y $\mathcal{K}_1^3 = \mathcal{K}_1$, y $I + \sinh\zeta \cdot \mathcal{K}_1 + (\cosh\zeta - 1) \cdot \mathcal{K}_1^2$ es la matriz de la izquierda. Es el análogo hiperbólico de $R_3(\theta) = e^{\theta \cdot J_3}$: la rapidez hace el papel del ángulo, y el seno y el coseno hiperbólicos, el de los trigonométricos.

**En una dirección cualquiera.** Con $\vec{n}$ unitario, $\mathcal{K}_k := E_{0k} + E_{k0}$ y $\vec{n} \cdot \vec{\mathcal{K}} := \sum_k n_k \cdot \mathcal{K}_k$, se cumplen $(\vec{n} \cdot \vec{\mathcal{K}})^2 = E_{00} + \sum_{j,k} n_j \cdot n_k \cdot E_{jk}$ y $(\vec{n} \cdot \vec{\mathcal{K}})^3 = \vec{n} \cdot \vec{\mathcal{K}}$, y el cambio de velocidad con rapidez $\zeta$ en la dirección $\vec{n}$ es

$$
\begin{aligned}
B(\zeta, \vec{n}) := e^{\zeta \cdot \vec{n} \cdot \vec{\mathcal{K}}} = \begin{pmatrix} \cosh\zeta & \sinh\zeta \cdot \vec{n}^{\mathsf{T}} \\ \sinh\zeta \cdot \vec{n} & I + (\cosh\zeta - 1) \cdot \vec{n} \cdot \vec{n}^{\mathsf{T}} \end{pmatrix},
\end{aligned}
$$

con velocidad $\vec{v} = c \cdot \tanh\zeta \cdot \vec{n}$. Deja sin cambiar las componentes de $\vec{q}$ perpendiculares a $\vec{n}$. Su primera columna es $(\cosh\zeta, \sinh\zeta \cdot \vec{n})$, un dato que se usa en el apartado 4.6.

### 4.4. La composición de cambios de velocidad

**En la misma dirección, las rapideces se suman.** $\zeta_1 \cdot \mathcal{K}_1$ y $\zeta_2 \cdot \mathcal{K}_1$ conmutan, y por el apartado 2.2, $B_1(\zeta_2) \cdot B_1(\zeta_1) = B_1(\zeta_1 + \zeta_2)$. Con la fórmula de la tangente hiperbólica de la suma, la velocidad resultante es

$$
\begin{aligned}
v = c \cdot \tanh(\zeta_1 + \zeta_2) = c \cdot \dfrac{\tanh\zeta_1 + \tanh\zeta_2}{1 + \tanh\zeta_1 \cdot \tanh\zeta_2} = \dfrac{v_1 + v_2}{1 + v_1 \cdot v_2/c^2},
\end{aligned}
$$

la **ley relativista de adición de velocidades**. Como $|\tanh| < 1$, $|v| < c$ para cualesquiera $v_1$ y $v_2$ menores que $c$ en valor absoluto. Cuando $c \to \infty$, $v \to v_1 + v_2$, la ley de Galileo del apartado 3.2. Las rapideces se suman; las velocidades, no.

**En direcciones distintas, el producto no es un cambio de velocidad.** Por la descomposición del apartado 4.6, es un cambio de velocidad seguido de un giro, la **rotación de Thomas–Wigner**, alrededor del eje perpendicular a las dos direcciones; está en el origen de la precesión de Thomas del espín del electrón (Thomas, 1926). A primer orden en las rapideces no aparece: es un efecto de segundo orden, el que mide el conmutador de dos generadores de cambios de velocidad (apartado 4.5).

### 4.5. Los generadores y sus conmutadores

**La condición sobre los generadores.** Si $e^{s \cdot X}$ es una transformación de Lorentz para todo $s$, derivando $(e^{s \cdot X})^{\mathsf{T}} \cdot \eta \cdot e^{s \cdot X} = \eta$ en $s = 0$, con el apartado 2.2, se obtiene

$$
\begin{aligned}
X^{\mathsf{T}} \cdot \eta + \eta \cdot X = 0,
\end{aligned}
$$

el análogo de $A^{\mathsf{T}} = -A$: la matriz $\eta \cdot X$ es antisimétrica. **Recíprocamente**, si $X$ la cumple, $X^{\mathsf{T}} = -\eta \cdot X \cdot \eta$, y por el apartado 2.2 (con $C = \eta = \eta^{-1}$), $(e^{s \cdot X})^{\mathsf{T}} = e^{s \cdot X^{\mathsf{T}}} = \eta \cdot e^{-s \cdot X} \cdot \eta$, así que $(e^{s \cdot X})^{\mathsf{T}} \cdot \eta \cdot e^{s \cdot X} = \eta \cdot e^{-s \cdot X} \cdot e^{s \cdot X} = \eta$. Además, la diagonal de $\eta \cdot X$ es nula, la de $X$ también, $\operatorname{tr} X = 0$ y $\det e^{s \cdot X} = 1$; y $(e^{s \cdot X})_{00}$, que vale $1$ en $s = 0$, varía de forma continua y no puede pasar a ser menor o igual que $-1$. Por tanto, $e^{s \cdot X} \in SO^+(1, 3)$ para todo $s$.

**Seis generadores.** Una matriz antisimétrica $4 \times 4$ tiene $6$ entradas libres, así que hay seis generadores independientes: los tres giros, $\mathcal{J}_k := \mathrm{diag}(0, J_k)$, con $J_k$ en el bloque espacial, y los tres cambios de velocidad, $\mathcal{K}_k = E_{0k} + E_{k0}$. Las $\mathcal{J}_k$ son antisimétricas y las $\mathcal{K}_k$, simétricas. Un generador general es $X = \vec{\omega} \cdot \vec{\mathcal{J}} + \vec{\zeta} \cdot \vec{\mathcal{K}}$.

**Conmutadores**, para $(i, j, k)$ igual a $(1, 2, 3)$, $(2, 3, 1)$ o $(3, 1, 2)$:

$$
\begin{aligned}
{[\mathcal{J}_i, \mathcal{J}_j]} = \mathcal{J}_k, \qquad [\mathcal{J}_i, \mathcal{K}_j] = \mathcal{K}_k, \qquad [\mathcal{K}_i, \mathcal{K}_j] = -\mathcal{J}_k,
\end{aligned}
$$

y $[\mathcal{J}_i, \mathcal{K}_i] = 0$. Los dos primeros son como en Galileo. El tercero es la novedad: por ejemplo, $\mathcal{K}_1 \cdot \mathcal{K}_2 = (E_{01} + E_{10}) \cdot (E_{02} + E_{20}) = E_{12}$, porque de los cuatro productos solo $E_{10} \cdot E_{02}$ no se anula, y del mismo modo $\mathcal{K}_2 \cdot \mathcal{K}_1 = E_{21}$; así, $[\mathcal{K}_1, \mathcal{K}_2] = E_{12} - E_{21} = -\mathcal{J}_3$. Por el apartado 2.7, dos cambios de velocidad pequeños en direcciones distintas, aplicados en un orden y deshechos en el otro, dejan un giro de segundo orden: la versión infinitesimal de la rotación de Thomas–Wigner. Los seis forman el **álgebra de Lorentz**.

### 4.6. Descomposición polar

**Teorema.** Toda $\Lambda \in SO^+(1, 3)$ se escribe de forma única como un cambio de velocidad por un giro, $\Lambda = B(\zeta, \vec{n}) \cdot \mathrm{diag}(1, R)$, con $R$ una rotación.

**Demostración.**

1. **El cambio de velocidad.** La primera columna de $\Lambda$, $(\Lambda_{00}, \vec{w})$ con $\vec{w} := (\Lambda_{10}, \Lambda_{20}, \Lambda_{30})$, cumple $\Lambda_{00}^2 - |\vec{w}|^2 = 1$ y $\Lambda_{00} \geq 1$ (apartado 4.2). Hay un único $\zeta \geq 0$ con $\cosh\zeta = \Lambda_{00}$, y entonces $\sinh\zeta = |\vec{w}|$. Si $\vec{w} \neq \vec{0}$, con $\vec{n} := \dfrac{\vec{w}}{|\vec{w}|}$, $B(\zeta, \vec{n})$ tiene la misma primera columna que $\Lambda$ (apartado 4.3); si $\vec{w} = \vec{0}$, $\zeta = 0$ y $B = I$.
2. **El giro.** $\Lambda' := B(\zeta, \vec{n})^{-1} \cdot \Lambda$ es de $SO^+(1, 3)$ y lleva $e_0 = (1, 0, 0, 0)$ a $B^{-1} \cdot \Lambda \cdot e_0 = B^{-1} \cdot B \cdot e_0 = e_0$: su primera columna es $e_0$. Por la última consecuencia del apartado 4.2, $\sum_k (\Lambda')_{0k}^2 = (\Lambda')_{00}^2 - 1 = 0$, así que su primera fila también es $(1, 0, 0, 0)$. Entonces $\Lambda' = \mathrm{diag}(1, R)$, y la condición $\Lambda'^{\mathsf{T}} \cdot \eta \cdot \Lambda' = \eta$ da $R^{\mathsf{T}} \cdot R = I$; con $\det \Lambda' = \det R = 1$, $R$ es una rotación.
3. **Unicidad.** Si $B \cdot \mathrm{diag}(1, R) = B' \cdot \mathrm{diag}(1, R')$, las primeras columnas coinciden, porque $\mathrm{diag}(1, R)$ deja fijo $e_0$, y un cambio de velocidad queda determinado por su primera columna (paso 1): $B = B'$, y entonces $R = R'$. $\blacksquare$

**Consecuencias.** Toda transformación de Lorentz es el producto de dos exponenciales, $e^{\zeta \cdot \vec{n} \cdot \vec{\mathcal{K}}} \cdot e^{\theta \cdot \vec{m} \cdot \vec{\mathcal{J}}}$ (apartado 2.5): tres parámetros para el cambio de velocidad y tres para el giro. Además, toda $\Lambda \in SO^+(1, 3)$ es una sola exponencial $e^X$, con $X$ un generador; es un resultado conocido que aquí se cita sin demostración (Nishikawa, 1983). El grupo no es compacto, a diferencia de $SO(3)$: la rapidez puede tomar cualquier valor real, y las entradas de $B(\zeta, \vec{n})$ no están acotadas.

### 4.7. Primer orden: el generador de la parte física

Un cambio de velocidad pequeño, con velocidad $\varepsilon \cdot \vec{u}$, tiene rapidez $\dfrac{\varepsilon \cdot |\vec{u}|}{c} + O(\varepsilon^3)$, y su generador es $\dfrac{1}{c} \cdot \vec{u} \cdot \vec{\mathcal{K}}$. A primer orden, $e^{\varepsilon \cdot X} \cdot x = x + \varepsilon \cdot X \cdot x + O(\varepsilon^2)$, con

$$
\begin{aligned}
X \cdot \begin{pmatrix} c \cdot t \\ \vec{q} \end{pmatrix} = \begin{pmatrix} \dfrac{\vec{u} \cdot \vec{q}}{c} \\ \vec{u} \cdot t \end{pmatrix}:
\end{aligned}
$$

$t \mapsto t + \varepsilon \cdot \dfrac{\vec{u} \cdot \vec{q}}{c^2}$ y $\vec{q} \mapsto \vec{q} + \varepsilon \cdot \vec{u} \cdot t$, el generador $(\tau, \vec{\xi}) = \left(\dfrac{\vec{u} \cdot \vec{q}}{c^2}, \vec{u} \cdot t\right)$ de la parte física, apartado 9.1. Los giros dan, como en el apartado 1.5, $\vec{q} \mapsto \vec{q} + \varepsilon \cdot \vec{\omega} \times \vec{q}$.

## 5. El grupo de Poincaré en forma de matrices

### 5.1. La matriz y su acción

Una transformación de Poincaré es una de Lorentz seguida de una traslación en el espacio-tiempo, $x' = \Lambda \cdot x + a$, con $a = (a_0, \vec{a})$, donde $a_0 = c \cdot b$ y $b$ es el desplazamiento temporal. Como en el apartado 3.1, se escribe como una matriz $5 \times 5$ que actúa sobre $(c \cdot t, \vec{q}, 1)$, con filas y columnas numeradas de $0$ a $4$:

$$
\begin{aligned}
\Pi(\Lambda, a) = \begin{pmatrix} \Lambda & a \\ 0^{\mathsf{T}} & 1 \end{pmatrix}, \qquad
\begin{pmatrix} x' \\ 1 \end{pmatrix} = \Pi(\Lambda, a) \cdot \begin{pmatrix} x \\ 1 \end{pmatrix},
\end{aligned}
$$

donde $0^{\mathsf{T}}$ es una fila de cuatro ceros.

* **Composición.** Por bloques, $\Pi(\Lambda_2, a_2) \cdot \Pi(\Lambda_1, a_1) = \Pi(\Lambda_2 \cdot \Lambda_1,\ \Lambda_2 \cdot a_1 + a_2)$: las transformaciones de Lorentz se multiplican, y la primera traslación se transforma con la segunda transformación de Lorentz antes de sumarse.
* **Identidad e inversa.** La identidad es $\Pi(I, 0)$. La inversa se obtiene despejando $x$ en $x' = \Lambda \cdot x + a$:

  $$
  \begin{aligned}
  \Pi(\Lambda, a)^{-1} = \Pi\big(\Lambda^{-1},\ -\Lambda^{-1} \cdot a\big), \qquad \Lambda^{-1} = \eta \cdot \Lambda^{\mathsf{T}} \cdot \eta.
  \end{aligned}
  $$

* **Asociatividad:** la del producto de matrices.

Con $\Lambda \in SO^+(1, 3)$, forman un grupo de $6 + 4 = 10$ parámetros, el **grupo de Poincaré**. No es conmutativo: un cambio de velocidad $B$ y una traslación $a$ dan $\Pi(B, 0) \cdot \Pi(I, a) = \Pi(B, B \cdot a)$ en un orden y $\Pi(I, a) \cdot \Pi(B, 0) = \Pi(B, a)$ en el otro. Con $a = (c \cdot b, \vec{0})$, una traslación temporal, la primera desplaza también la posición: $B \cdot a$ tiene componentes espaciales $c \cdot b \cdot \sinh\zeta \cdot \vec{n}$. Es el análogo del término cruzado de Galileo, y en el límite de velocidades pequeñas se reduce a él ($c \cdot \sinh\zeta \to v$).

### 5.2. Los diez generadores y sus conmutadores

Los generadores son las matrices $\begin{pmatrix} X_L & d \\ 0^{\mathsf{T}} & 0 \end{pmatrix}$, con $X_L$ un generador de Lorentz y $d$ una columna de cuatro números. Una base:

* $\mathcal{J}_k$ y $\mathcal{K}_k$, los de Lorentz en el bloque $4 \times 4$;
* $\mathcal{P}_\mu := E_{\mu 4}$, para $\mu = 0, 1, 2, 3$: la traslación en la coordenada $x_\mu$. $\mathcal{P}_0$ traslada $c \cdot t$, y la traslación temporal en $\tau$ es $e^{c \cdot \tau \cdot \mathcal{P}_0}$.

**Conmutadores**, además de los de Lorentz, para $(i, j, k)$ cíclico:

$$
\begin{aligned}
{[\mathcal{J}_i, \mathcal{P}_j]} &= \mathcal{P}_k, \qquad [\mathcal{J}_i, \mathcal{P}_0] = 0, \qquad [\mathcal{P}_\mu, \mathcal{P}_\nu] = 0, \\
{[\mathcal{K}_i, \mathcal{P}_0]} &= \mathcal{P}_i, \qquad [\mathcal{K}_i, \mathcal{P}_j] = \delta_{ij} \cdot \mathcal{P}_0,
\end{aligned}
$$

con $\delta_{ij}$ igual a $1$ si $i = j$ y a $0$ si no, y $[\mathcal{J}_i, \mathcal{P}_i] = 0$. Por ejemplo, $\mathcal{K}_i \cdot \mathcal{P}_j = (E_{0i} + E_{i0}) \cdot E_{j4} = \delta_{ij} \cdot E_{04}$, porque el único producto que puede no anularse es $E_{0i} \cdot E_{j4}$, y $\mathcal{P}_j \cdot \mathcal{K}_i = 0$, porque la fila $4$ de $\mathcal{K}_i$ es nula. Los diez forman el **álgebra de Poincaré**.

**Lo que cambia respecto de Galileo**, con $\mathcal{P}_0$ en el papel de $\mathcal{T}$: en Galileo, $[\mathcal{K}_i, \mathcal{K}_j] = 0$ y $[\mathcal{K}_i, \mathcal{P}_j] = 0$; en Poincaré, $[\mathcal{K}_i, \mathcal{K}_j] = -\mathcal{J}_k$ y $[\mathcal{K}_i, \mathcal{P}_j] = \delta_{ij} \cdot \mathcal{P}_0$. El primero es la rotación de Thomas–Wigner; el segundo dice que un cambio de velocidad mezcla las traslaciones espaciales con la temporal, como mezcla el espacio con el tiempo. El apartado 6 muestra cómo desaparecen los dos en el límite de Galileo.

### 5.3. Formas exponenciales

**Forma de producto.** Como $(a \cdot \mathcal{P})^2 = 0$, con $a \cdot \mathcal{P} := \sum_\mu a_\mu \cdot \mathcal{P}_\mu$, $e^{a \cdot \mathcal{P}} = I + a \cdot \mathcal{P} = \Pi(I, a)$, y por la ley de composición, $\Pi(I, a) \cdot \Pi(\Lambda, 0) = \Pi(\Lambda, a)$. Con la descomposición polar del apartado 4.6:

$$
\begin{aligned}
\Pi(\Lambda, a) = e^{a \cdot \mathcal{P}} \cdot e^{\zeta \cdot \vec{n} \cdot \vec{\mathcal{K}}} \cdot e^{\theta \cdot \vec{m} \cdot \vec{\mathcal{J}}},
\end{aligned}
$$

donde los generadores de Lorentz se entienden en el bloque $4 \times 4$. Como en el apartado 3.7, la traslación va a la izquierda y no hace falta corrección.

**Una sola exponencial.** Multiplicando por bloques, para $k \geq 1$,

$$
\begin{aligned}
\begin{pmatrix} X_L & d \\ 0^{\mathsf{T}} & 0 \end{pmatrix}^k = \begin{pmatrix} X_L^k & X_L^{k-1} \cdot d \\ 0^{\mathsf{T}} & 0 \end{pmatrix},
\end{aligned}
$$

y sumando la serie,

$$
\begin{aligned}
\exp\begin{pmatrix} X_L & d \\ 0^{\mathsf{T}} & 0 \end{pmatrix} = \Pi\big(e^{X_L},\ V(X_L) \cdot d\big), \qquad V(X_L) = \sum_{j=0}^{\infty} \dfrac{X_L^j}{(j+1)!},
\end{aligned}
$$

la misma serie $V$ del apartado 3.8. Con $X_L = \zeta \cdot \mathcal{K}_1$, como $\mathcal{K}_1^3 = \mathcal{K}_1$, las potencias se agrupan con las series hiperbólicas:

$$
\begin{aligned}
V(\zeta \cdot \mathcal{K}_1) = I + \dfrac{\cosh\zeta - 1}{\zeta} \cdot \mathcal{K}_1 + \dfrac{\sinh\zeta - \zeta}{\zeta} \cdot \mathcal{K}_1^2,
\end{aligned}
$$

el análogo hiperbólico de la $V$ con rotación del apartado 3.8, con $\cosh$ y $\sinh$ en lugar de $\cos$ y $\sin$ y algunos signos cambiados.

### 5.4. El campo vectorial de cada generador y su cantidad conservada

Con los coeficientes físicos de la parte física (giro $\vec{\omega}$, velocidad $\vec{u}$, traslación espacial $\vec{d}$ y temporal $\tau$), el generador general es

$$
\begin{aligned}
X = \vec{\omega} \cdot \vec{\mathcal{J}} + \dfrac{1}{c} \cdot \vec{u} \cdot \vec{\mathcal{K}} + \vec{d} \cdot \vec{\mathcal{P}} + c \cdot \tau \cdot \mathcal{P}_0,
\end{aligned}
$$

con $\vec{d} \cdot \vec{\mathcal{P}} := \sum_k d_k \cdot \mathcal{P}_k$. Multiplicando por la columna $(c \cdot t, \vec{q}, 1)$, el campo es

$$
\begin{aligned}
\dfrac{dt}{ds} = \tau + \dfrac{\vec{u} \cdot \vec{q}}{c^2}, \qquad \dfrac{d\vec{q}}{ds} = \vec{\omega} \times \vec{q} + \vec{u} \cdot t + \vec{d}.
\end{aligned}
$$

Es el generador $(\tau + \vec{u} \cdot \vec{q}/c^2,\ \vec{\omega} \times \vec{q} + \vec{u} \cdot t + \vec{d})$, y para una partícula libre relativista, con la parte física, apartado 9.3, $F = 0$ y

$$
\begin{aligned}
Q = \vec{p} \cdot \vec{\xi} - \left(\tau + \dfrac{\vec{u} \cdot \vec{q}}{c^2}\right) \cdot E = \vec{\omega} \cdot \vec{\ell} - \vec{u} \cdot \vec{G}_{\mathrm{rel}} + \vec{d} \cdot \vec{p} - \tau \cdot E.
\end{aligned}
$$

Con $N$ partículas libres, $\vec{\ell}$, $\vec{p}$, $E$ y $\vec{G}_{\mathrm{rel}}$ se sustituyen por los totales (parte física, apartado 9.5).

| Generador | Campo $(\tau,\ \vec{\xi})$ | Cantidad conservada |
| ------------------------------ | ---------------------------------------- | ---------------------------- |
| $\vec{n} \cdot \vec{\mathcal{J}}$ | $(0,\ \vec{n} \times \vec{q})$ | $\vec{n} \cdot \vec{\ell}$ |
| $\dfrac{1}{c} \cdot \vec{e} \cdot \vec{\mathcal{K}}$ | $\left(\dfrac{\vec{e} \cdot \vec{q}}{c^2},\ \vec{e} \cdot t\right)$ | $-\vec{e} \cdot \vec{G}_{\mathrm{rel}}$ |
| $\vec{e} \cdot \vec{\mathcal{P}}$ | $(0,\ \vec{e})$ | $\vec{e} \cdot \vec{p}$ |
| $c \cdot \mathcal{P}_0$ | $(1,\ \vec{0})$ | $-E$ |

Table: Los generadores de Poincaré, sus campos y sus cantidades conservadas.

## 6. De Poincaré a Galileo

### 6.1. Los generadores de Poincaré en las coordenadas de Galileo

Para comparar los dos grupos hay que escribirlos sobre la misma columna. Sea $S$ la matriz invertible que lleva $(c \cdot t, \vec{q}, 1)$ a $(\vec{q}, t, 1)$: reordena las componentes y divide la de $c \cdot t$ por $c$. Si $x' = \Pi \cdot x$, entonces $S \cdot x' = (S \cdot \Pi \cdot S^{-1}) \cdot (S \cdot x)$: en las coordenadas de Galileo, las matrices de Poincaré son $S \cdot \Pi \cdot S^{-1}$, y sus generadores, $S \cdot X \cdot S^{-1}$ (apartado 2.2).

Con la numeración de filas y columnas del apartado 3 (de $1$ a $5$, con la fila $4$ para $t$), y los generadores con los coeficientes físicos del apartado 5.4:

* **Giros y traslaciones espaciales:** $S \cdot \mathcal{J}_k \cdot S^{-1}$ y $S \cdot \mathcal{P}_k \cdot S^{-1}$ son los $\mathcal{J}_k$ y $\mathcal{P}_k$ de Galileo.
* **Traslación temporal:** $S \cdot (c \cdot \mathcal{P}_0) \cdot S^{-1} = E_{45}$, el $\mathcal{T}$ de Galileo.
* **Cambios de velocidad:** con $\mathcal{K}_k^{(c)} := S \cdot \left(\dfrac{1}{c} \cdot \mathcal{K}_k\right) \cdot S^{-1}$,
  $$
  \begin{aligned}
  \mathcal{K}_k^{(c)} = E_{k4} + \dfrac{1}{c^2} \cdot E_{4k}:
  \end{aligned}
  $$
  el término $E_{k4}$ es el cambio de velocidad de Galileo, $\dfrac{dq_k}{ds} = t$, y el término $\dfrac{1}{c^2} \cdot E_{4k}$ es la parte relativista, $\dfrac{dt}{ds} = \dfrac{q_k}{c^2}$.

Cuando $c \to \infty$, $\mathcal{K}_k^{(c)} \to \mathcal{K}_k$: los diez generadores de Poincaré tienden a los diez de Galileo.

### 6.2. Los conmutadores en el límite

Con $\mathcal{T} = S \cdot (c \cdot \mathcal{P}_0) \cdot S^{-1}$, los conmutadores del apartado 5.2 se escriben, para $(i, j, k)$ cíclico,

$$
\begin{aligned}
{[\mathcal{K}_i^{(c)}, \mathcal{K}_j^{(c)}]} = -\dfrac{1}{c^2} \cdot \mathcal{J}_k, \qquad [\mathcal{K}_i^{(c)}, \mathcal{T}] = \mathcal{P}_i, \qquad [\mathcal{K}_i^{(c)}, \mathcal{P}_j] = \dfrac{\delta_{ij}}{c^2} \cdot \mathcal{T},
\end{aligned}
$$

y los de los giros no cambian. Cuando $c \to \infty$, el primero y el tercero se anulan, y queda la tabla de Galileo del apartado 3.6. El grupo de Galileo es una **contracción** del de Poincaré (Inönü y Wigner, 1953): las mismas diez direcciones, con unas relaciones de conmutación que dependen de un parámetro, $\dfrac{1}{c^2}$, y que en el límite pierden dos términos. Lo que desaparece es lo propio de la relatividad: la rotación de Thomas–Wigner y la mezcla de las traslaciones espaciales con la temporal. En la matriz de Galileo, la fila de $t$ es $(0, 0, 0, 1, b)$: el tiempo no depende de la posición.

### 6.3. La carga central: la masa

**El corchete de Poisson.** Para dos funciones $f$ y $g$ de las posiciones y los momentos de $N$ partículas, se define

$$
\begin{aligned}
\{f, g\} := \sum_{i=1}^{N} \Big(\nabla_{\vec{q}_i} f \cdot \nabla_{\vec{p}_i} g - \nabla_{\vec{p}_i} f \cdot \nabla_{\vec{q}_i} g\Big).
\end{aligned}
$$

Por ejemplo, $\{q_{i,a}, p_{j,b}\}$ vale $1$ si $i = j$ y $a = b$, y $0$ en los demás casos. A lo largo de los movimientos, $\dfrac{df}{dt} = \{f, \bsH\} + \partial_t f$, por las ecuaciones de Hamilton (Goldstein et al., 2002, cap. 9). Es el análogo clásico del conmutador cuántico: a $[\hat{A}, \hat{B}]$ le corresponde $i \cdot \hbar \cdot \{A, B\}$ (Dirac, 1925).

**Galileo.** Para $N$ partículas libres, con las cantidades conservadas del apartado 3.9 como funciones de las posiciones y los momentos en cada instante $t$ fijo:

$$
\begin{aligned}
\{J_1, J_2\} &= J_3, \qquad \{J_1, P_2\} = P_3, \qquad \{J_1, G_2\} = G_3, \\
\{G_j, \bsH\} &= P_j, \qquad \{G_j, G_k\} = 0, \qquad \{P_j, \bsH\} = 0, \qquad \{J_j, \bsH\} = 0, \\
\{G_j, P_k\} &= M \cdot \delta_{jk}.
\end{aligned}
$$

Por ejemplo, $\{G_j, P_k\} = \sum_i m_i \cdot \{q_{i,j}, P_k\} = \sum_i m_i \cdot \delta_{jk} = M \cdot \delta_{jk}$. Con la correspondencia $\mathcal{J} \leftrightarrow \vec{J}$, $\mathcal{K} \leftrightarrow \vec{G}$, $\mathcal{P} \leftrightarrow \vec{P}$ y $\mathcal{T} \leftrightarrow \bsH$, las relaciones son las de los conmutadores de los generadores del apartado 3.6, con los mismos signos, salvo una: donde los generadores dan $[\mathcal{K}_j, \mathcal{P}_k] = 0$, los corchetes dan $\{G_j, P_k\} = M \cdot \delta_{jk}$. La masa total $M$ es una constante, y su corchete con cualquier función es nulo: es un término que conmuta con todo y que aparece en las relaciones de las cantidades conservadas sin estar en las de los generadores. Se llama **carga central**.

**En la mecánica cuántica.** Con $\hat{\vec{G}} = m \cdot \hat{\vec{q}} - \hat{\vec{p}} \cdot t$ para una partícula (parte física, apartado 10.5), la relación canónica da $[\hat{G}_j, \hat{p}_k] = i \cdot \hbar \cdot m \cdot \delta_{jk}$: el mismo término, multiplicado por $i \cdot \hbar$. Es la razón de que los operadores unitarios del grupo de Galileo se compongan como el grupo solo salvo fases que dependen de la masa, como $\hat{B} \cdot \hat{T} = e^{i \cdot m \cdot \vec{u} \cdot \vec{a}/\hbar} \cdot \hat{T} \cdot \hat{B}$ (parte física, apartado 10.5). Las representaciones del grupo de Galileo en la mecánica cuántica son **proyectivas**, es decir, salvo fases, y la masa es la carga central que las distingue; de ahí la regla de superselección de la masa (Bargmann, 1954; Lévy-Leblond, 1963).

**Poincaré.** Para una partícula libre relativista, con $\vec{G}_{\mathrm{rel}} = \dfrac{E \cdot \vec{q}}{c^2} - \vec{p} \cdot t$ y $E = \sqrt{|\vec{p}|^2 \cdot c^2 + m^2 \cdot c^4}$:

$$
\begin{aligned}
\{G_{\mathrm{rel},j}, p_k\} = \dfrac{E}{c^2} \cdot \delta_{jk}, \qquad \{G_{\mathrm{rel},j}, E\} = p_j, \qquad \{G_{\mathrm{rel},1}, G_{\mathrm{rel},2}\} = -\dfrac{\ell_3}{c^2}.
\end{aligned}
$$

Con la correspondencia $\mathcal{K}^{(c)} \leftrightarrow \vec{G}_{\mathrm{rel}}$ y $\mathcal{T} \leftrightarrow E$, son exactamente los conmutadores del apartado 6.2: $[\mathcal{K}_j^{(c)}, \mathcal{P}_k] = \dfrac{\delta_{jk}}{c^2} \cdot \mathcal{T}$, $[\mathcal{K}_j^{(c)}, \mathcal{T}] = \mathcal{P}_j$ y $[\mathcal{K}_1^{(c)}, \mathcal{K}_2^{(c)}] = -\dfrac{1}{c^2} \cdot \mathcal{J}_3$. En Poincaré no hay carga central: $\dfrac{E}{c^2}$ no es una constante, sino la cantidad conservada de la traslación temporal dividida por $c^2$.

**De dónde sale la masa de Galileo.** Cuando $c \to \infty$, $E = m \cdot c^2 + \dfrac{|\vec{p}|^2}{2 \cdot m} + O\!\left(\dfrac{1}{c^2}\right)$, y $\dfrac{E}{c^2} \to m$. En los generadores, el término $\dfrac{\delta_{jk}}{c^2} \cdot \mathcal{T}$ desaparece en el límite; en las cantidades conservadas, el término correspondiente, $\dfrac{E}{c^2} \cdot \delta_{jk}$, no desaparece, porque $E$ contiene la energía en reposo $m \cdot c^2$, y tiende a $m \cdot \delta_{jk}$. La carga central de Galileo es lo que queda de la energía en reposo: el mismo origen que la $F$ del cambio de velocidad de Galileo y la fase de la mecánica cuántica (parte física, apartados 9.4 y 10.6).

## 7. Resumen

| | Galileo | Poincaré |
| ---------------------------- | ------------------------------------ | ------------------------------------ |
| Matriz | $\Gamma(R, \vec{v}, \vec{a}, b)$, $5 \times 5$, sobre $(\vec{q}, t, 1)$ | $\Pi(\Lambda, a)$, $5 \times 5$, sobre $(c \cdot t, \vec{q}, 1)$ |
| Condición | $R^{\mathsf{T}} \cdot R = I$, $\det R = 1$ | $\Lambda^{\mathsf{T}} \cdot \eta \cdot \Lambda = \eta$, $\det \Lambda = 1$, $\Lambda_{00} \geq 1$ |
| Parámetros | $3 + 3 + 3 + 1 = 10$ | $3 + 3 + 3 + 1 = 10$ |
| Velocidades | se suman | se suman las rapideces |
| $[\mathcal{K}_i, \mathcal{K}_j]$ | $0$ | $-\mathcal{J}_k$ (rotación de Thomas–Wigner) |
| $[\mathcal{K}_i, \mathcal{P}_j]$ | $0$ | $\delta_{ij} \cdot \mathcal{P}_0$ |
| $[\mathcal{K}_i, \mathcal{T}]$ o $[\mathcal{K}_i, \mathcal{P}_0]$ | $\mathcal{P}_i$ | $\mathcal{P}_i$ |
| Campo del cambio de velocidad | $(0,\ \vec{u} \cdot t)$ | $\left(\dfrac{\vec{u} \cdot \vec{q}}{c^2},\ \vec{u} \cdot t\right)$ |
| $F$ del cambio de velocidad | $\sum_i m_i \cdot \vec{u} \cdot \vec{q}_i$ | $0$ |
| Cantidad del cambio de velocidad | $\vec{G} = M \cdot \vec{X} - \vec{P} \cdot t$ | $\vec{G}_{\mathrm{rel}} = \dfrac{E}{c^2} \cdot \vec{X}_E - \vec{P} \cdot t$ |
| Carga central | la masa: $\{G_j, P_k\} = M \cdot \delta_{jk}$ | no hay: $\{G_{\mathrm{rel},j}, p_k\} = \dfrac{E}{c^2} \cdot \delta_{jk}$ |

Table: Los grupos de Galileo y de Poincaré.

Cada fila de la columna de Galileo es el límite $c \to \infty$ de la de Poincaré, salvo la última, en la que el límite de $\dfrac{E}{c^2}$ es la masa.

## Referencias

* Bargmann, V. (1954). On unitary ray representations of continuous groups. *Annals of Mathematics*, *59*(1), 1–46.
* Dirac, P. A. M. (1925). The fundamental equations of quantum mechanics. *Proceedings of the Royal Society of London. Series A*, *109*(752), 642–653.
* Goldstein, H., Poole, C. y Safko, J. (2002). *Classical mechanics* (3.ª ed.). Addison-Wesley.
* Hall, B. C. (2015). *Lie groups, Lie algebras, and representations: An elementary introduction* (2.ª ed.). Springer.
* Inönü, E. y Wigner, E. P. (1953). On the contraction of groups and their representations. *Proceedings of the National Academy of Sciences*, *39*(6), 510–524.
* Lévy-Leblond, J.-M. (1963). Galilei group and nonrelativistic quantum mechanics. *Journal of Mathematical Physics*, *4*(6), 776–788.
* Nishikawa, M. (1983). On the exponential map of the group $O(p, q)_0$. *Memoirs of the Faculty of Science, Kyushu University. Series A, Mathematics*, *37*(1), 63–69.
* Thomas, L. H. (1926). The motion of the spinning electron. *Nature*, *117*(2945), 514.
