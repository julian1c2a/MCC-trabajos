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
  * **Ser afín es necesario, pero no basta.** Si $D = a(x, y) + b(x, y) \cdot y'$, hace falta una $F$ con $\partial_x F = a$ y $\partial_y F = b$. Por el teorema de Schwarz, $\partial_y \partial_x F = \partial_x \partial_y F$, y eso exige la condición de integrabilidad $\partial_y a = \partial_x b$: la forma diferencial $a \cdot dx + b \cdot dy$ tiene que ser cerrada. Si el dominio de $(x, y)$ es, por ejemplo, estrellado o simplemente conexo, esta condición basta (lema de Poincaré); en un dominio con agujeros, una forma cerrada puede no tener primitiva en todo él.
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

### 6.5. Desarrollo de la identidad de Noether en el caso general, con $\tau$ cualquiera

Recordemos cómo sale el término $D$: es la diferencia, a primer orden en $\varepsilon$, entre el integrando con $f$ y $x$ transformados y el integrando original, comparados en el mismo punto $x$ de la variable vieja. Por el cambio de variable del apartado 5, igualdad (1), el integrando transformado lleva el factor $\tilde{x}'(x) = 1 + \varepsilon \cdot \tau'(x) + O(\varepsilon^2)$. Escribimos $\bsL(\tilde{f}, \tilde{f}')(\tilde{x}) := \bsL\big(\tilde{f}(\tilde{x}), \tilde{f}'(\tilde{x}), \tilde{x}\big)$, con $\tilde{x} = \tilde{x}(x)$, y definimos $D$ como el coeficiente de $\varepsilon$:

$$
\begin{aligned}
D(x) := \left.\dfrac{d}{d\varepsilon}\Big(\bsL(\tilde{f}, \tilde{f}')(\tilde{x}) \cdot \tilde{x}'(x)\Big)\right|_{\varepsilon = 0}.
\end{aligned}
$$

**$D$ ya incluye el factor debido a $d\tilde{x}$.** Por el cambio de variable, $d\tilde{x} = \tilde{x}'(x) \cdot dx$, y ese factor $\tilde{x}'(x)$ está dentro de la definición. Por eso $D$ se integra respecto de la variable vieja, con $dx$, sin añadir nada más:

$$
\begin{aligned}
\int_{\tilde{x}(a)}^{\tilde{x}(b)} \bsL(\tilde{f}, \tilde{f}')(\tilde{x}) \,d\tilde{x} - \int_a^b \bsL(f, f')(x) \,dx = \varepsilon \cdot \int_a^b D(x) \,dx + O(\varepsilon^2).
\end{aligned}
$$

A primer orden, $\tilde{x}'(x) = 1 + \varepsilon \cdot \tau'(x) + O(\varepsilon^2)$, y el factor aporta a $D$ el término $\bsL \cdot \tau'$. Es el último sumando de la forma de cuatro términos del apartado 5 y, en el resultado de este apartado, la parte $\bsL \cdot \tau'$ de $(\tau \cdot \bsL)' = \tau \cdot \bsL' + \bsL \cdot \tau'$. No hay que confundirlo con el término $-\partial_{f'} \bsL \cdot \tau' \cdot f'$, que también lleva $\tau'$ pero tiene otro origen: sale de que $\tilde{f}'$ es la derivada respecto de la nueva variable, el cociente $\dfrac{Y'}{X'}$ del apartado 5. El primero cambia la medida con que se integra, y el segundo, la pendiente que recibe $\bsL$.

Entonces:

$$
\begin{aligned}
\varepsilon \cdot D(x) &\overset{(1)}{=} \bsL(\tilde{f}, \tilde{f}')(\tilde{x}) \cdot \tilde{x}'(x) - \bsL(f, f')(x) + O(\varepsilon^2) \\
&\overset{(2)}{=} \Big(\bsL(\tilde{f}, \tilde{f}')(x) + \varepsilon \cdot \tau(x) \cdot \dfrac{d}{dx}\bsL(\tilde{f}, \tilde{f}')(x)\Big) \cdot \big(1 + \varepsilon \cdot \tau'(x)\big) \\
&\qquad - \bsL(f, f')(x) + O(\varepsilon^2) \\
&\overset{(3)}{=} \Big(\bsL(\tilde{f}, \tilde{f}')(x) - \bsL(f, f')(x)\Big) \\
&\qquad + \varepsilon \cdot \Big(\tau(x) \cdot \bsL'(x) + \bsL(f, f')(x) \cdot \tau'(x)\Big) + O(\varepsilon^2).
\end{aligned}
$$

Justificación de cada igualdad:

* **(1)** Desarrollo de Taylor en $\varepsilon$, alrededor de $\varepsilon = 0$, de la función $\varepsilon \mapsto \bsL(\tilde{f}, \tilde{f}')(\tilde{x}) \cdot \tilde{x}'(x)$. Su valor en $\varepsilon = 0$ es $\bsL(f, f')(x)$, porque entonces $\tilde{x} = x$, $\tilde{f} = f$ y $\tilde{x}' = 1$; y su coeficiente de $\varepsilon$ es $D(x)$, por definición.
* **(2)** El punto se mueve: $\tilde{x} = x + \varepsilon \cdot \tau(x) + O(\varepsilon^2)$. La función $x \mapsto \bsL(\tilde{f}, \tilde{f}')(x)$ se evalúa en $\tilde{x}$ en lugar de en $x$, y el desarrollo de Taylor de primer orden en el punto da el término $\varepsilon \cdot \tau \cdot \dfrac{d}{dx}\bsL(\tilde{f}, \tilde{f}')$. Aquí $\dfrac{d}{dx}$ es la derivada de la función compuesta: al mover el punto se mueven los tres argumentos de $\bsL$, porque $\tilde{f}$ y $\tilde{f}'$ también se evalúan en el punto nuevo. El factor $1 + \varepsilon \cdot \tau'(x)$ es $\tilde{x}'(x)$.
* **(3)** Multiplicamos y llevamos los términos de orden $\varepsilon^2$ al resto. Además, $\bsL(\tilde{f}, \tilde{f}')$ y su derivada se diferencian de $\bsL(f, f')$ y de su derivada, $\bsL'(x) := \dfrac{d}{dx}\bsL(f, f')(x)$, en términos de orden $\varepsilon$. Como en los dos últimos sumandos van multiplicados por $\varepsilon$, se pueden sustituir sin cambiar más que el resto.

Para seguir, dividimos la última expresión en dos partes: la diferencia en el mismo punto, $\bsL(\tilde{f}, \tilde{f}')(x) - \bsL(f, f')(x)$, y el resto, $\varepsilon \cdot (\tau \cdot \bsL' + \bsL \cdot \tau')$.

**Primera parte: la diferencia en el mismo punto $x$.** En el punto viejo $x$, la función transformada no se diferencia de $f$ en $\varepsilon \cdot \xi$, sino en $\varepsilon \cdot \bar{\xi}$, con $\bar{\xi} := \xi - \tau \cdot f'$:

$$
\begin{aligned}
\tilde{f}(x) = f(x) + \varepsilon \cdot \bar{\xi}(x) + O(\varepsilon^2), \qquad \tilde{f}'(x) = f'(x) + \varepsilon \cdot \bar{\xi}'(x) + O(\varepsilon^2).
\end{aligned}
$$

* **La primera.** Por la definición de $\tilde{f}$, $\tilde{f}\big(\tilde{x}(x)\big) = Y(x) = f(x) + \varepsilon \cdot \xi(x) + O(\varepsilon^2)$. Y como $\tilde{x}(x) = x + \varepsilon \cdot \tau(x) + O(\varepsilon^2)$, el punto viejo es $x = \tilde{x}(x) - \varepsilon \cdot \tau(x) + O(\varepsilon^2)$. Desarrollando $\tilde{f}$ alrededor de $\tilde{x}(x)$:

  $$
  \begin{aligned}
  \tilde{f}(x) &= \tilde{f}\big(\tilde{x}(x)\big) - \varepsilon \cdot \tau(x) \cdot \tilde{f}'\big(\tilde{x}(x)\big) + O(\varepsilon^2) \\
  &= f(x) + \varepsilon \cdot \xi(x) - \varepsilon \cdot \tau(x) \cdot f'(x) + O(\varepsilon^2),
  \end{aligned}
  $$

  donde en el último paso $\tilde{f}'\big(\tilde{x}(x)\big) = f'(x) + O(\varepsilon)$, porque va multiplicado por $\varepsilon$. Geométricamente: si la gráfica se desplaza $\varepsilon \cdot \tau$ en horizontal, en un punto fijo el valor cambia en $-\varepsilon \cdot \tau \cdot f'$.
* **La segunda** se obtiene derivando la primera respecto de $x$. Para no tener que estimar la derivada del resto, se usa que las derivadas respecto de $\varepsilon$ y de $x$ conmutan (teorema de Schwarz): $\left.\partial_\varepsilon \tilde{f}'(x)\right|_{\varepsilon = 0} = \left.\partial_x \partial_\varepsilon \tilde{f}(x)\right|_{\varepsilon = 0} = \bar{\xi}'(x)$. Hace falta que $\tilde{f}(x)$ sea de clase $C^2$ como función de $(\varepsilon, x)$, lo que se cumple si $\Phi_\varepsilon$ es de clase $C^2$ en $(\varepsilon, x, y)$ y $f$ es de clase $C^2$.

Con estos dos desarrollos, el de Taylor de $\bsL$ en sus dos primeros argumentos, con $x$ fijo, da

$$
\begin{aligned}
&\bsL(\tilde{f}, \tilde{f}')(x) - \bsL(f, f')(x) \\
&\qquad = \varepsilon \cdot \Big(\partial_f \bsL(f, f')(x) \cdot \bar{\xi}(x) + \partial_{f'} \bsL(f, f')(x) \cdot \bar{\xi}'(x)\Big) + O(\varepsilon^2).
\end{aligned}
$$

Con $\tau = 0$, $\bar{\xi} = \xi$, y se recupera la expresión del apartado 6.2.

**Segunda parte: el resto.** Por la regla de derivación del producto,

$$
\begin{aligned}
\tau \cdot \bsL' + \bsL \cdot \tau' = (\tau \cdot \bsL)',
\end{aligned}
$$

con $\bsL = \bsL(f, f')(x)$: es una derivada total.

**El término integrando queda**, sumando las dos partes y quedándonos con el coeficiente de $\varepsilon$:

$$
\begin{aligned}
D = \partial_f \bsL \cdot \bar{\xi} + p \cdot \bar{\xi}' + (\tau \cdot \bsL)'.
\end{aligned}
$$

Es el lema de la guía del paso 8 (apartado 6.6): los dos primeros términos son el $D$ del caso $\tau = 0$ con $\bar{\xi}$ en lugar de $\xi$, y el tercero es una derivada total.

**Nota sobre los restos.** Que los restos sean de orden $\varepsilon^2$ exige un poco más de regularidad ($\Phi_\varepsilon$ y $f$ de clase $C^3$). Con clase $C^2$ son de orden menor que $\varepsilon$, $o(\varepsilon)$, y basta igual: $D$ es el coeficiente de $\varepsilon$, y solo se usa el primer orden.

A partir de aquí tomaremos una nueva notación (que es el hamiltoniano, que no hemos introducido hasta ahora):

$$
\begin{aligned}
\bsH := p \cdot f' - \bsL
\end{aligned}
$$

Ahora es el momento de añadir la hipótesis de simetría, a saber, $\exists F(x, y)$ tal que $\exists \partial_x F$ y es continua y $\exists \partial_y F$ y es continua, es decir, $F$ es de clase $C^1$, además de cumplir $D = \dfrac {d} {dx}F$, donde $\dfrac{d}{dx}F = \partial_x F + \partial_y F \cdot f'$ es la derivada de la función compuesta $x \mapsto F\big(x, f(x)\big)$. $F$ no depende de $f'$, por lo visto en el apartado 5, punto (3). Teniendo esto en cuenta, y sustituyendo en la la expresión general ya obtenida de $D$:

$$
\begin{aligned}
\dfrac {d}{dx} F = \partial_f \bsL \cdot \bar{\xi} + p \cdot \bar{\xi}' + (\tau \cdot \bsL)'.
\end{aligned}
$$

Desde 6.2. tenemos que, para toda función $\eta$ de clase $C^1$ en $[x_1, x_2]$ (la cadena del apartado 6.2 solo usa la regla del producto y que $\xi$ es de clase $C^1$, no que venga de una transformación):

$$
\begin{aligned}
\partial_f \bsL \cdot \eta + p \cdot \eta' = \varphi \cdot \eta + (p \cdot \eta)'.
\end{aligned}
$$

$\bar{\xi} = \xi - \tau \cdot f'$ es de clase $C^1$, porque $\xi$, $\tau$ y $f'$ lo son ($f$ es de clase $C^2$). Usando este lema que viene de 6.2., con $\eta = \bar{\xi}$, en la expresión antes obtenida:

$$
\begin{aligned}
\dfrac {d}{dx} F = \varphi \cdot \bar\xi + (p \cdot \bar\xi)' + (\tau \cdot \bsL)' = \varphi \cdot \bar\xi + \dfrac {d}{dx} (p \cdot \bar\xi + \tau \cdot \bsL).
\end{aligned}
$$

Y de aquí:
$$
\begin{aligned}
&\dfrac {d}{dx} F &&= \varphi \cdot \bar\xi + \dfrac {d}{dx}  \left( p \cdot \bar\xi + \tau \cdot \bsL \right) \\
&{} &&= \varphi \cdot \bar\xi + \dfrac {d}{dx} \left( p \cdot \bar\xi + \tau \cdot (p \cdot f' - \bsH) \right) \\
&{} &&= \varphi \cdot \bar\xi + \dfrac {d}{dx} \left( p \cdot \bar\xi - \tau \cdot \bsH + \tau \cdot p \cdot f' \right)  
\end{aligned}
$$

$$
\begin{aligned}
&-\varphi \cdot \bar\xi - \dfrac {d}{dx} ({\tau \cdot p \cdot f'}) = \dfrac {d}{dx} \left( p \cdot \bar\xi - \tau \cdot \bsH - F  \right)
\end{aligned}
$$

<!-- PASOS AÑADIDOS POR LA IA (10-10-2026): cómo deshacer \bar\xi y el término d/dx(tau·p·f') -->

Para terminar, deshacemos $\bar{\xi}$ y vemos que el término $\dfrac{d}{dx}(\tau \cdot p \cdot f')$ desaparece. Por pasos:

1. **Pasamos $\dfrac{d}{dx}(\tau \cdot p \cdot f')$ al otro lado:**

   $$
   \begin{aligned}
   \dfrac{d}{dx}\big(p \cdot \bar{\xi} - \tau \cdot \bsH - F\big) + \dfrac{d}{dx}\big(\tau \cdot p \cdot f'\big) = -\varphi \cdot \bar{\xi}.
   \end{aligned}
   $$

2. **Juntamos las dos derivadas en una**, por la linealidad de la derivada:

   $$
   \begin{aligned}
   \dfrac{d}{dx}\big(p \cdot \bar{\xi} + \tau \cdot p \cdot f' - \tau \cdot \bsH - F\big) = -\varphi \cdot \bar{\xi}.
   \end{aligned}
   $$

3. **Deshacemos $\bar{\xi}$ dentro del paréntesis.** Con $\bar{\xi} = \xi - \tau \cdot f'$, repartiendo el producto, los dos términos con $\tau \cdot p \cdot f'$ son opuestos y se cancelan:

   $$
   \begin{aligned}
   p \cdot \bar{\xi} + \tau \cdot p \cdot f' &= p \cdot (\xi - \tau \cdot f') + \tau \cdot p \cdot f' \\
   &= p \cdot \xi - \tau \cdot p \cdot f' + \tau \cdot p \cdot f' \\
   &= p \cdot \xi.
   \end{aligned}
   $$

4. **Sustituimos en el paso 2**, y deshacemos también $\bar{\xi}$ en el lado derecho. Queda la **identidad de Noether en el caso general**, válida para toda $f \in C^2([x_1, x_2])$:

   $$
   \begin{aligned}
   \dfrac{d}{dx}\big(p \cdot \xi - \tau \cdot \bsH - F\big) = -\varphi \cdot \big(\xi - \tau \cdot f'\big).
   \end{aligned}
   $$

5. **El teorema**, como en el apartado 6.3: sobre las soluciones $\varphi = 0$, y por el teorema del valor medio la cantidad $Q := p \cdot \xi - \tau \cdot \bsH - F$ es constante. Hace falta, además de lo del apartado 6.3, que $\bsH$ sea de clase $C^1$ a lo largo de $f$, lo que se cumple porque $p$, $f'$ y $\bsL(f, f')$ lo son. Con $\tau = 0$ se recupera el apartado 6.3; la comprobación con la energía está en la guía (apartado 6.6).

El término $\dfrac{d}{dx}(\tau \cdot p \cdot f')$ apareció porque, en el paréntesis del apartado anterior, $p \cdot \bar{\xi}$ y $\tau \cdot p \cdot f'$ se tratan por separado; al deshacer $\bar{\xi}$ se ve que su suma es $p \cdot \xi$, la cantidad con el generador original.

<!-- FIN DE LOS PASOS AÑADIDOS -->

<!-- GUÍA DE LA IA (09-10-2026) para el paso 8: se sustituye por el desarrollo propio -->

### Guía para el paso 8: el caso $\tau \neq 0$

La idea es reducir el caso general al del apartado 6.2, cambiando $\xi$ por el desplazamiento medido en un mismo punto $x$. Al hacerlo aparece la energía.

#### Lo que hay que obtener

2. **La identidad de Noether general**, para toda $f$:

   $$
   \begin{aligned}
   \dfrac{d}{dx}\big(p \cdot \xi - \tau \cdot \bsH - F\big) = -\varphi \cdot \big(\xi - \tau \cdot f'\big), \qquad \bsH := p \cdot f' - \bsL.
   \end{aligned}
   $$

3. **El teorema general.** Sobre las soluciones, $Q := p \cdot \xi - \tau \cdot \bsH - F$ es constante.

Con $\tau = 0$ tiene que salir exactamente el apartado 6.3.

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

## 7. Ejemplo: el camino más corto como gráfica

El funcional de la longitud de la gráfica de $f$, el del camino más corto entre dos puntos de «El formalismo lagrangiano: ejemplos matemáticos», tiene tres simetrías continuas. Una de ellas, el giro, mueve también la variable ($\tau \neq 0$), así que necesita el caso general del apartado 6.5. Con las tres cantidades conservadas se determina la recta sin resolver la ecuación de segundo orden.

### 7.1. El lagrangiano y sus funciones

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

### 7.2. Las tres simetrías

En los tres casos se usan la cantidad conservada $Q = p \cdot \xi - \tau \cdot \bsH - F$ y el lema $D = \partial_f \bsL \cdot \bar{\xi} + p \cdot \bar{\xi}' + (\tau \cdot \bsL)'$, con $\bar{\xi} = \xi - \tau \cdot f'$ (apartado 6.5).

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

### 7.3. Lo que se obtiene

1. **La recta, sin resolver la ecuación.** La primera fila dice que la pendiente es constante: como $u \mapsto \dfrac{u}{\sqrt{1 + u^2}}$ es estrictamente creciente, $p$ constante implica $f'$ constante, y la gráfica es una recta.
2. **La recta concreta, con el giro.** Sobre $f = m \cdot x + c$,

   $$
   \begin{aligned}
   Q_{\mathrm{giro}} = \dfrac{x \cdot m - (m \cdot x + c)}{\sqrt{1 + m^2}} = -\dfrac{c}{\sqrt{1 + m^2}},
   \end{aligned}
   $$

   que es menos la distancia, con signo, del origen a la recta. La pendiente y la distancia al origen determinan la recta; los extremos eligen después el segmento. Es el mismo resultado que el camino más corto en forma paramétrica de los ejemplos matemáticos de la serie. Allí hacía falta una curva con dos componentes para tratar el giro; aquí basta una función, porque el giro mueve también la variable.
3. **Dos cantidades que no son independientes.** $p^2 + \bsH^2 = \dfrac{f'^2 + 1}{1 + f'^2} = 1$ para **toda** $f$, no solo para las soluciones: los dos desplazamientos dan la misma información, $\sin^2\alpha + \cos^2\alpha = 1$. Tres simetrías dan tres cantidades conservadas, pero no tres datos independientes.
4. **Un ejemplo que no es simetría: la homotecia.** $\Phi_\varepsilon(x, y) = \big((1 + \varepsilon) \cdot x, (1 + \varepsilon) \cdot y\big)$, con $(\tau, \xi) = (x, y)$, multiplica la longitud por $1 + \varepsilon$. Entonces $D = \bsL = \sqrt{1 + y'^2}$, que no es afín en $y'$, y no existe $F$ (apartado 5, punto (3)).

### 7.4. Una precisión: el giro solo vale para ángulos pequeños

El giro de una gráfica solo es otra gráfica si $\varepsilon$ es pequeño: con giros grandes, la curva girada puede tener tramos verticales o volver hacia atrás. Es la condición $|\varepsilon| \ll 1$ del apartado 3.1, que exige que $\tilde{x}(x) = x - \varepsilon \cdot f(x) + O(\varepsilon^2)$ siga siendo creciente. Todo el razonamiento es local en $\varepsilon$, y para el teorema basta, porque solo usa el primer orden.

## 8. Generalización a varias funciones: $\bsL(\vec{f}, \vec{f}', x)$

Pasamos de una función $f$ a $n$ funciones $\vec{f} = (f_1, \dots, f_n)$ de la misma variable $x$. Casi todo se repite con una suma sobre las componentes; lo nuevo es la condición para que exista $F$ (apartado 8.3).

### 8.1. Notación

* $\vec{f} = (f_1, \dots, f_n): [x_1, x_2] \to \mathbb{R}^n$ es de clase $C^2$. Los índices $i, j = 1, \dots, n$ recorren las componentes.
* $\bsL(\vec{y}, \vec{y}', x)$ es una función de $2 \cdot n + 1$ variables reales, de clase $C^2$; $\vec{y}'$ es solo el nombre de las $n$ variables que ocupan el lugar de las derivadas. A lo largo de $\vec{f}$ escribimos $\bsL(\vec{f}, \vec{f}')(x) := \bsL\big(\vec{f}(x), \vec{f}'(x), x\big)$.
* **La transformación** actúa sobre los puntos de $\mathbb{R} \times \mathbb{R}^n$:

  $$
  \begin{aligned}
  \Phi_\varepsilon(x, \vec{y}) = \big(X_\varepsilon(x, \vec{y}),\ \vec{Y}_\varepsilon(x, \vec{y})\big),
  \end{aligned}
  $$

  de clase $C^2$ en $(\varepsilon, x, \vec{y})$ y con $\Phi_0$ igual a la identidad. A primer orden, $X_\varepsilon = x + \varepsilon \cdot \tau(x, \vec{y}) + O(\varepsilon^2)$ e $Y_{\varepsilon, i} = y_i + \varepsilon \cdot \xi_i(x, \vec{y}) + O(\varepsilon^2)$.
* **La gráfica** de $\vec{f}$ es la curva $(Id, \vec{f})$ de $\mathbb{R}^{1+n}$. La transformada tiene **una sola** variable nueva, común a todas las componentes, y $n$ funciones nuevas:

  $$
  \begin{aligned}
  \tilde{x}(x) := X_\varepsilon\big(x, \vec{f}(x)\big), \qquad \tilde{f}_i\big(\tilde{x}(x)\big) := Y_{\varepsilon, i}\big(x, \vec{f}(x)\big).
  \end{aligned}
  $$

  $X_\varepsilon$ puede depender de todas las $y_i$.
* **Momento conjugado, expresión de Euler–Lagrange y hamiltoniano**, a lo largo de $\vec{f}$:

  $$
  \begin{aligned}
  p_i &:= \partial_{f'_i} \bsL(\vec{f}, \vec{f}')(x), \qquad \varphi_i := \partial_{f_i} \bsL(\vec{f}, \vec{f}')(x) - p_i', \\
  \bsH &:= \sum_{i=1}^{n} p_i \cdot f'_i - \bsL.
  \end{aligned}
  $$

  Escribimos $\vec{p} = (p_1, \dots, p_n)$, $\vec{\xi} = (\xi_1, \dots, \xi_n)$ y $\vec{p} \cdot \vec{\xi} = \sum_i p_i \cdot \xi_i$.
* **Las soluciones** cumplen las $n$ ecuaciones de Euler–Lagrange, $\varphi_i = 0$ para $i = 1, \dots, n$ (la separación de las componentes de «El formalismo lagrangiano»).
* **Regularidad**, por los mismos argumentos que en el apartado 6.1, componente a componente: las $p_i$, las $\xi_i$ a lo largo de $\vec{f}$ y $\bsH$ son de clase $C^1$, y las $\varphi_i$ son continuas.
* La prima indica, como antes, la derivada respecto de $x$ a lo largo de $\vec{f}$.

### 8.2. El término $D$

La condición de simetría es la del apartado 4, con $\vec{f}$ en lugar de $f$ y $F(x, \vec{y})$ en lugar de $F(x, y)$. Como en el apartado 6.5, definimos $D$ como el coeficiente de $\varepsilon$ del integrando transformado, escrito en la variable vieja:

$$
\begin{aligned}
D(x) := \left.\dfrac{d}{d\varepsilon}\Big(\bsL(\tilde{\vec{f}}, \tilde{\vec{f}}')(\tilde{x}) \cdot \tilde{x}'(x)\Big)\right|_{\varepsilon = 0}.
\end{aligned}
$$

Entonces:

$$
\begin{aligned}
\varepsilon \cdot D(x) &\overset{(1)}{=} \bsL(\tilde{\vec{f}}, \tilde{\vec{f}}')(\tilde{x}) \cdot \tilde{x}'(x) - \bsL(\vec{f}, \vec{f}')(x) + O(\varepsilon^2) \\
&\overset{(2)}{=} \Big(\bsL(\tilde{\vec{f}}, \tilde{\vec{f}}')(x) + \varepsilon \cdot \tau \cdot \dfrac{d}{dx}\bsL(\tilde{\vec{f}}, \tilde{\vec{f}}')(x)\Big) \cdot \big(1 + \varepsilon \cdot \tau'\big) \\
&\qquad - \bsL(\vec{f}, \vec{f}')(x) + O(\varepsilon^2) \\
&\overset{(3)}{=} \Big(\bsL(\tilde{\vec{f}}, \tilde{\vec{f}}')(x) - \bsL(\vec{f}, \vec{f}')(x)\Big) + \varepsilon \cdot \big(\tau \cdot \bsL' + \bsL \cdot \tau'\big) + O(\varepsilon^2) \\
&\overset{(4)}{=} \varepsilon \cdot \sum_{i=1}^{n} \Big(\partial_{f_i} \bsL \cdot \bar{\xi}_i + p_i \cdot \bar{\xi}_i'\Big) + \varepsilon \cdot (\tau \cdot \bsL)' + O(\varepsilon^2),
\end{aligned}
$$

con $\bar{\xi}_i := \xi_i - \tau \cdot f'_i$.

Justificación de cada igualdad:

* **(1)** Desarrollo de Taylor en $\varepsilon$, como en el apartado 6.5: el valor en $\varepsilon = 0$ es $\bsL(\vec{f}, \vec{f}')(x)$ y el coeficiente de $\varepsilon$ es $D(x)$.
* **(2)** El punto se mueve, $\tilde{x} = x + \varepsilon \cdot \tau + O(\varepsilon^2)$, y el desarrollo de Taylor en el punto da el término con $\dfrac{d}{dx}$, la derivada de la función compuesta: al mover el punto se mueven los $2 \cdot n + 1$ argumentos de $\bsL$. El factor $1 + \varepsilon \cdot \tau'$ es $\tilde{x}'(x)$, el de $d\tilde{x} = \tilde{x}'(x) \cdot dx$.
* **(3)** Multiplicamos, llevamos los términos de orden $\varepsilon^2$ al resto y sustituimos $\bsL(\tilde{\vec{f}}, \tilde{\vec{f}}')$ por $\bsL(\vec{f}, \vec{f}')$ donde ya va multiplicado por $\varepsilon$; $\bsL'$ es la derivada de $\bsL(\vec{f}, \vec{f}')(x)$ respecto de $x$.
* **(4)** Dos partes, como en el apartado 6.5:
  * **En el mismo punto $x$**, cada componente transformada se diferencia de la original en $\varepsilon \cdot \bar{\xi}_i$: $\tilde{f}_i(x) = f_i(x) + \varepsilon \cdot \bar{\xi}_i(x) + O(\varepsilon^2)$ y $\tilde{f}_i'(x) = f_i'(x) + \varepsilon \cdot \bar{\xi}_i'(x) + O(\varepsilon^2)$. La deducción es la del apartado 6.5, componente a componente; el $\tau$ es el mismo para todas, porque la variable es común. El desarrollo de Taylor de $\bsL$ en sus $2 \cdot n$ primeros argumentos, con $x$ fijo, da la suma.
  * **El resto** es una derivada total, por la regla del producto: $\tau \cdot \bsL' + \bsL \cdot \tau' = (\tau \cdot \bsL)'$.

Quedándonos con el coeficiente de $\varepsilon$, el lema del apartado 6.5 en varias funciones es

$$
\begin{aligned}
D = \sum_{i=1}^{n} \Big(\partial_{f_i} \bsL \cdot \bar{\xi}_i + p_i \cdot \bar{\xi}_i'\Big) + (\tau \cdot \bsL)'.
\end{aligned}
$$

### 8.3. Cuándo existe $F$: las condiciones de integrabilidad

Como en el apartado 5, punto (3):

* **$D$ es del mismo tipo que $\bsL$:** una función de $(\vec{y}, \vec{y}', x)$, sin derivadas segundas, porque las $\xi_i$ y $\tau$ solo dependen de $(x, \vec{y})$.
* **$F$ no puede depender de $\vec{y}'$:** si dependiera, $\dfrac{dF}{dx}$ contendría las $f''_i$, y $D$ no las contiene. Así que $F = F(x, \vec{y})$, de clase $C^1$, y

  $$
  \begin{aligned}
  \dfrac{dF}{dx} = \partial_x F + \sum_{i=1}^{n} \partial_{y_i} F \cdot y_i'.
  \end{aligned}
  $$

* **$D$ tiene que ser afín en $\vec{y}'$:** $D = a(x, \vec{y}) + \sum_i b_i(x, \vec{y}) \cdot y_i'$, y la condición de simetría es la identidad $D = \dfrac{dF}{dx}$, es decir, $\partial_x F = a$ y $\partial_{y_i} F = b_i$ para todo $i$.
* **Ser afín no basta.** Por el teorema de Schwarz, las derivadas cruzadas de $F$ coinciden, y eso exige las **condiciones de integrabilidad**:

  $$
  \begin{aligned}
  \partial_{y_i} a = \partial_x b_i, \qquad \partial_{y_j} b_i = \partial_{y_i} b_j, \qquad i, j = 1, \dots, n.
  \end{aligned}
  $$

  Es decir, la forma diferencial $a \cdot dx + \sum_i b_i \cdot dy_i$ tiene que ser cerrada. Con $n = 1$ queda solo la primera, la del apartado 5; con $n \geq 2$ aparecen además condiciones entre las propias $b_i$.
* **El dominio.** Si el dominio de $(x, \vec{y})$ es, por ejemplo, estrellado o simplemente conexo, las condiciones bastan (lema de Poincaré). En un dominio con agujeros, una forma cerrada puede no tener primitiva en todo él; el ejemplo típico es la forma del ángulo alrededor de un punto excluido del plano.

### 8.4. La identidad y el teorema de Noether

**El lema del apartado 6.2, en varias funciones.** Para toda $\vec{\eta} = (\eta_1, \dots, \eta_n)$ de clase $C^1$:

$$
\begin{aligned}
\sum_{i=1}^{n} \Big(\partial_{f_i} \bsL \cdot \eta_i + p_i \cdot \eta_i'\Big)
&\overset{(1)}{=} \sum_{i=1}^{n} \Big(\partial_{f_i} \bsL \cdot \eta_i + (p_i \cdot \eta_i)' - p_i' \cdot \eta_i\Big) \\
&\overset{(2)}{=} \sum_{i=1}^{n} \big(\partial_{f_i} \bsL - p_i'\big) \cdot \eta_i + \Big(\sum_{i=1}^{n} p_i \cdot \eta_i\Big)' \\
&\overset{(3)}{=} \sum_{i=1}^{n} \varphi_i \cdot \eta_i + \Big(\sum_{i=1}^{n} p_i \cdot \eta_i\Big)'.
\end{aligned}
$$

* **(1)** Regla del producto en cada componente, $(p_i \cdot \eta_i)' = p_i' \cdot \eta_i + p_i \cdot \eta_i'$, despejada para $p_i \cdot \eta_i'$.
* **(2)** Sacamos factor común $\eta_i$ en cada sumando, y la suma de derivadas es la derivada de la suma (linealidad).
* **(3)** Definición de $\varphi_i$.

**La identidad.** Las $\bar{\xi}_i$ son de clase $C^1$, porque las $\xi_i$, $\tau$ y las $f'_i$ lo son. Aplicamos el lema con $\vec{\eta} = \bar{\vec{\xi}}$ al resultado del apartado 8.2, añadimos la hipótesis de simetría, $D = F'$, y deshacemos $\bar{\xi}_i$:

$$
\begin{aligned}
F' &\overset{(1)}{=} \sum_{i=1}^{n} \varphi_i \cdot \bar{\xi}_i + \Big(\sum_{i=1}^{n} p_i \cdot \bar{\xi}_i + \tau \cdot \bsL\Big)' \\
&\overset{(2)}{=} \sum_{i=1}^{n} \varphi_i \cdot \bar{\xi}_i + \Big(\sum_{i=1}^{n} p_i \cdot \xi_i - \tau \cdot \sum_{i=1}^{n} p_i \cdot f'_i + \tau \cdot \bsL\Big)' \\
&\overset{(3)}{=} \sum_{i=1}^{n} \varphi_i \cdot \bar{\xi}_i + \big(\vec{p} \cdot \vec{\xi} - \tau \cdot \bsH\big)'.
\end{aligned}
$$

* **(1)** Hipótesis de simetría, el lema del apartado 8.2 y el lema anterior con $\vec{\eta} = \bar{\vec{\xi}}$; las dos derivadas se juntan por linealidad.
* **(2)** Deshacemos $\bar{\xi}_i = \xi_i - \tau \cdot f'_i$ y repartimos el producto.
* **(3)** Sacamos factor común $-\tau$ de los dos últimos términos: $-\tau \cdot \big(\sum_i p_i \cdot f'_i - \bsL\big) = -\tau \cdot \bsH$.

Pasando $F'$ al otro lado, por linealidad, queda la **identidad de Noether en varias funciones**, válida para toda $\vec{f}$ de clase $C^2$:

$$
\begin{aligned}
\big(\vec{p} \cdot \vec{\xi} - \tau \cdot \bsH - F\big)' = -\sum_{i=1}^{n} \varphi_i \cdot \big(\xi_i - \tau \cdot f'_i\big).
\end{aligned}
$$

**El teorema.** Si $\vec{f}_0$ es una solución, todas las $\varphi_i$ son nulas en el intervalo y, por el teorema del valor medio, como en el apartado 6.3,

$$
\begin{aligned}
Q := \vec{p} \cdot \vec{\xi} - \tau \cdot \bsH - F
\end{aligned}
$$

es constante a lo largo de $\vec{f}_0$. Con $n = 1$ se recupera el apartado 6.5.

**Qué no hemos usado.** Que $\vec{f}$ sea solución: la identidad vale para toda $\vec{f}$. Ni ninguna condición sobre la matriz de las derivadas segundas de $\bsL$ respecto de las $y_i'$ (la matriz $W$ de «El formalismo lagrangiano»): la identidad vale aunque las ecuaciones de Euler–Lagrange no determinen las $f''_i$.

### 8.5. Ejemplos

Con $n = 2$ y $x$ en el papel del tiempo (masa $1$):

| Ejemplo | $\bsL$ | $(\tau, \vec{\xi})$ | $F$ | $Q$ |
| --- | --- | --- | --- | --- |
| Giro, campo central | $\dfrac{1}{2} \cdot \lvert\vec{y}'\rvert^2 - U(\lvert\vec{y}\rvert)$ | $\big(0, (-y_2, y_1)\big)$ | $0$ | $f_1 \cdot f_2' - f_2 \cdot f_1'$ |
| Traslación de la variable, campo central | $\dfrac{1}{2} \cdot \lvert\vec{y}'\rvert^2 - U(\lvert\vec{y}\rvert)$ | $\big(1, (0, 0)\big)$ | $0$ | $-\bsH = -\Big(\dfrac{1}{2} \cdot \lvert\vec{f}'\rvert^2 + U\Big)$ |
| Traslación en $y_1$, campo magnético | $\dfrac{1}{2} \cdot \lvert\vec{y}'\rvert^2 + \dfrac{B}{2} \cdot (y_1 \cdot y_2' - y_2 \cdot y_1')$ | $\big(0, (1, 0)\big)$ | $\dfrac{B}{2} \cdot y_2$ | $f_1' - B \cdot f_2$ |
| Cambio de parámetro, camino más corto | $\lvert\vec{y}'\rvert$ | $\big(\tau(x), (0, 0)\big)$ | $0$ | $-\tau \cdot \bsH \equiv 0$ |

Table: Ejemplos con dos funciones.

**Giro en un campo central.** Es lo que faltaba en el apartado 6.4: hace falta $n \geq 2$, porque un giro mezcla dos componentes. $D = \sum_i \big(\partial_{f_i} \bsL \cdot \xi_i + p_i \cdot \xi_i'\big)$, con $\partial_{f_i} \bsL = -U'(r) \cdot \dfrac{f_i}{r}$ y $r = |\vec{f}|$:

$$
\begin{aligned}
D = -\dfrac{U'(r)}{r} \cdot \big(f_1 \cdot (-f_2) + f_2 \cdot f_1\big) + \big(f_1' \cdot (-f_2') + f_2' \cdot f_1'\big) = 0.
\end{aligned}
$$

$Q = p_1 \cdot (-f_2) + p_2 \cdot f_1$ es el momento angular. Comprobación: $Q' = f_1 \cdot f_2'' - f_2 \cdot f_1''$, y con las ecuaciones $f_i'' = -U'(r) \cdot \dfrac{f_i}{r}$ queda $-\dfrac{U'(r)}{r} \cdot (f_1 \cdot f_2 - f_2 \cdot f_1) = 0$.

**Traslación de la variable.** Con $\tau = 1$ y $\vec{\xi} = \vec{0}$, $D = \partial_x \bsL = 0$, y $Q = -\bsH$: se conserva la energía, $\bsH = \dfrac{1}{2} \cdot |\vec{f}'|^2 + U$.

**Traslación en un campo magnético: un ejemplo con $F \neq 0$ y las condiciones de integrabilidad.** Es una carga en un campo magnético uniforme perpendicular al plano, con el potencial vector $\dfrac{B}{2} \cdot (-y_2, y_1)$ («El formalismo lagrangiano: parte física»). Con $\vec{\xi} = (1, 0)$ y $\tau = 0$, $D = \partial_{y_1} \bsL = \dfrac{B}{2} \cdot y_2'$. Es afín, con $a = 0$, $b_1 = 0$ y $b_2 = \dfrac{B}{2}$; las condiciones de integrabilidad se cumplen, porque todos los coeficientes son constantes, y $F = \dfrac{B}{2} \cdot y_2$. Con $p_1 = f_1' - \dfrac{B}{2} \cdot f_2$:

$$
\begin{aligned}
Q = p_1 - F = f_1' - \dfrac{B}{2} \cdot f_2 - \dfrac{B}{2} \cdot f_2 = f_1' - B \cdot f_2.
\end{aligned}
$$

Comprobación: la ecuación de Euler–Lagrange de $f_1$ es $f_1'' = B \cdot f_2'$, y $Q' = f_1'' - B \cdot f_2' = 0$. Es la primera componente del vector $\vec{K}$ de «El formalismo lagrangiano: parte física»: no se conserva la cantidad de movimiento $f_1'$, sino $f_1' - B \cdot f_2$.

**Cambio de parámetro en el camino más corto: una relación entre las ecuaciones.** Con $\bsL = |\vec{y}'|$ (curvas regulares, $\vec{f}' \neq \vec{0}$), $\vec{\xi} = \vec{0}$ y $\tau(x)$ una función **cualquiera** de clase $C^1$, la forma de cuatro términos del apartado 5, componente a componente, da

$$
\begin{aligned}
D = \sum_{i=1}^{n} p_i \cdot \big(-\tau' \cdot f'_i\big) + \bsL \cdot \tau' = -\tau' \cdot \bsH,
\end{aligned}
$$

y $\bsH = \sum_i \dfrac{f'_i \cdot f'_i}{|\vec{f}'|} - |\vec{f}'| = 0$ para toda $\vec{f}$. Así que $D = 0$, $F = 0$ y $Q = -\tau \cdot \bsH \equiv 0$: el teorema no da nada. Pero la identidad sí: su lado izquierdo es nulo, así que

$$
\begin{aligned}
0 = -\sum_{i=1}^{n} \varphi_i \cdot \big(0 - \tau \cdot f'_i\big) = \tau \cdot \sum_{i=1}^{n} f'_i \cdot \varphi_i
\end{aligned}
$$

para toda $\tau$ y toda $\vec{f}$. Tomando $\tau = 1$, $\sum_i f'_i \cdot \varphi_i = 0$: las $n$ ecuaciones de Euler–Lagrange no son independientes. Es la libertad de elegir el parámetro de la curva, y el caso más sencillo del segundo teorema de Noether: una simetría que depende de una función arbitraria da una relación entre las ecuaciones, no una cantidad conservada.

Las cuentas de los ejemplos están comprobadas con SymPy en el archivo borrador-Noether-v2-comprobaciones.py, en el mismo directorio que este borrador.

<!-- COMENTARIOS DE LA IA (10-10-2026): respuestas a dos preguntas (varias variables independientes; la partícula en un campo central). Se sustituyen por el desarrollo propio -->

## Comentarios: varias variables independientes y la partícula en un campo central

### Pregunta 1: varias variables independientes, $\bsL\big(\vec{f}(\vec{x}), J_{\vec{f}}(\vec{x}), \vec{x}\big)$

Sí se generaliza. Es, de hecho, el caso que trata el artículo original de Noether (1918): integrales múltiples, con varias funciones de varias variables. El esquema es el mismo (lema, hipótesis de simetría, identidad), con tres cambios de fondo:

* el factor $\tilde{x}'(x)$ pasa a ser un **determinante**;
* $F$ pasa a ser un **campo vectorial**, y la condición de simetría pide que $D$ sea una **divergencia**;
* el resultado es una **ley de conservación local** (una divergencia nula), no una constante; para obtener una constante hacen falta además condiciones de contorno.

#### Notación

* $\vec{x} = (x_1, \dots, x_m)$ recorre un dominio $\Omega \subset \mathbb{R}^m$, y $\vec{f} = (f_1, \dots, f_n): \Omega \to \mathbb{R}^n$ es de clase $C^2$. Los índices $i, j$ recorren las funciones y $k, l$ las variables.
* $J_{\vec{f}}$ es la matriz jacobiana, de elementos $\partial_k f_i := \dfrac{\partial f_i}{\partial x_k}$.
* $\bsL(\vec{y}, Z, \vec{x})$ es una función de clase $C^2$; $Z = (z_{ik})$ es el nombre de las $n \cdot m$ variables que ocupan el lugar de $J_{\vec{f}}$. El funcional es $\bsS[\vec{f}] = \int_\Omega \bsL(\vec{f}, J_{\vec{f}}, \vec{x})\, d^m x$.
* $d_k$ es la derivada respecto de $x_k$ de una expresión evaluada a lo largo de $\vec{f}$, incluida la dependencia a través de $\vec{f}$ y de $J_{\vec{f}}$: es el papel que tenía la prima. En cambio, $\partial_{x_k} \bsL$ es la derivada respecto del argumento $x_k$, con los demás fijos.
* **Momentos y expresiones de Euler–Lagrange.** Hay un momento por cada función y cada variable:

  $$
  \begin{aligned}
  u_{ik} := \partial_{z_{ik}} \bsL(\vec{f}, J_{\vec{f}}, \vec{x}), \qquad \varphi_i := \partial_{f_i} \bsL - \sum_{k=1}^{m} d_k u_{ik}.
  \end{aligned}
  $$

  Las soluciones cumplen $\varphi_i = 0$, que ahora son ecuaciones en derivadas parciales. Con $m = 1$, $u_{i1} = p_i$ y se recupera el apartado 8.1.

#### La transformación

* Actúa sobre los puntos de $\mathbb{R}^m \times \mathbb{R}^n$, con generador $(\vec{\tau}, \vec{\xi})$, funciones de $(\vec{x}, \vec{y})$:

  $$
  \begin{aligned}
  X_{\varepsilon, k}(\vec{x}, \vec{y}) &= x_k + \varepsilon \cdot \tau_k(\vec{x}, \vec{y}) + O(\varepsilon^2), \\
  Y_{\varepsilon, i}(\vec{x}, \vec{y}) &= y_i + \varepsilon \cdot \xi_i(\vec{x}, \vec{y}) + O(\varepsilon^2).
  \end{aligned}
  $$

* La gráfica $(Id, \vec{f})$ es una superficie de dimensión $m$ en $\mathbb{R}^{m+n}$, y la transformada se define como en el apartado 8.1: $\tilde{\vec{x}}(\vec{x}) := \vec{X}_\varepsilon\big(\vec{x}, \vec{f}(\vec{x})\big)$ y $\tilde{f}_i\big(\tilde{\vec{x}}(\vec{x})\big) := Y_{\varepsilon, i}\big(\vec{x}, \vec{f}(\vec{x})\big)$.
* **Hace falta que $\tilde{\vec{x}}$ sea un difeomorfismo** de $\Omega$ sobre su imagen $\tilde{\Omega}$: es el análogo de que $\tilde{x}$ sea creciente (apartado 3.1). Con $|\varepsilon|$ pequeño lo es, por ejemplo, si $\Omega$ es convexo y acotado, porque $\tilde{\vec{x}}$ es una perturbación de la identidad.

#### Lo que cambia, paso a paso

1. **El factor de $d^m \tilde{x}$ es un determinante.** Por el teorema del cambio de variables, $d^m \tilde{x} = \det J_{\tilde{\vec{x}}}(\vec{x}) \cdot d^m x$. Los elementos de $J_{\tilde{\vec{x}}}$ son $\delta_{kl} + \varepsilon \cdot d_l \tau_k + O(\varepsilon^2)$, y

   $$
   \begin{aligned}
   \det J_{\tilde{\vec{x}}} = 1 + \varepsilon \cdot \sum_{k=1}^{m} d_k \tau_k + O(\varepsilon^2).
   \end{aligned}
   $$

   La razón: en la fórmula de Leibniz del determinante, el producto de los elementos de la diagonal es $1 + \varepsilon \cdot \sum_k d_k \tau_k + O(\varepsilon^2)$, y cualquier otro producto contiene al menos dos elementos fuera de la diagonal, cada uno de orden $\varepsilon$. La divergencia $\sum_k d_k \tau_k$ ocupa el lugar de $\tau'$.

2. **Las pendientes forman una matriz.** Derivamos la definición de $\tilde{f}_i$ respecto de $x_l$ con la regla de la cadena y sustituimos los desarrollos de primer orden:

   $$
   \begin{aligned}
   \sum_{k=1}^{m} \partial_k \tilde{f}_i(\tilde{\vec{x}}) \cdot d_l \tilde{x}_k &= d_l Y_{\varepsilon, i}, \\
   d_l \tilde{x}_k &= \delta_{kl} + \varepsilon \cdot d_l \tau_k + O(\varepsilon^2), \\
   d_l Y_{\varepsilon, i} &= \partial_l f_i + \varepsilon \cdot d_l \xi_i + O(\varepsilon^2).
   \end{aligned}
   $$

   Igualando los coeficientes de $\varepsilon$:

   $$
   \begin{aligned}
   \partial_l \tilde{f}_i(\tilde{\vec{x}}) = \partial_l f_i + \varepsilon \cdot \Big(d_l \xi_i - \sum_{k=1}^{m} \partial_k f_i \cdot d_l \tau_k\Big) + O(\varepsilon^2).
   \end{aligned}
   $$

   En forma matricial, $J_{\tilde{\vec{f}}}(\tilde{\vec{x}}) = J_{\vec{Y}} \cdot J_{\tilde{\vec{x}}}^{-1}$. Con $m = 1$ es el cociente $\tilde{f}_i' = \dfrac{Y_i'}{X'}$ de los apartados 5 y 8.

3. **En el mismo punto**, cada función transformada se diferencia de la original en $\varepsilon \cdot \bar{\xi}_i$, con

   $$
   \begin{aligned}
   \bar{\xi}_i := \xi_i - \sum_{k=1}^{m} \tau_k \cdot \partial_k f_i,
   \end{aligned}
   $$

   porque desplazar el punto en la dirección $\vec{\tau}$ cambia $f_i$, a primer orden, en la derivada direccional $\sum_k \tau_k \cdot \partial_k f_i$. Con $m = 1$ es $\xi_i - \tau \cdot f'_i$.

4. **El lema del apartado 8.2.** Definimos $D$ igual, como el coeficiente de $\varepsilon$ de $\bsL(\tilde{\vec{f}}, J_{\tilde{\vec{f}}}, \tilde{\vec{x}}) \cdot \det J_{\tilde{\vec{x}}}(\vec{x})$, y la misma deducción da

   $$
   \begin{aligned}
   D = \sum_{i=1}^{n} \Big(\partial_{f_i} \bsL \cdot \bar{\xi}_i + \sum_{k=1}^{m} u_{ik} \cdot d_k \bar{\xi}_i\Big) + \sum_{k=1}^{m} d_k(\tau_k \cdot \bsL).
   \end{aligned}
   $$

   En el mismo punto, el desarrollo de Taylor en $\vec{y}$ y $Z$ da la primera suma; el resto, $\sum_k \big(\tau_k \cdot d_k \bsL + \bsL \cdot d_k \tau_k\big)$, es una divergencia por la regla del producto.

5. **La condición de simetría.** La integral transformada, sobre $\tilde{\Omega}$, tiene que ser la original más un término de borde:

   $$
   \begin{aligned}
   &\int_{\tilde{\Omega}} \bsL(\tilde{\vec{f}}, J_{\tilde{\vec{f}}}, \tilde{\vec{x}})\, d^m \tilde{x} \\
   &\qquad = \int_{\Omega} \bsL(\vec{f}, J_{\vec{f}}, \vec{x})\, d^m x + \varepsilon \cdot \int_{\partial\Omega} \vec{F} \cdot \vec{n}\, dS + O(\varepsilon^2),
   \end{aligned}
   $$

   para todo subdominio $\Omega$, con $\vec{n}$ la normal exterior y $\vec{F} = (F_1, \dots, F_m)$ evaluado en $\big(\vec{x}, \vec{f}(\vec{x})\big)$. Con $m = 1$, el borde de $[a, b]$ son los dos extremos, con normales $-1$ y $+1$, y el término de borde es $F(b) - F(a)$, como en el apartado 4. Por el teorema de la divergencia, y porque vale en todo subdominio, la condición equivale a

   $$
   \begin{aligned}
   D = \sum_{k=1}^{m} d_k F_k.
   \end{aligned}
   $$

6. **Cuándo existe $\vec{F}$.**
   * **Si cada $F_k$ solo depende de $(\vec{x}, \vec{y})$**, $\sum_k d_k F_k = \sum_k \partial_{x_k} F_k + \sum_{i, k} \partial_{y_i} F_k \cdot z_{ik}$ es afín en $Z$. Así que $D = a + \sum_{i, k} b_{ik} \cdot z_{ik}$, con $a = \sum_k \partial_{x_k} F_k$ y $b_{ik} = \partial_{y_i} F_k$, y las condiciones de integrabilidad son

     $$
     \begin{aligned}
     \partial_{y_j} b_{ik} = \partial_{y_i} b_{jk}, \qquad \partial_{y_i} a = \sum_{k=1}^{m} \partial_{x_k} b_{ik}.
     \end{aligned}
     $$

     La primera, para cada $k$, es la simetría de las derivadas segundas de $F_k$ respecto de las $y$ (teorema de Schwarz); la segunda sale de derivar $a$ respecto de $y_i$ e intercambiar el orden de derivación. Con $m = 1$ son las del apartado 8.3.
   * **Con $m \geq 2$, $D$ no tiene por qué ser afín.** El argumento del apartado 5, punto (3), deja de valer: $F_k$ puede depender de $Z$ si las derivadas segundas se cancelan en la divergencia. Por ejemplo, con $n = m = 2$, por el teorema de Schwarz,

     $$
     \begin{aligned}
     d_1\big(f_1 \cdot \partial_2 f_2\big) + d_2\big(-f_1 \cdot \partial_1 f_2\big) = \partial_1 f_1 \cdot \partial_2 f_2 - \partial_2 f_1 \cdot \partial_1 f_2 = \det J_{\vec{f}},
     \end{aligned}
     $$

     que es cuadrático en $Z$. Con $m = 1$ no ocurre, porque $\dfrac{dF}{dx}$ contiene $\sum_i \partial_{y_i'} F \cdot y_i''$, que no se cancela con nada.
   * **$\vec{F}$ no es única:** se le puede sumar cualquier campo de divergencia nula. Con $m = 1$, solo una constante.

7. **El lema del apartado 6.2 y la identidad.** Por la regla del producto en cada $k$ y la definición de $\varphi_i$, para toda $\vec{\eta}$ de clase $C^1$:

   $$
   \begin{aligned}
   &\sum_{i=1}^{n} \Big(\partial_{f_i} \bsL \cdot \eta_i + \sum_{k=1}^{m} u_{ik} \cdot d_k \eta_i\Big) \\
   &\qquad = \sum_{i=1}^{n} \varphi_i \cdot \eta_i + \sum_{k=1}^{m} d_k\Big(\sum_{i=1}^{n} u_{ik} \cdot \eta_i\Big).
   \end{aligned}
   $$

   Lo aplicamos con $\vec{\eta} = \bar{\vec{\xi}}$, añadimos la hipótesis $D = \sum_k d_k F_k$ y deshacemos $\bar{\xi}_i$ como en el apartado 8.4:

   $$
   \begin{aligned}
   \sum_{i=1}^{n} u_{ik} \cdot \bar{\xi}_i + \tau_k \cdot \bsL &= \sum_{i=1}^{n} u_{ik} \cdot \xi_i - \sum_{l=1}^{m} T_{kl} \cdot \tau_l, \\
   T_{kl} &:= \sum_{i=1}^{n} u_{ik} \cdot \partial_l f_i - \delta_{kl} \cdot \bsL.
   \end{aligned}
   $$

   $T$ es una matriz $m \times m$, el **tensor de energía-momento canónico**, y generaliza $\bsH$: con $m = 1$, $T_{11} = \bsH$. Queda la **identidad de Noether para campos**, válida para toda $\vec{f}$ de clase $C^2$:

   $$
   \begin{aligned}
   \sum_{k=1}^{m} d_k J_k = -\sum_{i=1}^{n} \varphi_i \cdot \bar{\xi}_i, \qquad J_k := \sum_{i=1}^{n} u_{ik} \cdot \xi_i - \sum_{l=1}^{m} T_{kl} \cdot \tau_l - F_k.
   \end{aligned}
   $$

   El campo $\vec{J} = (J_1, \dots, J_m)$ es la **corriente de Noether**. Con $m = 1$, $J_1$ es la $Q$ del apartado 8.4.

8. **El teorema: una ley de conservación local.** Sobre una solución, $\sum_k d_k J_k = 0$: la corriente tiene divergencia nula en todo punto, pero ya no hay una constante. Para obtenerla, separamos el tiempo, $x_1 = t$, de las variables espaciales $x_2, \dots, x_m$, e integramos en una región espacial fija $R$:

   $$
   \begin{aligned}
   \dfrac{d}{dt} \int_R J_1\, d^{m-1}x = -\int_{\partial R} \sum_{k=2}^{m} J_k \cdot n_k\, dS,
   \end{aligned}
   $$

   por la derivación bajo el signo integral y el teorema de la divergencia en las variables espaciales. Si el flujo por el borde se anula (extremos fijos, condiciones periódicas o campos que se anulan en el infinito), $\int_R J_1\, d^{m-1}x$ es constante. Este paso ocupa el lugar del teorema del valor medio del apartado 6.3, y la conservación depende ahora también de las condiciones de contorno.

9. **Ejemplo: la cuerda vibrante.** Con $n = 1$, $m = 2$, $(x_1, x_2) = (t, x)$ (aquí $x$ es la posición sobre la cuerda) y la velocidad de propagación $c$:

   $$
   \begin{aligned}
   \bsL = \dfrac{1}{2} \cdot (\partial_t f)^2 - \dfrac{c^2}{2} \cdot (\partial_x f)^2, \qquad u_1 = \partial_t f, \qquad u_2 = -c^2 \cdot \partial_x f.
   \end{aligned}
   $$

   La traslación en el tiempo, $\vec{\tau} = (1, 0)$ y $\xi = 0$, es una simetría con $\vec{F} = \vec{0}$, porque $\bsL$ no depende de $t$. Su corriente es $J_k = -T_{k1}$:

   $$
   \begin{aligned}
   J_1 = -\mathcal{E}, \quad \mathcal{E} := \dfrac{1}{2} \cdot (\partial_t f)^2 + \dfrac{c^2}{2} \cdot (\partial_x f)^2, \qquad J_2 = c^2 \cdot \partial_x f \cdot \partial_t f.
   \end{aligned}
   $$

   La ley de conservación es $d_t \mathcal{E} = d_x\big(c^2 \cdot \partial_x f \cdot \partial_t f\big)$ sobre las soluciones de $\partial_t^2 f = c^2 \cdot \partial_x^2 f$. Con los extremos fijos, $\partial_t f = 0$ en ellos, el flujo se anula y la energía, la integral de $\mathcal{E}$ a lo largo de la cuerda, es constante.

### Pregunta 2: la partícula en un campo central

#### Precisiones previas

* **Es el apartado 8, no la pregunta 1.** Hay una sola variable independiente, $t$ (la $x$ de los apartados anteriores), y $n = 3$ funciones, $\vec{f} = \vec{r} = (x, y, z)$. Aquí $x, y, z$ son las coordenadas del punto, no la variable independiente ni los argumentos de $\bsL$; por eso escribimos los generadores y $F$ como funciones de $(t, \vec{r})$. El punto indica la derivada respecto de $t$ (la prima de antes), y $m$ es la masa (en la pregunta 1 era el número de variables).
* **El lagrangiano** es $\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{r}}|^2 - V(|\vec{r}|)$, con $\dot{\vec{r}}$ en la energía cinética (en la pregunta está escrito $|\vec{r}|^2$). Escribimos $r = |\vec{r}|$, $\vec{p} = m \cdot \dot{\vec{r}}$ y $V'$ para la derivada de $V$ respecto de $r$.
* **En esféricas**, $x = r \cdot \sin\theta \cdot \cos\phi$, $y = r \cdot \sin\theta \cdot \sin\phi$ y $z = r \cdot \cos\theta$, con $r > 0$ y $0 < \theta < \pi$ (fuera del eje $z$, donde las coordenadas esféricas son singulares). Aviso: $\phi$ es el ángulo; las $\varphi_i$ siguen siendo las expresiones de Euler–Lagrange. Entonces

  $$
  \begin{aligned}
  \bsL &= \dfrac{1}{2} \cdot m \cdot \big(\dot{r}^2 + r^2 \cdot \dot{\theta}^2 + r^2 \cdot \sin^2\theta \cdot \dot{\phi}^2\big) - V(r), \\
  p_r &= m \cdot \dot{r}, \qquad p_\theta = m \cdot r^2 \cdot \dot{\theta}, \qquad p_\phi = m \cdot r^2 \cdot \sin^2\theta \cdot \dot{\phi}.
  \end{aligned}
  $$

* **$Q$ no depende de las coordenadas.** Si $\vec{r} = \vec{R}(\vec{q})$ es un cambio de coordenadas que no depende de $t$, entonces $\dot{\vec{r}} = J_{\vec{R}} \cdot \dot{\vec{q}}$ y, por la regla de la cadena, $\vec{p}_{\vec{q}} = J_{\vec{R}}^{\mathsf{T}} \cdot \vec{p}_{\vec{r}}$. El generador se transforma como una velocidad, $\vec{\xi}_{\vec{r}} = J_{\vec{R}} \cdot \vec{\xi}_{\vec{q}}$, así que

  $$
  \begin{aligned}
  \vec{p}_{\vec{q}} \cdot \vec{\xi}_{\vec{q}} = \big(J_{\vec{R}}^{\mathsf{T}} \cdot \vec{p}_{\vec{r}}\big) \cdot \vec{\xi}_{\vec{q}} = \vec{p}_{\vec{r}} \cdot \big(J_{\vec{R}} \cdot \vec{\xi}_{\vec{q}}\big) = \vec{p}_{\vec{r}} \cdot \vec{\xi}_{\vec{r}}.
  \end{aligned}
  $$

  Del mismo modo, $\bsH$ y $F$ son los mismos en las dos coordenadas. Las coordenadas deciden qué cantidades se ven con facilidad, no cuáles existen.

#### Giros

* **Giro de ángulo $\varepsilon$ alrededor del eje de vector unitario $\vec{n}$:** $\tau = 0$ y $\vec{\xi} = \vec{n} \times \vec{r}$.
* **Es una simetría con $F = 0$:**

  $$
  \begin{aligned}
  D = \nabla_{\vec{r}} \bsL \cdot \vec{\xi} + \vec{p} \cdot \dot{\vec{\xi}} = -\dfrac{V'(r)}{r} \cdot \vec{r} \cdot (\vec{n} \times \vec{r}) + m \cdot \dot{\vec{r}} \cdot (\vec{n} \times \dot{\vec{r}}) = 0,
  \end{aligned}
  $$

  porque un producto mixto con un vector repetido es nulo.
* **La cantidad conservada**, por la propiedad cíclica del producto mixto, es

  $$
  \begin{aligned}
  Q = \vec{p} \cdot (\vec{n} \times \vec{r}) = \vec{n} \cdot (\vec{r} \times \vec{p}) = \vec{n} \cdot \vec{\ell}, \qquad \vec{\ell} := \vec{r} \times \vec{p}.
  \end{aligned}
  $$

  Los tres ejes dan las tres componentes del momento angular.
* **En esféricas, el giro alrededor del eje $z$** es $\phi \mapsto \phi + \varepsilon$, con $\vec{\xi} = (0, 0, 1)$ en $(r, \theta, \phi)$. $\bsL$ no depende de $\phi$ (es una coordenada **cíclica**), así que $D = \partial_\phi \bsL = 0$ y $Q = p_\phi = m \cdot r^2 \cdot \sin^2\theta \cdot \dot{\phi} = \ell_z$. Es la regla general: el momento de una coordenada cíclica se conserva (el teorema con $\tau = 0$ y $\vec{\xi}$ igual a un vector de la base).
* **Los giros alrededor de los ejes $x$ e $y$** no desplazan una sola coordenada esférica. Sus generadores se obtienen con la regla de la cadena. Para el eje $x$, $\vec{\xi} = (1, 0, 0) \times \vec{r} = (0, -z, y)$ en cartesianas; derivando $\cos\theta = \dfrac{z}{r}$ y $\tan\phi = \dfrac{y}{x}$ en esa dirección, con $r$ fijo, sale la primera línea, y la segunda, igual:

  $$
  \begin{aligned}
  \text{eje } x&: \quad (\xi_r, \xi_\theta, \xi_\phi) = (0, -\sin\phi, -\cot\theta \cdot \cos\phi), \\
  \text{eje } y&: \quad (\xi_r, \xi_\theta, \xi_\phi) = (0, \cos\phi, -\cot\theta \cdot \sin\phi).
  \end{aligned}
  $$

  Con $Q = p_\theta \cdot \xi_\theta + p_\phi \cdot \xi_\phi$:

  $$
  \begin{aligned}
  \ell_x &= -m \cdot r^2 \cdot \big(\sin\phi \cdot \dot{\theta} + \sin\theta \cdot \cos\theta \cdot \cos\phi \cdot \dot{\phi}\big), \\
  \ell_y &= m \cdot r^2 \cdot \big(\cos\phi \cdot \dot{\theta} - \sin\theta \cdot \cos\theta \cdot \sin\phi \cdot \dot{\phi}\big).
  \end{aligned}
  $$

  Se conservan aunque ninguna coordenada esférica sea cíclica para ellos; con el eje polar en la dirección $x$, $\ell_x$ sería el momento de un ángulo cíclico. Además, $|\vec{\ell}|^2 = p_\theta^2 + \dfrac{p_\phi^2}{\sin^2\theta}$.

#### Traslación en el tiempo

* $\tilde{t} = t + \varepsilon$: $\tau = 1$ y $\vec{\xi} = \vec{0}$. El cambio $t \mapsto t - t_0$ de la pregunta es el elemento $\varepsilon = -t_0$ de esta familia.
* $D = \partial_t \bsL \cdot \tau = 0$, porque $\bsL$ no depende explícitamente de $t$, y $F = 0$.
* $Q = -\bsH$, con

  $$
  \begin{aligned}
  \bsH &= p_r \cdot \dot{r} + p_\theta \cdot \dot{\theta} + p_\phi \cdot \dot{\phi} - \bsL \\
  &= \dfrac{1}{2} \cdot m \cdot \big(\dot{r}^2 + r^2 \cdot \dot{\theta}^2 + r^2 \cdot \sin^2\theta \cdot \dot{\phi}^2\big) + V(r) = E,
  \end{aligned}
  $$

  la energía. En cartesianas sale lo mismo, $\dfrac{1}{2} \cdot m \cdot |\dot{\vec{r}}|^2 + V(r)$.

#### Traslaciones en el espacio

* $\tilde{\vec{r}} = \vec{r} + \varepsilon \cdot \vec{e}$, con $\vec{e}$ un vector constante no nulo: $\tau = 0$ y $\vec{\xi} = \vec{e}$. El cambio $\vec{r} \mapsto \vec{r} - \vec{r}_0$ de la pregunta es el elemento con $\varepsilon \cdot \vec{e} = -\vec{r}_0$. Se escriben mejor en cartesianas: en esféricas mezclan $r$, $\theta$ y $\phi$.
* $D = \nabla_{\vec{r}} \bsL \cdot \vec{e} = -\dfrac{V'(r)}{r} \cdot (\vec{e} \cdot \vec{r})$, porque $\dot{\vec{\xi}} = \vec{0}$.
* **No es una simetría si $V' \neq 0$.** $D$ no contiene $\dot{\vec{r}}$, así que, por el apartado 8.3, tendría que ser $\partial_t F$ con $\partial_{y_i} F = 0$: $F$, y con ella $D$, solo dependerían de $t$. Pero $D$ se anula en el plano $\vec{e} \cdot \vec{r} = 0$, así que sería nula en todo punto, y eso obliga a $V'(r) \cdot (\vec{e} \cdot \vec{r}) = 0$ para todo $\vec{r}$, es decir, $V' = 0$.
* **El motivo:** $V(|\vec{r}|)$ distingue el origen $O$, el centro de fuerzas, y desplazar la trayectoria cambia su distancia a él. La cantidad de movimiento no se conserva: $\dot{\vec{p}} = -\dfrac{V'(r)}{r} \cdot \vec{r}$.
* **Solo con $V$ constante** (partícula libre) es una simetría, con $F = 0$, y da $Q = \vec{e} \cdot \vec{p}$: se conserva la cantidad de movimiento.

#### Cambio a un observador con velocidad constante

* El nuevo observador se mueve respecto de $O$ con velocidad constante $\vec{v} = \varepsilon \cdot \vec{u}$ y coincide con $O$ en $t = 0$. Mide las posiciones $\tilde{\vec{r}} = \vec{r} - \varepsilon \cdot \vec{u} \cdot t$, y el tiempo no cambia (mecánica de Galileo): $\tau = 0$ y $\vec{\xi} = -\vec{u} \cdot t$. El generador depende de la variable independiente, y la teoría lo admite: $\vec{\xi}$ es una función de $(t, \vec{r})$.
* $D = \nabla_{\vec{r}} \bsL \cdot \vec{\xi} + \vec{p} \cdot \dot{\vec{\xi}}$, es decir,

  $$
  \begin{aligned}
  D = t \cdot \dfrac{V'(r)}{r} \cdot (\vec{u} \cdot \vec{r}) - m \cdot \vec{u} \cdot \dot{\vec{r}}.
  \end{aligned}
  $$

* **Partícula libre ($V$ constante).** $D = -m \cdot \vec{u} \cdot \dot{\vec{r}} = \dfrac{d}{dt}\big(-m \cdot \vec{u} \cdot \vec{r}\big)$: es una simetría con $F = -m \cdot \vec{u} \cdot \vec{r}$, otro ejemplo con $F \neq 0$. Entonces

  $$
  \begin{aligned}
  Q = \vec{p} \cdot \vec{\xi} - F = -t \cdot \vec{u} \cdot \vec{p} + m \cdot \vec{u} \cdot \vec{r} = \vec{u} \cdot \vec{K}, \qquad \vec{K} := m \cdot \vec{r} - \vec{p} \cdot t.
  \end{aligned}
  $$

  Las tres direcciones de $\vec{u}$ dan la conservación de $\vec{K}$: $m \cdot \vec{r}(t) - \vec{p} \cdot t = m \cdot \vec{r}(0)$, el movimiento rectilíneo uniforme. Comprobación: $\dot{\vec{K}} = m \cdot \dot{\vec{r}} - \vec{p} - \dot{\vec{p}} \cdot t = -\dot{\vec{p}} \cdot t = \vec{0}$.
* **Con $V' \neq 0$ no es una simetría.** $D$ es afín en $\dot{\vec{r}}$, con término independiente $t \cdot \dfrac{V'(r)}{r} \cdot (\vec{u} \cdot \vec{r})$ y coeficientes constantes $-m \cdot u_i$. La condición de integrabilidad del apartado 8.3 (la derivada del término independiente respecto de $y_i$ es igual a la derivada respecto de $t$ del coeficiente, que es $0$) exige que el término independiente no dependa de $\vec{r}$; como en las traslaciones, eso solo ocurre si $V' = 0$. El motivo: el nuevo observador ve moverse el centro de fuerzas, y el potencial $V\big(|\tilde{\vec{r}} + \vec{v} \cdot t|\big)$ depende explícitamente del tiempo.

#### Por qué el campo central pierde las traslaciones y los cambios de velocidad

El campo central es lo que queda del problema de dos cuerpos, con $n = 6$:

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot m_1 \cdot |\dot{\vec{r}}_1|^2 + \dfrac{1}{2} \cdot m_2 \cdot |\dot{\vec{r}}_2|^2 - V(|\vec{r}_1 - \vec{r}_2|).
\end{aligned}
$$

* **Ahí sí son simetrías** desplazar las dos partículas a la vez, $\vec{\xi} = (\vec{e}, \vec{e})$, y cambiar de observador, $\vec{\xi} = (-\vec{u} \cdot t, -\vec{u} \cdot t)$, porque $|\vec{r}_1 - \vec{r}_2|$ no cambia. Dan la cantidad de movimiento total, $\vec{P} = \vec{p}_1 + \vec{p}_2$, y $\vec{K} = M \cdot \vec{R} - \vec{P} \cdot t$, con $M = m_1 + m_2$ y $\vec{R}$ el centro de masas, que se mueve con velocidad constante.
* **Al separar el centro de masas**, el movimiento relativo, $\vec{r} = \vec{r}_1 - \vec{r}_2$, es el problema del campo central, con la masa reducida $\dfrac{m_1 \cdot m_2}{M}$ en el lugar de $m$. De las transformaciones de Galileo solo conserva los giros y la traslación en el tiempo.
* **Una precisión.** Para potenciales concretos hay más cantidades conservadas: con el de Kepler, $V = -\dfrac{k}{r}$, el vector de Laplace–Runge–Lenz. Su simetría tiene un generador que depende de la velocidad, y queda fuera del marco de este borrador, donde $\tau$ y $\vec{\xi}$ solo dependen de $(t, \vec{r})$.

#### Resumen

| Transformación | $(\tau, \vec{\xi})$ | Simetría | $F$ | $Q$ |
| -------------------------- | ---------------------- | ------------------ | ------------------ | ---------------- |
| Giro alrededor de $\vec{n}$ | $(0, \vec{n} \times \vec{r})$ | Sí | $0$ | $\vec{n} \cdot \vec{\ell}$ |
| Traslación en el tiempo | $(1, \vec{0})$ | Sí | $0$ | $-\bsH = -E$ |
| Traslación en el espacio | $(0, \vec{e})$ | Solo si $V' = 0$ | $0$ | $\vec{e} \cdot \vec{p}$ |
| Cambio de velocidad | $(0, -\vec{u} \cdot t)$ | Solo si $V' = 0$ | $-m \cdot \vec{u} \cdot \vec{r}$ | $\vec{u} \cdot \vec{K}$ |

Table: Partícula en un campo central $V(r)$. En las dos últimas filas, $F$ y $Q$ son los de la partícula libre.

Las cuentas de estos comentarios (la identidad para campos, con $D$ calculado desde la definición; la cuerda; los generadores en esféricas y $\ell_x$, $\ell_y$, $\ell_z$; la energía; los valores de $D$ de las traslaciones y de los cambios de velocidad; la partícula libre y los dos cuerpos) están comprobadas en el mismo archivo de SymPy.

<!-- FIN DE LOS COMENTARIOS -->
