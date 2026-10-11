---
author: "Julián Calderón Almendros"
---

# El teorema de Noether: ejemplos matemáticos

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-11
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

**Versión 1.** Este documento pertenece a la versión 1 de la serie, que se conserva. La versión 2, en los documentos con sufijo -v2 de este mismo directorio, es la que se mantiene al día: usa la familia $\Phi_\varepsilon$ en lugar de $\bsT_\epsilon$, transformaciones de los puntos con generador $(\tau, \xi)$ y apartados numerados, y añade, entre otras cosas, los grupos de Lorentz y de Poincaré y la mecánica cuántica no relativista. Las líneas «Fuente:» de la versión para el trabajo remiten a la versión 2.

Ejemplos de «El teorema de Noether: parte matemática». Son los mismos funcionales de «El formalismo lagrangiano: ejemplos matemáticos»: allí se resolvían las ecuaciones de Euler–Lagrange; aquí se buscan sus simetrías y se comprueba que las cantidades conservadas dan la misma solución, o parte de ella, sin resolver ecuaciones de segundo orden. En cada ejemplo se siguen los mismos pasos:

1. elegir una transformación y calcular su generador $\vec{\xi}$;
2. calcular $\bsdelta_{\vec{\xi}} \bsL$ y ver si es una derivada total $\dfrac{dF}{dx}$;
3. si lo es, escribir la cantidad conservada $Q = \sum_i p_i \cdot \xi_i - F$;
4. comprobarla con la solución conocida.

## Ejemplo: el camino más corto como gráfica

Las funciones son $f: [a, b] \to \mathbb{R}$, de clase $C^2$, con $n = 1$, y la longitud de la gráfica es el funcional de

$$
\begin{aligned}
\bsL(f, f', x) = \sqrt{1 + f'^2}, \qquad p = \partial_{f'} \bsL = \dfrac{f'}{\sqrt{1 + f'^2}}.
\end{aligned}
$$

Es conveniente usar el ángulo $\alpha(x) \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$ que forma la tangente con el eje $x$, definido por $f'(x) = \tan\alpha(x)$. Como $1 + \tan^2\alpha = \dfrac{1}{\cos^2\alpha}$ y $\cos\alpha > 0$, se tiene $\sqrt{1 + f'^2} = \dfrac{1}{\cos\alpha}$, y $p = \tan\alpha \cdot \cos\alpha = \sin\alpha$.

### Desplazamiento vertical

**1.** La transformación $f \to f + \epsilon$ desplaza la gráfica hacia arriba. Su generador es $\xi = 1$, con $\xi' = 0$.

**2.** $\bsL$ no depende de $f$, así que $\bsdelta_{\xi} \bsL = \partial_f \bsL \cdot 1 + p \cdot 0 = 0$: es una simetría con $F = 0$. Desplazar un camino no cambia su longitud.

**3.** Se conserva $Q = p \cdot 1 = \sin\alpha$: a lo largo de una solución, el ángulo de la tangente es constante.

**4.** La función $u \mapsto \dfrac{u}{\sqrt{1 + u^2}}$ tiene derivada $(1 + u^2)^{-3/2} > 0$, así que es estrictamente creciente e inyectiva. Por tanto, $p$ constante implica $f'$ constante, y $f$ es una función afín: una recta. Es la solución de «El formalismo lagrangiano: ejemplos matemáticos», obtenida aquí sin la ecuación $f'' = 0$.

### Desplazamiento horizontal

**1.** La transformación $f(x) \to f(x + \epsilon)$ desplaza la gráfica en horizontal. Su generador es $\xi = f'$.

**2.** $\bsL$ no depende explícitamente de $x$: es una simetría con $F = \bsL$ (parte matemática, identidad de Beltrami).

**3.** Se conserva

$$
\begin{aligned}
\bsH = f' \cdot p - \bsL &= \dfrac{f'^2}{\sqrt{1 + f'^2}} - \sqrt{1 + f'^2} = \dfrac{f'^2 - (1 + f'^2)}{\sqrt{1 + f'^2}} \\
&= -\dfrac{1}{\sqrt{1 + f'^2}} = -\cos\alpha.
\end{aligned}
$$

**4.** $\bsH$ constante implica $|f'|$ constante, digamos $|f'| = c$. Si $c > 0$, $f'$ solo puede valer $c$ o $-c$, y por el teorema de los valores intermedios, siendo continua, no puede pasar de uno a otro sin anularse: $f'$ es constante. Si $c = 0$, $f' = 0$. En los dos casos, $f$ es afín.

### Qué muestra el ejemplo

* Las dos simetrías expresan que en el plano no hay puntos privilegiados, y cada una da una ecuación de primer orden en lugar de la de segundo orden de Euler–Lagrange.
* Aquí dan la misma información: $\sin\alpha$ y $\cos\alpha$ constantes dicen lo mismo, porque con $\alpha \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$ cada una determina $\alpha$. En general, dos cantidades conservadas no tienen por qué ser independientes.
* Los giros del plano no aparecen: el giro de una gráfica puede dejar de ser una gráfica. Para tratarlos hace falta la forma paramétrica.

## Ejemplo: el camino más corto en forma paramétrica

Como en «El formalismo lagrangiano: ejemplos matemáticos», los caminos son curvas regulares $\vec{f} = (f_1, f_2): [a, b] \to \mathbb{R}^2$, con $\vec{f}' \neq \vec{0}$, y

$$
\begin{aligned}
\bsL = |\vec{f}'| = \sqrt{f'^2_1 + f'^2_2}, \qquad p_i = \dfrac{f'_i}{|\vec{f}'|} = u_i,
\end{aligned}
$$

donde $\vec{u} := \dfrac{\vec{f}'}{|\vec{f}'|}$ es el vector tangente unitario. Tres familias continuas de transformaciones del plano conservan las longitudes: las traslaciones en cada eje y los giros alrededor del origen. Además, la longitud no depende de la parametrización.

### Traslaciones

**1.** $\vec{f} \to \vec{f} + \epsilon \cdot \vec{e}_k$, con $k = 1$ o $k = 2$. Generador $\vec{\xi} = \vec{e}_k$.

**2.** $\bsL$ no depende de $\vec{f}$: simetría con $F = 0$.

**3.** Se conserva $Q_k = p_k = u_k$. Con las dos traslaciones, el vector tangente unitario $\vec{u}$ es constante.

**4.** Es la conclusión de «El formalismo lagrangiano: ejemplos matemáticos», que allí se obtenía de las ecuaciones de Euler–Lagrange: la curva recorre un segmento, $\vec{f}_0(x) = \vec{A} + s(x) \cdot \vec{u}$, con $s(x)$ la longitud recorrida desde $\vec{A}$.

### El giro alrededor del origen

**1.** El giro de ángulo $\epsilon$ es $(f_1, f_2) \to (f_1 \cdot \cos\epsilon - f_2 \cdot \sin\epsilon,\ f_1 \cdot \sin\epsilon + f_2 \cdot \cos\epsilon)$. Como en la parte matemática, su generador es $\vec{\xi} = (-f_2, f_1)$, con $\vec{\xi}' = (-f'_2, f'_1)$.

**2.** $\bsL$ no depende de $\vec{f}$, y

$$
\begin{aligned}
\bsdelta_{\vec{\xi}} \bsL = p_1 \cdot (-f'_2) + p_2 \cdot f'_1 = \dfrac{-f'_1 \cdot f'_2 + f'_2 \cdot f'_1}{|\vec{f}'|} = 0.
\end{aligned}
$$

Es una simetría con $F = 0$: girar una curva no cambia su longitud.

**3.** Se conserva

$$
\begin{aligned}
Q_{\mathrm{giro}} = p_1 \cdot (-f_2) + p_2 \cdot f_1 = f_1 \cdot u_2 - f_2 \cdot u_1.
\end{aligned}
$$

**4.** Sobre la solución, $\vec{f}_0 = \vec{A} + s \cdot \vec{u}$ con $\vec{u}$ constante:

$$
\begin{aligned}
Q_{\mathrm{giro}} = (A_1 + s \cdot u_1) \cdot u_2 - (A_2 + s \cdot u_2) \cdot u_1 = A_1 \cdot u_2 - A_2 \cdot u_1,
\end{aligned}
$$

que no depende de $s$. Su significado: $|A_1 \cdot u_2 - A_2 \cdot u_1|$ es el área del paralelogramo de lados $\vec{A}$ y $\vec{u}$, y como $|\vec{u}| = 1$, es la altura de ese paralelogramo sobre el lado $\vec{u}$, es decir, la **distancia del origen a la recta** que contiene el segmento. El signo indica a qué lado de la recta queda el origen.

### Las cantidades conservadas determinan la recta

Una recta del plano queda determinada por dos números: el ángulo de su dirección y su distancia al origen, con signo. Las traslaciones dan la dirección, $\vec{u}$, y el giro, la distancia. Las tres cantidades conservadas determinan, por tanto, la recta que contiene la solución, sin resolver ninguna ecuación de segundo orden. Los extremos $\vec{A}$ y $\vec{B}$ eligen después el segmento.

Las tres no son independientes: $u_1^2 + u_2^2 = 1$. Tres parámetros de simetría dan tres cantidades conservadas, pero eso no garantiza que sean funcionalmente independientes.

### El cambio de parámetro: una relación entre las ecuaciones

La longitud tampoco depende de cómo se recorre la curva. En la parte matemática («Transformaciones que también mueven la variable») se ha visto que, como $\bsL$ no depende de $x$ y es homogénea de grado $1$ en $\vec{f}'$ ($|\lambda \cdot \vec{f}'| = \lambda \cdot |\vec{f}'|$ para $\lambda > 0$):

* $\bsH = \sum_i p_i \cdot f'_i - \bsL = \dfrac{f'^2_1 + f'^2_2}{|\vec{f}'|} - |\vec{f}'| = 0$ para toda curva;
* el cambio de parámetro $\tilde{x} = x + \epsilon \cdot \tau(x)$, con $\vec{\xi} = \vec{0}$, es una simetría con $F = 0$ para **toda** función $\tau$ de clase $C^1$;
* su cantidad conservada, $Q = -\tau \cdot \bsH$, es idénticamente nula.

El teorema no da aquí información. La identidad de Noether, en cambio, sí. Con el generador a variable fija, $\bar{\xi}_i = -\tau \cdot f'_i$, y $\bar{F} = -\tau \cdot \bsL$, dice que, para toda curva,

$$
\begin{aligned}
\dfrac{d}{dx}\left( -\tau \cdot \sum_{i=1}^{2} p_i \cdot f'_i + \tau \cdot \bsL \right) = \sum_{i=1}^{2} \varphi_i \cdot \tau \cdot f'_i.
\end{aligned}
$$

El lado izquierdo es $\dfrac{d}{dx}(-\tau \cdot \bsH) = 0$. Como $\tau$ es arbitraria, tomando $\tau = 1$ queda

$$
\begin{aligned}
f'_1 \cdot \varphi_1 + f'_2 \cdot \varphi_2 = 0 \quad \text{para toda curva regular}.
\end{aligned}
$$

Las dos ecuaciones de Euler–Lagrange no son independientes: si $\varphi_1 = 0$ en un punto donde $f'_2 \neq 0$, también $\varphi_2 = 0$ en ese punto, y al revés. Es la observación de «El formalismo lagrangiano: ejemplos matemáticos» («Infinitas soluciones con la misma imagen»), que allí se comprobaba con la matriz $W$ y aquí aparece como consecuencia de una simetría. Una simetría que depende de una función arbitraria no da una cantidad conservada, sino una relación entre las ecuaciones. Es la situación que generaliza el segundo teorema de Noether, y la que se da en la relatividad general con los cambios de coordenadas («El contexto histórico»).

## Ejemplo: ecuaciones con la estructura de las de Newton

Como en «El formalismo lagrangiano: ejemplos matemáticos», la variable se llama $t$, recorre $[t_1, t_2]$, $\dot{f}_i := \dfrac{df_i}{dt}$, y

$$
\begin{aligned}
\bsL(\vec{f}, \dot{\vec{f}}, t) = \dfrac{1}{2} \cdot \sum_{i=1}^{n} \dot{f}_i^2 - V(\vec{f}), \qquad p_i = \dot{f}_i,
\end{aligned}
$$

con $V$ de clase $C^2$. Las ecuaciones de Euler–Lagrange son $\ddot{f}_i = -\partial_{f_i} V$.

### La traslación de la variable: la energía

$\bsL$ no depende explícitamente de $t$, y por la identidad de Beltrami se conserva

$$
\begin{aligned}
\bsH = \sum_{i=1}^{n} \dot{f}_i \cdot \dot{f}_i - \bsL = \dfrac{1}{2} \cdot \sum_{i=1}^{n} \dot{f}_i^2 + V(\vec{f}).
\end{aligned}
$$

En «El formalismo lagrangiano: ejemplos matemáticos» esta cantidad se obtenía multiplicando cada ecuación por $\dot{f}_{0,i}$ y sumando. Ahora se ve de dónde procede: de que $\bsL$ no depende de $t$.

### Una componente que no aparece

Si $V$ no depende de $f_k$, $\bsL$ tampoco, y se conserva $p_k = \dot{f}_k$: la componente $k$ varía de forma lineal en $t$.

### Los giros: el momento angular sin masa

Supongamos que $V$ solo depende de la distancia al origen, $V(\vec{f}) = W(|\vec{f}|)$ con $W$ de clase $C^2$ en $(0, \infty)$, y que las soluciones no pasan por el origen.

**1.** Para cada par de componentes $j < k$, el giro en el plano de $f_j$ y $f_k$ tiene, como en la parte matemática, el generador $\xi_j = -f_k$, $\xi_k = f_j$ y las demás componentes nulas.

**2.** La parte de $\dot{\vec{f}}$ da $p_j \cdot \dot{\xi}_j + p_k \cdot \dot{\xi}_k = \dot{f}_j \cdot (-\dot{f}_k) + \dot{f}_k \cdot \dot{f}_j = 0$. La de $V$, con $\partial_{f_i} W(|\vec{f}|) = W'(|\vec{f}|) \cdot \dfrac{f_i}{|\vec{f}|}$:

$$
\begin{aligned}
-\partial_{f_j} V \cdot \xi_j - \partial_{f_k} V \cdot \xi_k = -\dfrac{W'(|\vec{f}|)}{|\vec{f}|} \cdot \big(f_j \cdot (-f_k) + f_k \cdot f_j\big) = 0.
\end{aligned}
$$

Es una simetría con $F = 0$.

**3.** Se conserva

$$
\begin{aligned}
Q_{jk} = p_j \cdot (-f_k) + p_k \cdot f_j = f_j \cdot \dot{f}_k - f_k \cdot \dot{f}_j.
\end{aligned}
$$

**4.** Comprobación directa: $\dot{Q}_{jk} = \dot{f}_j \cdot \dot{f}_k + f_j \cdot \ddot{f}_k - \dot{f}_k \cdot \dot{f}_j - f_k \cdot \ddot{f}_j = -\dfrac{W'(|\vec{f}|)}{|\vec{f}|} \cdot (f_j \cdot f_k - f_k \cdot f_j) = 0$.

Hay un giro por cada plano de coordenadas, es decir, $\dfrac{n \cdot (n - 1)}{2}$ cantidades. Con $n = 3$ son tres, las componentes de $\vec{f} \times \dot{\vec{f}}$: el momento angular de la parte física, todavía sin la masa.

## Ejemplo: la ecuación de Laplace

Como en «El formalismo lagrangiano: ejemplos matemáticos», $t$ es aquí una segunda coordenada del plano, no el tiempo, y $f(x, t)$ describe una membrana casi plana sobre el rectángulo $\Omega$, con

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot \left((\partial_x f)^2 + (\partial_t f)^2\right), \qquad u_x = \partial_{\partial_x f} \bsL = \partial_x f, \qquad u_t = \partial_{\partial_t f} \bsL = \partial_t f.
\end{aligned}
$$

La ecuación de Euler–Lagrange es la de Laplace, $\partial^2_x f + \partial^2_t f = 0$. Aplicamos el teorema de varias variables de la parte matemática, con $m = 2$ y $n = 1$.

### El desplazamiento de la altura

$f \to f + \epsilon$ tiene generador $\xi = 1$. Como $\bsL$ no depende de $f$, $\bsdelta_{\xi} \bsL = 0$: simetría con $F_x = F_t = 0$. La corriente conservada es $(Q_x, Q_t) = (\partial_x f, \partial_t f) = \nabla f$, y la ley de conservación,

$$
\begin{aligned}
\partial_x Q_x + \partial_t Q_t = \partial^2_x f + \partial^2_t f = 0,
\end{aligned}
$$

es la propia ecuación de Laplace. Ocurre siempre que $\bsL$ no depende de $f$: la ecuación de Euler–Lagrange ya es una ley de conservación. Integrada sobre un rectángulo contenido en $\Omega$, como en la parte matemática, dice que el flujo de $\nabla f$ a través de su borde es nulo.

### El desplazamiento en $x$

**1.** $f(x, t) \to f(x + \epsilon, t)$ tiene generador $\xi = \partial_x f$.

**2.** Por la regla de la cadena, como $\bsL$ no depende explícitamente de $x$,

$$
\begin{aligned}
\bsdelta_{\xi} \bsL = u_x \cdot \partial_x(\partial_x f) + u_t \cdot \partial_t(\partial_x f) = \partial_x f \cdot \partial^2_x f + \partial_t f \cdot \partial^2_{tx} f = \partial_x\big[\bsL\big],
\end{aligned}
$$

donde $\partial_x[\bsL]$ es la derivada de la función compuesta. Es una simetría con $F_x = \bsL$ y $F_t = 0$.

**3.** La corriente conservada es

$$
\begin{aligned}
Q_x = u_x \cdot \partial_x f - \bsL = \dfrac{1}{2} \cdot \left((\partial_x f)^2 - (\partial_t f)^2\right), \qquad Q_t = u_t \cdot \partial_x f = \partial_t f \cdot \partial_x f.
\end{aligned}
$$

**4.** Comprobación directa, con el teorema de Schwarz para $\partial^2_{tx} f = \partial^2_{xt} f$:

$$
\begin{aligned}
\partial_x Q_x + \partial_t Q_t &= \partial_x f \cdot \partial^2_x f - \partial_t f \cdot \partial^2_{xt} f + \partial^2_t f \cdot \partial_x f + \partial_t f \cdot \partial^2_{tx} f \\
&= \partial_x f \cdot \left(\partial^2_x f + \partial^2_t f\right),
\end{aligned}
$$

que es nulo sobre las soluciones. A diferencia del caso anterior, esta ley no es la ecuación de Euler–Lagrange, sino una consecuencia nueva de ella. El desplazamiento en $t$ da, del mismo modo, una segunda corriente.
