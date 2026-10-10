---
author: "Julián Calderón Almendros"
---

# El teorema de Noether: ejemplos matemáticos (versión 2)

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-10
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

Ejemplos de «El teorema de Noether: parte matemática (versión 2)», a la que llamamos aquí la parte matemática; sus apartados se citan como «parte matemática, apartado 6.5». Son los funcionales de «El formalismo lagrangiano: ejemplos matemáticos»: allí se resolvían las ecuaciones de Euler–Lagrange; aquí se buscan sus simetrías y se comprueba que las cantidades conservadas dan la misma solución, o parte de ella, sin resolver ecuaciones de segundo orden. En cada ejemplo se siguen los mismos pasos:

1. elegir una familia de transformaciones $\Phi_\varepsilon$ de los puntos y calcular su generador $(\tau, \xi)$;
2. calcular $D$ con la forma de cuatro términos (parte matemática, apartado 5) y ver si es una derivada total $\dfrac{dF}{dx}$;
3. si lo es, escribir la cantidad conservada $Q = p \cdot \xi - \tau \cdot \bsH - F$;
4. comprobarla con la solución conocida.

La versión 2 de la serie consta de cuatro documentos:

* «El teorema de Noether: parte matemática (versión 2)»: la teoría, con una función, varias funciones y varias variables, los flujos, las derivadas de Fréchet y de Lie, y una guía de dimensión infinita.
* «El teorema de Noether: ejemplos matemáticos (versión 2)»: el camino más corto, como gráfica y en forma paramétrica, las ecuaciones con la estructura de las de Newton y la ecuación de Laplace.
* «El teorema de Noether: parte física (versión 2)»: los sistemas de partículas, el grupo de Galileo, el grupo de Lorentz y el de Poincaré, y la mecánica cuántica no relativista.
* «El teorema de Noether: ejemplos físicos (versión 2)» (en preparación).

**Diferencias con la versión 1**, cuyos documentos se conservan. La versión 1 escribe la familia de transformaciones $\bsT_\epsilon$, con el parámetro $\epsilon$, y usa generadores que pueden depender de las derivadas. La versión 2 usa $\Phi_\varepsilon$ y $\varepsilon$, como el trabajo «La importancia de las simetrías en física», y transformaciones de los puntos con generador $(\tau, \xi)$; la relación entre las dos formas está en el apartado 9.6 de la parte matemática.

## 1. El camino más corto como gráfica

El funcional de la longitud de la gráfica de $f$, el del camino más corto entre dos puntos de «El formalismo lagrangiano: ejemplos matemáticos», tiene tres simetrías continuas: familias de un parámetro real que cumplen la condición del apartado 4 de la parte matemática, a diferencia de una simetría discreta, como la reflexión $(x, y) \mapsto (x, -y)$, que no forma parte de ninguna familia continua que empiece en la identidad. Una de ellas, el giro, mueve también la variable ($\tau \neq 0$), así que necesita el caso general del apartado 6.5 de la parte matemática. Con las tres cantidades conservadas se determina la recta sin resolver la ecuación de segundo orden.

### 1.1. El lagrangiano y sus funciones

$$
\begin{aligned}
\bsL(y, y', x) = \sqrt{1 + y'^2}.
\end{aligned}
$$

A lo largo de $f$:

$$
\begin{aligned}
p = \dfrac{f'}{\sqrt{1 + f'^2}}, \qquad \bsH = p \cdot f' - \bsL = \dfrac{f'^2 - (1 + f'^2)}{\sqrt{1 + f'^2}} = -\dfrac{1}{\sqrt{1 + f'^2}}.
\end{aligned}
$$

Con el ángulo $\alpha \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$ que forma la tangente con el eje $x$, $f' = \tan\alpha$, se tiene $p = \sin\alpha$ y $\bsH = -\cos\alpha$.

### 1.2. Las tres simetrías

En los tres casos se usan la cantidad conservada $Q = p \cdot \xi - \tau \cdot \bsH - F$ y el lema $D = \partial_f \bsL \cdot \bar{\xi} + p \cdot \bar{\xi}' + (\tau \cdot \bsL)'$, con $\bar{\xi} = \xi - \tau \cdot f'$ (parte matemática, apartado 6.5).

| Transformación | $(\tau, \xi)$ | $D$ | $F$ | $Q$ |
| ------------------------------ | ------------ | -------------------- | ------ | -------------------------- |
| Desplazamiento vertical | $(0, 1)$ | $\partial_y \bsL = 0$ | $0$ | $p = \sin\alpha$ |
| Desplazamiento horizontal | $(1, 0)$ | $\partial_x \bsL = 0$ | $0$ | $-\bsH = \cos\alpha$ |
| Giro alrededor del origen | $(-y, x)$ | $0$ | $0$ | $\dfrac{x \cdot f' - f}{\sqrt{1 + f'^2}}$ |

* **Desplazamientos.** $\bsL$ no depende de $y$ ni explícitamente de $x$, así que $D = 0$ y $F = 0$.
* **Giro.** El giro de ángulo $\varepsilon$ lleva $(x, y)$ a $(x \cdot \cos\varepsilon - y \cdot \sin\varepsilon,\ x \cdot \sin\varepsilon + y \cdot \cos\varepsilon)$, y a primer orden $(\tau, \xi) = (-y, x)$. A lo largo de $f$, $\bar{\xi} = x + f \cdot f'$ y $\bar{\xi}' = 1 + f'^2 + f \cdot f''$. Como $\partial_f \bsL = 0$:

  $$
  \begin{aligned}
  p \cdot \bar{\xi}' &= f' \cdot \sqrt{1 + f'^2} + \dfrac{f \cdot f' \cdot f''}{\sqrt{1 + f'^2}}, \\
  (\tau \cdot \bsL)' &= \big(-f \cdot \sqrt{1 + f'^2}\big)' = -f' \cdot \sqrt{1 + f'^2} - \dfrac{f \cdot f' \cdot f''}{\sqrt{1 + f'^2}}.
  \end{aligned}
  $$

  La suma es nula: $D = 0$ y $F = 0$. Es la expresión de que la longitud no cambia al girar. La cantidad conservada es $Q = p \cdot x - (-f) \cdot \bsH = p \cdot x + f \cdot \bsH$, la de la tabla.

### 1.3. Lo que se obtiene

1. **La recta, sin resolver la ecuación.** La primera fila dice que la pendiente es constante: como $u \mapsto \dfrac{u}{\sqrt{1 + u^2}}$ es estrictamente creciente, $p$ constante implica $f'$ constante, y la gráfica es una recta.
2. **La recta concreta, con el giro.** Sobre la recta $f(x) = \kappa \cdot x + \lambda$, con pendiente $\kappa$ y ordenada en el origen $\lambda$,

   $$
   \begin{aligned}
   Q_{\mathrm{giro}} = \dfrac{x \cdot \kappa - (\kappa \cdot x + \lambda)}{\sqrt{1 + \kappa^2}} = -\dfrac{\lambda}{\sqrt{1 + \kappa^2}}.
   \end{aligned}
   $$

   Su valor absoluto, $\dfrac{|\lambda|}{\sqrt{1 + \kappa^2}}$, es la distancia del origen a la recta, y su signo es positivo si la recta pasa por debajo del origen ($\lambda < 0$). La pendiente y la distancia al origen determinan la recta; los extremos eligen después el segmento. Es el mismo resultado que el del camino más corto en forma paramétrica (apartado 2.2). Allí hacía falta una curva con dos componentes para tratar el giro; aquí basta una función, porque el giro mueve también la variable.
3. **Dos cantidades que no son independientes.** $p^2 + \bsH^2 = \dfrac{f'^2 + 1}{1 + f'^2} = 1$ para **toda** $f$, no solo para las soluciones: los dos desplazamientos dan la misma información, $\sin^2\alpha + \cos^2\alpha = 1$. Tres simetrías dan tres cantidades conservadas, pero no tres datos independientes.
4. **Un ejemplo que no es simetría: la homotecia.** $\Phi_\varepsilon(x, y) = \big((1 + \varepsilon) \cdot x, (1 + \varepsilon) \cdot y\big)$, con $(\tau, \xi) = (x, y)$, multiplica la longitud por $1 + \varepsilon$. Entonces $D = \bsL = \sqrt{1 + y'^2}$, que no es afín en $y'$, y no existe $F$ (parte matemática, apartado 5, punto (3)).

### 1.4. Una precisión: el giro solo vale para ángulos pequeños

El giro de una gráfica solo es otra gráfica si $\varepsilon$ es pequeño: con giros grandes, la curva girada puede tener tramos verticales o volver hacia atrás. Es la condición $|\varepsilon| \ll 1$ del apartado 3.1 de la parte matemática, que exige que $\tilde{x}(x) = x - \varepsilon \cdot f(x) + O(\varepsilon^2)$ siga siendo creciente. Todo el razonamiento es local en $\varepsilon$, y para el teorema basta, porque solo usa el primer orden.

## 2. El camino más corto en forma paramétrica

Los caminos son curvas $\vec{f} = (f_1, f_2): [a, b] \to \mathbb{R}^2$ de clase $C^2$ y **regulares**, con $\vec{f}' \neq \vec{0}$ en todo punto, como en «El formalismo lagrangiano: ejemplos matemáticos». Es el apartado 7 de la parte matemática con $n = 2$:

$$
\begin{aligned}
\bsL(\vec{y}, \vec{y}', x) = |\vec{y}'| = \sqrt{y_1'^2 + y_2'^2}, \qquad p_i = \dfrac{f'_i}{|\vec{f}'|} = w_i,
\end{aligned}
$$

donde $\vec{w} := \dfrac{\vec{f}'}{|\vec{f}'|}$ es el vector tangente unitario. Las traslaciones y los giros del plano de los valores conservan las longitudes y no mueven la variable ($\tau = 0$); el cambio de parámetro solo mueve la variable.

### 2.1. Traslaciones

* **La familia.** La traslación en la dirección del eje $k$, con $k = 1$ o $k = 2$, es $\Phi_\varepsilon(x, \vec{y}) = (x, \vec{y} + \varepsilon \cdot \vec{e}_k)$, con $\vec{e}_k$ el vector con un $1$ en el lugar $k$ y $0$ en el otro. Su generador es $\tau = 0$ y $\vec{\xi} = \vec{e}_k$.
* **Simetría.** $\bsL$ no depende de $\vec{y}$, así que $D = \partial_{y_k} \bsL = 0$: es una simetría con $F = 0$.
* **Cantidad conservada.** $Q_k = p_k = w_k$. Con las dos traslaciones, el vector tangente unitario $\vec{w}$ es constante.
* **Comprobación.** Es la conclusión de «El formalismo lagrangiano: ejemplos matemáticos», que allí se obtenía de las ecuaciones de Euler–Lagrange: la curva recorre un segmento, $\vec{f}_0(x) = \vec{A} + s(x) \cdot \vec{w}$, con $\vec{A}$ el punto inicial y $s(x)$ la longitud recorrida desde él.

### 2.2. El giro alrededor del origen

* **La familia.** El giro de ángulo $\varepsilon$ de los valores, $\Phi_\varepsilon(x, y_1, y_2) = (x,\ y_1 \cdot \cos\varepsilon - y_2 \cdot \sin\varepsilon,\ y_1 \cdot \sin\varepsilon + y_2 \cdot \cos\varepsilon)$, tiene el generador $\tau = 0$ y $\vec{\xi} = (-y_2, y_1)$, como en la parte matemática, apartado 3.2.
* **Simetría.** $\bsL$ no depende de $\vec{y}$, y a lo largo de $\vec{f}$, $\vec{\xi}' = (-f'_2, f'_1)$:

  $$
  \begin{aligned}
  D = p_1 \cdot (-f'_2) + p_2 \cdot f'_1 = \dfrac{-f'_1 \cdot f'_2 + f'_2 \cdot f'_1}{|\vec{f}'|} = 0.
  \end{aligned}
  $$

  Es una simetría con $F = 0$: girar una curva no cambia su longitud.
* **Cantidad conservada.**

  $$
  \begin{aligned}
  Q_{\mathrm{giro}} = p_1 \cdot (-f_2) + p_2 \cdot f_1 = f_1 \cdot w_2 - f_2 \cdot w_1.
  \end{aligned}
  $$

* **Comprobación.** Sobre la solución, $\vec{f}_0 = \vec{A} + s \cdot \vec{w}$ con $\vec{w}$ constante,

  $$
  \begin{aligned}
  Q_{\mathrm{giro}} = (A_1 + s \cdot w_1) \cdot w_2 - (A_2 + s \cdot w_2) \cdot w_1 = A_1 \cdot w_2 - A_2 \cdot w_1,
  \end{aligned}
  $$

  que no depende de $s$. Su valor absoluto es el área del paralelogramo de lados $\vec{A}$ y $\vec{w}$, y como $|\vec{w}| = 1$, es la altura de ese paralelogramo sobre el lado $\vec{w}$: la **distancia del origen a la recta** que contiene el segmento. El signo indica a qué lado de la recta queda el origen.

### 2.3. Las cantidades conservadas determinan la recta

Una recta del plano queda determinada por dos números: el ángulo de su dirección y su distancia al origen, con signo. Las traslaciones dan la dirección, $\vec{w}$, y el giro, la distancia. Las tres cantidades conservadas determinan, por tanto, la recta que contiene la solución, sin resolver ninguna ecuación de segundo orden; los extremos eligen después el segmento.

Las tres no son independientes: $w_1^2 + w_2^2 = 1$ para toda curva. Tres parámetros de simetría dan tres cantidades conservadas, pero eso no garantiza que den tres datos independientes.

### 2.4. El cambio de parámetro: una relación entre las ecuaciones

La longitud tampoco depende de cómo se recorre la curva. El cambio de parámetro $\tilde{x} = x + \varepsilon \cdot \tau(x)$, con $\vec{\xi} = \vec{0}$ y $\tau$ una función **cualquiera** de clase $C^1$, es una transformación de los puntos que solo mueve la variable.

* **$\bsH = 0$ para toda curva**, porque $\bsH = \sum_i p_i \cdot f'_i - \bsL = \dfrac{f'^2_1 + f'^2_2}{|\vec{f}'|} - |\vec{f}'| = 0$.
* **Es una simetría para toda $\tau$.** La forma de cuatro términos (parte matemática, apartado 5) da $D = \sum_i p_i \cdot \big(-\tau' \cdot f'_i\big) + \bsL \cdot \tau' = -\tau' \cdot \bsH = 0$, así que $F = 0$.
* **El teorema no da información**: la cantidad conservada, $Q = -\tau \cdot \bsH$, es nula para toda curva.
* **La identidad sí la da.** Con $\vec{\xi} = \vec{0}$, $F = 0$ y $Q = 0$, la identidad de Noether de la parte matemática, apartado 7.4, dice que, para toda $\tau$ y toda curva regular,

  $$
  \begin{aligned}
  0 = -\sum_{i=1}^{2} \varphi_i \cdot \big(0 - \tau \cdot f'_i\big) = \tau \cdot \big(f'_1 \cdot \varphi_1 + f'_2 \cdot \varphi_2\big).
  \end{aligned}
  $$

  Con $\tau = 1$, $f'_1 \cdot \varphi_1 + f'_2 \cdot \varphi_2 = 0$ para toda curva regular.
* **Consecuencia.** Las dos ecuaciones de Euler–Lagrange no son independientes: si $\varphi_1 = 0$ en un punto donde $f'_2 \neq 0$, también $\varphi_2 = 0$ en ese punto, y al revés. Es la observación de «El formalismo lagrangiano: ejemplos matemáticos» («Infinitas soluciones con la misma imagen»), que allí se comprobaba con la matriz $W$ y aquí aparece como consecuencia de una simetría. Una simetría que depende de una función arbitraria no da una cantidad conservada, sino una relación entre las ecuaciones: es la situación del segundo teorema de Noether (parte matemática, apartado 7.5). Es también la de la relatividad general, la teoría de la gravitación de Einstein, cuyas ecuaciones no cambian con los cambios de coordenadas del espacio y del tiempo («El contexto histórico»).

### 2.5. Cualquier lagrangiano homogéneo de grado 1

Supongamos que $\bsL$ no depende de $x$ y que $\bsL(\vec{y}, \lambda \cdot \vec{y}') = \lambda \cdot \bsL(\vec{y}, \vec{y}')$ para todo $\lambda > 0$, en los puntos con $\vec{y}' \neq \vec{0}$. Derivando esta igualdad respecto de $\lambda$ en $\lambda = 1$ (el teorema de Euler de las funciones homogéneas, Tema 1, apartado 7.1) se obtiene $\sum_i y'_i \cdot \partial_{y'_i} \bsL = \bsL$, es decir, $\bsH = 0$ para toda $\vec{f}$. Con $\vec{\xi} = \vec{0}$ y $\tau(x)$ cualquiera, la forma de cuatro términos da $D = \sum_i p_i \cdot \big(-\tau' \cdot f'_i\big) + \bsL \cdot \tau' = -\tau' \cdot \bsH = 0$, y se llega a la misma relación, $\sum_i f'_i \cdot \varphi_i = 0$. Les ocurre a todos los funcionales que no dependen de la parametrización de la curva. Dos ejemplos:

* **La longitud de una curva sobre una superficie.** Con coordenadas $(y_1, y_2)$ sobre la superficie, la longitud es $\int \sqrt{\sum_{i,j} g_{ij}(\vec{y}) \cdot y_i' \cdot y_j'} \,dx$, donde las funciones $g_{ij}$ (la **métrica** de la superficie) dan el cuadrado de la longitud de un vector tangente a partir de sus componentes. Las curvas que hacen estacionaria la longitud se llaman **geodésicas**; en el plano son las rectas.
* **El principio de Fermat.** La luz sigue una trayectoria que hace estacionario el tiempo de recorrido, que es proporcional a $\int n_{\mathrm{r}}(\vec{y}) \cdot |\vec{y}'| \,dx$, donde $n_{\mathrm{r}}$, el **índice de refracción** del medio, es el cociente entre la velocidad de la luz en el vacío y en el medio. Lo escribimos $n_{\mathrm{r}}$ para no confundirlo con el número de funciones, $n$.

## 3. Ecuaciones con la estructura de las de Newton

Como en «El formalismo lagrangiano: ejemplos matemáticos», la variable se llama $t$ y recorre $[a, b]$, el punto indica la derivada respecto de $t$ (la prima de la parte matemática), y

$$
\begin{aligned}
\bsL(\vec{y}, \dot{\vec{y}}, t) = \dfrac{1}{2} \cdot \sum_{i=1}^{n} \dot{y}_i^2 - V(\vec{y}), \qquad p_i = \dot{f}_i,
\end{aligned}
$$

con $V$ de clase $C^2$. Las ecuaciones de Euler–Lagrange son $\ddot{f}_i = -\partial_{y_i} V$: tienen la forma de las de Newton con masa $1$ y fuerza $-\partial_{y_i} V$.

### 3.1. La traslación en el tiempo: la energía

* **La familia.** $\Phi_\varepsilon(t, \vec{y}) = (t + \varepsilon, \vec{y})$, con $\tau = 1$ y $\vec{\xi} = \vec{0}$.
* **Simetría.** Por la forma de cuatro términos, $D = \partial_t \bsL = 0$, porque $\bsL$ no depende explícitamente de $t$; así que $F = 0$.
* **Cantidad conservada.** $Q = -\bsH$, con

  $$
  \begin{aligned}
  \bsH = \sum_{i=1}^{n} \dot{f}_i \cdot \dot{f}_i - \bsL = \dfrac{1}{2} \cdot \sum_{i=1}^{n} \dot{f}_i^2 + V(\vec{f}).
  \end{aligned}
  $$

  Es la identidad de Beltrami (parte matemática, apartado 6.7). En «El formalismo lagrangiano: ejemplos matemáticos» esta cantidad se obtenía multiplicando cada ecuación por $\dot{f}_{0,i}$ y sumando; ahora se ve de dónde procede: de que $\bsL$ no depende de $t$.

### 3.2. Una componente que no aparece

Si $V$ no depende de $y_k$, $\bsL$ tampoco: la traslación $\vec{\xi} = \vec{e}_k$, con $\tau = 0$, es una simetría con $F = 0$, y se conserva $p_k = \dot{f}_k$. La componente $k$ varía de forma lineal en $t$: $y_k$ es una coordenada cíclica (parte matemática, apartado 6.7).

### 3.3. Los giros: el momento angular sin masa

Supongamos que $V$ solo depende de la distancia al origen, $V(\vec{y}) = U(|\vec{y}|)$, con $U$ de clase $C^2$ en $(0, \infty)$, y que las soluciones no pasan por el origen.

* **La familia.** Para cada par de componentes $j < k$, el giro en el plano de $y_j$ e $y_k$ tiene el generador $\tau = 0$, $\xi_j = -y_k$, $\xi_k = y_j$ y las demás componentes nulas (parte matemática, apartado 7.5).
* **Simetría.** La parte cinética da $p_j \cdot \dot{\xi}_j + p_k \cdot \dot{\xi}_k = \dot{f}_j \cdot (-\dot{f}_k) + \dot{f}_k \cdot \dot{f}_j = 0$. La del potencial, con $\partial_{y_i} U(|\vec{y}|) = U'(|\vec{y}|) \cdot \dfrac{y_i}{|\vec{y}|}$:

  $$
  \begin{aligned}
  -\partial_{y_j} V \cdot \xi_j - \partial_{y_k} V \cdot \xi_k = -\dfrac{U'(|\vec{f}|)}{|\vec{f}|} \cdot \big(f_j \cdot (-f_k) + f_k \cdot f_j\big) = 0.
  \end{aligned}
  $$

  Es una simetría con $F = 0$.
* **Cantidad conservada.**

  $$
  \begin{aligned}
  Q_{jk} = p_j \cdot (-f_k) + p_k \cdot f_j = f_j \cdot \dot{f}_k - f_k \cdot \dot{f}_j.
  \end{aligned}
  $$

* **Comprobación directa.** Con las ecuaciones de Euler–Lagrange, $\dot{Q}_{jk} = \dot{f}_j \cdot \dot{f}_k + f_j \cdot \ddot{f}_k - \dot{f}_k \cdot \dot{f}_j - f_k \cdot \ddot{f}_j = -\dfrac{U'(|\vec{f}|)}{|\vec{f}|} \cdot (f_j \cdot f_k - f_k \cdot f_j) = 0$.

Hay un giro por cada plano de coordenadas, es decir, $\dfrac{n \cdot (n - 1)}{2}$ cantidades. Con $n = 3$ son tres, las componentes del producto vectorial $\vec{f} \times \dot{\vec{f}}$: el momento angular de la parte física, todavía sin la masa.

## 4. La ecuación de Laplace

Dos variables, $(x_1, x_2)$ en una caja $\Omega$ del plano, y una función $f(x_1, x_2)$: la altura de una membrana casi plana. En «El formalismo lagrangiano: ejemplos matemáticos» las variables se llamaban $x$ y $t$, pero $t$ no era el tiempo. Es el apartado 8 de la parte matemática con $n = 1$ y $m = 2$; con una sola función omitimos el índice $i$:

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot \big((\partial_1 f)^2 + (\partial_2 f)^2\big), \qquad u_1 = \partial_1 f, \qquad u_2 = \partial_2 f.
\end{aligned}
$$

La expresión de Euler–Lagrange es $\varphi = -\big(\partial_1^2 f + \partial_2^2 f\big)$, y la ecuación, la de **Laplace**, $\partial_1^2 f + \partial_2^2 f = 0$. El tensor de energía-momento (parte matemática, apartado 8.6) es

$$
\begin{aligned}
T_{11} = -T_{22} = \dfrac{1}{2} \cdot \big((\partial_1 f)^2 - (\partial_2 f)^2\big), \qquad T_{12} = T_{21} = \partial_1 f \cdot \partial_2 f.
\end{aligned}
$$

### 4.1. El desplazamiento de la altura

* **La familia.** $\Phi_\varepsilon(\vec{x}, y) = (\vec{x}, y + \varepsilon)$, con $\vec{\tau} = \vec{0}$ y $\xi = 1$. Como $\bsL$ no depende de $y$, $D = 0$: es una simetría con $\vec{F} = \vec{0}$.
* **Corriente.** $Q_k = u_k$, es decir, $\vec{Q} = (\partial_1 f, \partial_2 f)$, el gradiente de $f$.
* **Ley de conservación.** $d_{x_1} Q_1 + d_{x_2} Q_2 = \partial_1^2 f + \partial_2^2 f = 0$ es la propia ecuación de Laplace. Ocurre siempre que $\bsL$ no depende de $y$: la ecuación de Euler–Lagrange ya es una ley de conservación. Integrada sobre una subcaja, como en la parte matemática, apartado 8.4, dice que el flujo del gradiente de $f$ a través de su frontera es nulo.

### 4.2. La traslación en $x_1$

* **La familia.** $\Phi_\varepsilon(x_1, x_2, y) = (x_1 + \varepsilon, x_2, y)$, con $\vec{\tau} = (1, 0)$ y $\xi = 0$. Por la forma de cuatro términos, $D = \partial_{x_1} \bsL = 0$: simetría con $\vec{F} = \vec{0}$.
* **Corriente.** $Q_k = -T_{k1}$:

  $$
  \begin{aligned}
  Q_1 = -\dfrac{1}{2} \cdot \big((\partial_1 f)^2 - (\partial_2 f)^2\big), \qquad Q_2 = -\partial_2 f \cdot \partial_1 f.
  \end{aligned}
  $$

* **Comprobación directa**, con el teorema de Schwarz para $\partial_1 \partial_2 f = \partial_2 \partial_1 f$:

  $$
  \begin{aligned}
  d_{x_1} Q_1 + d_{x_2} Q_2 &= -\partial_1 f \cdot \partial_1^2 f + \partial_2 f \cdot \partial_1 \partial_2 f - \partial_2^2 f \cdot \partial_1 f - \partial_2 f \cdot \partial_2 \partial_1 f \\
  &= -\partial_1 f \cdot \big(\partial_1^2 f + \partial_2^2 f\big),
  \end{aligned}
  $$

  que es $-\varphi \cdot \bar{\xi}$ con $\bar{\xi} = -\partial_1 f$, y se anula sobre las soluciones. A diferencia del apartado 4.1, esta ley no es la ecuación de Euler–Lagrange, sino una consecuencia nueva de ella. La traslación en $x_2$ da, del mismo modo, la corriente $Q_k = -T_{k2}$.
* **Relación con la versión anterior.** Allí la traslación era $f(x, t) \to f(x + \varepsilon, t)$, que corresponde a $\vec{\tau} = (-1, 0)$, y la corriente sale con el signo contrario.

### 4.3. Los giros del plano

* **La familia.** El giro de ángulo $\varepsilon$ de las variables, con $\vec{\tau} = (-x_2, x_1)$ y $\xi = 0$.
* **Simetría.** Las derivadas de $\vec{\tau}$ son $d_{x_1} \tau_1 = 0$, $d_{x_2} \tau_1 = -1$, $d_{x_1} \tau_2 = 1$ y $d_{x_2} \tau_2 = 0$, así que la divergencia de $\vec{\tau}$ es nula. En la forma de cuatro términos (parte matemática, apartado 8.3), el término de las pendientes es $u_1 \cdot (-\partial_2 f) + u_2 \cdot \partial_1 f = 0$, y los demás son nulos: $D = 0$, simetría con $\vec{F} = \vec{0}$.
* **Corriente.** $Q_k = -\sum_l T_{kl} \cdot \tau_l = x_2 \cdot T_{k1} - x_1 \cdot T_{k2}$: la corriente del «momento angular» de la membrana, combinación de las de las dos traslaciones con coeficientes que dependen del punto.

Las cuentas de este documento están comprobadas con SymPy en Teorema-de-Noether-v2-comprobaciones.py.
