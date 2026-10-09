<!-- COMENTARIO HTML PARA LA IA:
No he quedado contento con lo que he escrito del teorema de Noether. Voy a ir planteando párrafo a párrafo lo que pretendo. 
-->

## 1. Qué buscamos

Hasta ahora hemos planteado un problema de variación sobre un funcional $\bsS$, que depende de una función $f$ de una variable real, y hemos buscado las funciones $f$ que lo hacen estacionario. $\bsS[f]$ es la integral, entre los extremos del intervalo de la variable independiente, de $\bsL(f, f', x)$: un operador que convierte la función $f$, su derivada $f'$ y cada punto $x$ del intervalo en un valor a integrar.

Ahora buscamos **transformaciones de $f$ que no cambien el valor de $\bsS[f]$**.

## 2. La transformación actúa sobre los puntos del plano

Para poder mover a la vez la variable $x$ y los valores de $f$, la transformación no actúa directamente sobre $f$, sino sobre los puntos $(x, y)$ del plano:

$$
\begin{aligned}
\Phi(x, y) = \big(X(x, y),\ Y(x, y)\big).
\end{aligned}
$$

* $X$ dice dónde va la variable, e $Y$, dónde va el valor.
* La nueva variable puede depender también del valor. Por ejemplo, en un giro del plano de ángulo $\varepsilon$, $X(x, y) = x \cdot \cos\varepsilon - y \cdot \sin\varepsilon$.

Una función $f$ se transforma transformando su gráfica, la curva $x \mapsto \big(x, f(x)\big)$, es decir, el par de funciones $(Id, f)$. La curva transformada, $\Phi(Id, f)$, es la gráfica de una nueva función $\tilde{f}$, definida sobre una nueva variable $\tilde{x}$:

$$
\begin{aligned}
\tilde{x}(x) := X\big(x, f(x)\big), \qquad \tilde{f}\big(\tilde{x}(x)\big) := Y\big(x, f(x)\big).
\end{aligned}
$$

## 3. Una familia de transformaciones

No trabajamos con una transformación, sino con una familia $\Phi_\varepsilon = (X_\varepsilon, Y_\varepsilon)$, que depende de un parámetro real $\varepsilon$.

### 3.1. Lo que le pedimos

1. **Que para $\varepsilon = 0$ sea la identidad:** $\Phi_0(x, y) = (x, y)$, es decir, $\Phi_0(f) = f$.
   * Es lo mismo que pedir que $\Phi_0$ sea el elemento neutro de la composición: $\Phi_0 \circ \Phi_\varepsilon = \Phi_\varepsilon \circ \Phi_0 = \Phi_\varepsilon$.
2. **Que dependa de $\varepsilon$ de forma derivable:** $\Phi_\varepsilon(x, y)$ es de clase $C^2$ en $(\varepsilon, x, y)$.
   * Así, para $|\varepsilon| \ll 1$, $\tilde{x}(x)$ es estrictamente creciente, porque su derivada está próxima a $1$; tiene inversa, y $\tilde{f}$ está bien definida.

Estas dos condiciones son las únicas que necesita el teorema de Noether, porque solo usa el primer orden en $\varepsilon$.

### 3.2. Una condición más: la ley de grupo

Se puede pedir además:

3. **Que componer sea sumar los parámetros**, de forma exacta: $\Phi_\varepsilon \circ \Phi_\eta = \Phi_{\varepsilon + \eta}$ para todo $\varepsilon$ y $\eta$.

Consecuencias:

* **La inversa sale sola:** $\Phi_{-\varepsilon} \circ \Phi_\varepsilon = \Phi_0 = Id$, así que la inversa de $\Phi_\varepsilon$ es $\Phi_{-\varepsilon}$.
* **Las transformaciones de la familia conmutan entre sí**, porque $\varepsilon + \eta = \eta + \varepsilon$. No es una restricción: las que pueden no conmutar son las de familias distintas.
  * Los giros alrededor de un mismo eje conmutan: $R_z(\alpha) \cdot R_z(\beta) = R_z(\alpha + \beta)$.
  * Los giros alrededor de ejes distintos no conmutan, pero forman familias distintas.
* **La familia es un grupo con la composición:** es cerrada, tiene elemento neutro ($\Phi_0$) e inversos ($\Phi_{-\varepsilon}$), y la composición es asociativa.
  * Se llama **grupo uniparamétrico de transformaciones**. Es el flujo del campo vectorial que genera la transformación (Tema 1, apartado 4.4).
  * Si la ley solo vale para $\varepsilon$ y $\eta$ pequeños, es un grupo local de transformaciones.

Dos observaciones:

* **La ley tiene que ser exacta.** Con un término de error, $\Phi_\varepsilon \circ \Phi_\eta = \Phi_{\varepsilon + \eta} + O(\cdot)$, no exige nada: cualquier familia que cumpla las condiciones 1 y 2 la cumple a primer orden.
* **El teorema no la necesita.** $\Phi_\varepsilon(x, y) = (x, y + \sin\varepsilon)$ no cumple la ley de grupo, porque $\sin\varepsilon + \sin\eta \neq \sin(\varepsilon + \eta)$; pero a primer orden es el desplazamiento vertical, $(x, y + \varepsilon)$, y da la misma cantidad conservada. La ley es útil porque siempre se puede elegir la familia de modo que la cumpla, y los ejemplos físicos (traslaciones, giros, cambios de velocidad y traslación en el tiempo) ya la cumplen.

## 4. La condición de simetría

Si el dominio de $f$ es $[x_1, x_2] \subseteq \mathbb{R}$, lo que buscamos tiene que ocurrir en cada subintervalo $[a, b]$, con $x_1 \leq a < b \leq x_2$:

* el funcional de $\tilde{f}$ sobre el intervalo transformado, $[\tilde{x}(a), \tilde{x}(b)]$, es igual al de $f$ sobre $[a, b]$,
* salvo un término que solo depende de los extremos,
* y salvo términos de orden $\varepsilon^2$.

Es decir:

$$
\begin{aligned}
&\forall [a,b] \subseteq [x_1,x_2], \ \forall f \in C^2([x_1,x_2]): \\
&\int_{\tilde{x}(a)}^{\tilde{x}(b)} \bsL\big(\tilde{f}(\tilde{x}), \tilde{f}'(\tilde{x}), \tilde{x}\big) \,d\tilde{x} \\
&\qquad = \int_{a}^{b} \bsL\big(f(x), f'(x), x\big) \,dx + \varepsilon \cdot \big(F(b) - F(a)\big) + O(\varepsilon^2),
\end{aligned}
$$

donde $F(x, y)$ es una función de dos variables, la misma para todas las $f$, que se evalúa en $\big(x, f(x)\big)$: depende del punto y del valor de $f$ en él. En el apartado 5, punto (3), se ve por qué no puede depender de $f'$.

* Con $F = 0$, el funcional no cambia a primer orden.
* Se admite $F \neq 0$ porque sin ese término quedarían fuera casos que necesitamos, como el desplazamiento vertical en un campo uniforme o los cambios de velocidad de la relatividad de Galileo.

La familia $\Phi_\varepsilon$ tiene que cumplir esta condición:

* **para toda función $f \in C^2([x_1, x_2])$**, no solo para las soluciones de Euler–Lagrange, que forman una clase de funciones mucho más pequeña;
* **sin valores fijados en los extremos**, a diferencia del problema de la estacionariedad.

## 5. La condición, paso a paso

La condición del apartado 4 compara dos integrales sobre intervalos distintos. Para ver qué exige, llevamos la integral transformada al intervalo $[a, b]$ y la desarrollamos en $\varepsilon$.

**Notación.** A lo largo de $f$ escribimos

$$
\begin{aligned}
X(x) := X_\varepsilon\big(x, f(x)\big), \qquad Y(x) := Y_\varepsilon\big(x, f(x)\big),
\end{aligned}
$$

es decir, $X(x) = \text{First}\big(\Phi_\varepsilon(x, f(x))\big)$ e $Y(x) = \text{Second}\big(\Phi_\varepsilon(x, f(x))\big)$. Así, $\tilde{x}(x) = X(x)$ y $\tilde{f}\big(X(x)\big) = Y(x)$. $X'(x)$ e $Y'(x)$ son las derivadas de estas funciones de $x$, es decir, derivadas totales a lo largo de $f$, y no las derivadas parciales de $X_\varepsilon$ e $Y_\varepsilon$.

A primer orden, la transformación es

$$
\begin{aligned}
X_\varepsilon(x, y) = x + \varepsilon \cdot \tau(x, y) + O(\varepsilon^2), \qquad Y_\varepsilon(x, y) = y + \varepsilon \cdot \xi(x, y) + O(\varepsilon^2),
\end{aligned}
$$

y a lo largo de $f$ escribimos $\tau(x) := \tau\big(x, f(x)\big)$ y $\xi(x) := \xi\big(x, f(x)\big)$, con sus derivadas $\tau'$ y $\xi'$ también totales.

**La cadena de igualdades:**

$$
\begin{aligned}
\int_{X(a)}^{X(b)} \bsL\big(\tilde{f}(\tilde{x}), \tilde{f}'(\tilde{x}), \tilde{x}\big) \,d\tilde{x}
&\overset{(1)}{=} \int_a^b \bsL\left(Y(x),\ \dfrac{Y'(x)}{X'(x)},\ X(x)\right) \cdot X'(x) \,dx \\
&\overset{(2)}{=} \int_a^b \Big(\bsL\big(f, f', x\big) + \varepsilon \cdot D(x)\Big) \,dx + O(\varepsilon^2) \\
&\overset{(3)}{=} \int_a^b \left(\bsL\big(f, f', x\big) + \varepsilon \cdot \dfrac{dF}{dx}\right) dx + O(\varepsilon^2) \\
&\overset{(4)}{=} \int_a^b \bsL\big(f, f', x\big) \,dx + \varepsilon \cdot \big(F(b) - F(a)\big) + O(\varepsilon^2).
\end{aligned}
$$

El primer miembro y el último son los dos lados de la condición del apartado 4. Las igualdades (1), (2) y (4) valen para cualquier transformación; la (3) es la que define la simetría.

**Por qué se cumple cada igualdad:**

* **(1) Cambio de variable $\tilde{x} = X(x)$.** Para $|\varepsilon| \ll 1$, $X(x)$ es estrictamente creciente, así que el cambio es válido. Los límites pasan a ser $a$ y $b$, y el diferencial, $d\tilde{x} = X'(x) \cdot dx$. El primer argumento es $\tilde{f}\big(X(x)\big) = Y(x)$, por la definición de $\tilde{f}$. El segundo, $\tilde{f}'$, es la derivada respecto de la **nueva** variable; derivando respecto de $x$ la definición $\tilde{f}\big(X(x)\big) = Y(x)$, por la regla de la cadena,

  $$
  \begin{aligned}
  \tilde{f}'\big(X(x)\big) \cdot X'(x) = Y'(x)
  \quad \Longrightarrow \quad
  \tilde{f}'\big(X(x)\big) = \dfrac{Y'(x)}{X'(x)}:
  \end{aligned}
  $$

  el cociente de las derivadas de las dos componentes de la curva transformada. El tercer argumento es el punto nuevo, $\tilde{x} = X(x)$.

* **(2) Desarrollo a primer orden en $\varepsilon$.** Con la transformación a primer orden,

  $$
  \begin{aligned}
  X(x) &= x + \varepsilon \cdot \tau(x), & X'(x) &= 1 + \varepsilon \cdot \tau'(x), \\
  Y(x) &= f(x) + \varepsilon \cdot \xi(x), & Y'(x) &= f'(x) + \varepsilon \cdot \xi'(x),
  \end{aligned}
  $$

  salvo términos de orden $\varepsilon^2$. Como $\dfrac{1}{1 + \varepsilon \cdot \tau'} = 1 - \varepsilon \cdot \tau' + O(\varepsilon^2)$,

  $$
  \begin{aligned}
  \dfrac{Y'(x)}{X'(x)} = f' + \varepsilon \cdot \big(\xi' - \tau' \cdot f'\big) + O(\varepsilon^2).
  \end{aligned}
  $$

  Desarrollando $\bsL$ por Taylor en sus tres argumentos y multiplicando por $X'(x) = 1 + \varepsilon \cdot \tau'$, el integrando es $\bsL(f, f', x) + \varepsilon \cdot D(x) + O(\varepsilon^2)$, con

  $$
  \begin{aligned}
  D := \partial_f \bsL \cdot \xi + \partial_{f'} \bsL \cdot \big(\xi' - \tau' \cdot f'\big) + \partial_x \bsL \cdot \tau + \bsL \cdot \tau'.
  \end{aligned}
  $$

  El resto, integrado en $[a, b]$, sigue siendo de orden $\varepsilon^2$, porque las derivadas segundas de $\bsL$ son continuas en un conjunto cerrado y acotado (el argumento de la cota uniforme de «El formalismo lagrangiano»).

  **$D$ es del mismo tipo que $\bsL$.** $\bsL$ es una función de tres variables reales, $(y, y', x) \mapsto \bsL(y, y', x)$, que a lo largo de $f$ se evalúa en $\big(f(x), f'(x), x\big)$; aquí $y'$ es solo el nombre de la segunda variable. $D$ también lo es: sus ingredientes son las derivadas parciales de $\bsL$, que son funciones de $(y, y', x)$, y $\tau$, $\xi$ y sus derivadas totales, que también lo son, porque $\tau' = \partial_x \tau + \partial_y \tau \cdot y'$ y $\xi' = \partial_x \xi + \partial_y \xi \cdot y'$. $D$ va, por tanto, del mismo conjunto de partida que $\bsL$ al mismo conjunto de llegada, $\mathbb{R}$, y no contiene $y''$. Si $\tau$ o $\xi$ dependieran de $f'$, sus derivadas contendrían $f''$ y $D$ ya no sería del mismo tipo; con transformaciones de los puntos del plano, como las de este documento, no ocurre.

* **(3) La hipótesis de simetría.** Es la única igualdad que no vale siempre: la transformación es una simetría si $D = \dfrac{dF}{dx}$ en cada punto, para toda $f$. El término es $\varepsilon \cdot \dfrac{dF}{dx}$, con el factor $\varepsilon$.

  * **Por qué en cada punto.** La condición se pide en todo subintervalo: si $\int_a^b \left(D - \dfrac{dF}{dx}\right) dx = 0$ para todo $[a, b]$, derivando respecto de $b$, por el teorema fundamental del cálculo, el integrando, que es continuo, es nulo.
  * **Lo que se exige no es que $D$ tenga primitiva.** A lo largo de cada $f$, $D$ es una función continua de $x$ y siempre tiene primitiva, $\int_{x_1}^{x} D(s) \,ds$. Pero esa primitiva depende de todos los valores de $f$ entre $x_1$ y $x$. Lo que se exige es que la primitiva sea **local**: una sola función $F$, la misma para todas las $f$, evaluada en el punto.
  * **La condición es una igualdad entre funciones del mismo tipo que $\bsL$.** Si $F$ dependiera de $y'$, $\dfrac{dF}{dx}$ contendría $f''$, y $D$ no la contiene. Por tanto, $F$ solo depende de $x$ y de $y$, como se ha dicho en el apartado 4, y la condición es la identidad

    $$
    \begin{aligned}
    D(y, y', x) = \partial_x F(x, y) + \partial_y F(x, y) \cdot y' \qquad \text{para todo } (y, y', x),
    \end{aligned}
    $$

    entre dos funciones de tres variables. Como el lado derecho es una función afín de $y'$, $D$ también tiene que serlo.
  * **Un ejemplo de cada caso**, con $\bsL = \dfrac{1}{2} \cdot y'^2 - g \cdot y$ (el tiro vertical, con $x$ como tiempo):
    * desplazamiento vertical, $\Phi_\varepsilon(x, y) = (x, y + \varepsilon)$: $\tau = 0$, $\xi = 1$ y $D = \partial_y \bsL = -g$, que es $\partial_x F$ con $F = -g \cdot x$. Es una simetría;
    * escala de los valores, $\Phi_\varepsilon(x, y) = \big(x, (1 + \varepsilon) \cdot y\big)$: $\tau = 0$, $\xi = y$, $\xi' = y'$ y $D = -g \cdot y + y'^2$. A lo largo de cada $f$ tiene primitiva, pero es cuadrática en $y'$, y ninguna $F(x, y)$ la reproduce. No es una simetría.

* **(4) Regla de Barrow.** $\int_a^b \dfrac{dF}{dx} \,dx = F(b) - F(a)$.

Si la variable no se mueve, $\tau = 0$, y $D$ se reduce a $\partial_f \bsL \cdot \xi + \partial_{f'} \bsL \cdot \xi'$: la variación primera de $\bsL$ en la dirección $\xi$.

## 6. La identidad de Noether

### 6.1. Notación

Por comodidad, y para usar la notación habitual, definimos a lo largo de $f$ el **momento conjugado**, $p$, y la **expresión de Euler–Lagrange**, $\varphi$:

$$
\begin{aligned}
p(x) &:= {\partial}_{f'} \bsL\big(f(x), f'(x), x\big) \\
\varphi(x) &:= {\partial}_f \bsL\big(f(x), f'(x), x\big) - \dfrac{dp}{dx}(x).
\end{aligned}
$$

$\varphi = 0$ es la ecuación de Euler–Lagrange: sus soluciones son las $f$ con $\varphi = 0$ en todo el intervalo. Pero $\varphi$ está definida para toda $f$, sea o no una solución.

**Regularidad.** Lo que sigue usa tres hechos:

* $p$ es de clase $C^1$: $\partial_{f'} \bsL$ lo es, porque $\bsL$ es de clase $C^2$, y $x \mapsto \big(f(x), f'(x), x\big)$ también, porque $f$ es de clase $C^2$. La composición de funciones de clase $C^1$ es de clase $C^1$, por la regla de la cadena.
* $\xi$ es de clase $C^1$ a lo largo de $f$, porque $\xi(x, y)$ lo es y $f$ también.
* $\varphi$ es continua, porque $\partial_f \bsL$ y $p'$ lo son.

En lo que sigue, la prima indica la derivada respecto de $x$ a lo largo de $f$: $p' = \dfrac{dp}{dx}$, $\xi' = \dfrac{d\xi}{dx}$ y $(p \cdot \xi)' = \dfrac{d}{dx}(p \cdot \xi)$.

### 6.2. El caso $\tau = 0$

Veamos un caso particular: el caso $\tau = 0$, es decir, las transformaciones que mueven los valores y no la variable, como el desplazamiento vertical o la escala de los valores. Ahí $D = {\partial}_f \bsL \cdot \xi + p \cdot \xi'$.

Vamos a demostrar que, para toda $f$, cuando $\tau = 0$, $D = \varphi \cdot \xi + \dfrac{d}{dx}\big(p \cdot \xi\big)$:

$$
\begin{aligned}
D &\overset{(1)}{=} {\partial}_f \bsL \cdot \xi + {\partial}_{f'} \bsL \cdot \big(\xi' - \tau' \cdot f'\big) + {\partial}_x \bsL \cdot \tau + \bsL \cdot \tau' \\
&\overset{(2)}{=} {\partial}_f \bsL \cdot \xi + {\partial}_{f'} \bsL \cdot \xi' \\
&\overset{(3)}{=} {\partial}_f \bsL \cdot \xi + p \cdot \xi' \\
&\overset{(4)}{=} {\partial}_f \bsL \cdot \xi + (p \cdot \xi)' - p' \cdot \xi \\
&\overset{(5)}{=} ({\partial}_f \bsL - p') \cdot \xi + (p \cdot \xi)' \\
&\overset{(6)}{=} \left({\partial}_f \bsL - \dfrac{d}{dx}{\partial}_{f'} \bsL\right) \cdot \xi + (p \cdot \xi)' \\
&\overset{(7)}{=} \varphi \cdot \xi + \dfrac{d}{dx}\big(p \cdot \xi\big).
\end{aligned}
$$

Justificación de cada igualdad:

* **(1)** Es la definición de $D$ del apartado 5, punto (2): el coeficiente de $\varepsilon$ en el desarrollo de Taylor del integrando transformado.
* **(2)** Introducimos la hipótesis $\tau = 0$. Como $\tau$ es nula en todo el intervalo, también $\tau' = 0$, y se anulan los tres términos que contienen $\tau$ o $\tau'$.
* **(3)** Usamos la notación del apartado 6.1, $\partial_{f'} \bsL = p$.
* **(4)** Usamos la regla de derivación del producto $p \cdot \xi$, $(p \cdot \xi)' = p' \cdot \xi + p \cdot \xi'$, despejada para $p \cdot \xi'$. Para usarla hace falta que $p$ y $\xi$ sean derivables, que es lo que asegura la regularidad del apartado 6.1.
* **(5)** Sacamos factor común $\xi$ (propiedad distributiva).
* **(6)** Desglosamos $p'$ según la definición de $p$: $p' = \dfrac{d}{dx}\partial_{f'} \bsL$ es la derivada de la función compuesta $x \mapsto \partial_{f'} \bsL\big(f(x), f'(x), x\big)$, no la derivada parcial $\partial_x \partial_{f'} \bsL$. Así se ve la expresión de Euler–Lagrange.
* **(7)** Usamos la definición de $\varphi$.

**Qué no hemos usado.** Ni la hipótesis de simetría, $D = \dfrac{dF}{dx}$, ni que $f$ sea una solución de Euler–Lagrange. Por tanto, $D = \varphi \cdot \xi + (p \cdot \xi)'$ es una identidad: vale para toda $f \in C^2([x_1, x_2])$ y para toda transformación con $\tau = 0$. El paso siguiente consiste en añadirle la hipótesis de simetría.

### 6.3. La hipótesis de simetría: identidad y teorema de Noether

Ahora usamos la hipótesis de simetría (apartado 5, punto (3)): la integral del integrando transformado sobre el intervalo transformado es igual a la del integrando original sobre su intervalo, salvo un término que solo depende de los extremos, $\varepsilon \cdot \big(F(b) - F(a)\big)$, y salvo términos de orden $\varepsilon^2$. Eso equivale a $D = \dfrac{dF}{dx}$ en cada punto, también para toda $f$.

Antes conviene recordar de qué depende cada función, todas evaluadas a lo largo de $f$:

* $p$ depende de $f$, de $f'$ y de $x$: $p(x) = \partial_{f'} \bsL\big(f(x), f'(x), x\big)$;
* $\xi$ depende solo de $f$ y de $x$: $\xi(x) = \xi\big(x, f(x)\big)$. Su derivada, $\xi' = \partial_x \xi + \partial_y \xi \cdot f'$, sí depende de $f'$;
* $F$ depende solo de $f$ y de $x$: $F(x) = F\big(x, f(x)\big)$, de clase $C^1$, y $\dfrac{dF}{dx} = \partial_x F + \partial_y F \cdot f'$ es la derivada de la función compuesta.

Igualamos las dos expresiones de $D$, la del apartado 6.2 y la de la hipótesis de simetría:

$$
\begin{aligned}
\varphi \cdot \xi + \dfrac{d}{dx}\big(p \cdot \xi\big) &= \dfrac{dF}{dx} \\
-\varphi \cdot \xi &= \dfrac{d}{dx}\big(p \cdot \xi\big) - \dfrac{dF}{dx} \\
&= \dfrac{d}{dx}\big(p \cdot \xi - F\big).
\end{aligned}
$$

En la segunda línea pasamos $\varphi \cdot \xi$ a la derecha y $\dfrac{dF}{dx}$ a la izquierda; en la tercera usamos la linealidad de la derivada.

**Identidad de Noether** (caso $\tau = 0$). Para toda $f \in C^2([x_1, x_2])$, sea o no una solución,

$$
\begin{aligned}
\dfrac{d}{dx}\big(p \cdot \xi - F\big) = -\varphi \cdot \xi.
\end{aligned}
$$

**Teorema de Noether** (caso $\tau = 0$). Si $f_0$ es una solución de las ecuaciones de Euler–Lagrange, $\varphi = 0$ en todo el intervalo, como vimos al definirla, y la identidad queda

$$
\begin{aligned}
\dfrac{d}{dx}\big(p \cdot \xi - F\big) = 0.
\end{aligned}
$$

Por el teorema del valor medio, una función continua en $[x_1, x_2]$, derivable en el interior y con derivada nula, es constante. $p \cdot \xi - F$ cumple estas hipótesis, porque $p$, $\xi$ y $F\big(x, f(x)\big)$ son de clase $C^1$. Por tanto, la cantidad

$$
\begin{aligned}
Q := p \cdot \xi - F
\end{aligned}
$$

es constante a lo largo de $f_0$. El valor de la constante depende de la solución $f_0$.

Elegimos el signo $p \cdot \xi - F$, y no $F - p \cdot \xi$, porque así, en el caso más sencillo, $Q$ es exactamente $p$ (primer ejemplo del apartado siguiente). Las dos son constantes; es una convención.

### 6.4. Comprobación: tres ejemplos

Con una sola función y $\tau = 0$, con $x$ en el papel del tiempo y la masa igual a $1$. Las dos primeras filas son el desplazamiento vertical, sin campo y con un campo uniforme; la tercera, un cambio de velocidad:

| $\Phi_\varepsilon(x, y)$ | $\bsL$ | $\xi$ | $D$ | $F$ | $Q = p \cdot \xi - F$ |
| --- | --- | --- | --- | --- | --- |
| $(x, y + \varepsilon)$ | $\dfrac{1}{2} \cdot y'^2$ | $1$ | $0$ | $0$ | $f'$ |
| $(x, y + \varepsilon)$ | $\dfrac{1}{2} \cdot y'^2 - g \cdot y$ | $1$ | $-g$ | $-g \cdot x$ | $f' + g \cdot x$ |
| $(x, y + \varepsilon \cdot x)$ | $\dfrac{1}{2} \cdot y'^2$ | $x$ | $y'$ | $y$ | $x \cdot f' - f$ |

En los tres casos, $p = f'$ y $D = \partial_y \bsL \cdot \xi + p \cdot \xi'$ (apartado 6.2). Comprobación de que $Q$ es constante, con la solución explícita y sin usar el teorema:

* **Primera fila.** La ecuación de Euler–Lagrange es $f'' = 0$, así que $f = c_0 + c_1 \cdot x$ y $Q = f' = c_1$: el momento. Es la coordenada cíclica: $\bsL$ no depende de $y$.
* **Segunda fila.** La ecuación es $f'' = -g$, y $\dfrac{d}{dx}(f' + g \cdot x) = -g + g = 0$. $Q$ es la velocidad en $x = 0$.
* **Tercera fila.** $D = 0 \cdot x + f' \cdot 1 = f' = \dfrac{d}{dx} f$, así que $F(x, y) = y$. Con $f = c_0 + c_1 \cdot x$, $Q = x \cdot c_1 - (c_0 + c_1 \cdot x) = -c_0$: menos la posición en $x = 0$. Aquí $\xi$ depende del punto, y $Q$ ya no es un momento.

**Qué es $Q$.** $\xi$ dice cuánto mueve la transformación el valor de $f$ en cada punto, por unidad de $\varepsilon$; $p \cdot \xi$ es el momento en la dirección en que la transformación mueve las cosas; y $F$ es la corrección que hace falta cuando la transformación cambia $\bsL$ en una derivada total. Cada simetría tiene su $\xi$, y por eso da su propia cantidad: cambiar $\xi$ cambia el significado de $Q$. Con una sola función y $\tau = 0$ solo aparecen cantidades como las de la tabla. El momento angular necesita al menos dos funciones, porque un giro mezcla dos coordenadas, y la energía necesita mover la variable, $\tau \neq 0$.

<!-- GUÍA DE LA IA (09-10-2026) para el paso 8: se sustituye por el desarrollo propio -->

### 6.5. Guía para el paso 8: el caso $\tau \neq 0$

La idea es reducir el caso general al del apartado 6.2, cambiando $\xi$ por el desplazamiento medido en un mismo punto $x$. Al hacerlo aparece la energía.

#### Lo que hay que obtener

1. **Un lema: reducción a variable fija.** Con

   $$
   \begin{aligned}
   \bar{\xi} := \xi - \tau \cdot f',
   \end{aligned}
   $$

   el $D$ completo del apartado 5 se escribe

   $$
   \begin{aligned}
   D = \partial_f \bsL \cdot \bar{\xi} + p \cdot \bar{\xi}' + (\tau \cdot \bsL)'.
   \end{aligned}
   $$

   Los dos primeros términos son el $D$ del caso $\tau = 0$ con $\bar{\xi}$ en lugar de $\xi$, y el tercero es una derivada total.

2. **La identidad de Noether general**, para toda $f$:

   $$
   \begin{aligned}
   \dfrac{d}{dx}\big(p \cdot \xi - \tau \cdot \bsH - F\big) = -\varphi \cdot \big(\xi - \tau \cdot f'\big), \qquad \bsH := p \cdot f' - \bsL.
   \end{aligned}
   $$

3. **El teorema general.** Sobre las soluciones, $Q := p \cdot \xi - \tau \cdot \bsH - F$ es constante.

Con $\tau = 0$ tiene que salir exactamente el apartado 6.3.

#### Pistas

1. **Partir de la definición completa de $D$**, con sus cuatro términos (apartado 5, punto (2)).
2. **Sustituir $\xi = \bar{\xi} + \tau \cdot f'$** en todos los sitios donde aparece $\xi$, también dentro de $\xi'$. Por la regla del producto, $\xi' = \bar{\xi}' + \tau' \cdot f' + \tau \cdot f''$.
3. **Vigilar una cancelación.** El término $-\partial_{f'} \bsL \cdot \tau' \cdot f'$ de $D$ se cancela con otro que sale al desarrollar $\xi'$. Si no se cancela, hay un error de signo.
4. **Agrupar lo que multiplica a $\tau$.** Tiene que quedar $\tau \cdot \big(\partial_f \bsL \cdot f' + \partial_{f'} \bsL \cdot f'' + \partial_x \bsL\big)$. Por la regla de la cadena es la derivada total de $\bsL$ a lo largo de $f$, $\bsL'$: la «diferencial total» del primer apartado de «El formalismo lagrangiano».
5. **Juntar $\tau \cdot \bsL' + \bsL \cdot \tau'$** con la regla del producto: es $(\tau \cdot \bsL)'$. Con esto queda el lema.
6. **Aplicar el apartado 6.2 a $\bar{\xi}$.** Allí solo se usó la regla del producto, así que vale con $\bar{\xi}$ en lugar de $\xi$: $\partial_f \bsL \cdot \bar{\xi} + p \cdot \bar{\xi}' = \varphi \cdot \bar{\xi} + (p \cdot \bar{\xi})'$. Advertencia de regularidad: $\bar{\xi}$ ya no es del «mismo tipo» que $\xi$, porque contiene $f'$, y $\bar{\xi}'$ contiene $f''$. Pero es de clase $C^1$, porque $f$ es de clase $C^2$, y eso basta para la regla del producto.
7. **Añadir la hipótesis de simetría** y pasar a un lado todo lo que es derivada, como en el apartado 6.3. Después, desarrollar $p \cdot \bar{\xi} + \tau \cdot \bsL$ hasta que aparezca $\bsH$.
8. **Qué significa $\bar{\xi}$.** Si la gráfica se desplaza $\varepsilon \cdot \tau$ en horizontal, en un punto fijo $x$ el valor cambia en $-\varepsilon \cdot \tau \cdot f'(x)$. Por eso $\bar{\xi} = \xi - \tau \cdot f'$ es el cambio vertical neto en el mismo $x$. Es la «Reducción al caso anterior» de la parte matemática de la serie.

#### Comprobaciones

* **La energía.** Traslación de la variable, $\Phi_\varepsilon(x, y) = (x + \varepsilon, y)$: $\tau = 1$ y $\xi = 0$. Entonces $D = \partial_x \bsL$, que es nulo si $\bsL$ no depende explícitamente de $x$; así, $F = 0$ y $Q = -\bsH$. Con $\bsL = \dfrac{1}{2} \cdot y'^2 - g \cdot y$, $\bsH = \dfrac{1}{2} \cdot f'^2 + g \cdot f$, que es la energía. Comprobación: $\bsH' = f' \cdot (f'' + g) = 0$, porque $f'' = -g$.
* **Un caso con $\tau$ y $\xi$ a la vez (opcional).** El giro del plano, con $\tau = -y$ y $\xi = x$, y $\bsL = \sqrt{1 + y'^2}$, la longitud de la gráfica. La longitud no cambia al girar, así que $F = 0$, y debe salir

  $$
  \begin{aligned}
  Q = \dfrac{x \cdot f' - f}{\sqrt{1 + f'^2}}.
  \end{aligned}
  $$

  Sobre una recta $f = m \cdot x + c$, $Q = -\dfrac{c}{\sqrt{1 + m^2}}$: menos la distancia, con signo, del origen a la recta. Coincide con el camino más corto en forma paramétrica de los ejemplos matemáticos de la serie.

Cuando el lema (pistas 1 a 5) esté escrito, conviene revisarlo antes de seguir: es donde es más fácil equivocarse con los signos.

<!-- FIN DE LA GUÍA -->
