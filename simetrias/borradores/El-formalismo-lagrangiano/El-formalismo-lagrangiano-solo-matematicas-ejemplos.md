---
author: "Julián Calderón Almendros"
---

# El formalismo lagrangiano: ejemplos matemáticos

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-03
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

Ejemplos de la parte matemática («El formalismo lagrangiano: parte matemática»), todavía sin leyes físicas: el camino más corto entre dos puntos del plano, primero entre gráficas y después en forma paramétrica; la superficie casi plana de área mínima, que lleva a la ecuación de Laplace; y un sistema de ecuaciones con la estructura de las de Newton.

## Ejemplo: el camino más corto entre dos puntos del plano

Como primer ejemplo, buscamos el camino más corto entre dos puntos del plano, $A = (x_1, y_1)$ y $B = (x_2, y_2)$, con $x_1 < x_2$. La distancia entre dos puntos $(a_1, b_1)$ y $(a_2, b_2)$ del plano es

$$
\begin{aligned}
\operatorname{dist}\big((a_1, b_1), (a_2, b_2)\big) := \sqrt{(a_2 - a_1)^2 + (b_2 - b_1)^2}.
\end{aligned}
$$

La escribimos $\operatorname{dist}$, y no $d$, para no confundirla con el diferencial. Como caminos consideramos las gráficas $y = f(x)$ de las funciones del conjunto de partida del primer apartado de la parte matemática, con $[a,b] = [x_1, x_2]$, $f(x_1) = y_1$ y $f(x_2) = y_2$. Aplicar la fórmula de la distancia a los extremos $A$ y $B$ da la longitud del segmento que los une, que es precisamente lo que queremos comparar con la de los demás caminos. Para medir un camino curvo, la fórmula se aplica a puntos muy próximos del propio camino.

### La longitud de un camino

Para dos puntos vecinos de la gráfica, $(x, f(x))$ y $(x + \Delta x, f(x + \Delta x))$, la fórmula de la distancia da

$$
\begin{aligned}
(\Delta s)^2 = (\Delta x)^2 + \big(f(x + \Delta x) - f(x)\big)^2 \approx (\Delta x)^2 + f'(x)^2 \cdot (\Delta x)^2,
\end{aligned}
$$

así que cada trozo mide aproximadamente $\Delta s \approx \sqrt{1 + f'(x)^2} \cdot \Delta x$. Sumando los trozos se obtiene la longitud. Para hacerlo con rigor, aproximamos el camino por poligonales inscritas.

1. **Una poligonal inscrita.** Tomamos una partición $x_1 = \xi_0 < \xi_1 < \dots < \xi_n = x_2$ y unimos con segmentos los puntos $(\xi_k, f(\xi_k))$. La poligonal mide

   $$
   \begin{aligned}
   \sum_{k=1}^{n} \sqrt{(\xi_k - \xi_{k-1})^2 + \big(f(\xi_k) - f(\xi_{k-1})\big)^2}.
   \end{aligned}
   $$

2. **El teorema del valor medio.** En cada tramo existe $c_k \in (\xi_{k-1}, \xi_k)$ tal que $f(\xi_k) - f(\xi_{k-1}) = f'(c_k) \cdot (\xi_k - \xi_{k-1})$. Sacando de la raíz el factor $\xi_k - \xi_{k-1} > 0$, cada segmento mide $\sqrt{1 + f'(c_k)^2} \cdot (\xi_k - \xi_{k-1})$.

3. **Una suma de Riemann.** La longitud de la poligonal es, por tanto, $\sum_{k=1}^{n} \sqrt{1 + f'(c_k)^2} \cdot (\xi_k - \xi_{k-1})$, que es una suma de Riemann de la función continua $\sqrt{1 + f'(x)^2}$. Cuando la partición se refina, es decir, cuando la mayor de las longitudes $\xi_k - \xi_{k-1}$ tiende a $0$, la suma converge a la integral.

Definimos la longitud del camino como ese límite:

$$
\begin{aligned}
\bsS[f] := \int_{x_1}^{x_2} \sqrt{1 + f'(x)^2} \,dx.
\end{aligned}
$$

Es un funcional del tipo del primer apartado de la parte matemática, con

$$
\begin{aligned}
\bsL(f, f', x) = \sqrt{1 + f'^2}.
\end{aligned}
$$

$\bsL$ no depende ni de su primer argumento ni del tercero, solo de $f'$, y tiene derivadas de todos los órdenes, así que cumple las hipótesis de la parte matemática. Conviene llamar $\ell(w) := \sqrt{1 + w^2}$, de modo que $\bsL(f, f', x) = \ell(f')$. Sus dos primeras derivadas son

$$
\begin{aligned}
\ell'(w) = \dfrac{w}{\sqrt{1 + w^2}}, \qquad \ell''(w) = \dfrac{1}{\left(1 + w^2\right)^{3/2}} > 0.
\end{aligned}
$$

### La ecuación de Euler–Lagrange

Las derivadas parciales de $\bsL$ son

$$
\begin{aligned}
\dfrac{\partial \bsL}{\partial f}(f, f', x) = 0, \qquad \dfrac{\partial \bsL}{\partial f'}(f, f', x) = \ell'(f') = \dfrac{f'}{\sqrt{1 + f'^2}}.
\end{aligned}
$$

La ecuación de Euler–Lagrange queda

$$
\begin{aligned}
-\dfrac{d}{dx}\left(\dfrac{f'_0(x)}{\sqrt{1 + f'_0(x)^2}}\right) = 0,
\end{aligned}
$$

es decir, $\ell'(f'_0(x)) = C$ para todo $x \in [x_1, x_2]$, con $C$ constante. Como $\ell'' > 0$, la función $\ell'$ es estrictamente creciente y toma cada valor una sola vez. Por tanto, la derivada $f'_0$ también es constante; llamamos $m$ a su valor, de modo que $f'_0(x) = m$ para todo $x$. Integrando, $f_0(x) = m \cdot x + n$, con $n$ otra constante: la gráfica de $f_0$ es una recta de pendiente $m$.

Se llega a lo mismo con la forma desarrollada de la ecuación de Euler–Lagrange. Como $\dfrac{\partial \bsL}{\partial f}$, $\dfrac{\partial^2 \bsL}{\partial f \partial f'}$ y $\dfrac{\partial^2 \bsL}{\partial x \partial f'}$ son nulas, solo queda el término con $f''_0$:

$$
\begin{aligned}
\dfrac{\partial^2 \bsL}{\partial f'^2} \cdot f''_0(x) = \dfrac{f''_0(x)}{\left(1 + f'_0(x)^2\right)^{3/2}} = 0.
\end{aligned}
$$

El denominador no se anula nunca, así que $f''_0(x) = 0$, y de nuevo $f'_0$ es constante. En ambos casos, $f_0(x) = m \cdot x + n$, con $m$ y $n$ constantes.

### Las condiciones de contorno

Imponemos $f_0(x_1) = y_1$ y $f_0(x_2) = y_2$:

$$
\begin{aligned}
m \cdot x_1 + n = y_1, \qquad m \cdot x_2 + n = y_2.
\end{aligned}
$$

Restando, $m \cdot (x_2 - x_1) = y_2 - y_1$. Como $x_1 < x_2$, el sistema tiene solución única:

$$
\begin{aligned}
m = \dfrac{y_2 - y_1}{x_2 - x_1}, \qquad f_0(x) = y_1 + m \cdot (x - x_1).
\end{aligned}
$$

Es la recta que pasa por $A$ y $B$. Como comprobación, su longitud es la distancia entre $A$ y $B$ (en el segundo paso se usa que $x_2 - x_1 > 0$ para meterlo dentro de la raíz):

$$
\begin{aligned}
\bsS[f_0] &= \int_{x_1}^{x_2} \sqrt{1 + m^2} \,dx = (x_2 - x_1) \cdot \sqrt{1 + \dfrac{(y_2 - y_1)^2}{(x_2 - x_1)^2}} \\
&= \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} = \operatorname{dist}(A, B).
\end{aligned}
$$

### Mínimo, no solo estacionario

La ecuación de Euler–Lagrange solo garantiza que la recta hace estacionario a $\bsS$. En este ejemplo se puede demostrar además que es el mínimo, sin calcular la variación segunda, gracias a que $\ell$ es convexa.

1. **$\ell$ queda por encima de su recta tangente.** Para todo $w \in \mathbb{R}$,

   $$
   \begin{aligned}
   \ell(w) \geq \ell(m) + \ell'(m) \cdot (w - m),
   \end{aligned}
   $$

   con igualdad solo si $w = m$. En efecto, por el desarrollo de Taylor con resto de Lagrange, la diferencia entre los dos lados es $\dfrac{1}{2} \cdot \ell''(c) \cdot (w - m)^2$ para algún $c$ entre $m$ y $w$, y es positiva si $w \neq m$, porque $\ell'' > 0$.

2. **Lo aplicamos a cualquier camino.** Sea $f$ una función cualquiera del conjunto de partida. Sustituyendo $w = f'(x)$ e integrando entre $x_1$ y $x_2$:

   $$
   \begin{aligned}
   \bsS[f] \geq (x_2 - x_1) \cdot \ell(m) + \ell'(m) \cdot \int_{x_1}^{x_2} \big(f'(x) - m\big) \,dx.
   \end{aligned}
   $$

3. **El término lineal se anula.** Como $f$ toma en los extremos los mismos valores que $f_0$,

   $$
   \begin{aligned}
   \int_{x_1}^{x_2} \big(f'(x) - m\big) \,dx &= f(x_2) - f(x_1) - m \cdot (x_2 - x_1) \\
   &= (y_2 - y_1) - (y_2 - y_1) = 0.
   \end{aligned}
   $$

   Por tanto, $\bsS[f] \geq (x_2 - x_1) \cdot \ell(m) = \bsS[f_0]$.

4. **La igualdad solo se da para la recta.** La función $x \mapsto \ell(f'(x)) - \ell(m) - \ell'(m) \cdot (f'(x) - m)$ es continua y no negativa. Si $f'(x_*) \neq m$ en algún punto $x_*$, por continuidad $f' \neq m$ en un intervalo alrededor de $x_*$, donde esa función es positiva; su integral es entonces positiva, y $\bsS[f] > \bsS[f_0]$. La igualdad exige $f' = m$ en todo $[x_1, x_2]$, es decir, $f = f_0$.

La recta es, por tanto, el mínimo global y único de la longitud entre todos los caminos del conjunto de partida.

### Alcance del resultado

* Solo hemos comparado caminos que son gráficas $y = f(x)$. Quedan fuera los que retroceden en $x$ o tienen tramos verticales, y también el caso $x_1 = x_2$. Para incluirlos hay que describir el camino con un parámetro, $(x(\tau), y(\tau))$. Entonces hay dos funciones incógnita, y una ecuación de Euler–Lagrange para cada una; se trata más adelante, en el ejemplo «El camino más corto en forma paramétrica».
* La recta es de clase $C^2$, así que pertenece al conjunto de partida: exigir dos derivadas continuas no ha dejado fuera la solución.

## Ejemplo: la membrana casi plana y la ecuación de Laplace

En este ejemplo, $t$ no es el tiempo, sino una segunda coordenada del plano. Consideramos la superficie $z = f(x,t)$ sobre el rectángulo $\Omega$, con los valores en $\operatorname{Fr}(\Omega)$ fijados: es una membrana sujeta a un marco.

### El área y su aproximación para pendientes pequeñas

Un rectángulo pequeño de lados $dx$ y $dt$ se corresponde, sobre la superficie y a primer orden, con el paralelogramo que generan los vectores $(dx, 0, \partial_x f \cdot dx)$ y $(0, dt, \partial_t f \cdot dt)$. Su área es la norma de su producto vectorial:

$$
\begin{aligned}
\left|(1, 0, \partial_x f) \times (0, 1, \partial_t f)\right| \cdot dx \cdot dt &= \left|(-\partial_x f, -\partial_t f, 1)\right| \cdot dx \cdot dt \\
&= \sqrt{1 + (\partial_x f)^2 + (\partial_t f)^2} \cdot dx \cdot dt.
\end{aligned}
$$

Sumando todos los trozos, el área de la superficie es

$$
\begin{aligned}
\mathcal{A}[f] := \int_{t_1}^{t_2} \int_{x_1}^{x_2} \sqrt{1 + \big(\partial_x f(x,t)\big)^2 + \big(\partial_t f(x,t)\big)^2} \,dx \,dt.
\end{aligned}
$$

Si las pendientes son pequeñas, usamos el desarrollo $\sqrt{1 + w} = 1 + \dfrac{w}{2} + O(w^2)$ con $w = (\partial_x f)^2 + (\partial_t f)^2$:

$$
\begin{aligned}
\mathcal{A}[f] \approx (x_2 - x_1) \cdot (t_2 - t_1) + \dfrac{1}{2} \cdot \int_{t_1}^{t_2} \int_{x_1}^{x_2} \Big(\big(\partial_x f(x,t)\big)^2 + \big(\partial_t f(x,t)\big)^2\Big) \,dx \,dt.
\end{aligned}
$$

El primer término es el área del rectángulo $\Omega$ y no depende de $f$. Para una membrana casi plana, minimizar el área equivale aproximadamente a minimizar el funcional $\bsS$ con

$$
\begin{aligned}
\bsL(f, \partial_x f, \partial_t f, x, t) = \dfrac{1}{2} \cdot \left((\partial_x f)^2 + (\partial_t f)^2\right).
\end{aligned}
$$

A partir de aquí trabajamos con este $\bsL$, que ya no es una aproximación: es el funcional del ejemplo.

### La ecuación de Laplace

$\bsL$ no depende de $f$ ni depende explícitamente de $x$ ni de $t$. Sus derivadas parciales son

$$
\begin{aligned}
\partial_f \bsL = 0, \qquad \partial_{\partial_x f} \bsL = \partial_x f, \qquad \partial_{\partial_t f} \bsL = \partial_t f,
\end{aligned}
$$

y la ecuación de Euler–Lagrange queda

$$
\begin{aligned}
-\dfrac{\partial}{\partial x}\Big(\partial_x f_0(x,t)\Big) - \dfrac{\partial}{\partial t}\Big(\partial_t f_0(x,t)\Big) = 0,
\end{aligned}
$$

es decir,

$$
\begin{aligned}
\partial^2_x f_0 + \partial^2_t f_0 = 0.
\end{aligned}
$$

Es la ecuación de Laplace. Con la forma desarrollada se llega a lo mismo: $\partial_{\partial_x f} \partial_{\partial_x f} \bsL = \partial_{\partial_t f} \partial_{\partial_t f} \bsL = 1$, y todas las demás derivadas de $\bsL$ que aparecen en ella son nulas.

### Una solución en el cuadrado unidad

Tomamos $\Omega = [0,1] \times [0,1]$, es decir, $x_1 = t_1 = 0$ y $x_2 = t_2 = 1$, y como valores en la frontera

$$
\begin{aligned}
f(x,1) = \sin(\pi \cdot x), \qquad f(x,0) = 0, \qquad f(0,t) = f(1,t) = 0.
\end{aligned}
$$

Son compatibles en las esquinas, porque $\sin 0 = \sin \pi = 0$. Como en el Tema 1, apartado 1.4.4, buscamos una solución de variables separadas, $f_0(x,t) = \sin(\pi \cdot x) \cdot Y(t)$, que ya cumple las condiciones en los lados $x = 0$ y $x = 1$. Sustituyendo en la ecuación de Laplace:

$$
\begin{aligned}
-\pi^2 \cdot \sin(\pi \cdot x) \cdot Y(t) + \sin(\pi \cdot x) \cdot Y''(t) = 0 \implies Y''(t) = \pi^2 \cdot Y(t).
\end{aligned}
$$

Su solución general es $Y(t) = C_1 \cdot \cosh(\pi \cdot t) + C_2 \cdot \sinh(\pi \cdot t)$. La condición en $t = 0$ da $Y(0) = C_1 = 0$, y la condición en $t = 1$ da $Y(1) = C_2 \cdot \sinh \pi = 1$. Por tanto,

$$
\begin{aligned}
f_0(x,t) = \sin(\pi \cdot x) \cdot \dfrac{\sinh(\pi \cdot t)}{\sinh \pi}.
\end{aligned}
$$

Comprobación: $\partial^2_x f_0 = -\pi^2 \cdot f_0$ y $\partial^2_t f_0 = \pi^2 \cdot f_0$, que suman $0$; y en la frontera, $f_0(x,1) = \sin(\pi \cdot x)$, y $f_0$ se anula en los otros tres lados.

### Es el mínimo

Sea $f$ una función cualquiera del conjunto de partida, y sea $h := f - f_0$, que es de clase $C^2(\Omega)$ y se anula en $\operatorname{Fr}(\Omega)$. Como $\bsL$ es cuadrático, el desarrollo es exacto, sin resto:

$$
\begin{aligned}
&\bsL(f_0 + h, \partial_x f_0 + \partial_x h, \partial_t f_0 + \partial_t h)(x,t) \\
&\quad = \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) + \partial_x f_0 \cdot \partial_x h + \partial_t f_0 \cdot \partial_t h \\
&\qquad + \dfrac{1}{2} \cdot \left((\partial_x h)^2 + (\partial_t h)^2\right),
\end{aligned}
$$

con todas las funciones evaluadas en $(x,t)$. Al integrar, el término central da $\bsdelta\bsS[f_0]$ calculada con esta $h$, que es nula porque $f_0$ cumple la ecuación de Euler–Lagrange. Queda

$$
\begin{aligned}
\bsS[f] - \bsS[f_0] = \dfrac{1}{2} \cdot \int_{t_1}^{t_2} \int_{x_1}^{x_2} \Big(\big(\partial_x h(x,t)\big)^2 + \big(\partial_t h(x,t)\big)^2\Big) \,dx \,dt \geq 0.
\end{aligned}
$$

La igualdad exige que el integrando, que es continuo y no negativo, sea nulo en todo $\Omega$: si fuera positivo en un punto, lo sería en un rectángulo alrededor de él, y la integral sería positiva. Entonces $\partial_x h = \partial_t h = 0$ en $\Omega$, así que $h$ es constante, y como se anula en la frontera, $h = 0$. Por tanto, $f_0$ es el mínimo global y único de $\bsS$. En particular, la solución de la ecuación de Laplace con estos valores en la frontera es única: cualquier otra sería también el mínimo único.

En los ejemplos físicos, la cuerda vibrante tiene un funcional que solo se diferencia de este en un signo, y sin embargo su función estacionaria no es un mínimo.

## Ejemplo: el camino más corto en forma paramétrica

Este ejemplo completa el del camino más corto entre dos puntos del plano, que solo comparaba gráficas $y = f(x)$. Ahora describimos los caminos con un parámetro: $\vec{f}(x) = (f_1(x), f_2(x))$, con $x \in [a, b]$, de modo que $m = 1$ y $n = 2$. Los extremos están fijados, $\vec{f}(a) = \vec{A}$ y $\vec{f}(b) = \vec{B}$, con $\vec{A} \neq \vec{B}$. Así se incluyen los caminos que retroceden o tienen tramos verticales.

Exigimos además que la curva sea regular, $\vec{f}'(x) \neq \vec{0}$ para todo $x$, porque el integrando que vamos a usar no es derivable donde $\vec{f}' = \vec{0}$. Esta exigencia no impide aplicar lo anterior. Como $|\vec{f}'_0|$ es continua en el intervalo cerrado y acotado $[a,b]$, tiene un mínimo positivo; para $|\epsilon|$ suficientemente pequeño, $\vec{f}'_0 + \epsilon \cdot \vec{h}'$ tampoco se anula, y todo el cálculo se hace donde $\bsL$ es derivable.

Con el mismo razonamiento de las poligonales inscritas del primer ejemplo, aplicando el teorema del valor medio a cada componente y la continuidad uniforme de $\vec{f}'$ en $[a, b]$, la longitud de la curva es

$$
\begin{aligned}
\bsS[\vec{f}] = \int_a^b \sqrt{f'_1(x)^2 + f'_2(x)^2} \,dx = \int_a^b |\vec{f}'(x)| \,dx, \qquad \bsL = \sqrt{f'^2_1 + f'^2_2}.
\end{aligned}
$$

**Las ecuaciones de Euler–Lagrange.** $\bsL$ no depende de $f_1$, de $f_2$ ni de $x$, y $\partial_{f'_i} \bsL = \dfrac{f'_i}{|\vec{f}'|}$. Las dos ecuaciones son

$$
\begin{aligned}
\dfrac{d}{dx}\left(\dfrac{f'_{0,i}(x)}{|\vec{f}'_0(x)|}\right) = 0, \qquad i = 1, 2.
\end{aligned}
$$

Dicen que el vector tangente unitario $\vec{u}(x) := \dfrac{\vec{f}'_0(x)}{|\vec{f}'_0(x)|}$ es constante: $\vec{u}(x) = \vec{e}$, con $|\vec{e}| = 1$. Entonces $\vec{f}'_0(x) = |\vec{f}'_0(x)| \cdot \vec{e}$, e integrando entre $a$ y $x$,

$$
\begin{aligned}
\vec{f}_0(x) = \vec{A} + s(x) \cdot \vec{e}, \qquad s(x) := \int_a^x |\vec{f}'_0(\xi)| \,d\xi.
\end{aligned}
$$

La función $s$, que mide la longitud recorrida desde $\vec{A}$, es estrictamente creciente, porque su derivada $|\vec{f}'_0|$ es positiva, y $s(a) = 0$. Imponiendo $\vec{f}_0(b) = \vec{B}$ queda $\vec{B} - \vec{A} = s(b) \cdot \vec{e}$, con $s(b) > 0$, así que

$$
\begin{aligned}
\vec{e} = \dfrac{\vec{B} - \vec{A}}{|\vec{B} - \vec{A}|}, \qquad s(b) = |\vec{B} - \vec{A}|.
\end{aligned}
$$

La curva recorre el segmento de $\vec{A}$ a $\vec{B}$, sin retroceder, y su longitud es $\bsS[\vec{f}_0] = s(b) = |\vec{B} - \vec{A}|$, la distancia entre los dos puntos.

**Infinitas soluciones con la misma imagen.** Las ecuaciones fijan la imagen de la curva, el segmento, pero no la función $s$: cualquier forma de recorrer el segmento de $\vec{A}$ a $\vec{B}$ sin detenerse y sin retroceder es solución. La razón es que la longitud no depende de la parametrización. Si $\theta: [a, b] \to [a, b]$ es de clase $C^2$, con $\theta(a) = a$, $\theta(b) = b$ y $\theta' > 0$, el cambio de variable $y = \theta(x)$ da

$$
\begin{aligned}
\bsS[\vec{f} \circ \theta] = \int_a^b |\vec{f}'(\theta(x))| \cdot \theta'(x) \,dx = \int_a^b |\vec{f}'(y)| \,dy = \bsS[\vec{f}].
\end{aligned}
$$

En términos de la forma desarrollada, la matriz $W$ no es invertible:

$$
\begin{aligned}
W = \dfrac{1}{|\vec{f}'|^3} \cdot \begin{pmatrix} f'^2_2 & -f'_1 \cdot f'_2 \\ -f'_1 \cdot f'_2 & f'^2_1 \end{pmatrix}, \qquad \det W = \dfrac{f'^2_2 \cdot f'^2_1 - (f'_1 \cdot f'_2)^2}{|\vec{f}'|^6} = 0.
\end{aligned}
$$

Las dos ecuaciones no son independientes: la combinación $\sum_i f'_{0,i} \cdot \dfrac{d u_i}{dx} = |\vec{f}'_0| \cdot \left(\vec{u} \cdot \dfrac{d\vec{u}}{dx}\right)$ es idénticamente nula, porque $\vec{u} \cdot \vec{u} = 1$ y, al derivar, $2 \cdot \vec{u} \cdot \dfrac{d\vec{u}}{dx} = 0$. Hay una sola ecuación independiente para dos funciones incógnita, y la libertad que queda es la de la parametrización.

**Es el mínimo.** Para cualquier curva admisible, la desigualdad $\left|\int_a^b \vec{v}(x) \,dx\right| \leq \int_a^b |\vec{v}(x)| \,dx$, aplicada a $\vec{v} = \vec{f}'$, da

$$
\begin{aligned}
|\vec{B} - \vec{A}| = \left|\int_a^b \vec{f}'(x) \,dx\right| \leq \int_a^b |\vec{f}'(x)| \,dx = \bsS[\vec{f}].
\end{aligned}
$$

La desigualdad se demuestra así. Sea $\vec{w} := \int_a^b \vec{v}(x) \,dx$; si $\vec{w} = \vec{0}$, es inmediata. Si no, por la desigualdad de Cauchy–Schwarz,

$$
\begin{aligned}
|\vec{w}|^2 = \vec{w} \cdot \int_a^b \vec{v}(x) \,dx = \int_a^b \vec{w} \cdot \vec{v}(x) \,dx \leq \int_a^b |\vec{w}| \cdot |\vec{v}(x)| \,dx,
\end{aligned}
$$

y basta dividir por $|\vec{w}|$. La igualdad exige $\vec{w} \cdot \vec{v}(x) = |\vec{w}| \cdot |\vec{v}(x)|$ en todo $[a, b]$, porque los dos lados son continuos; es decir, que $\vec{v}(x)$ tenga siempre la dirección y el sentido de $\vec{w}$. Con $\vec{v} = \vec{f}'$, eso significa que la curva recorre el segmento sin retroceder. Por tanto, el segmento es el mínimo de la longitud, y los únicos caminos admisibles que lo alcanzan son sus parametrizaciones regulares.

## Ejemplo: ecuaciones con la estructura de las de Newton

Tomamos $m = 1$, con la variable llamada $t$ y el intervalo $[t_1, t_2]$, y $n$ cualquiera. Escribimos $\dot{f}_i := \dfrac{d f_i}{dt}$ y consideramos

$$
\begin{aligned}
\bsL(\vec{f}, \dot{\vec{f}}, t) = \dfrac{1}{2} \cdot \sum_{i=1}^{n} \dot{f}_i^2 - V(\vec{f}),
\end{aligned}
$$

donde $V: \mathbb{R}^n \to \mathbb{R}$ es de clase $C^2$. Las derivadas parciales son $\partial_{f_i} \bsL = -\partial_{f_i} V$ y $\partial_{\dot{f}_i} \bsL = \dot{f}_i$, y las ecuaciones de Euler–Lagrange quedan

$$
\begin{aligned}
-\partial_{f_i} V\big(\vec{f}_0(t)\big) - \dfrac{d}{dt}\big(\dot{f}_{0,i}(t)\big) = 0, \qquad i = 1, \dots, n,
\end{aligned}
$$

es decir,

$$
\begin{aligned}
\ddot{f}_{0,i}(t) = -\partial_{f_i} V\big(\vec{f}_0(t)\big), \qquad i = 1, \dots, n.
\end{aligned}
$$

Es la estructura de las ecuaciones de Newton para una fuerza que deriva de un potencial, todavía sin masa. En la parte física se introduce la masa $m_i$ de cada partícula; allí, $m$ designa siempre una masa. En este caso, $W$ es la matriz identidad, que sí es invertible, y el sistema está ya resuelto para las derivadas segundas.

Multiplicando cada ecuación por $\dot{f}_{0,i}$ y sumando en $i$ se obtiene una cantidad que no cambia con $t$:

$$
\begin{aligned}
\dfrac{d}{dt}\left(\dfrac{1}{2} \cdot \sum_{i=1}^{n} \dot{f}_{0,i}^2 + V(\vec{f}_0)\right) = \sum_{i=1}^{n} \dot{f}_{0,i} \cdot \ddot{f}_{0,i} + \sum_{i=1}^{n} \partial_{f_i} V(\vec{f}_0) \cdot \dot{f}_{0,i} = 0.
\end{aligned}
$$

Es el análogo de la conservación de la energía, y aparece porque $\bsL$ no depende explícitamente de $t$.
