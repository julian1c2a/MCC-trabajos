---
author: "Julián Calderón Almendros"
---

# El teorema de Noether: parte matemática (versión 2)

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-10
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

Esta serie continúa «El formalismo lagrangiano». Allí se buscaban las funciones que hacen estacionario un funcional; aquí se estudian las transformaciones que no cambian el funcional y lo que se deduce de ellas: cantidades que no cambian a lo largo de las soluciones. Como aquella serie, estos documentos son un superconjunto de lo que entra en el trabajo «La importancia de las simetrías en física».

La versión 2 de la serie consta de cuatro documentos:

* «El teorema de Noether: parte matemática (versión 2)»: la teoría, con una función, varias funciones y varias variables, los flujos, las derivadas de Fréchet y de Lie, y una guía de dimensión infinita.
* «El teorema de Noether: ejemplos matemáticos (versión 2)»: el camino más corto, como gráfica y en forma paramétrica, las ecuaciones con la estructura de las de Newton y la ecuación de Laplace.
* «El teorema de Noether: parte física (versión 2)» (en preparación): los sistemas de partículas, el grupo de Galileo, el grupo de Lorentz y la mecánica cuántica no relativista.
* «El teorema de Noether: ejemplos físicos (versión 2)» (en preparación).

**Diferencias con la versión 1**, cuyos documentos se conservan. La versión 1 escribe la familia de transformaciones $\bsT_\epsilon$, con el parámetro $\epsilon$, y usa generadores que pueden depender de las derivadas. La versión 2 usa $\Phi_\varepsilon$ y $\varepsilon$, como el trabajo «La importancia de las simetrías en física», y transformaciones de los puntos con generador $(\tau, \xi)$; la relación entre las dos formas está en el apartado 9.6 de la parte matemática.

## 1. Qué buscamos

Hasta ahora hemos planteado un problema de variación sobre un funcional $\bsS$, que depende de una función $f$ de una variable real, y hemos buscado las funciones $f$ que lo hacen estacionario. $\bsS[f]$ es la integral, entre los extremos del intervalo de la variable independiente, de $\bsL(f, f', x)$: una función, el **lagrangiano**, que convierte la función $f$, su derivada $f'$ y cada punto $x$ del intervalo en un valor a integrar.

Ahora buscamos **transformaciones de $f$ que no cambien el valor de $\bsS[f]$**.

### 1.1. Planteamiento y definiciones

* **El lagrangiano.** $\bsL(y, y', x)$ es una función de tres variables reales, de clase $C^2$ en un abierto de $\mathbb{R}^3$ (en los ejemplos, en todo $\mathbb{R}^3$); $y'$ es solo el nombre de su segunda variable, que a lo largo de una función ocupa el lugar de la derivada (apartado 5, punto (2)). A lo largo de una función $f$ escribimos $\bsL(f, f')(x) := \bsL\big(f(x), f'(x), x\big)$.
* **Sus derivadas parciales.** $\partial_f \bsL$, $\partial_{f'} \bsL$ y $\partial_x \bsL$ son las derivadas parciales de $\bsL$ respecto de su primera, segunda y tercera variable, evaluadas en $\big(f(x), f'(x), x\big)$; cuando no se evalúan a lo largo de una función, las escribimos $\partial_y \bsL$ y $\partial_{y'} \bsL$. $\partial_x \bsL$ es la derivada respecto de la tercera variable con las otras dos fijas, y no la derivada de $x \mapsto \bsL(f, f')(x)$.
* **El funcional.** Un funcional es una aplicación que asigna un número real a cada función de un conjunto. Aquí, $f: [a, b] \to \mathbb{R}$ es de clase $C^2$, y para cada subintervalo $[c, d] \subseteq [a, b]$ el funcional es

  $$
  \begin{aligned}
  \bsS_{[c,d]}[f] := \int_c^d \bsL(f, f')(x) \,dx, \qquad \bsS := \bsS_{[a,b]}.
  \end{aligned}
  $$

* **Estacionariedad y ecuación de Euler–Lagrange** (lo establecido en «El formalismo lagrangiano: parte matemática»). La **variación primera** de $\bsS$ en una función $f_0$, en la dirección de una función $h$ de clase $C^2$, es

  $$
  \begin{aligned}
  \bsdelta\bsS[f_0](h) := \left.\dfrac{d}{d\varepsilon} \bsS[f_0 + \varepsilon \cdot h]\right|_{\varepsilon = 0} = \int_a^b \big(\partial_f \bsL \cdot h + \partial_{f'} \bsL \cdot h'\big) \,dx,
  \end{aligned}
  $$

  con las derivadas de $\bsL$ evaluadas a lo largo de $f_0$. $f_0$ hace **estacionario** a $\bsS$ con los extremos fijos si $\bsdelta\bsS[f_0](h) = 0$ para toda $h$ con $h(a) = h(b) = 0$; lo escribimos $\bsdelta\bsS[f_0] = 0$. Allí se demuestra que eso ocurre si y solo si $f_0$ cumple en todo $[a, b]$ la **ecuación de Euler–Lagrange**, $\partial_f \bsL - \dfrac{d}{dx}\partial_{f'} \bsL = 0$. Sus **soluciones** son las funciones de clase $C^2$ que la cumplen.
* **Sin condiciones de contorno.** En «El formalismo lagrangiano» todas las funciones del conjunto de partida tenían los mismos valores en los extremos, porque se buscaban las estacionarias con los extremos fijos. Aquí no se impone ninguna condición de contorno: la condición de simetría (apartado 4) se refiere a todas las funciones de clase $C^2$, y el teorema, a todas las soluciones de las ecuaciones de Euler–Lagrange, sean cuales sean sus valores en los extremos.
* **Lo que se busca.** Una **simetría** es una familia de transformaciones, que depende de un parámetro real $\varepsilon$, que no cambia $\bsS$ salvo un término que solo depende de los extremos del intervalo y salvo términos de orden $\varepsilon^2$; la definición precisa es la del apartado 4. Una **cantidad conservada** es una expresión construida con $x$, $f(x)$ y $f'(x)$ que toma el mismo valor en todo $[a, b]$ cuando $f$ es una solución. El **teorema de Noether** asocia a cada simetría una cantidad conservada (apartados 6.3 y 6.5).
* **Órdenes de magnitud.** $O(\varepsilon^2)$ es un término acotado, en valor absoluto, por $C \cdot \varepsilon^2$ para $|\varepsilon|$ pequeño, con $C$ constante; $o(\varepsilon)$ es un término que, dividido por $\varepsilon$, tiende a $0$ con $\varepsilon$. «Para $|\varepsilon| \ll 1$» significa «para todo $\varepsilon$ con $|\varepsilon| < \varepsilon_0$», con un $\varepsilon_0 > 0$ que depende de los datos: la familia, la función y el intervalo.

### 1.2. Cómo se generaliza y avisos de notación

El documento empieza con una función de una variable y lo generaliza tres veces: a $n$ funciones de una variable (apartado 7), a $n$ funciones de $m$ variables (apartado 8) y a funciones con valores en un espacio vectorial de dimensión infinita (apartado 10). La notación de cada caso se introduce en su apartado, con un aviso cuando cambia, y la tabla del final del documento la resume.

**Palabras con dos usos.**

* **Campo.** Un **campo vectorial** en una región del plano, o de $\mathbb{R}^N$, asigna a cada punto un vector; es el sentido de los apartados 3 y 9. Un **campo de fuerzas**, como el campo uniforme o el campo central de los ejemplos, es un campo vectorial que da la fuerza en cada punto. En física se llama también **campo** a una función de las variables espaciales y del tiempo, como el desplazamiento de una cuerda (apartado 8.7).
* **Flujo.** El **flujo de un campo vectorial** es la familia de transformaciones que mueve cada punto a lo largo de la curva que tiene en cada punto la dirección del campo (apartados 3.3 y 9.1). El **flujo de un campo a través de una superficie** es la cantidad que la atraviesa (apartados 8.4 y 8.7).

**Letras con varios usos.**

* $\tilde{x}$: la función $\tilde{x}(x)$ del apartado 2 y, en las integrales de los apartados 4 y 5, la variable de integración del intervalo transformado.
* $d$: el extremo derecho de los subintervalos $[c, d]$; en $dx$, $\dfrac{d}{dx}$, $d_x$ y $d_{x_k}$ forma parte del símbolo de derivada.
* $c$: el extremo izquierdo de los subintervalos; en el apartado 8.8, la velocidad de propagación de las ondas.
* $k$: el índice de las variables (apartado 8); en algunos ejemplos, una constante, con aviso en cada caso.
* $m$: el número de variables (apartado 8); en los comentarios del final, una masa.
* $B$: el campo magnético del apartado 7.5; una caja en el apartado 8.
* $\eta$: el segundo parámetro de la ley de grupo (apartado 3.3); una función cualquiera de clase $C^1$ en los lemas de los apartados 6.5, 7.4 y 8.6.
* $g$: la aceleración de la gravedad en los ejemplos; una función cualquiera en el apartado 9.2.
* $i$: el índice de las funciones; en el apartado 10.3, la unidad imaginaria.
* $H$: $\bsH$, en negrita, es la función del apartado 6.5; $\hat{H}$, con gorro, un operador (apartado 10.3); $\mathcal{H}$, caligráfica, un espacio de Hilbert (apartado 10).
* $\vec{A}$: el potencial vector en el apartado 7.5 y el vector de Laplace–Runge–Lenz en el 9.6; $\hat{A}$, con gorro, un operador (apartado 10).
* $\alpha$, $\beta$, $\gamma$, $\kappa$, $\lambda$: constantes, coeficientes o funciones auxiliares que se definen en cada lugar. Por ejemplo, $\alpha$ es un coeficiente en los apartados 6.6, 7.3 y 8.5 y el ángulo de la tangente en «El teorema de Noether: ejemplos matemáticos (versión 2)», apartado 1.

## 2. La transformación actúa sobre los puntos del plano

Para poder mover a la vez la variable $x$ y los valores de $f$, la transformación no actúa directamente sobre $f$, sino sobre los puntos $(x, y)$ del plano:

$$
\begin{aligned}
\Phi(x, y) = \big(X(x, y),\ Y(x, y)\big).
\end{aligned}
$$

* $X$ dice dónde va la variable, e $Y$, dónde va el valor.
* La nueva variable puede depender también del valor. Por ejemplo, en un giro del plano de ángulo $\varepsilon$, $X(x, y) = x \cdot \cos\varepsilon - y \cdot \sin\varepsilon$.

Una función $f$ se transforma transformando su gráfica, la curva $x \mapsto \big(x, f(x)\big)$, es decir, el par de funciones $(Id, f)$, con $Id(x) := x$ la función identidad. La curva transformada, que escribimos $\Phi(Id, f)$, es $x \mapsto \Phi\big(x, f(x)\big)$, y es la gráfica de una nueva función $\tilde{f}$, definida sobre una nueva variable $\tilde{x}$:

$$
\begin{aligned}
\tilde{x}(x) := X\big(x, f(x)\big), \qquad \tilde{f}\big(\tilde{x}(x)\big) := Y\big(x, f(x)\big).
\end{aligned}
$$

* **Cuándo existe $\tilde{f}$.** La segunda definición solo tiene sentido si cada punto nuevo procede de un solo punto viejo, es decir, si $\tilde{x}$ es invertible. Para las familias del apartado 3 lo es cuando el parámetro es pequeño (apartado 3.1).
* **A lo largo de la gráfica.** Llamamos también $\tilde{y}(x) := Y\big(x, f(x)\big)$. La gráfica transformada es la curva $x \mapsto \big(\tilde{x}(x), \tilde{y}(x)\big)$, y la definición de $\tilde{f}$ se escribe $\tilde{f}\big(\tilde{x}(x)\big) = \tilde{y}(x)$. $X$ e $Y$ son funciones de dos variables, definidas en el plano; $\tilde{x}$ e $\tilde{y}$ son funciones de una variable, definidas a lo largo de $f$, y sus derivadas, $\tilde{x}'$ e $\tilde{y}'$, incluyen la dependencia a través de $f$.

**Cómo se generaliza.** El plano es el caso de una función de una variable. En los apartados siguientes cambia el espacio de los puntos, pero no la idea: $\mathbb{R} \times \mathbb{R}^n$ con $n$ funciones (apartado 7), $\mathbb{R}^m \times \mathbb{R}^n$ con $m$ variables (apartado 8) y $\mathbb{R} \times E$, con $E$ un espacio de Banach, un espacio vectorial con una norma en el que toda sucesión de Cauchy converge (apartados 9.2 y 10). En todos los casos la transformación mueve a la vez la variable y los valores, y la función transformada se obtiene transformando su gráfica. El mapa de la notación, al final del documento, resume cómo cambia cada símbolo.

## 3. Una familia de transformaciones

No trabajamos con una transformación, sino con una familia $\Phi_\varepsilon = (X_\varepsilon, Y_\varepsilon)$, que depende de un parámetro real $\varepsilon$. Cada $\Phi_\varepsilon$ está definida en un abierto $U$ del plano que contiene la gráfica de $f$ (en los ejemplos, todo el plano), para $|\varepsilon| < \varepsilon_0$.

### 3.1. Lo que le pedimos

1. **Que para $\varepsilon = 0$ sea la identidad:** $\Phi_0(x, y) = (x, y)$. Entonces, con $\varepsilon = 0$, $\tilde{x}(x) = x$ y $\tilde{f} = f$: la familia empieza sin cambiar nada.
   * Es lo mismo que pedir que $\Phi_0$ sea el elemento neutro de la composición: $\Phi_0 \circ \Phi_\varepsilon = \Phi_\varepsilon \circ \Phi_0 = \Phi_\varepsilon$.
2. **Que dependa de $\varepsilon$ de forma derivable:** $\Phi_\varepsilon(x, y)$ es de clase $C^2$ en $(\varepsilon, x, y)$.
   * Así, para $|\varepsilon| \ll 1$, $\tilde{x}(x)$ es estrictamente creciente, porque su derivada está próxima a $1$; tiene inversa, y $\tilde{f}$ está bien definida.

Estas dos condiciones son las únicas que necesita el teorema de Noether, porque solo usa el primer orden en $\varepsilon$.

### 3.2. El generador

Como $\Phi_\varepsilon$ es de clase $C^2$ en $\varepsilon$ y $\Phi_0$ es la identidad, el desarrollo de Taylor en $\varepsilon$ alrededor de $\varepsilon = 0$ da

$$
\begin{aligned}
X_\varepsilon(x, y) = x + \varepsilon \cdot \tau(x, y) + O(\varepsilon^2), \qquad Y_\varepsilon(x, y) = y + \varepsilon \cdot \xi(x, y) + O(\varepsilon^2),
\end{aligned}
$$

con

$$
\begin{aligned}
\big(\tau(x, y),\ \xi(x, y)\big) := \left.\dfrac{\partial}{\partial \varepsilon} \Phi_\varepsilon(x, y)\right|_{\varepsilon = 0}.
\end{aligned}
$$

* El par $(\tau, \xi)$ es el **generador** de la familia: un campo vectorial del plano que da, en cada punto, la dirección y la rapidez con que la familia empieza a moverlo. $\tau$ mueve la variable, y $\xi$, el valor.
* Es de clase $C^1$, porque $\Phi_\varepsilon$ es de clase $C^2$.
* El teorema de Noether solo usa el generador: dos familias con el mismo generador dan la misma condición de simetría y la misma cantidad conservada (apartado 3.3, segunda observación).
* **Otra notación.** En el Tema 1, apartado 4.4, el parámetro se llama $s$ y el campo, $(\xi^t, \xi^x)$, con $t$ en el lugar de $x$.

**Tres ejemplos**, los de la versión anterior de «El teorema de Noether: parte matemática», escritos como transformaciones de los puntos:

1. **Desplazar el valor**, $\Phi_\varepsilon(x, y) = (x, y + \varepsilon)$. Entonces $\tilde{x}(x) = x$ y $\tilde{f}(x) = f(x) + \varepsilon$: la gráfica sube $\varepsilon$. El generador es $(\tau, \xi) = (0, 1)$.
2. **Desplazar la variable**, $\Phi_\varepsilon(x, y) = (x + \varepsilon, y)$. Entonces $\tilde{x}(x) = x + \varepsilon$ y $\tilde{f}(x + \varepsilon) = f(x)$, es decir, $\tilde{f}(x) = f(x - \varepsilon)$: la gráfica se desplaza $\varepsilon$ hacia la derecha. El generador es $(\tau, \xi) = (1, 0)$.
   * **Aviso del signo.** En la versión anterior, desplazar la variable es $f(x) \to f(x + \varepsilon)$, que desplaza la gráfica hacia la izquierda. Corresponde a $\Phi_\varepsilon(x, y) = (x - \varepsilon, y)$, con generador $(-1, 0)$: es la misma familia recorrida en sentido contrario, y cambian de signo el generador y la cantidad conservada.
3. **Girar el plano** un ángulo $\varepsilon$ alrededor del origen:

   $$
   \begin{aligned}
   \Phi_\varepsilon(x, y) = \big(x \cdot \cos\varepsilon - y \cdot \sin\varepsilon,\ x \cdot \sin\varepsilon + y \cdot \cos\varepsilon\big).
   \end{aligned}
   $$

   Como $\cos\varepsilon = 1 + O(\varepsilon^2)$ y $\sin\varepsilon = \varepsilon + O(\varepsilon^2)$, el generador es $(\tau, \xi) = (-y, x)$. Mueve a la vez la variable y el valor, y $\tilde{f}$ solo existe para $\varepsilon$ pequeño («El teorema de Noether: ejemplos matemáticos (versión 2)», apartado 1.4).
   * En la versión anterior, el tercer ejemplo es el giro de dos funciones, $f_1$ y $f_2$, que no mueve la variable. Necesita dos funciones y se trata en el apartado 7: los puntos son $(x, y_1, y_2)$, el generador de los valores es un vector $\vec{\xi} = (\xi_1, \xi_2)$, y el giro tiene $\tau = 0$ y $\vec{\xi} = (-y_2, y_1)$.

### 3.3. Una condición más: la ley de grupo

Se puede pedir además:

3. **Que componer sea sumar los parámetros**, de forma exacta: $\Phi_\varepsilon \circ \Phi_\eta = \Phi_{\varepsilon + \eta}$ para todo $\varepsilon$ y $\eta$.

Consecuencias:

* **La inversa sale sola:** $\Phi_{-\varepsilon} \circ \Phi_\varepsilon = \Phi_0 = Id$, así que la inversa de $\Phi_\varepsilon$ es $\Phi_{-\varepsilon}$.
* **Las transformaciones de la familia conmutan entre sí**, porque $\varepsilon + \eta = \eta + \varepsilon$. No es una restricción: las que pueden no conmutar son las de familias distintas.
  * Los giros alrededor de un mismo eje conmutan: $R_z(\alpha) \cdot R_z(\beta) = R_z(\alpha + \beta)$, donde $R_z(\alpha)$ es la matriz del giro de ángulo $\alpha$ alrededor del eje $z$,

    $$
    \begin{aligned}
    R_z(\alpha) = \begin{pmatrix} \cos\alpha & -\sin\alpha & 0 \\ \sin\alpha & \cos\alpha & 0 \\ 0 & 0 & 1 \end{pmatrix}.
    \end{aligned}
    $$
  * Los giros alrededor de ejes distintos no conmutan, pero forman familias distintas.
* **La familia es un grupo con la composición:** es cerrada, tiene elemento neutro ($\Phi_0$) e inversos ($\Phi_{-\varepsilon}$), y la composición es asociativa.
  * Se llama **grupo uniparamétrico de transformaciones**. Es el **flujo** de su generador, el campo vectorial del apartado 3.2: para cada punto $P$, la curva $\varepsilon \mapsto \Phi_\varepsilon(P)$ es la solución de la ecuación diferencial $\dfrac{d}{d\varepsilon} \Phi_\varepsilon(P) = (\tau, \xi)\big(\Phi_\varepsilon(P)\big)$ con $\Phi_0(P) = P$, y se llama **curva integral** del campo. Así, la familia se recupera de su generador (Tema 1, apartado 4.4; apartado 9.1).
  * Si la ley solo vale para $\varepsilon$ y $\eta$ pequeños, es un grupo local de transformaciones.

Dos observaciones:

* **La ley tiene que ser exacta.** Con un término de error, $\Phi_\varepsilon \circ \Phi_\eta = \Phi_{\varepsilon + \eta} + O(\varepsilon^2 + \eta^2)$, no exige nada: cualquier familia que cumpla las condiciones 1 y 2 la cumple, porque los dos lados valen $P + (\varepsilon + \eta) \cdot (\tau, \xi)(P)$ salvo términos de segundo orden en $\varepsilon$ y $\eta$.
* **El teorema no la necesita.** $\Phi_\varepsilon(x, y) = (x, y + \sin\varepsilon)$ no cumple la ley de grupo, porque $\sin\varepsilon + \sin\eta \neq \sin(\varepsilon + \eta)$; pero a primer orden es el desplazamiento vertical, $(x, y + \varepsilon)$, y da la misma cantidad conservada. La ley es útil porque siempre se puede elegir la familia de modo que la cumpla (el flujo del generador), los ejemplos físicos (traslaciones, giros, cambios de velocidad y traslación en el tiempo) ya la cumplen, y con ella la condición infinitesimal da la invariancia para todo $\varepsilon$ (apartado 9.5).

## 4. La condición de simetría

Si el dominio de $f$ es $[a, b] \subseteq \mathbb{R}$, lo que buscamos tiene que ocurrir en cada subintervalo $[c, d]$, con $a \leq c < d \leq b$:

* el funcional de $\tilde{f}$ sobre el intervalo transformado, $[\tilde{x}(c), \tilde{x}(d)]$, es igual al de $f$ sobre $[c, d]$,
* salvo un término que solo depende de los extremos,
* y salvo términos de orden $\varepsilon^2$.

Es decir:

$$
\begin{aligned}
&\forall [c,d] \subseteq [a,b], \ \forall f \in C^2([a,b]): \\
&\int_{\tilde{x}(c)}^{\tilde{x}(d)} \bsL\big(\tilde{f}(\tilde{x}), \tilde{f}'(\tilde{x}), \tilde{x}\big) \,d\tilde{x} \\
&\qquad = \int_{c}^{d} \bsL\big(f(x), f'(x), x\big) \,dx + \varepsilon \cdot \big(F(d) - F(c)\big) + O(\varepsilon^2),
\end{aligned}
$$

donde $F(x, y)$ es una función de dos variables, la misma para todas las $f$, que se evalúa en $\big(x, f(x)\big)$: depende del punto y del valor de $f$ en él. En el apartado 5, punto (3), se ve por qué no puede depender de $f'$. En la fórmula abreviamos $F(x) := F\big(x, f(x)\big)$. En la integral transformada, $\tilde{x}$ es la variable de integración, que recorre el intervalo transformado; la función $\tilde{x}(x)$ del apartado 2 da sus extremos.

* Con $F = 0$, el funcional no cambia a primer orden.
* Se admite $F \neq 0$ porque sin ese término quedarían fuera casos que necesitamos, como el desplazamiento vertical en un campo uniforme (una fuerza constante, como la gravedad cerca del suelo) o los cambios de velocidad de la relatividad de Galileo. Los dos están en la tabla del apartado 6.4: con $\bsL = \dfrac{1}{2} \cdot y'^2 - g \cdot y$, el desplazamiento $(x, y + \varepsilon)$, y con $\bsL = \dfrac{1}{2} \cdot y'^2$, el cambio de velocidad $(x, y + \varepsilon \cdot x)$.
* **Por qué un término de borde no importa.** A primer orden, el integrando transformado es $\bsL + \varepsilon \cdot \dfrac{dF}{dx}$ (apartado 5), donde $\dfrac{dF}{dx} = \partial_x F + \partial_y F \cdot f'$ es la derivada de la función compuesta $x \mapsto F\big(x, f(x)\big)$, que llamamos **derivada total** a lo largo de $f$. Sumar a $\bsL$ una derivada total no cambia qué funciones son estacionarias con los extremos fijos, porque $\int_c^d \dfrac{dF}{dx} \,dx = F(d) - F(c)$ vale lo mismo para todas las funciones con los mismos valores en los extremos. Por tanto, tampoco cambia las soluciones de las ecuaciones de Euler–Lagrange, que son esas estacionarias (apartado 1.1; véase también «El formalismo lagrangiano: anexos», «Sumar una derivada total no cambia las ecuaciones»). Lo que importa son las ecuaciones, y una derivada total no las cambia; por eso no se exige $F = 0$.

La familia $\Phi_\varepsilon$ tiene que cumplir esta condición:

* **para toda función $f \in C^2([a, b])$**, no solo para las soluciones de Euler–Lagrange, que forman una clase de funciones mucho más pequeña;
* **sin valores fijados en los extremos**, a diferencia del problema de la estacionariedad.

**Simetría y estacionariedad.** Las dos ideas usan la variación primera, pero responden a preguntas distintas:

| | Estacionariedad | Simetría |
| ---------------------- | -------------------------------------------- | -------------------------------------------- |
| Qué se fija | una función $f_0$ | una familia $\Phi_\varepsilon$, es decir, su generador $(\tau, \xi)$ |
| Qué se recorre | todas las variaciones $h$, nulas en los extremos | todas las funciones $f$, sin condiciones de contorno |
| Qué se exige | $\bsdelta\bsS[f_0] = 0$ (apartado 1.1) | $D = \dfrac{dF}{dx}$, con $D$ el coeficiente de $\varepsilon$ del integrando transformado (apartado 5) |
| De qué es propiedad | de la función $f_0$ | de $\bsL$ |
| Para qué sirve | seleccionar las soluciones | obtener cantidades constantes a lo largo de las soluciones |

Table: Estacionariedad y simetría.

## 5. La condición, paso a paso

La condición del apartado 4 compara dos integrales sobre intervalos distintos. Para ver qué exige, llevamos la integral transformada al intervalo $[c, d]$ y la desarrollamos en $\varepsilon$.

**Notación.** Usamos las funciones de una variable del apartado 2, que ahora dependen de $\varepsilon$:

$$
\begin{aligned}
\tilde{x}(x) = X_\varepsilon\big(x, f(x)\big), \qquad \tilde{y}(x) = Y_\varepsilon\big(x, f(x)\big), \qquad \tilde{f}\big(\tilde{x}(x)\big) = \tilde{y}(x).
\end{aligned}
$$

$\tilde{x}'(x)$ e $\tilde{y}'(x)$ son las derivadas de estas funciones de $x$, es decir, derivadas totales a lo largo de $f$, y no las derivadas parciales de $X_\varepsilon$ e $Y_\varepsilon$.

Con el generador del apartado 3.2, a primer orden la transformación es

$$
\begin{aligned}
X_\varepsilon(x, y) = x + \varepsilon \cdot \tau(x, y) + O(\varepsilon^2), \qquad Y_\varepsilon(x, y) = y + \varepsilon \cdot \xi(x, y) + O(\varepsilon^2),
\end{aligned}
$$

y a lo largo de $f$ escribimos $\tau(x) := \tau\big(x, f(x)\big)$ y $\xi(x) := \xi\big(x, f(x)\big)$, con sus derivadas $\tau'$ y $\xi'$ también totales.

**La cadena de igualdades:**

$$
\begin{aligned}
\int_{\tilde{x}(c)}^{\tilde{x}(d)} \bsL\big(\tilde{f}(\tilde{x}), \tilde{f}'(\tilde{x}), \tilde{x}\big) \,d\tilde{x}
&\overset{(1)}{=} \int_c^d \bsL\left(\tilde{y}(x),\ \dfrac{\tilde{y}'(x)}{\tilde{x}'(x)},\ \tilde{x}(x)\right) \cdot \tilde{x}'(x) \,dx \\
&\overset{(2)}{=} \int_c^d \Big(\bsL\big(f, f', x\big) + \varepsilon \cdot D(x)\Big) \,dx + O(\varepsilon^2) \\
&\overset{(3)}{=} \int_c^d \left(\bsL\big(f, f', x\big) + \varepsilon \cdot \dfrac{dF}{dx}\right) dx + O(\varepsilon^2) \\
&\overset{(4)}{=} \int_c^d \bsL\big(f, f', x\big) \,dx + \varepsilon \cdot \big(F(d) - F(c)\big) + O(\varepsilon^2).
\end{aligned}
$$

El primer miembro y el último son los dos lados de la condición del apartado 4. Las igualdades (1), (2) y (4) valen para cualquier transformación; la (3) es la que define la simetría.

**Por qué se cumple cada igualdad:**

* **(1) Cambio de variable $\tilde{x} = \tilde{x}(x)$.** Para $|\varepsilon| \ll 1$, $\tilde{x}(x)$ es estrictamente creciente, así que el cambio es válido. Los límites pasan a ser $c$ y $d$, y el diferencial, $d\tilde{x} = \tilde{x}'(x) \cdot dx$. El primer argumento es $\tilde{f}\big(\tilde{x}(x)\big) = \tilde{y}(x)$, por la definición de $\tilde{f}$. El segundo, $\tilde{f}'$, es la derivada respecto de la **nueva** variable; derivando respecto de $x$ la definición $\tilde{f}\big(\tilde{x}(x)\big) = \tilde{y}(x)$, por la regla de la cadena,

  $$
  \begin{aligned}
  \tilde{f}'\big(\tilde{x}(x)\big) \cdot \tilde{x}'(x) = \tilde{y}'(x)
  \quad \Longrightarrow \quad
  \tilde{f}'\big(\tilde{x}(x)\big) = \dfrac{\tilde{y}'(x)}{\tilde{x}'(x)}:
  \end{aligned}
  $$

  el cociente de las derivadas de las dos componentes de la curva transformada. El tercer argumento es el punto nuevo, $\tilde{x}(x)$.

* **(2) Desarrollo a primer orden en $\varepsilon$.** Con la transformación a primer orden,

  $$
  \begin{aligned}
  \tilde{x}(x) &= x + \varepsilon \cdot \tau(x), & \tilde{x}'(x) &= 1 + \varepsilon \cdot \tau'(x), \\
  \tilde{y}(x) &= f(x) + \varepsilon \cdot \xi(x), & \tilde{y}'(x) &= f'(x) + \varepsilon \cdot \xi'(x),
  \end{aligned}
  $$

  salvo términos de orden $\varepsilon^2$. Como $\dfrac{1}{1 + \varepsilon \cdot \tau'} = 1 - \varepsilon \cdot \tau' + O(\varepsilon^2)$,

  $$
  \begin{aligned}
  \dfrac{\tilde{y}'(x)}{\tilde{x}'(x)} = f' + \varepsilon \cdot \big(\xi' - \tau' \cdot f'\big) + O(\varepsilon^2).
  \end{aligned}
  $$

  Desarrollando $\bsL$ por Taylor en sus tres argumentos y multiplicando por $\tilde{x}'(x) = 1 + \varepsilon \cdot \tau'$, el integrando es $\bsL(f, f', x) + \varepsilon \cdot D(x) + O(\varepsilon^2)$, con

  $$
  \begin{aligned}
  D := \partial_f \bsL \cdot \xi + \partial_{f'} \bsL \cdot \big(\xi' - \tau' \cdot f'\big) + \partial_x \bsL \cdot \tau + \bsL \cdot \tau'.
  \end{aligned}
  $$

  El resto, integrado en $[c, d]$, sigue siendo de orden $\varepsilon^2$. Las derivadas segundas de $\bsL$ y de $\Phi_\varepsilon$ son continuas en un conjunto cerrado y acotado que contiene todos los puntos que intervienen: para $|\varepsilon| \leq \varepsilon_0$, los puntos $\big(f(x), f'(x), x\big)$ con $x \in [c, d]$ y los que resultan de ellos al aplicar la familia. Por tanto, están acotadas, y el resto de Taylor está acotado por $C \cdot \varepsilon^2$ con $C$ independiente de $x$; integrado en $[c, d]$, por $C \cdot (d - c) \cdot \varepsilon^2$ (es el argumento de la cota uniforme de «El formalismo lagrangiano»).

  **$D$ es del mismo tipo que $\bsL$.** $\bsL$ es una función de tres variables reales, $(y, y', x) \mapsto \bsL(y, y', x)$, que a lo largo de $f$ se evalúa en $\big(f(x), f'(x), x\big)$; aquí $y'$ es solo el nombre de la segunda variable. $D$ también lo es: sus ingredientes son las derivadas parciales de $\bsL$, que son funciones de $(y, y', x)$, y $\tau$, $\xi$ y sus derivadas totales, que también lo son, porque $\tau' = \partial_x \tau + \partial_y \tau \cdot y'$ y $\xi' = \partial_x \xi + \partial_y \xi \cdot y'$. $D$ va, por tanto, del mismo conjunto de partida que $\bsL$ al mismo conjunto de llegada, $\mathbb{R}$, y no contiene $y''$. Si $\tau$ o $\xi$ dependieran de $f'$, sus derivadas contendrían $f''$ y $D$ ya no sería del mismo tipo; con transformaciones de los puntos del plano, como las de este documento, no ocurre.

* **(3) La hipótesis de simetría.** Es la única igualdad que no vale siempre: la transformación es una simetría si $D = \dfrac{dF}{dx}$ en cada punto, para toda $f$. El término es $\varepsilon \cdot \dfrac{dF}{dx}$, con el factor $\varepsilon$.

  * **Por qué en cada punto.** La condición se pide en todo subintervalo: si $\int_c^d \left(D - \dfrac{dF}{dx}\right) dx = 0$ para todo $[c, d]$, derivando respecto de $d$, por el teorema fundamental del cálculo, el integrando, que es continuo, es nulo.
  * **Lo que se exige no es que $D$ tenga primitiva.** A lo largo de cada $f$, $D$ es una función continua de $x$ y siempre tiene primitiva, $\int_{a}^{x} D(s) \,ds$. Pero esa primitiva depende de todos los valores de $f$ entre $a$ y $x$. Lo que se exige es que la primitiva sea **local**: una sola función $F$, la misma para todas las $f$, evaluada en el punto.
  * **Los valores en un punto son libres.** En un punto $x_0$, los valores de $f$, $f'$ y $f''$ pueden elegirse con independencia: $f(x) = y_0 + y_0' \cdot (x - x_0) + \dfrac{1}{2} \cdot y_0'' \cdot (x - x_0)^2$ es de clase $C^2$ y toma en $x_0$ los valores $y_0$, $y_0'$ e $y_0''$ que se quiera. Como la condición se pide para toda $f$, una igualdad en $x_0$ entre expresiones de $f(x_0)$, $f'(x_0)$ y $f''(x_0)$ tiene que valer para todos los valores de $(y_0, y_0', y_0'', x_0)$: es una identidad entre funciones de esas variables. Es lo que permite, en los puntos siguientes, separar los términos con $y''$ y con $y'$.
  * **La condición es una igualdad entre funciones del mismo tipo que $\bsL$.** Si $F$ dependiera de $y'$, $\dfrac{dF}{dx}$ contendría el término $\partial_{y'} F \cdot f''$, y $D$ no contiene $f''$; como $f''$ es libre, $\partial_{y'} F = 0$. Por tanto, $F$ solo depende de $x$ y de $y$, como se ha dicho en el apartado 4, y la condición es la identidad

    $$
    \begin{aligned}
    D(y, y', x) = \partial_x F(x, y) + \partial_y F(x, y) \cdot y' \qquad \text{para todo } (y, y', x),
    \end{aligned}
    $$

    entre dos funciones de tres variables. Como el lado derecho es una función afín de $y'$, $D$ también tiene que serlo.
  * **Ser afín es necesario, pero no basta.** Si $D = \alpha(x, y) + \beta(x, y) \cdot y'$, hace falta una $F$ con $\partial_x F = \alpha$ y $\partial_y F = \beta$. Llamamos $\alpha$ y $\beta$ a los coeficientes, y no $a$ y $b$, para no confundirlos con los extremos de $[a, b]$. Si $\alpha$ y $\beta$ son de clase $C^1$, $F$ es de clase $C^2$ y, por el teorema de Schwarz, $\partial_y \partial_x F = \partial_x \partial_y F$, lo que exige la **condición de integrabilidad** $\partial_y \alpha = \partial_x \beta$.
  * **El lenguaje de las formas diferenciales.** La expresión $\omega = \alpha \cdot dx + \beta \cdot dy$, con $\alpha$ y $\beta$ continuas en un abierto $U$ del plano, se llama **forma diferencial de primer grado**; aquí funciona como una notación para el par $(\alpha, \beta)$. Es **exacta** si existe una función $F$ de clase $C^1$, su **primitiva**, con $\partial_x F = \alpha$ y $\partial_y F = \beta$; con $\alpha$ y $\beta$ de clase $C^1$, es **cerrada** si $\partial_y \alpha = \partial_x \beta$. Por el teorema de Schwarz, toda forma exacta con coeficientes de clase $C^1$ es cerrada. La condición de simetría pide que la forma de $D$ sea exacta.
  * **Cuándo basta la condición: el lema de Poincaré.** Un abierto $U$ es **estrellado** respecto de un punto $P_*$ si contiene el segmento que une $P_*$ con cada uno de sus puntos; por ejemplo, un rectángulo, un disco o todo el plano. El **lema de Poincaré** dice que, en un abierto estrellado, toda forma cerrada es exacta; la primitiva se obtiene integrando $\omega$ a lo largo de esos segmentos (la fórmula está en el apartado 7.3). En un abierto con agujeros no basta: en el plano sin el origen, $\omega = \dfrac{-y \cdot dx + x \cdot dy}{x^2 + y^2}$ es cerrada, pero no exacta. Sus primitivas en cada región estrellada que no contiene el origen son el ángulo polar más una constante, y el ángulo polar no puede definirse de forma continua a lo largo de una vuelta completa alrededor del origen.
  * **Un caso que se reconoce enseguida.** Si $D$ no depende de $y'$, $\beta = 0$, y la condición de integrabilidad se reduce a $\partial_y \alpha = 0$: $D$ solo puede depender de $x$, y entonces $F(x) = \int_a^x D(s) \,ds$. Si $D$ depende de $y$ y no de $y'$, la transformación no es una simetría. Por ejemplo, con el oscilador, $\bsL = \dfrac{1}{2} \cdot y'^2 - \dfrac{k}{2} \cdot y^2$ ($k$ es aquí la constante elástica), el desplazamiento vertical da $D = \partial_y \bsL = -k \cdot y$, que depende de $y$: no es una simetría.
  * **Un ejemplo de cada caso**, con $\bsL = \dfrac{1}{2} \cdot y'^2 - g \cdot y$ (el tiro vertical, con $x$ como tiempo, masa $1$ y $g > 0$ la aceleración de la gravedad):
    * desplazamiento vertical, $\Phi_\varepsilon(x, y) = (x, y + \varepsilon)$: $\tau = 0$, $\xi = 1$ y $D = \partial_y \bsL = -g$, que es $\partial_x F$ con $F = -g \cdot x$. Es una simetría;
    * escala de los valores, $\Phi_\varepsilon(x, y) = \big(x, (1 + \varepsilon) \cdot y\big)$: $\tau = 0$, $\xi = y$, $\xi' = y'$ y $D = -g \cdot y + y'^2$. A lo largo de cada $f$ tiene primitiva, pero es cuadrática en $y'$, y ninguna $F(x, y)$ la reproduce. No es una simetría.

* **(4) Regla de Barrow.** $\int_c^d \dfrac{dF}{dx} \,dx = F(d) - F(c)$.

Si la variable no se mueve, $\tau = 0$, y $D$ se reduce a $\partial_f \bsL \cdot \xi + \partial_{f'} \bsL \cdot \xi'$: el integrando de la variación primera del apartado 1.1, con $\xi$ en el lugar de $h$, pero con dos diferencias: $h$ era una función cualquiera, independiente de $f$ y nula en los extremos; $\xi$ es una regla fija, $\xi\big(x, f(x)\big)$, que se calcula a partir de $f$ y no tiene por qué anularse en los extremos.

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

**Qué no hemos usado.** Ni la hipótesis de simetría, $D = \dfrac{dF}{dx}$, ni que $f$ sea una solución de Euler–Lagrange. Por tanto, $D = \varphi \cdot \xi + (p \cdot \xi)'$ es una identidad: vale para toda $f \in C^2([a, b])$ y para toda transformación con $\tau = 0$. El paso siguiente consiste en añadirle la hipótesis de simetría.

### 6.3. La hipótesis de simetría: identidad y teorema de Noether

Ahora usamos la hipótesis de simetría (apartado 5, punto (3)): la integral del integrando transformado sobre el intervalo transformado es igual a la del integrando original sobre su intervalo, salvo un término que solo depende de los extremos, $\varepsilon \cdot \big(F(d) - F(c)\big)$, y salvo términos de orden $\varepsilon^2$. Eso equivale a $D = \dfrac{dF}{dx}$ en cada punto, también para toda $f$.

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

**Identidad de Noether** (caso $\tau = 0$). Para toda $f \in C^2([a, b])$, sea o no una solución,

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

Por el teorema del valor medio, una función continua en $[a, b]$, derivable en el interior y con derivada nula, es constante. $p \cdot \xi - F$ cumple estas hipótesis, porque $p$, $\xi$ y $F\big(x, f(x)\big)$ son de clase $C^1$. Por tanto, la cantidad

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

* **Primera fila.** La ecuación de Euler–Lagrange es $f'' = 0$, así que $f = y_0 + v_0 \cdot x$, con $y_0$ y $v_0$ constantes, y $Q = f' = v_0$: el momento conjugado $p$. $\bsL$ no depende de $y$; se dice que $y$ es una **coordenada cíclica**, y su momento conjugado se conserva (apartado 6.7).
* **Segunda fila.** La ecuación es $f'' = -g$, y $\dfrac{d}{dx}(f' + g \cdot x) = -g + g = 0$. $Q$ es la velocidad en $x = 0$.
* **Tercera fila.** $D = 0 \cdot x + f' \cdot 1 = f' = \dfrac{d}{dx} f$, así que $F(x, y) = y$. Con $f = y_0 + v_0 \cdot x$, $Q = x \cdot v_0 - (y_0 + v_0 \cdot x) = -y_0$: menos la posición en $x = 0$. Aquí $\xi$ depende del punto, y $Q$ ya no es un momento.

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
\int_{\tilde{x}(c)}^{\tilde{x}(d)} \bsL(\tilde{f}, \tilde{f}')(\tilde{x}) \,d\tilde{x} - \int_c^d \bsL(f, f')(x) \,dx = \varepsilon \cdot \int_c^d D(x) \,dx + O(\varepsilon^2).
\end{aligned}
$$

A primer orden, $\tilde{x}'(x) = 1 + \varepsilon \cdot \tau'(x) + O(\varepsilon^2)$, y el factor aporta a $D$ el término $\bsL \cdot \tau'$. Es el último sumando de la forma de cuatro términos del apartado 5 y, en el resultado de este apartado, la parte $\bsL \cdot \tau'$ de $(\tau \cdot \bsL)' = \tau \cdot \bsL' + \bsL \cdot \tau'$. No hay que confundirlo con el término $-\partial_{f'} \bsL \cdot \tau' \cdot f'$, que también lleva $\tau'$ pero tiene otro origen: sale de que $\tilde{f}'$ es la derivada respecto de la nueva variable, el cociente $\dfrac{\tilde{y}'}{\tilde{x}'}$ del apartado 5. El primero cambia el elemento de integración, $d\tilde{x} = \tilde{x}' \cdot dx$, y el segundo, la pendiente que recibe $\bsL$.

Entonces, con $\bsL'(x) := \dfrac{d}{dx}\bsL(f, f')(x)$, la derivada de la función compuesta:

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

* **El punto viejo está en el dominio de $\tilde{f}$**, que es $[\tilde{x}(a), \tilde{x}(b)]$, si $x$ está en el interior de $[a, b]$ y $|\varepsilon| \ll 1$. En los extremos basta extender $f$ a un intervalo algo mayor, por ejemplo con su desarrollo de Taylor de segundo orden en cada extremo, que sigue siendo de clase $C^2$; en $[a, b]$ no cambia nada.
* **La primera.** Por la definición de $\tilde{f}$, $\tilde{f}\big(\tilde{x}(x)\big) = \tilde{y}(x) = f(x) + \varepsilon \cdot \xi(x) + O(\varepsilon^2)$. Y como $\tilde{x}(x) = x + \varepsilon \cdot \tau(x) + O(\varepsilon^2)$, el punto viejo es $x = \tilde{x}(x) - \varepsilon \cdot \tau(x) + O(\varepsilon^2)$. Desarrollando $\tilde{f}$ alrededor de $\tilde{x}(x)$:

  $$
  \begin{aligned}
  \tilde{f}(x) &= \tilde{f}\big(\tilde{x}(x)\big) - \varepsilon \cdot \tau(x) \cdot \tilde{f}'\big(\tilde{x}(x)\big) + O(\varepsilon^2) \\
  &= f(x) + \varepsilon \cdot \xi(x) - \varepsilon \cdot \tau(x) \cdot f'(x) + O(\varepsilon^2),
  \end{aligned}
  $$

  donde en el último paso $\tilde{f}'\big(\tilde{x}(x)\big) = f'(x) + O(\varepsilon)$, porque va multiplicado por $\varepsilon$. Geométricamente: si la gráfica se desplaza $\varepsilon \cdot \tau$ en horizontal, en un punto fijo el valor cambia en $-\varepsilon \cdot \tau \cdot f'$.
* **La segunda** se obtiene derivando la primera respecto de $x$. Para no tener que estimar la derivada del resto, se usa que las derivadas respecto de $\varepsilon$ y de $x$ conmutan (teorema de Schwarz): $\left.\partial_\varepsilon \tilde{f}'(x)\right|_{\varepsilon = 0} = \left.\partial_x \partial_\varepsilon \tilde{f}(x)\right|_{\varepsilon = 0} = \bar{\xi}'(x)$. Hace falta que $\tilde{f}(x)$ sea de clase $C^2$ como función de $(\varepsilon, x)$, lo que se cumple si $\Phi_\varepsilon$ es de clase $C^2$ en $(\varepsilon, x, y)$ y $f$ es de clase $C^2$, por el teorema de la función inversa:
  * **Teorema de la función inversa.** Si $G$ es de clase $C^k$, con $k \geq 1$, en un abierto de $\mathbb{R}^N$, y su matriz jacobiana es invertible en un punto $P_0$, existe un abierto $W$ que contiene a $P_0$ tal que $G$ es inyectiva en $W$, $G(W)$ es abierto y la inversa $G^{-1}: G(W) \to W$ es de clase $C^k$, con matriz jacobiana la inversa de la de $G$.
  * Una aplicación biyectiva de clase $C^k$ cuya inversa también es de clase $C^k$ se llama **difeomorfismo** (de clase $C^k$).
  * Aquí se aplica a $(\varepsilon, x) \mapsto \big(\varepsilon, \tilde{x}(x)\big)$, con $\tilde{x}$ dependiente de $\varepsilon$, cuya matriz jacobiana tiene determinante $\tilde{x}'(x) \neq 0$. Como además $\tilde{x}$ es estrictamente creciente, la inversa está definida en todo el intervalo transformado, es de clase $C^2$, y $\tilde{f} = \tilde{y} \circ \tilde{x}^{-1}$ también.

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

Es el lema del caso general: los dos primeros términos son el $D$ del caso $\tau = 0$ con $\bar{\xi}$ en lugar de $\xi$, y el tercero es una derivada total.

**Nota sobre los restos.** Que los restos sean de orden $\varepsilon^2$ exige un poco más de regularidad ($\Phi_\varepsilon$ y $f$ de clase $C^3$). Con clase $C^2$ son de orden menor que $\varepsilon$, $o(\varepsilon)$, y basta igual: $D$ es el coeficiente de $\varepsilon$, y solo se usa el primer orden.

A partir de aquí tomaremos una nueva notación (que es el hamiltoniano, que no hemos introducido hasta ahora):

$$
\begin{aligned}
\bsH := p \cdot f' - \bsL
\end{aligned}
$$

Se llama hamiltoniano porque, escrito como función de $(y, p, x)$ mediante la transformada de Legendre (Tema 1, apartados 5 y 6), es el hamiltoniano de la mecánica; aquí solo se usa a lo largo de $f$.

Ahora es el momento de añadir la hipótesis de simetría, a saber, $\exists F(x, y)$ tal que $\exists \partial_x F$ y es continua y $\exists \partial_y F$ y es continua, es decir, $F$ es de clase $C^1$, además de cumplir $D = \dfrac {d} {dx}F$, donde $\dfrac{d}{dx}F = \partial_x F + \partial_y F \cdot f'$ es la derivada de la función compuesta $x \mapsto F\big(x, f(x)\big)$. $F$ no depende de $f'$, por lo visto en el apartado 5, punto (3). Teniendo esto en cuenta, y sustituyendo en la la expresión general ya obtenida de $D$:

$$
\begin{aligned}
\dfrac {d}{dx} F = \partial_f \bsL \cdot \bar{\xi} + p \cdot \bar{\xi}' + (\tau \cdot \bsL)'.
\end{aligned}
$$

Desde 6.2. tenemos que, para toda función $\eta$ de clase $C^1$ en $[a, b]$ (la cadena del apartado 6.2 solo usa la regla del producto y que $\xi$ es de clase $C^1$, no que venga de una transformación):

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

4. **Sustituimos en el paso 2**, y deshacemos también $\bar{\xi}$ en el lado derecho. Queda la **identidad de Noether en el caso general**, válida para toda $f \in C^2([a, b])$:

   $$
   \begin{aligned}
   \dfrac{d}{dx}\big(p \cdot \xi - \tau \cdot \bsH - F\big) = -\varphi \cdot \big(\xi - \tau \cdot f'\big).
   \end{aligned}
   $$

5. **El teorema**, como en el apartado 6.3: sobre las soluciones $\varphi = 0$, y por el teorema del valor medio la cantidad $Q := p \cdot \xi - \tau \cdot \bsH - F$ es constante. Hace falta, además de lo del apartado 6.3, que $\bsH$ sea de clase $C^1$ a lo largo de $f$, lo que se cumple porque $p$, $f'$ y $\bsL(f, f')$ lo son. Con $\tau = 0$ se recupera el apartado 6.3.

El término $\dfrac{d}{dx}(\tau \cdot p \cdot f')$ apareció porque, en el paréntesis del apartado anterior, $p \cdot \bar{\xi}$ y $\tau \cdot p \cdot f'$ se tratan por separado; al deshacer $\bar{\xi}$ se ve que su suma es $p \cdot \xi$, la cantidad con el generador original.

**Comprobación con la energía.** La traslación de la variable, $\Phi_\varepsilon(x, y) = (x + \varepsilon, y)$, tiene $\tau = 1$ y $\xi = 0$. Por la forma de cuatro términos del apartado 5, $D = \partial_x \bsL$, que es nulo si $\bsL$ no depende explícitamente de $x$; entonces $F = 0$ y $Q = -\bsH$. Con $\bsL = \dfrac{1}{2} \cdot y'^2 - g \cdot y$ (el tiro vertical del apartado 5), $\bsH = p \cdot f' - \bsL = \dfrac{1}{2} \cdot f'^2 + g \cdot f$, que es la energía, y $\bsH' = f' \cdot (f'' + g) = 0$ sobre las soluciones, porque $f'' = -g$. El giro del plano, que mueve a la vez la variable y el valor, se trata en «El teorema de Noether: ejemplos matemáticos (versión 2)», apartado 1.

### 6.6. Observaciones

* **El valor de $Q$ depende de la solución.** El teorema dice que $Q$ no cambia a lo largo de cada solución, no que valga lo mismo en todas.
* **La identidad dice más que el teorema.** Vale para toda $f$, y expresa $Q'$ en función de la expresión de Euler–Lagrange: $Q' = -\varphi \cdot \bar{\xi}$.
* **Linealidad.** $D$ es lineal en el generador: en la forma de cuatro términos del apartado 5, cada sumando es lineal en $(\tau, \xi)$ o en sus derivadas. Si $(\tau_1, \xi_1)$ y $(\tau_2, \xi_2)$ son simetrías, con $F_1$ y $F_2$, la combinación $\alpha \cdot (\tau_1, \xi_1) + \beta \cdot (\tau_2, \xi_2)$ también lo es, con $\alpha \cdot F_1 + \beta \cdot F_2$, y su cantidad conservada es $\alpha \cdot Q_1 + \beta \cdot Q_2$, porque $Q = p \cdot \xi - \tau \cdot \bsH - F$ también es lineal. Lo mismo vale para una **familia de varios parámetros**, $\Phi_{\vec{\varepsilon}}$ con $\vec{\varepsilon} = (\varepsilon_1, \dots, \varepsilon_N)$ y $\Phi_{\vec{0}}$ igual a la identidad: cada parámetro $\varepsilon_j$ tiene su generador, la derivada parcial de $\Phi_{\vec{\varepsilon}}$ respecto de $\varepsilon_j$ en $\vec{\varepsilon} = \vec{0}$. Si los $N$ generadores son linealmente independientes, la familia da $N$ cantidades conservadas, una por parámetro. Por ejemplo, con tres funciones (apartado 7), las traslaciones en las tres direcciones del espacio dan las tres componentes de la cantidad de movimiento.
* **$F$ y $Q$ están definidas salvo una constante aditiva**, porque $F + C$, con $C$ constante, tiene la misma derivada que $F$.
* **$Q$ puede ser constante para toda $f$**, y no solo para las soluciones. Entonces el teorema no da información, y la identidad se reduce a $\varphi \cdot \bar{\xi} = 0$ para toda $f$. Con varias funciones es una relación entre las ecuaciones de Euler–Lagrange, que dejan de ser independientes: una combinación de sus expresiones, con coeficientes que dependen de $f$, se anula para toda $f$. Es el caso del cambio de parámetro en el camino más corto (apartado 7.5; «El teorema de Noether: ejemplos matemáticos (versión 2)», apartado 2.4).

### 6.7. Dos casos particulares

#### La función no aparece en $\bsL$

Desplazar el valor, con $(\tau, \xi) = (0, 1)$. En la forma de cuatro términos del apartado 5 solo queda $D = \partial_y \bsL$, y la cantidad conservada sería $Q = p - F$:

* **Si $\bsL$ no depende de $y$**, es una simetría con $F = 0$, y se conserva $Q = p$. Se ve también directamente: la ecuación de Euler–Lagrange se reduce a $p' = 0$. Una variable de la que $\bsL$ no depende se llama **coordenada cíclica** (o ignorable): su momento conjugado se conserva (primera fila de la tabla del apartado 6.4).
* **Si $\partial_y \bsL$ solo depende de $x$**, $\partial_y \bsL = \gamma(x)$ con $\gamma$ continua, también es una simetría, con $F(x) = \int_a^x \gamma(s) \,ds$. Se conserva $Q = p - \int_a^x \gamma(s) \,ds$, que es la ecuación de Euler–Lagrange, $p' = \gamma(x)$, integrada una vez. Es el campo uniforme (segunda fila de la tabla del apartado 6.4, con $\gamma = -g$).
* **Si $\partial_y \bsL$ depende de $y$ y no de $y'$**, no es una simetría, por el criterio del apartado 5, punto (3).
* **Con varias funciones** vale lo mismo para cada componente que no aparece en $\bsL$, con $\vec{\xi} = \vec{e}_k$, el vector con un $1$ en el lugar $k$ y $0$ en los demás (apartado 7).

#### Cuando $\bsL$ no depende de la variable: la identidad de Beltrami

Desplazar la variable, con $(\tau, \xi) = (1, 0)$. En la forma de cuatro términos del apartado 5 solo queda $D = \partial_x \bsL$.

* **Si $\bsL$ no depende explícitamente de $x$**, $D = 0$: es una simetría con $F = 0$, y se conserva $Q = -\bsH$. Es la **identidad de Beltrami**: si $\bsL$ no depende de $x$, $\bsH$ es constante a lo largo de las soluciones. En mecánica, con $x$ como tiempo, es la conservación de la energía (comprobación al final del apartado 6.5).
* **Si $\bsL$ depende de $x$**, la transformación no es una simetría, pero el lema del apartado 6.5 sigue valiendo, porque no usa la hipótesis de simetría. Con $\bar{\xi} = \xi - \tau \cdot f' = -f'$:

  $$
  \begin{aligned}
  \partial_x \bsL = D &\overset{(1)}{=} \partial_f \bsL \cdot \bar{\xi} + p \cdot \bar{\xi}' + (\tau \cdot \bsL)' \\
  &\overset{(2)}{=} \varphi \cdot \bar{\xi} + \big(p \cdot \bar{\xi} + \tau \cdot \bsL\big)' \\
  &\overset{(3)}{=} -\varphi \cdot f' + \big(-p \cdot f' + \bsL\big)' \\
  &\overset{(4)}{=} -\varphi \cdot f' - \bsH'.
  \end{aligned}
  $$

  * **(1)** El lema del apartado 6.5.
  * **(2)** El lema del apartado 6.2 con $\eta = \bar{\xi}$, y la linealidad de la derivada.
  * **(3)** $\tau = 1$ y $\bar{\xi} = -f'$.
  * **(4)** Definición de $\bsH = p \cdot f' - \bsL$.

  Despejando, $\bsH' = -\partial_x \bsL - \varphi \cdot f'$, y sobre las soluciones, $\bsH' = -\partial_x \bsL$: la dependencia explícita de $x$ es exactamente lo que impide que $\bsH$ se conserve.
* **Relación con la versión anterior.** Allí la identidad de Beltrami se obtiene con el generador $\xi = f'$, que depende de la derivada, y con $F = \bsL$, y la cantidad conservada es $\bsH$, sin el signo menos. Es la misma transformación vista en un punto fijo. Desplazar la variable como en la versión anterior, $f(x) \to f(x + \varepsilon)$, es $\Phi_\varepsilon(x, y) = (x - \varepsilon, y)$ (apartado 3.2), con $\tau = -1$. Su desplazamiento en un punto fijo es $\bar{\xi} = 0 - (-1) \cdot f' = f'$, el generador de la versión anterior, y su cantidad conservada es $Q = -\tau \cdot \bsH = \bsH$. La relación general entre las dos formas se ve en el apartado 9.6.

## 7. Generalización a varias funciones: $\bsL(\vec{f}, \vec{f}', x)$

Pasamos de una función $f$ a $n$ funciones $\vec{f} = (f_1, \dots, f_n)$ de la misma variable $x$. Casi todo se repite con una suma sobre las componentes; lo nuevo es la condición para que exista $F$ (apartado 7.3).

### 7.1. Notación

* $\vec{f} = (f_1, \dots, f_n): [a, b] \to \mathbb{R}^n$ es de clase $C^2$. Los índices $i, j = 1, \dots, n$ recorren las componentes.
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
* **Las soluciones** cumplen las $n$ ecuaciones de Euler–Lagrange, $\varphi_i = 0$ para $i = 1, \dots, n$. Son las funciones que hacen estacionario a $\bsS$ con los extremos fijos: tomando variaciones con una sola componente no nula se obtiene una ecuación por componente («El formalismo lagrangiano: parte matemática», la separación de las componentes).
* **Regularidad**, por los mismos argumentos que en el apartado 6.1, componente a componente: las $p_i$, las $\xi_i$ a lo largo de $\vec{f}$ y $\bsH$ son de clase $C^1$, y las $\varphi_i$ son continuas.
* La prima indica, como antes, la derivada respecto de $x$ a lo largo de $\vec{f}$.

### 7.2. El término $D$

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

### 7.3. Cuándo existe $F$: las condiciones de integrabilidad

Como en el apartado 5, punto (3):

* **$D$ es del mismo tipo que $\bsL$:** una función de $(\vec{y}, \vec{y}', x)$, sin derivadas segundas, porque las $\xi_i$ y $\tau$ solo dependen de $(x, \vec{y})$.
* **$F$ no puede depender de $\vec{y}'$:** si dependiera, $\dfrac{dF}{dx}$ contendría las $f''_i$, y $D$ no las contiene. Así que $F = F(x, \vec{y})$, de clase $C^1$, y

  $$
  \begin{aligned}
  \dfrac{dF}{dx} = \partial_x F + \sum_{i=1}^{n} \partial_{y_i} F \cdot y_i'.
  \end{aligned}
  $$

* **$D$ tiene que ser afín en $\vec{y}'$:** $D = \alpha(x, \vec{y}) + \sum_i \beta_i(x, \vec{y}) \cdot y_i'$, y la condición de simetría es la identidad $D = \dfrac{dF}{dx}$ para todos los valores de $(\vec{y}, \vec{y}', x)$, es decir, $\partial_x F = \alpha$ y $\partial_{y_i} F = \beta_i$ para todo $i$. Llamamos $\alpha$ y $\beta_i$ a los coeficientes, y no $a$ y $b_i$, para no confundirlos con los extremos de $[a, b]$.
* **Ser afín no basta.** Si $\alpha$ y las $\beta_i$ son de clase $C^1$, $F$ es de clase $C^2$, y por el teorema de Schwarz sus derivadas cruzadas coinciden. Eso exige las **condiciones de integrabilidad**:

  $$
  \begin{aligned}
  \partial_{y_i} \alpha = \partial_x \beta_i, \qquad \partial_{y_j} \beta_i = \partial_{y_i} \beta_j, \qquad i, j = 1, \dots, n.
  \end{aligned}
  $$

  Con $n = 1$ queda solo la primera, la del apartado 5; con $n \geq 2$ aparecen además condiciones entre las propias $\beta_i$.
* **El lenguaje de las formas diferenciales**, el del apartado 5, punto (3), con más variables. Una **forma diferencial de primer grado** en un abierto $U$ de $\mathbb{R}^{1+n}$ es una expresión $\omega = \alpha \cdot dx + \sum_i \beta_i \cdot dy_i$, con coeficientes continuos en $U$; aquí funciona como una notación para la lista de coeficientes $(\alpha, \beta_1, \dots, \beta_n)$. Es **exacta** si existe una función $F$ de clase $C^1$, su **primitiva**, con $\partial_x F = \alpha$ y $\partial_{y_i} F = \beta_i$; con coeficientes de clase $C^1$, es **cerrada** si cumple las condiciones de integrabilidad. Por el teorema de Schwarz, toda forma exacta con coeficientes de clase $C^1$ es cerrada. La condición de simetría pide que $D$ proceda de una forma exacta.
* **Cuándo bastan: el lema de Poincaré.** Como en el apartado 5, en un abierto estrellado (por ejemplo, una caja, una bola o todo el espacio) toda forma cerrada es exacta. Una primitiva es la integral de $\omega$ a lo largo del segmento que va de $P_* = (x_*, \vec{y}_*)$ a $P = (x, \vec{y})$:

  $$
  \begin{aligned}
  F(P) = \int_0^1 \Big(&\alpha\big(P_* + s \cdot (P - P_*)\big) \cdot (x - x_*) \\
  &+ \sum_{i=1}^{n} \beta_i\big(P_* + s \cdot (P - P_*)\big) \cdot (y_i - y_{*, i})\Big) \,ds.
  \end{aligned}
  $$

  Que sus derivadas parciales son $\alpha$ y las $\beta_i$ se comprueba con las condiciones de integrabilidad y la **derivación bajo el signo integral**: si $h(s, P)$ y su derivada parcial respecto de una coordenada de $P$ son continuas para $s \in [0, 1]$ y $P$ en un abierto, la derivada de $\int_0^1 h(s, P) \,ds$ respecto de esa coordenada existe, es continua y es la integral de la derivada.
* **En un abierto con agujeros no bastan**, como muestra la forma del ángulo del apartado 5.

### 7.4. La identidad y el teorema de Noether

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

**La identidad.** Las $\bar{\xi}_i$ son de clase $C^1$, porque las $\xi_i$, $\tau$ y las $f'_i$ lo son. Aplicamos el lema con $\vec{\eta} = \bar{\vec{\xi}}$ al resultado del apartado 7.2, añadimos la hipótesis de simetría, $D = F'$, y deshacemos $\bar{\xi}_i$:

$$
\begin{aligned}
F' &\overset{(1)}{=} \sum_{i=1}^{n} \varphi_i \cdot \bar{\xi}_i + \Big(\sum_{i=1}^{n} p_i \cdot \bar{\xi}_i + \tau \cdot \bsL\Big)' \\
&\overset{(2)}{=} \sum_{i=1}^{n} \varphi_i \cdot \bar{\xi}_i + \Big(\sum_{i=1}^{n} p_i \cdot \xi_i - \tau \cdot \sum_{i=1}^{n} p_i \cdot f'_i + \tau \cdot \bsL\Big)' \\
&\overset{(3)}{=} \sum_{i=1}^{n} \varphi_i \cdot \bar{\xi}_i + \big(\vec{p} \cdot \vec{\xi} - \tau \cdot \bsH\big)'.
\end{aligned}
$$

* **(1)** Hipótesis de simetría, el lema del apartado 7.2 y el lema anterior con $\vec{\eta} = \bar{\vec{\xi}}$; las dos derivadas se juntan por linealidad.
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

**Qué no hemos usado.** Que $\vec{f}$ sea solución: la identidad vale para toda $\vec{f}$. Ni ninguna condición sobre la matriz $W$ de las derivadas segundas de $\bsL$ respecto de las $y_i'$, de elementos $W_{ij} := \partial_{y'_i} \partial_{y'_j} \bsL$ («El formalismo lagrangiano»). Desarrollando las derivadas $p_i'$, las ecuaciones de Euler–Lagrange son $\sum_j W_{ij} \cdot f''_j = R_i$, donde $R_i$ reúne los términos sin derivadas segundas, y solo determinan las $f''_j$ si $\det W \neq 0$. La identidad vale aunque no las determinen.

### 7.5. Ejemplos

Con $n = 2$ y $x$ en el papel del tiempo (masa $1$). Los dos campos de fuerzas de la tabla son:

* **Campo central:** la fuerza sobre el punto $\vec{y}$ tiene la dirección de $\vec{y}$ y un módulo que solo depende de $r = |\vec{y}| > 0$. Procede de una energía potencial $U(r)$, de clase $C^2$ para $r > 0$: la fuerza es $-U'(r) \cdot \dfrac{\vec{y}}{r}$.
* **Campo magnético:** una partícula de carga y masa $1$ se mueve en el plano, en un campo magnético uniforme, de intensidad $B$, perpendicular a él. Su lagrangiano es $\dfrac{1}{2} \cdot |\vec{y}'|^2 + \vec{A} \cdot \vec{y}'$, donde el **potencial vector** $\vec{A}$ es un campo vectorial del plano con $\partial_{y_1} A_2 - \partial_{y_2} A_1 = B$; tomamos $\vec{A} = \dfrac{B}{2} \cdot (-y_2, y_1)$. Las ecuaciones de Euler–Lagrange son $f_1'' = B \cdot f_2'$ y $f_2'' = -B \cdot f_1'$: la fuerza es perpendicular a la velocidad (fuerza de Lorentz).

| Ejemplo | $\bsL$ | $(\tau, \vec{\xi})$ | $F$ | $Q$ |
| --- | --- | --- | --- | --- |
| Giro, campo central | $\dfrac{1}{2} \cdot \lvert\vec{y}'\rvert^2 - U(\lvert\vec{y}\rvert)$ | $\big(0, (-y_2, y_1)\big)$ | $0$ | $f_1 \cdot f_2' - f_2 \cdot f_1'$ |
| Traslación de la variable, campo central | $\dfrac{1}{2} \cdot \lvert\vec{y}'\rvert^2 - U(\lvert\vec{y}\rvert)$ | $\big(1, (0, 0)\big)$ | $0$ | $-\bsH = -\Big(\dfrac{1}{2} \cdot \lvert\vec{f}'\rvert^2 + U\Big)$ |
| Traslación en $y_1$, campo magnético | $\dfrac{1}{2} \cdot \lvert\vec{y}'\rvert^2 + \dfrac{B}{2} \cdot (y_1 \cdot y_2' - y_2 \cdot y_1')$ | $\big(0, (1, 0)\big)$ | $\dfrac{B}{2} \cdot y_2$ | $f_1' - B \cdot f_2$ |
| Cambio de parámetro, camino más corto | $\lvert\vec{y}'\rvert$ | $\big(\tau(x), (0, 0)\big)$ | $0$ | $-\tau \cdot \bsH = 0$ para toda $\vec{f}$ |

Table: Ejemplos con dos funciones.

**Giro en un campo central.** Es lo que faltaba en el apartado 6.4: hace falta $n \geq 2$, porque un giro mezcla dos componentes. $D = \sum_i \big(\partial_{f_i} \bsL \cdot \xi_i + p_i \cdot \xi_i'\big)$, con $\partial_{f_i} \bsL = -U'(r) \cdot \dfrac{f_i}{r}$ y $r = |\vec{f}|$:

$$
\begin{aligned}
D = -\dfrac{U'(r)}{r} \cdot \big(f_1 \cdot (-f_2) + f_2 \cdot f_1\big) + \big(f_1' \cdot (-f_2') + f_2' \cdot f_1'\big) = 0.
\end{aligned}
$$

$Q = p_1 \cdot (-f_2) + p_2 \cdot f_1$ es el momento angular. Comprobación: $Q' = f_1 \cdot f_2'' - f_2 \cdot f_1''$, y con las ecuaciones $f_i'' = -U'(r) \cdot \dfrac{f_i}{r}$ queda $-\dfrac{U'(r)}{r} \cdot (f_1 \cdot f_2 - f_2 \cdot f_1) = 0$.

**Traslación de la variable.** Con $\tau = 1$ y $\vec{\xi} = \vec{0}$, $D = \partial_x \bsL = 0$, y $Q = -\bsH$: se conserva la energía, $\bsH = \dfrac{1}{2} \cdot |\vec{f}'|^2 + U$.

**Traslación en un campo magnético: un ejemplo con $F \neq 0$ y las condiciones de integrabilidad.** Es la carga en el campo magnético descrita antes de la tabla («El formalismo lagrangiano: parte física»). Con $\vec{\xi} = (1, 0)$ y $\tau = 0$, $D = \partial_{y_1} \bsL = \dfrac{B}{2} \cdot y_2'$. Es afín, con $\alpha = 0$, $\beta_1 = 0$ y $\beta_2 = \dfrac{B}{2}$ (apartado 7.3); las condiciones de integrabilidad se cumplen, porque todos los coeficientes son constantes, y $F = \dfrac{B}{2} \cdot y_2$. Con $p_1 = f_1' - \dfrac{B}{2} \cdot f_2$:

$$
\begin{aligned}
Q = p_1 - F = f_1' - \dfrac{B}{2} \cdot f_2 - \dfrac{B}{2} \cdot f_2 = f_1' - B \cdot f_2.
\end{aligned}
$$

Comprobación: la ecuación de Euler–Lagrange de $f_1$ es $f_1'' = B \cdot f_2'$, y $Q' = f_1'' - B \cdot f_2' = 0$. Es la primera componente del vector $\vec{K} := (f_1' - B \cdot f_2,\ f_2' + B \cdot f_1)$, que es constante sobre las soluciones, porque $(f_2' + B \cdot f_1)' = f_2'' + B \cdot f_1' = 0$ («El formalismo lagrangiano: parte física»). No se conserva la cantidad de movimiento $f_1'$, sino $f_1' - B \cdot f_2$.

**Cambio de parámetro en el camino más corto: una relación entre las ecuaciones.** Con $\bsL = |\vec{y}'|$ (curvas regulares, $\vec{f}' \neq \vec{0}$), $\vec{\xi} = \vec{0}$ y $\tau(x)$ una función **cualquiera** de clase $C^1$, la forma de cuatro términos del apartado 5, componente a componente, da

$$
\begin{aligned}
D = \sum_{i=1}^{n} p_i \cdot \big(-\tau' \cdot f'_i\big) + \bsL \cdot \tau' = -\tau' \cdot \bsH,
\end{aligned}
$$

y $\bsH = \sum_i \dfrac{f'_i \cdot f'_i}{|\vec{f}'|} - |\vec{f}'| = 0$ para toda $\vec{f}$. Así que $D = 0$, $F = 0$ y $Q = -\tau \cdot \bsH$ es nula para toda $\vec{f}$: el teorema no da nada. Pero la identidad sí: su lado izquierdo es nulo, así que

$$
\begin{aligned}
0 = -\sum_{i=1}^{n} \varphi_i \cdot \big(0 - \tau \cdot f'_i\big) = \tau \cdot \sum_{i=1}^{n} f'_i \cdot \varphi_i
\end{aligned}
$$

para toda $\tau$ y toda $\vec{f}$. Tomando $\tau = 1$, $\sum_i f'_i \cdot \varphi_i = 0$: las $n$ ecuaciones de Euler–Lagrange no son independientes. Es la libertad de elegir el parámetro de la curva, y el caso más sencillo del **segundo teorema de Noether**. Ese teorema trata las simetrías que dependen de funciones arbitrarias de la variable, como aquí $\tau(x)$, y no de un número finito de parámetros: no dan cantidades conservadas, sino relaciones, válidas para toda $\vec{f}$, entre las expresiones de Euler–Lagrange y sus derivadas.

Las cuentas de los ejemplos están comprobadas con SymPy en el archivo Teorema-de-Noether-v2-comprobaciones.py, en el mismo directorio que este documento.

## 8. Generalización a varias variables: $\bsL(\vec{f}, J_{\vec{f}}, \vec{x})$

Pasamos de $n$ funciones de una variable a $n$ funciones de $m$ variables, $\vec{f}(\vec{x})$. Es el caso que trata el artículo original de Noether (1918), con integrales múltiples. En «El teorema de Noether: parte matemática», apartado «Varias variables», está el caso en que las variables no se mueven, $\vec{\tau} = \vec{0}$; aquí se mueven también. El esquema es el del apartado 7, con sumas sobre las variables, y hay tres cambios de fondo:

* el factor $\tilde{x}'$ pasa a ser un **determinante jacobiano** (apartado 8.2);
* $F$ pasa a ser un **campo vectorial** $\vec{F} = (F_1, \dots, F_m)$, y la condición de simetría pide que $D$ sea su **divergencia**, la suma de las derivadas de cada componente $F_k$ respecto de la variable $x_k$ (apartados 8.4 y 8.5);
* el teorema da una **ley de conservación local**, una igualdad que dice que la divergencia de un campo es nula en cada punto, y no una constante; para obtener una constante hacen falta además condiciones de contorno (apartados 8.6 y 8.7).

Con $m = 1$, cada paso se reduce al del apartado 7.

### 8.1. Notación

* **Las variables y las funciones.** El dominio es la caja $\Omega := [a_1, b_1] \times \dots \times [a_m, b_m] \subset \mathbb{R}^m$, el producto cartesiano de $m$ intervalos, que también escribimos $\prod_k [a_k, b_k]$, como en «El formalismo lagrangiano: parte matemática», y $\vec{f} = (f_1, \dots, f_n): \Omega \to \mathbb{R}^n$ es de clase $C^2$. Los índices $i, j = 1, \dots, n$ recorren las funciones, y $k, l = 1, \dots, m$, las variables.
* **El jacobiano.** $J_{\vec{f}}$ es la matriz de $n$ filas y $m$ columnas de elementos $\partial_k f_i := \dfrac{\partial f_i}{\partial x_k}$.
* **El lagrangiano.** $\bsL(\vec{y}, Z, \vec{x})$ es una función de $n + n \cdot m + m$ variables reales, de clase $C^2$. $Z = (z_{ik})$ es solo el nombre de las $n \cdot m$ variables que ocupan el lugar de $J_{\vec{f}}$, como $\vec{y}'$ en el apartado 7. A lo largo de $\vec{f}$ escribimos $\bsL(\vec{f}, J_{\vec{f}})(\vec{x}) := \bsL\big(\vec{f}(\vec{x}), J_{\vec{f}}(\vec{x}), \vec{x}\big)$, y el funcional es

  $$
  \begin{aligned}
  \bsS[\vec{f}] = \int_\Omega \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) \,dx_1 \cdots dx_m.
  \end{aligned}
  $$

* **La derivada a lo largo de $\vec{f}$.** Para una función $G(\vec{y}, Z, \vec{x})$, $d_{x_k} G$ es la derivada respecto de $x_k$ de la función compuesta $\vec{x} \mapsto G\big(\vec{f}(\vec{x}), J_{\vec{f}}(\vec{x}), \vec{x}\big)$. Por la regla de la cadena (el excurso de «El formalismo lagrangiano: parte matemática»),

  $$
  \begin{aligned}
  d_{x_k} G = \partial_{x_k} G + \sum_{j=1}^{n} \partial_{y_j} G \cdot \partial_k f_j + \sum_{j=1}^{n} \sum_{l=1}^{m} \partial_{z_{jl}} G \cdot \partial_k \partial_l f_j.
  \end{aligned}
  $$

  $d_{x_k}$ hace el papel de la prima: $\partial_{x_k} G$ es la derivada respecto del argumento $x_k$, con los demás fijos, y $d_{x_k} G$ incluye además la dependencia a través de $\vec{f}$ y de $J_{\vec{f}}$. Si $G$ solo depende de $(\vec{x}, \vec{y})$, falta la última suma. Para las propias funciones, $d_{x_k} f_i = \partial_k f_i$.
* **La transformación** actúa sobre los puntos de $\mathbb{R}^m \times \mathbb{R}^n$:

  $$
  \begin{aligned}
  \Phi_\varepsilon(\vec{x}, \vec{y}) = \big(\vec{X}_\varepsilon(\vec{x}, \vec{y}),\ \vec{Y}_\varepsilon(\vec{x}, \vec{y})\big),
  \end{aligned}
  $$

  de clase $C^2$ en $(\varepsilon, \vec{x}, \vec{y})$ y con $\Phi_0$ igual a la identidad. A primer orden,

  $$
  \begin{aligned}
  X_{\varepsilon, k} = x_k + \varepsilon \cdot \tau_k(\vec{x}, \vec{y}) + O(\varepsilon^2), \qquad Y_{\varepsilon, i} = y_i + \varepsilon \cdot \xi_i(\vec{x}, \vec{y}) + O(\varepsilon^2).
  \end{aligned}
  $$

  El generador tiene $m$ componentes en las variables, $\vec{\tau} = (\tau_1, \dots, \tau_m)$, y $n$ en los valores, $\vec{\xi} = (\xi_1, \dots, \xi_n)$. A lo largo de $\vec{f}$ escribimos $\tau_k(\vec{x}) := \tau_k\big(\vec{x}, \vec{f}(\vec{x})\big)$ y $\xi_i(\vec{x}) := \xi_i\big(\vec{x}, \vec{f}(\vec{x})\big)$.
* **La gráfica** de $\vec{f}$ es el conjunto $\big\{\big(\vec{x}, \vec{f}(\vec{x})\big) : \vec{x} \in \Omega\big\}$, una superficie de dimensión $m$ en $\mathbb{R}^{m+n}$. La transformada tiene una variable nueva, que ahora es un vector común a todas las funciones, y $n$ funciones nuevas:

  $$
  \begin{aligned}
  \tilde{\vec{x}}(\vec{x}) := \vec{X}_\varepsilon\big(\vec{x}, \vec{f}(\vec{x})\big), \qquad \tilde{f}_i\big(\tilde{\vec{x}}(\vec{x})\big) := Y_{\varepsilon, i}\big(\vec{x}, \vec{f}(\vec{x})\big).
  \end{aligned}
  $$

* **$\tilde{\vec{x}}$ tiene que ser un difeomorfismo** de $\Omega$ sobre su imagen, $\tilde{\Omega} := \tilde{\vec{x}}(\Omega)$, para que las $\tilde{f}_i$ estén bien definidas. Es el análogo de que $\tilde{x}$ sea creciente (apartado 3.1), y se cumple para $|\varepsilon|$ pequeño:
  * **Es una perturbación de la identidad:** $\tilde{\vec{x}} = Id + \varepsilon \cdot \vec{w}_\varepsilon$, con $\vec{w}_\varepsilon(\vec{x}) = \int_0^1 \partial_\varepsilon \vec{X}_{s \cdot \varepsilon}\big(\vec{x}, \vec{f}(\vec{x})\big) \,ds$ (teorema fundamental del cálculo en $\varepsilon$). Sea $\varepsilon_0 > 0$ tal que la familia está definida para $|\varepsilon| \leq \varepsilon_0$. Las derivadas de $\vec{w}_\varepsilon$ respecto de las $x_k$ existen y son continuas en $(\varepsilon, \vec{x})$, por la derivación bajo el signo integral (apartado 7.3). Como son continuas en el conjunto cerrado y acotado $[-\varepsilon_0, \varepsilon_0] \times \Omega$, están acotadas por una constante $M$.
  * **Es inyectiva.** La caja es convexa: el segmento entre dos de sus puntos, $\vec{z}_1$ y $\vec{z}_2$, está en ella. Por la **desigualdad del valor medio**, $|\vec{w}_\varepsilon(\vec{z}_1) - \vec{w}_\varepsilon(\vec{z}_2)| \leq m \cdot M \cdot |\vec{z}_1 - \vec{z}_2|$. (Se obtiene aplicando el teorema del valor medio de una variable a $t \mapsto \vec{v} \cdot \vec{w}_\varepsilon\big(\vec{z}_2 + t \cdot (\vec{z}_1 - \vec{z}_2)\big)$, con $\vec{v}$ el vector unitario en la dirección de $\vec{w}_\varepsilon(\vec{z}_1) - \vec{w}_\varepsilon(\vec{z}_2)$; el factor $m \cdot M$ acota la matriz jacobiana de $\vec{w}_\varepsilon$, que tiene $m^2$ elementos acotados por $M$.) Entonces $|\tilde{\vec{x}}(\vec{z}_1) - \tilde{\vec{x}}(\vec{z}_2)| \geq (1 - |\varepsilon| \cdot m \cdot M) \cdot |\vec{z}_1 - \vec{z}_2|$, que es positivo si $\vec{z}_1 \neq \vec{z}_2$ y $|\varepsilon| < \dfrac{1}{m \cdot M}$.
  * **Su inversa es de clase $C^2$**, por el teorema de la función inversa (apartado 6.5), aplicado en un abierto que contiene la caja: $\det J_{\tilde{\vec{x}}}$ está próximo a $1$ (apartado 8.2) y no se anula, y como $\tilde{\vec{x}}$ es inyectiva, las inversas locales son la inversa de $\tilde{\vec{x}}$. Por tanto, $\tilde{\vec{x}}$ es un difeomorfismo (apartado 6.5) de $\Omega$ sobre su imagen.
* **Momentos y expresiones de Euler–Lagrange**, a lo largo de $\vec{f}$. Hay un momento por cada función y cada variable:

  $$
  \begin{aligned}
  u_{ik} := \partial_{z_{ik}} \bsL(\vec{f}, J_{\vec{f}})(\vec{x}), \qquad \varphi_i := \partial_{f_i} \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) - \sum_{k=1}^{m} d_{x_k} u_{ik}.
  \end{aligned}
  $$

  En «El formalismo lagrangiano: parte matemática», $\partial_{z_{ik}} \bsL$ se escribe $\partial_{\partial_{x_k} f_i} \bsL$. Con $m = 1$, $u_{i1} = p_i$ y $\varphi_i$ es la del apartado 7.1.
* **Las soluciones** cumplen las $n$ ecuaciones de Euler–Lagrange, $\varphi_i = 0$, que ahora son ecuaciones en derivadas parciales: en ellas intervienen las derivadas parciales de las $f_i$ respecto de varias variables. Son las funciones que hacen estacionario a $\bsS$ con los valores fijados en la frontera de $\Omega$ («El formalismo lagrangiano: parte matemática», generalización a funciones vectoriales de varias variables).
* **Regularidad**, por los argumentos del apartado 6.1: las $u_{ik}$, y las $\tau_k$ y las $\xi_i$ a lo largo de $\vec{f}$, son de clase $C^1$, y las $\varphi_i$ son continuas.

### 8.2. Las dos piezas nuevas: el factor de volumen y las pendientes

Son los análogos de $\tilde{x}'$ y de $\dfrac{\tilde{y}'}{\tilde{x}'}$ del apartado 5, punto (2). A lo largo de $\vec{f}$ llamamos $J_{\vec{\tau}}$ y $J_{\vec{\xi}}$ a las matrices jacobianas de $\vec{x} \mapsto \vec{\tau}(\vec{x})$ y de $\vec{x} \mapsto \vec{\xi}(\vec{x})$, de elementos $d_{x_l} \tau_k$ y $d_{x_l} \xi_i$; $J_{\tilde{\vec{y}}}$ a la de $\vec{x} \mapsto \tilde{\vec{y}}(\vec{x}) := \vec{Y}_\varepsilon\big(\vec{x}, \vec{f}(\vec{x})\big)$; e $I$ a la matriz identidad $m \times m$. Las derivadas respecto de $\varepsilon$ y de $\vec{x}$ conmutan (teorema de Schwarz, como en el apartado 6.5), así que, salvo términos de orden $\varepsilon^2$,

$$
\begin{aligned}
J_{\tilde{\vec{x}}} = I + \varepsilon \cdot J_{\vec{\tau}}, \qquad J_{\tilde{\vec{y}}} = J_{\vec{f}} + \varepsilon \cdot J_{\vec{\xi}}.
\end{aligned}
$$

**El factor de volumen.** El **teorema del cambio de variables** dice: si $G$ es un difeomorfismo de clase $C^1$ de un abierto que contiene la caja $B$ sobre su imagen, y $h$ es continua en $G(B)$, entonces

$$
\begin{aligned}
\int_{G(B)} h(\vec{u}) \,du_1 \cdots du_m = \int_B h\big(G(\vec{x})\big) \cdot \big|\det J_G(\vec{x})\big| \,dx_1 \cdots dx_m.
\end{aligned}
$$

La integral de la izquierda es sobre una región que no tiene por qué ser una caja: se define como la integral, sobre una caja que la contiene, de la función que vale $h$ en la región y $0$ fuera, y existe porque la frontera de $G(B)$ tiene volumen nulo. Con $G = \tilde{\vec{x}}$, se escribe $d\tilde{x}_1 \cdots d\tilde{x}_m = \det J_{\tilde{\vec{x}}}(\vec{x}) \cdot dx_1 \cdots dx_m$, con

$$
\begin{aligned}
\det J_{\tilde{\vec{x}}} = 1 + \varepsilon \cdot \operatorname{tr} J_{\vec{\tau}} + O(\varepsilon^2) = 1 + \varepsilon \cdot \sum_{k=1}^{m} d_{x_k} \tau_k + O(\varepsilon^2).
\end{aligned}
$$

* **Por qué.** En la fórmula de Leibniz, $\det A = \sum_{\sigma} \operatorname{sgn}(\sigma) \cdot \prod_k A_{k \sigma(k)}$, con la suma sobre las permutaciones $\sigma$ de $\{1, \dots, m\}$. La identidad da el producto de la diagonal, $\prod_k (1 + \varepsilon \cdot d_{x_k} \tau_k) = 1 + \varepsilon \cdot \sum_k d_{x_k} \tau_k + O(\varepsilon^2)$. Cualquier otra permutación mueve al menos dos índices, así que su producto contiene al menos dos elementos fuera de la diagonal, cada uno de orden $\varepsilon$.
* **La suma $\sum_k d_{x_k} \tau_k$ es la divergencia** de $\vec{\tau}$ a lo largo de $\vec{f}$, y ocupa el lugar de $\tau'$. Con $m = 1$, $\det J_{\tilde{\vec{x}}} = \tilde{x}' = 1 + \varepsilon \cdot \tau'$.
* Para $|\varepsilon|$ pequeño, $\det J_{\tilde{\vec{x}}} > 0$, así que coincide con su valor absoluto, que es el que aparece en el teorema del cambio de variables.

**Las pendientes.** Derivamos la definición $\tilde{f}_i\big(\tilde{\vec{x}}(\vec{x})\big) = \tilde{y}_i(\vec{x})$ respecto de $x_l$. Por la regla de la cadena, $\sum_k \partial_k \tilde{f}_i(\tilde{\vec{x}}) \cdot d_{x_l} \tilde{x}_k = d_{x_l} \tilde{y}_i$, es decir, en forma matricial,

$$
\begin{aligned}
J_{\tilde{\vec{f}}}(\tilde{\vec{x}}) \cdot J_{\tilde{\vec{x}}} = J_{\tilde{\vec{y}}} \quad \Longrightarrow \quad J_{\tilde{\vec{f}}}(\tilde{\vec{x}}) = J_{\tilde{\vec{y}}} \cdot J_{\tilde{\vec{x}}}^{-1},
\end{aligned}
$$

porque $J_{\tilde{\vec{x}}}$ es invertible. Como $(I + \varepsilon \cdot J_{\vec{\tau}}) \cdot (I - \varepsilon \cdot J_{\vec{\tau}}) = I - \varepsilon^2 \cdot J_{\vec{\tau}}^2$, la inversa es $J_{\tilde{\vec{x}}}^{-1} = I - \varepsilon \cdot J_{\vec{\tau}} + O(\varepsilon^2)$, y

$$
\begin{aligned}
J_{\tilde{\vec{f}}}(\tilde{\vec{x}}) &= \big(J_{\vec{f}} + \varepsilon \cdot J_{\vec{\xi}}\big) \cdot \big(I - \varepsilon \cdot J_{\vec{\tau}}\big) + O(\varepsilon^2) \\
&= J_{\vec{f}} + \varepsilon \cdot \big(J_{\vec{\xi}} - J_{\vec{f}} \cdot J_{\vec{\tau}}\big) + O(\varepsilon^2).
\end{aligned}
$$

Elemento a elemento:

$$
\begin{aligned}
\partial_l \tilde{f}_i(\tilde{\vec{x}}) = \partial_l f_i + \varepsilon \cdot \Big(d_{x_l} \xi_i - \sum_{k=1}^{m} \partial_k f_i \cdot d_{x_l} \tau_k\Big) + O(\varepsilon^2).
\end{aligned}
$$

Con $m = 1$ es $\dfrac{\tilde{y}_i'}{\tilde{x}'} = f_i' + \varepsilon \cdot (\xi_i' - \tau' \cdot f_i') + O(\varepsilon^2)$, la del apartado 5, punto (2), para cada componente.

### 8.3. El término $D$

Como en el apartado 6.5, definimos $D$ como el coeficiente de $\varepsilon$ del integrando transformado, escrito en la variable vieja:

$$
\begin{aligned}
D(\vec{x}) := \left.\dfrac{d}{d\varepsilon}\Big(\bsL(\tilde{\vec{f}}, J_{\tilde{\vec{f}}})(\tilde{\vec{x}}) \cdot \det J_{\tilde{\vec{x}}}(\vec{x})\Big)\right|_{\varepsilon = 0}.
\end{aligned}
$$

$D$ ya incluye el factor de volumen, igual que en una variable incluía $\tilde{x}'$.

**La forma de cuatro términos.** Por el apartado 8.2, los argumentos de $\bsL$ se desplazan, por unidad de $\varepsilon$, en $\xi_i$ (los valores), en $d_{x_l} \xi_i - \sum_k \partial_k f_i \cdot d_{x_l} \tau_k$ (las pendientes) y en $\tau_k$ (el punto), y el factor de volumen aporta $\bsL \cdot \sum_k d_{x_k} \tau_k$. El desarrollo de Taylor de $\bsL$ da

$$
\begin{aligned}
D &= \sum_{i=1}^{n} \partial_{f_i} \bsL \cdot \xi_i + \sum_{i=1}^{n} \sum_{l=1}^{m} u_{il} \cdot \Big(d_{x_l} \xi_i - \sum_{k=1}^{m} \partial_k f_i \cdot d_{x_l} \tau_k\Big) \\
&\qquad + \sum_{k=1}^{m} \partial_{x_k} \bsL \cdot \tau_k + \bsL \cdot \sum_{k=1}^{m} d_{x_k} \tau_k.
\end{aligned}
$$

Con $m = 1$ es la del apartado 5, punto (2), componente a componente.

**$D$ es del mismo tipo que $\bsL$**, como en el apartado 5: una función de $(\vec{y}, Z, \vec{x})$, sin derivadas segundas. Sus ingredientes son las derivadas parciales de $\bsL$; las $\partial_k f_i$, que son las variables $z_{ik}$; y las derivadas $d_{x_l} \xi_i = \partial_{x_l} \xi_i + \sum_j \partial_{y_j} \xi_i \cdot z_{jl}$ y $d_{x_l} \tau_k$, que tampoco contienen derivadas segundas, porque $\vec{\xi}$ y $\vec{\tau}$ solo dependen de $(\vec{x}, \vec{y})$.

**El lema.** Como en el apartado 7.2:

$$
\begin{aligned}
\varepsilon \cdot D &\overset{(1)}{=} \bsL(\tilde{\vec{f}}, J_{\tilde{\vec{f}}})(\tilde{\vec{x}}) \cdot \det J_{\tilde{\vec{x}}} - \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) + O(\varepsilon^2) \\
&\overset{(2)}{=} \Big(\bsL(\tilde{\vec{f}}, J_{\tilde{\vec{f}}})(\vec{x}) + \varepsilon \cdot \sum_{k=1}^{m} \tau_k \cdot d_{x_k} \bsL(\tilde{\vec{f}}, J_{\tilde{\vec{f}}})(\vec{x})\Big) \\
&\qquad \cdot \Big(1 + \varepsilon \cdot \sum_{k=1}^{m} d_{x_k} \tau_k\Big) - \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) + O(\varepsilon^2) \\
&\overset{(3)}{=} \Big(\bsL(\tilde{\vec{f}}, J_{\tilde{\vec{f}}})(\vec{x}) - \bsL(\vec{f}, J_{\vec{f}})(\vec{x})\Big) \\
&\qquad + \varepsilon \cdot \sum_{k=1}^{m} \big(\tau_k \cdot d_{x_k} \bsL + \bsL \cdot d_{x_k} \tau_k\big) + O(\varepsilon^2) \\
&\overset{(4)}{=} \varepsilon \cdot \sum_{i=1}^{n} \Big(\partial_{f_i} \bsL \cdot \bar{\xi}_i + \sum_{k=1}^{m} u_{ik} \cdot d_{x_k} \bar{\xi}_i\Big) + \varepsilon \cdot \sum_{k=1}^{m} d_{x_k}(\tau_k \cdot \bsL) + O(\varepsilon^2),
\end{aligned}
$$

con

$$
\begin{aligned}
\bar{\xi}_i := \xi_i - \sum_{k=1}^{m} \tau_k \cdot \partial_k f_i.
\end{aligned}
$$

Justificación de cada igualdad:

* **(1)** Desarrollo de Taylor en $\varepsilon$. El valor en $\varepsilon = 0$ es $\bsL(\vec{f}, J_{\vec{f}})(\vec{x})$, porque entonces $\tilde{\vec{x}} = \vec{x}$, $\tilde{\vec{f}} = \vec{f}$ y $\det J_{\tilde{\vec{x}}} = 1$; el coeficiente de $\varepsilon$ es $D(\vec{x})$, por definición.
* **(2)** El punto se mueve, $\tilde{\vec{x}} = \vec{x} + \varepsilon \cdot \vec{\tau} + O(\varepsilon^2)$, y el desarrollo de Taylor de primer orden en el punto, en $m$ variables, da la suma $\varepsilon \cdot \sum_k \tau_k \cdot d_{x_k}(\cdots)$, la derivada direccional en la dirección $\vec{\tau}$. Es la derivada de la función compuesta, porque al mover el punto se mueven todos los argumentos de $\bsL$. El segundo factor es $\det J_{\tilde{\vec{x}}}$ (apartado 8.2).
* **(3)** Multiplicamos, llevamos los términos de orden $\varepsilon^2$ al resto y sustituimos $\tilde{\vec{f}}$ por $\vec{f}$ donde ya va multiplicado por $\varepsilon$. Ahora $d_{x_k} \bsL$ es la derivada de $\bsL(\vec{f}, J_{\vec{f}})$.
* **(4)** Dos partes, como en el apartado 6.5:
  * **En el mismo punto $\vec{x}$**, cada función transformada se diferencia de la original en $\varepsilon \cdot \bar{\xi}_i$. Si $\vec{x}$ es interior a $\Omega$ y $|\varepsilon| \ll 1$, está en el dominio de $\tilde{f}_i$; en la frontera basta extender $\vec{f}$, como en el apartado 6.5. El punto viejo es $\vec{x} = \tilde{\vec{x}} - \varepsilon \cdot \vec{\tau} + O(\varepsilon^2)$. El desarrollo de Taylor de $\tilde{f}_i$ alrededor de $\tilde{\vec{x}}$, la definición de $\tilde{f}_i$ y $\partial_k \tilde{f}_i(\tilde{\vec{x}}) = \partial_k f_i + O(\varepsilon)$ (apartado 8.2) dan

    $$
    \begin{aligned}
    \tilde{f}_i(\vec{x}) = \tilde{f}_i(\tilde{\vec{x}}) - \varepsilon \cdot \sum_{k=1}^{m} \tau_k \cdot \partial_k \tilde{f}_i(\tilde{\vec{x}}) + O(\varepsilon^2) = f_i + \varepsilon \cdot \bar{\xi}_i + O(\varepsilon^2).
    \end{aligned}
    $$

    Desplazar la gráfica $\varepsilon \cdot \vec{\tau}$ en las variables cambia el valor en un punto fijo en menos la derivada direccional, $-\varepsilon \cdot \sum_k \tau_k \cdot \partial_k f_i$. Derivando respecto de $x_k$, con el teorema de Schwarz como en el apartado 6.5, $\partial_k \tilde{f}_i(\vec{x}) = \partial_k f_i + \varepsilon \cdot d_{x_k} \bar{\xi}_i + O(\varepsilon^2)$. El desarrollo de Taylor de $\bsL$ en sus $n + n \cdot m$ primeros argumentos, con $\vec{x}$ fijo, da la primera suma.
  * **El resto es una divergencia**, por la regla del producto en cada $k$: $\tau_k \cdot d_{x_k} \bsL + \bsL \cdot d_{x_k} \tau_k = d_{x_k}(\tau_k \cdot \bsL)$.

Quedándonos con el coeficiente de $\varepsilon$, el **lema en varias variables** es

$$
\begin{aligned}
D = \sum_{i=1}^{n} \Big(\partial_{f_i} \bsL \cdot \bar{\xi}_i + \sum_{k=1}^{m} u_{ik} \cdot d_{x_k} \bar{\xi}_i\Big) + \sum_{k=1}^{m} d_{x_k}(\tau_k \cdot \bsL).
\end{aligned}
$$

En $d_{x_k} \bar{\xi}_i$ y en $d_{x_k}(\tau_k \cdot \bsL)$ aparecen derivadas segundas de $\vec{f}$, pero se cancelan entre sí, porque la forma de cuatro términos no las contiene.

### 8.4. La condición de simetría: $D$ es una divergencia

**La condición.** Como en el apartado 4, se pide en cada subcaja $B := [c_1, d_1] \times \dots \times [c_m, d_m] \subseteq \Omega$ (aquí $B$ es una caja, no el campo magnético del apartado 7.5) y para toda $\vec{f}$ de clase $C^2$, sin valores fijados en la frontera:

$$
\begin{aligned}
&\int_{\tilde{\vec{x}}(B)} \bsL(\tilde{\vec{f}}, J_{\tilde{\vec{f}}})(\tilde{\vec{x}}) \,d\tilde{x}_1 \cdots d\tilde{x}_m \\
&\qquad = \int_B \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) \,dx_1 \cdots dx_m \\
&\qquad\quad + \varepsilon \cdot \sum_{k=1}^{m} \int_{B_k} \Big[F_k\Big]_{x_k = c_k}^{x_k = d_k} d\hat{x}_k + O(\varepsilon^2).
\end{aligned}
$$

* $\vec{F} = (F_1, \dots, F_m)$ es un campo de $m$ funciones $F_k(\vec{x}, \vec{y})$ de clase $C^1$, el mismo para todas las $\vec{f}$, que se evalúa en $\big(\vec{x}, \vec{f}(\vec{x})\big)$.
* $B_k$ es la caja de las otras $m - 1$ variables y $d\hat{x}_k$, el producto de sus diferenciales, como en «El formalismo lagrangiano: parte matemática». El término de $\vec{F}$ es su **flujo** saliente a través de las caras de $B$: lo que sale por las caras $x_k = d_k$ menos lo que entra por las caras $x_k = c_k$.
* Con $m = 1$, $B = [c_1, d_1]$ es el subintervalo $[c, d]$ del apartado 4, no hay otras variables y el término es $F(d) - F(c)$.
* La región transformada, $\tilde{\vec{x}}(B)$, ya no es una caja. No importa, porque el cambio de variables la lleva de vuelta a $B$.

**La condición, paso a paso**, como en el apartado 5, con $\bsL = \bsL(\vec{f}, J_{\vec{f}})(\vec{x})$ en el lado derecho:

$$
\begin{aligned}
&\int_{\tilde{\vec{x}}(B)} \bsL(\tilde{\vec{f}}, J_{\tilde{\vec{f}}})(\tilde{\vec{x}}) \,d\tilde{x}_1 \cdots d\tilde{x}_m \\
&\quad \overset{(1)}{=} \int_B \bsL(\tilde{\vec{f}}, J_{\tilde{\vec{f}}})\big(\tilde{\vec{x}}(\vec{x})\big) \cdot \det J_{\tilde{\vec{x}}}(\vec{x}) \,dx_1 \cdots dx_m \\
&\quad \overset{(2)}{=} \int_B \big(\bsL + \varepsilon \cdot D\big) \,dx_1 \cdots dx_m + O(\varepsilon^2) \\
&\quad \overset{(3)}{=} \int_B \Big(\bsL + \varepsilon \cdot \sum_{k=1}^{m} d_{x_k} F_k\Big) \,dx_1 \cdots dx_m + O(\varepsilon^2) \\
&\quad \overset{(4)}{=} \int_B \bsL \,dx_1 \cdots dx_m + \varepsilon \cdot \sum_{k=1}^{m} \int_{B_k} \Big[F_k\Big]_{x_k = c_k}^{x_k = d_k} d\hat{x}_k + O(\varepsilon^2).
\end{aligned}
$$

* **(1) Cambio de variables** $\tilde{\vec{x}} = \tilde{\vec{x}}(\vec{x})$, válido porque $\tilde{\vec{x}}$ es un difeomorfismo (apartado 8.1), con el factor de volumen del apartado 8.2.
* **(2) Definición de $D$** (apartado 8.3). El resto, integrado en $B$, sigue siendo de orden $\varepsilon^2$: las derivadas segundas de $\bsL$ y de $\Phi_\varepsilon$ son continuas en un conjunto cerrado y acotado que contiene todos los puntos que intervienen, y por tanto están acotadas, así que el resto de Taylor está acotado por $C \cdot \varepsilon^2$ con $C$ independiente de $\vec{x}$ (como en el apartado 5, punto (2)).
* **(3) La hipótesis de simetría:** $D = \sum_k d_{x_k} F_k$ en cada punto, para toda $\vec{f}$. Es la única igualdad que no vale siempre.
* **(4) Teorema de Fubini y regla de Barrow** en cada variable, como en la integración por partes de «El formalismo lagrangiano: parte matemática»:

  $$
  \begin{aligned}
  \int_B d_{x_k} F_k \,dx_1 \cdots dx_m = \int_{B_k} \left(\int_{c_k}^{d_k} d_{x_k} F_k \,dx_k\right) d\hat{x}_k = \int_{B_k} \Big[F_k\Big]_{x_k = c_k}^{x_k = d_k} d\hat{x}_k.
  \end{aligned}
  $$

  Es el teorema de la divergencia en una caja.

**Por qué en cada punto.** Si $\int_B \big(D - \sum_k d_{x_k} F_k\big) \,dx_1 \cdots dx_m = 0$ en toda subcaja $B$, el integrando, que es continuo, es nulo: si fuera positivo en un punto, lo sería en una subcaja pequeña alrededor de él, y la integral en esa subcaja sería positiva (lo mismo si fuera negativo). Es el análogo de derivar respecto de $d$ en el apartado 5, punto (3).

**Lo que se exige no es que $D$ sea una divergencia a lo largo de cada $\vec{f}$.** Eso se cumple siempre: por ejemplo, $D = d_{x_1} G$ con $G(\vec{x}) = \int_{a_1}^{x_1} D(s, x_2, \dots, x_m) \,ds$. Pero ese campo depende de los valores de $\vec{f}$ en todo un segmento. Lo que se exige es un campo **local**, $F_k(\vec{x}, \vec{y})$, el mismo para todas las $\vec{f}$ y evaluado en el punto.

### 8.5. Cuándo existe $\vec{F}$: las condiciones de integrabilidad

Como en los apartados 5, punto (3), y 7.3:

* **$D$ tiene que ser afín en $Z$.** Si cada $F_k$ solo depende de $(\vec{x}, \vec{y})$,

  $$
  \begin{aligned}
  \sum_{k=1}^{m} d_{x_k} F_k = \sum_{k=1}^{m} \partial_{x_k} F_k + \sum_{i=1}^{n} \sum_{k=1}^{m} \partial_{y_i} F_k \cdot z_{ik}
  \end{aligned}
  $$

  es afín en $Z$. Así que $D = \alpha(\vec{x}, \vec{y}) + \sum_{i, k} \beta_{ik}(\vec{x}, \vec{y}) \cdot z_{ik}$, y la condición de simetría es la identidad $\alpha = \sum_k \partial_{x_k} F_k$ y $\beta_{ik} = \partial_{y_i} F_k$ para todo $i$ y todo $k$.
* **Las condiciones de integrabilidad.** Si existe $\vec{F}$, con $\alpha$ y las $\beta_{ik}$ de clase $C^1$,

  $$
  \begin{aligned}
  \partial_{y_j} \beta_{ik} = \partial_{y_i} \beta_{jk}, \qquad \partial_{y_i} \alpha = \sum_{k=1}^{m} \partial_{x_k} \beta_{ik}.
  \end{aligned}
  $$

  * La primera, para cada $k$, es el teorema de Schwarz para $F_k$ en las variables $\vec{y}$: $\partial_{y_j} \partial_{y_i} F_k = \partial_{y_i} \partial_{y_j} F_k$.
  * La segunda sale de derivar $\alpha = \sum_k \partial_{x_k} F_k$ respecto de $y_i$ e intercambiar el orden de derivación (teorema de Schwarz): $\partial_{y_i} \alpha = \sum_k \partial_{x_k} \partial_{y_i} F_k = \sum_k \partial_{x_k} \beta_{ik}$.
  * Con $m = 1$ son las del apartado 7.3, con $\beta_i := \beta_{i1}$: $\partial_{y_j} \beta_i = \partial_{y_i} \beta_j$ y $\partial_{y_i} \alpha = \partial_x \beta_i$.
  * Con $m \geq 2$, la segunda solo fija cómo depende $\alpha$ de $\vec{y}$. Cómo depende de $\vec{x}$ es libre, porque cualquier función continua de $\vec{x}$ es una divergencia (el último paso de la demostración siguiente).
* **También bastan**, si $\alpha$ y las $\beta_{ik}$ son de clase $C^2$ y los valores $\vec{y}$ recorren una caja $K \subseteq \mathbb{R}^n$ (o un conjunto estrellado). La demostración tiene tres pasos:
  1. **Las $\vec{y}$.** Con $\vec{x}$ y $k$ fijos, la primera condición dice que la forma $\sum_i \beta_{ik} \cdot dy_i$ es cerrada en $K$. Por el lema de Poincaré (apartado 7.3), existe $F_k^0(\vec{x}, \vec{y})$ con $\partial_{y_i} F_k^0 = \beta_{ik}$. La fórmula explícita del lema, con $\vec{y}_*$ el centro de $K$,

     $$
     \begin{aligned}
     F_k^0(\vec{x}, \vec{y}) = \int_0^1 \sum_{i=1}^{n} \beta_{ik}\big(\vec{x}, \vec{y}_* + s \cdot (\vec{y} - \vec{y}_*)\big) \cdot (y_i - y_{*, i}) \,ds,
     \end{aligned}
     $$

     muestra que también es derivable respecto de $\vec{x}$ (derivación bajo el signo integral, apartado 7.3).
  2. **Lo que falta no depende de $\vec{y}$.** $\chi := \alpha - \sum_k \partial_{x_k} F_k^0$ cumple $\partial_{y_i} \chi = \partial_{y_i} \alpha - \sum_k \partial_{x_k} \beta_{ik} = 0$, por la segunda condición. Como $K$ es una caja, para cada $\vec{y}$ la función $s \mapsto \chi\big(\vec{x}, \vec{y}_* + s \cdot (\vec{y} - \vec{y}_*)\big)$ tiene derivada nula en $[0, 1]$ y, por el teorema del valor medio, es constante: $\chi$ solo depende de $\vec{x}$.
  3. **Las $\vec{x}$.** Tomamos $F_1 := F_1^0 + \int_{a_1}^{x_1} \chi(s, x_2, \dots, x_m) \,ds$ y $F_k := F_k^0$ para $k \geq 2$. Entonces $\partial_{y_i} F_k = \beta_{ik}$ y $\sum_k \partial_{x_k} F_k = \sum_k \partial_{x_k} F_k^0 + \chi = \alpha$.
* **$\vec{F}$ no es única.** Se le puede sumar cualquier campo cuya divergencia sea nula a lo largo de toda $\vec{f}$. Con $m = 1$ solo hay constantes; con $m \geq 2$ hay muchos más, por ejemplo $(\partial_{x_2} \zeta, -\partial_{x_1} \zeta, 0, \dots, 0)$ con $\zeta(\vec{x})$ de clase $C^2$. Haber puesto $\chi$ en $F_1$, en el paso 3, es una de esas elecciones.
* **Con $m \geq 2$, $F_k$ podría depender de $Z$.** En una variable, $F$ no podía depender de $y'$, porque $\dfrac{dF}{dx}$ contendría $y''$ y nada lo cancela. Con varias variables, las derivadas segundas pueden cancelarse en la divergencia. Con $n = m = 2$, por el teorema de Schwarz,

  $$
  \begin{aligned}
  d_{x_1}\big(f_1 \cdot \partial_2 f_2\big) + d_{x_2}\big(-f_1 \cdot \partial_1 f_2\big) = \partial_1 f_1 \cdot \partial_2 f_2 - \partial_2 f_1 \cdot \partial_1 f_2 = \det J_{\vec{f}},
  \end{aligned}
  $$

  que es cuadrático en $Z$. Si se admiten estos campos, $D$ ya no tiene por qué ser afín. $\det J_{\vec{f}}$ es un **lagrangiano nulo**: sus expresiones de Euler–Lagrange son idénticamente nulas. Aquí nos quedamos con $F_k(\vec{x}, \vec{y})$, que basta para los ejemplos; la identidad del apartado 8.6 vale igual para cualquier campo con $D = \sum_k d_{x_k} F_k$ y $F_k$ de clase $C^1$ a lo largo de $\vec{f}$.

### 8.6. La identidad y el teorema de Noether

**El lema del apartado 6.2, en varias variables.** Para toda $\vec{\eta} = (\eta_1, \dots, \eta_n)$ de clase $C^1$ en $\Omega$:

$$
\begin{aligned}
&\sum_{i=1}^{n} \Big(\partial_{f_i} \bsL \cdot \eta_i + \sum_{k=1}^{m} u_{ik} \cdot d_{x_k} \eta_i\Big) \\
&\quad \overset{(1)}{=} \sum_{i=1}^{n} \Big(\partial_{f_i} \bsL \cdot \eta_i + \sum_{k=1}^{m} \big(d_{x_k}(u_{ik} \cdot \eta_i) - d_{x_k} u_{ik} \cdot \eta_i\big)\Big) \\
&\quad \overset{(2)}{=} \sum_{i=1}^{n} \Big(\partial_{f_i} \bsL - \sum_{k=1}^{m} d_{x_k} u_{ik}\Big) \cdot \eta_i + \sum_{k=1}^{m} d_{x_k}\Big(\sum_{i=1}^{n} u_{ik} \cdot \eta_i\Big) \\
&\quad \overset{(3)}{=} \sum_{i=1}^{n} \varphi_i \cdot \eta_i + \sum_{k=1}^{m} d_{x_k}\Big(\sum_{i=1}^{n} u_{ik} \cdot \eta_i\Big).
\end{aligned}
$$

* **(1)** Regla del producto para cada $i$ y cada $k$, $d_{x_k}(u_{ik} \cdot \eta_i) = d_{x_k} u_{ik} \cdot \eta_i + u_{ik} \cdot d_{x_k} \eta_i$, despejada para $u_{ik} \cdot d_{x_k} \eta_i$.
* **(2)** Sacamos factor común $\eta_i$ en cada sumando, y la suma de las derivadas es la derivada de la suma (linealidad).
* **(3)** Definición de $\varphi_i$.

**Notación: el tensor de energía-momento.** Como $\bsH$ en el apartado 6.5, definimos a lo largo de $\vec{f}$ la matriz $m \times m$

$$
\begin{aligned}
T_{kl} := \sum_{i=1}^{n} u_{ik} \cdot \partial_l f_i - \delta_{kl} \cdot \bsL,
\end{aligned}
$$

donde $\delta_{kl}$ vale $1$ si $k = l$ y $0$ si no. Con $m = 1$, $T_{11} = \sum_i p_i \cdot f'_i - \bsL = \bsH$. Se llama **tensor de energía-momento canónico**. «Tensor» es el nombre que da la física a las magnitudes con índices cuyas componentes cambian de una forma determinada al cambiar de coordenadas; aquí solo usamos que es una matriz $m \times m$ de funciones. «Canónico» indica que sale directamente del lagrangiano, sin modificarlo. «Energía-momento» se explica en el apartado 8.7.

**La identidad.** Las $\bar{\xi}_i$ son de clase $C^1$, porque las $\xi_i$, las $\tau_k$ y las $\partial_k f_i$ lo son. Aplicamos el lema con $\vec{\eta} = \bar{\vec{\xi}}$ al resultado del apartado 8.3, añadimos la hipótesis de simetría, $D = \sum_k d_{x_k} F_k$, y deshacemos $\bar{\xi}_i$:

$$
\begin{aligned}
\sum_{k=1}^{m} d_{x_k} F_k &\overset{(1)}{=} \sum_{i=1}^{n} \varphi_i \cdot \bar{\xi}_i + \sum_{k=1}^{m} d_{x_k}\Big(\sum_{i=1}^{n} u_{ik} \cdot \bar{\xi}_i + \tau_k \cdot \bsL\Big) \\
&\overset{(2)}{=} \sum_{i=1}^{n} \varphi_i \cdot \bar{\xi}_i + \sum_{k=1}^{m} d_{x_k}\Big(\sum_{i=1}^{n} u_{ik} \cdot \xi_i - \sum_{l=1}^{m} \tau_l \cdot \sum_{i=1}^{n} u_{ik} \cdot \partial_l f_i + \tau_k \cdot \bsL\Big) \\
&\overset{(3)}{=} \sum_{i=1}^{n} \varphi_i \cdot \bar{\xi}_i + \sum_{k=1}^{m} d_{x_k}\Big(\sum_{i=1}^{n} u_{ik} \cdot \xi_i - \sum_{l=1}^{m} T_{kl} \cdot \tau_l\Big).
\end{aligned}
$$

* **(1)** Hipótesis de simetría, el lema del apartado 8.3 y el lema anterior con $\vec{\eta} = \bar{\vec{\xi}}$; las divergencias se juntan por linealidad.
* **(2)** Deshacemos $\bar{\xi}_i = \xi_i - \sum_l \tau_l \cdot \partial_l f_i$ (con $l$ como índice de la suma, para no repetir $k$) y repartimos el producto.
* **(3)** Escribimos $\tau_k \cdot \bsL = \sum_l \delta_{kl} \cdot \tau_l \cdot \bsL$ y sacamos factor común $-\tau_l$: $-\sum_l \tau_l \cdot \big(\sum_i u_{ik} \cdot \partial_l f_i - \delta_{kl} \cdot \bsL\big) = -\sum_l T_{kl} \cdot \tau_l$.

Pasando $\sum_k d_{x_k} F_k$ al otro lado, por linealidad, queda la **identidad de Noether en varias variables**, válida para toda $\vec{f}$ de clase $C^2$:

$$
\begin{aligned}
\sum_{k=1}^{m} d_{x_k} Q_k = -\sum_{i=1}^{n} \varphi_i \cdot \Big(\xi_i - \sum_{k=1}^{m} \tau_k \cdot \partial_k f_i\Big),
\end{aligned}
$$

con

$$
\begin{aligned}
Q_k := \sum_{i=1}^{n} u_{ik} \cdot \xi_i - \sum_{l=1}^{m} T_{kl} \cdot \tau_l - F_k.
\end{aligned}
$$

* El campo $\vec{Q} = (Q_1, \dots, Q_m)$ es la **corriente de Noether**. Sus componentes son de clase $C^1$, porque lo son las $u_{ik}$, las $\xi_i$, las $T_{kl}$, las $\tau_l$ y las $F_k$ a lo largo de $\vec{f}$.
* Con $m = 1$, $Q_1$ es la $Q$ del apartado 7.4.
* Con $\vec{\tau} = \vec{0}$ es la corriente de «El teorema de Noether: parte matemática», $Q_k = \sum_i u_{ik} \cdot \xi_i - F_k$.

**El teorema: una ley de conservación local.** Si $\vec{f}_0$ es una solución, todas las $\varphi_i$ son nulas en $\Omega$, y

$$
\begin{aligned}
\sum_{k=1}^{m} d_{x_k} Q_k = 0 \qquad \text{en todo } \Omega:
\end{aligned}
$$

la corriente de Noether tiene divergencia nula. Con $m = 1$ es $Q' = 0$, y el teorema del valor medio da una constante (apartado 6.3). Con $m \geq 2$, un campo de divergencia nula no tiene por qué ser constante; lo que ocupa el lugar de la constante se ve en el apartado 8.7.

**Qué no hemos usado.** Que $\vec{f}$ sea solución: la identidad vale para toda $\vec{f}$. Ni ninguna condición sobre las derivadas segundas de $\bsL$ respecto de las variables $Z$.

### 8.7. Cuando una variable es el tiempo: la cantidad conservada

Seguimos el convenio de «El formalismo lagrangiano: parte matemática»: la variable temporal es $x_0 := t \in [t_1, t_2]$, y $x_1, \dots, x_m$ son las coordenadas espaciales, en una caja $\Omega$. **Atención:** hay $m + 1$ variables, y $\Omega$ es solo la caja espacial. Los índices $\mu, \nu = 0, \dots, m$ recorren todas las variables, con $d_{x_0} = d_t$, y los apartados 8.1 a 8.6 valen en el dominio $[t_1, t_2] \times \Omega$ con $\sum_\mu$ en lugar de $\sum_k$.

**La ley local** es una **ecuación de continuidad**: la que cumplen una **densidad** $\rho$, una cantidad por unidad de volumen, y su **densidad de flujo** $\vec{\jmath}$, la cantidad que atraviesa, por unidad de tiempo, una unidad de superficie perpendicular a cada eje, cuando esa cantidad no se crea ni se destruye: $d_t \rho + \sum_k d_{x_k} \jmath_k = 0$. Aquí $Q_0$ hace de densidad y $(Q_1, \dots, Q_m)$, de densidad de flujo:

$$
\begin{aligned}
d_t Q_0 + \sum_{k=1}^{m} d_{x_k} Q_k = 0.
\end{aligned}
$$

**La ley integral.** Integramos en $\Omega$ para cada $t$ fijo:

$$
\begin{aligned}
\dfrac{d}{dt} \int_\Omega Q_0 \,dx_1 \cdots dx_m
&\overset{(1)}{=} \int_\Omega d_t Q_0 \,dx_1 \cdots dx_m \\
&\overset{(2)}{=} -\sum_{k=1}^{m} \int_\Omega d_{x_k} Q_k \,dx_1 \cdots dx_m \\
&\overset{(3)}{=} -\sum_{k=1}^{m} \int_{\Omega_k} \Big[Q_k\Big]_{x_k = a_k}^{x_k = b_k} d\hat{x}_k.
\end{aligned}
$$

* **(1)** Derivación bajo el signo integral: $Q_0$ y $d_t Q_0$ son continuas en el conjunto cerrado y acotado $[t_1, t_2] \times \Omega$.
* **(2)** La ley local, sobre una solución.
* **(3)** Teorema de Fubini y regla de Barrow en cada variable espacial, como en el apartado 8.4, igualdad (4); $\Omega_k$ es la caja de las otras $m - 1$ coordenadas espaciales.

**El teorema.** Si las condiciones de contorno anulan el flujo por la frontera de $\Omega$ en todo instante, la cantidad

$$
\begin{aligned}
\mathcal{Q}(t) := \int_\Omega Q_0 \,dx_1 \cdots dx_m
\end{aligned}
$$

tiene derivada nula y, por el teorema del valor medio, es constante en $[t_1, t_2]$. Es lo que ocupa el lugar del apartado 6.3. Ahora hay dos hipótesis de naturaleza distinta:

* **la simetría**, que da la ley local para toda solución;
* **las condiciones de contorno**, que hacen que el total se conserve.

Una simetría de $\bsL$ da siempre la ley local, pero el total no se conserva si el contorno rompe la simetría (apartado 8.8).

**Las traslaciones dan el tensor $T$.** Si $\bsL$ no depende explícitamente de $x_\nu$, la traslación en esa variable, $\vec{\tau} = \vec{e}_\nu$ y $\vec{\xi} = \vec{0}$, tiene $D = \partial_{x_\nu} \bsL = 0$ (forma de cuatro términos), es una simetría con $\vec{F} = \vec{0}$, y su corriente es

$$
\begin{aligned}
Q_\mu = -T_{\mu\nu}, \qquad \mu = 0, \dots, m.
\end{aligned}
$$

La columna $\nu$ de $T$ es, cambiada de signo, la corriente de la traslación en $x_\nu$:

* **la traslación en el tiempo** ($\nu = 0$) da la densidad $-T_{00} = -\big(\sum_i u_{i0} \cdot \partial_t f_i - \bsL\big)$, menos la densidad de energía: es $\bsH$ con $\partial_t$ en el lugar de la prima;
* **las traslaciones en el espacio** ($\nu = k \geq 1$) dan las densidades $-T_{0k} = -\sum_i u_{i0} \cdot \partial_k f_i$, las de la cantidad de movimiento del campo en la dirección $x_k$. El signo menos aparece porque trasladar las variables en $+\varepsilon$ cambia los valores, en un punto fijo, en $-\varepsilon \cdot \partial_k f_i$: es $\bar{\xi}_i = -\partial_k f_i$, y la densidad es $\sum_i u_{i0} \cdot \bar{\xi}_i$.

De ahí el nombre de tensor de energía-momento.

### 8.8. Ejemplo: la cuerda vibrante

Es la cuerda de «El teorema de Noether: ejemplos físicos»: $f(t, x)$ es el desplazamiento transversal, en el instante $t$, del punto de la cuerda que está en reposo en $x$. Para desplazamientos pequeños, la energía cinética por unidad de longitud es $\dfrac{1}{2} \cdot \mu \cdot (\partial_t f)^2$, con $\mu$ la densidad lineal de masa, y la energía elástica por unidad de longitud es $\dfrac{1}{2} \cdot T_0 \cdot (\partial_x f)^2$, con $T_0$ la tensión; el lagrangiano es su diferencia. Tomamos $\mu = 1$ y escribimos $T_0 = c^2$, donde $c$ resulta ser la velocidad de propagación de las ondas (allí la tensión se llamaba $\tau$, que aquí es el generador). Hay una función, $n = 1$, y una coordenada espacial, $m = 1$: $(x_0, x_1) = (t, x)$, con $x \in [a_1, b_1]$. Con una sola función omitimos el índice $i$:

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot (\partial_t f)^2 - \dfrac{c^2}{2} \cdot (\partial_x f)^2, \qquad u_0 = \partial_t f, \qquad u_1 = -c^2 \cdot \partial_x f.
\end{aligned}
$$

La ecuación de Euler–Lagrange, $\varphi = -d_t(\partial_t f) + d_x(c^2 \cdot \partial_x f) = 0$, es la ecuación de ondas, $\partial_t^2 f = c^2 \cdot \partial_x^2 f$. El tensor de energía-momento, con $\mathcal{E}$ la densidad de energía, es

$$
\begin{aligned}
T &= \begin{pmatrix} T_{00} & T_{01} \\ T_{10} & T_{11} \end{pmatrix} = \begin{pmatrix} \mathcal{E} & \partial_t f \cdot \partial_x f \\ -c^2 \cdot \partial_x f \cdot \partial_t f & -\mathcal{E} \end{pmatrix}, \\
\mathcal{E} &:= \dfrac{1}{2} \cdot (\partial_t f)^2 + \dfrac{c^2}{2} \cdot (\partial_x f)^2.
\end{aligned}
$$

Por ejemplo, $T_{11} = u_1 \cdot \partial_x f - \bsL = -c^2 \cdot (\partial_x f)^2 - \dfrac{1}{2} \cdot (\partial_t f)^2 + \dfrac{c^2}{2} \cdot (\partial_x f)^2 = -\mathcal{E}$.

$\bsL$ no depende de $t$, de $x$ ni de $f$, así que las tres traslaciones son simetrías con $\vec{F} = \vec{0}$. Con los extremos fijos, $f(t, a_1) = f(t, b_1) = 0$ en todo instante, $\partial_t f = 0$ en los extremos:

| Simetría | $(\vec{\tau}, \xi)$ | $Q_0$ | $Q_1$ | $Q_1$ en los extremos fijos |
| ---------------------------------------- | -------------------------- | -------------------------- | -------------------------------- | ---------------------------- |
| Traslación en $t$ | $\big((1, 0), 0\big)$ | $-\mathcal{E}$ | $c^2 \cdot \partial_x f \cdot \partial_t f$ | $0$ |
| Traslación en $x$ | $\big((0, 1), 0\big)$ | $-\partial_t f \cdot \partial_x f$ | $\mathcal{E}$ | $\dfrac{c^2}{2} \cdot (\partial_x f)^2$ |
| Desplazamiento vertical | $\big((0, 0), 1\big)$ | $\partial_t f$ | $-c^2 \cdot \partial_x f$ | $-c^2 \cdot \partial_x f$ |

Table: Las tres traslaciones de la cuerda vibrante.

* **La traslación en $t$:** el flujo se anula en los extremos y la energía, $\int_{a_1}^{b_1} \mathcal{E} \,dx$, es constante.
* **La traslación en $x$** es la única de las tres que mueve las variables ($\vec{\tau} \neq \vec{0}$), y es la novedad respecto de «El teorema de Noether: ejemplos físicos». La ley local se cumple, pero el total no se conserva: por el apartado 8.7,

  $$
  \begin{aligned}
  \dfrac{d}{dt} \int_{a_1}^{b_1} \big(-\partial_t f \cdot \partial_x f\big) \,dx &= -\Big[\mathcal{E}\Big]_{x = a_1}^{x = b_1} \\
  &= -\dfrac{c^2}{2} \cdot \Big((\partial_x f)^2(t, b_1) - (\partial_x f)^2(t, a_1)\Big),
  \end{aligned}
  $$

  que en general no es nulo. $\bsL$ es invariante por traslaciones en $x$, pero los extremos fijos no.
* **El desplazamiento vertical:** su ley local es la propia ecuación de ondas, $d_t(\partial_t f) - d_x(c^2 \cdot \partial_x f) = 0$, y el total, la cantidad de movimiento transversal, cambia por las fuerzas de los soportes, como en «El teorema de Noether: ejemplos físicos».
* **Con condiciones periódicas**, $f$ y $\partial_x f$ iguales en los dos extremos, los tres flujos coinciden en $a_1$ y en $b_1$, los corchetes se anulan y las tres cantidades se conservan.

Comprobación de la identidad con la traslación en $x$: $\bar{\xi} = 0 - 1 \cdot \partial_x f$, y

$$
\begin{aligned}
d_t Q_0 + d_x Q_1 &= -\partial_t^2 f \cdot \partial_x f - \partial_t f \cdot \partial_t \partial_x f + \partial_t f \cdot \partial_x \partial_t f + c^2 \cdot \partial_x f \cdot \partial_x^2 f \\
&= \partial_x f \cdot \big(c^2 \cdot \partial_x^2 f - \partial_t^2 f\big) = -\varphi \cdot \bar{\xi},
\end{aligned}
$$

porque $\varphi = c^2 \cdot \partial_x^2 f - \partial_t^2 f$: se anula sobre las soluciones, como dice el teorema.

Las cuentas de este apartado (el $D$ calculado desde la definición, con el determinante y la jacobiana; la forma de cuatro términos; el lema; la identidad; el lagrangiano nulo; el tensor $T$ y las tres corrientes de la cuerda) están comprobadas con SymPy en Teorema-de-Noether-v2-comprobaciones.py.

## 9. Flujos, derivada de Fréchet y derivada de Lie

Hasta aquí solo hemos usado el primer orden de la familia $\Phi_\varepsilon$: su generador. Este apartado completa el cuadro en seis pasos:

* cómo se recupera la familia a partir del generador cuando cumple la ley de grupo (apartado 9.1);
* la derivada de Fréchet, que da las reglas de derivación sin coordenadas y permite pasar, en el apartado 10, a funciones con valores en espacios de dimensión infinita (apartado 9.2);
* cómo actúa la familia sobre las derivadas de $f$: la prolongación (apartado 9.3);
* la derivada de Lie, que muestra que $D$ es la derivada del elemento $\bsL \cdot dx$ a lo largo del flujo (apartado 9.4);
* por qué, con la ley de grupo, la condición infinitesimal da la invariancia para todo $\varepsilon$ (apartado 9.5);
* las simetrías cuyo generador depende de las derivadas, que son las de la versión anterior (apartado 9.6).

Trabajamos en el plano, con una función de una variable; al final de cada subapartado se indica qué cambia con $n$ funciones o con $m$ variables.

### 9.1. Del generador a la familia: el flujo

**Definiciones.** Sea $U$ un abierto del plano.

* Un **campo vectorial** en $U$ asigna a cada punto $P = (x, y)$ un vector $V(P) = \big(\tau(P), \xi(P)\big)$. El generador de una familia (apartado 3.2) es un campo vectorial.
* Una **curva integral** de $V$ es una curva $\varepsilon \mapsto \big(X(\varepsilon), Y(\varepsilon)\big)$ cuyo vector velocidad es, para cada $\varepsilon$, el del campo en el punto donde está. Es un sistema de dos ecuaciones diferenciales ordinarias de primer orden:

  $$
  \begin{aligned}
  \dfrac{dX}{d\varepsilon} = \tau(X, Y), \qquad \dfrac{dY}{d\varepsilon} = \xi(X, Y).
  \end{aligned}
  $$

* El **flujo** de $V$ es la familia $\Phi_\varepsilon$ que lleva cada punto $P$ al punto que alcanza, con el parámetro $\varepsilon$, la curva integral que sale de $P$ con $\varepsilon = 0$.

**Lo que se sabe del Tema 1, apartado 4.4.** Allí se estudia en el plano $(t, x)$, con el parámetro $s$ y el campo $(\xi^t, \xi^x)$; las demostraciones valen igual en $\mathbb{R}^m \times \mathbb{R}^n$:

* si $V$ es de clase $C^1$, por cada punto pasa una única curva integral (teorema de Picard–Lindelöf), definida al menos para $|\varepsilon|$ pequeño;
* el flujo cumple $\Phi_0 = Id$ y la ley de grupo, $\Phi_\varepsilon \circ \Phi_\eta = \Phi_{\varepsilon + \eta}$, allí donde está definido.

A eso añadimos, sin demostración, el **teorema de dependencia regular respecto de las condiciones iniciales**: si $V$ es de clase $C^k$, con $k \geq 1$, el flujo $\Phi_\varepsilon(P)$ es de clase $C^k$ como función de $(\varepsilon, P)$. Con $V$ de clase $C^2$, el flujo cumple, por tanto, lo que pide el apartado 3.1.

**El recíproco: una familia con la ley de grupo es el flujo de su generador.** Sea $\Phi_\varepsilon$ una familia con la ley de grupo, derivable respecto de $\varepsilon$, con generador $V$, y sea $P$ un punto fijo:

$$
\begin{aligned}
\dfrac{d}{d\varepsilon} \Phi_\varepsilon(P)
&\overset{(1)}{=} \left.\dfrac{d}{d\sigma} \Phi_{\varepsilon + \sigma}(P)\right|_{\sigma = 0} \\
&\overset{(2)}{=} \left.\dfrac{d}{d\sigma} \Phi_\sigma\big(\Phi_\varepsilon(P)\big)\right|_{\sigma = 0} \\
&\overset{(3)}{=} V\big(\Phi_\varepsilon(P)\big).
\end{aligned}
$$

* **(1)** La derivada respecto de $\varepsilon$ es la derivada en $\sigma = 0$ de la función desplazada $\sigma \mapsto \Phi_{\varepsilon + \sigma}(P)$.
* **(2)** Ley de grupo: $\Phi_{\varepsilon + \sigma} = \Phi_\sigma \circ \Phi_\varepsilon$.
* **(3)** Definición del generador (apartado 3.2), aplicada en el punto $\Phi_\varepsilon(P)$.

Así, $\varepsilon \mapsto \Phi_\varepsilon(P)$ es una curva integral de $V$ que sale de $P$, y por la unicidad es la del flujo. **Con la ley de grupo, el generador determina la familia.**

**Sin la ley de grupo, no la determina.** $(x, y + \varepsilon)$ y $(x, y + \sin\varepsilon)$ tienen el mismo generador, $(0, 1)$. La primera es su flujo; la segunda es la misma familia con otro parámetro, $\sin\varepsilon$ en lugar de $\varepsilon$.

**Tres ejemplos.**

1. **El giro**, $V = (-y, x)$. Hay que resolver $\dfrac{dX}{d\varepsilon} = -Y$ y $\dfrac{dY}{d\varepsilon} = X$, con $(X, Y) = (x, y)$ en $\varepsilon = 0$. La familia del apartado 3.2 lo cumple:

   $$
   \begin{aligned}
   \dfrac{d}{d\varepsilon}\big(x \cdot \cos\varepsilon - y \cdot \sin\varepsilon\big) &= -\big(x \cdot \sin\varepsilon + y \cdot \cos\varepsilon\big), \\
   \dfrac{d}{d\varepsilon}\big(x \cdot \sin\varepsilon + y \cdot \cos\varepsilon\big) &= x \cdot \cos\varepsilon - y \cdot \sin\varepsilon,
   \end{aligned}
   $$

   y en $\varepsilon = 0$ vale $(x, y)$. Por la unicidad, es el flujo.
2. **El cambio de velocidad**, $V = (0, x)$, con $x$ en el papel del tiempo. $\dfrac{dX}{d\varepsilon} = 0$ da $X = x$, y entonces $\dfrac{dY}{d\varepsilon} = x$ da $Y = y + \varepsilon \cdot x$. El flujo es $\Phi_\varepsilon(x, y) = (x, y + \varepsilon \cdot x)$, el de la tercera fila de la tabla del apartado 6.4.
3. **La escala de los valores**, $V = (0, y)$. $\dfrac{dY}{d\varepsilon} = Y$ da $Y = e^\varepsilon \cdot y$, y el flujo es $(x, e^\varepsilon \cdot y)$. La familia $\big(x, (1 + \varepsilon) \cdot y\big)$ del apartado 5, punto (3), tiene el mismo generador, pero no es un flujo, porque $(1 + \varepsilon) \cdot (1 + \eta) \neq 1 + \varepsilon + \eta$.

**Con $n$ funciones o $m$ variables**, el campo tiene $m + n$ componentes, $(\vec{\tau}, \vec{\xi})$, y el sistema, $m + n$ ecuaciones; lo demás no cambia.

### 9.2. La derivada de Fréchet

En los apartados 5 a 8 se han usado cinco herramientas del cálculo: la regla de la cadena, la regla del producto, el desarrollo de Taylor de primer orden, la desigualdad del valor medio y el teorema de Schwarz. Todas se han usado con derivadas parciales respecto de coordenadas. La derivada de Fréchet las formula sin coordenadas, y así valen también cuando los valores de $f$ están en un espacio de dimensión infinita, como un espacio de funciones (apartado 10).

#### Espacios normados, espacios de Banach y dual

* Un **espacio normado** es un espacio vectorial real $E$ con una **norma**: una función $\lVert \cdot \rVert: E \to [0, \infty)$ tal que $\lVert v \rVert = 0$ solo si $v = 0$, $\lVert \lambda \cdot v \rVert = |\lambda| \cdot \lVert v \rVert$ y $\lVert v + w \rVert \leq \lVert v \rVert + \lVert w \rVert$. La norma da las distancias, $\lVert v - w \rVert$, y con ellas los límites y la continuidad.
* Un **espacio de Banach** es un espacio normado completo: toda sucesión de Cauchy, es decir, con $\lVert v_k - v_l \rVert \to 0$ cuando $k, l \to \infty$, tiene límite en $E$.
* **Ejemplos.** $\mathbb{R}^n$, con la norma euclídea. El espacio $C^0([a, b])$ de las funciones continuas en $[a, b]$, con la norma $\lVert g \rVert_\infty := \max_{x \in [a, b]} |g(x)|$; es completo porque el límite de una sucesión de funciones continuas en esa norma, es decir, el límite uniforme, es continuo, y tiene dimensión infinita, porque las funciones $1, x, x^2, \dots$ son linealmente independientes.
* Una aplicación lineal $A: E \to F$ entre espacios normados es **continua** si y solo si existe una constante $C$ con $\lVert A\,v \rVert \leq C \cdot \lVert v \rVert$ para todo $v$; la menor de esas constantes es la **norma** de $A$, $\lVert A \rVert$. En dimensión finita, toda aplicación lineal es continua. En dimensión infinita, no: la derivada $g \mapsto g'$, de las funciones de clase $C^1$ en $[0, 2 \cdot \pi]$ en $C^0([0, 2 \cdot \pi])$, con la norma $\lVert \cdot \rVert_\infty$ en los dos, no lo es, porque $\lVert \sin(k \cdot x) \rVert_\infty = 1$ y $\lVert k \cdot \cos(k \cdot x) \rVert_\infty = k$ para todo entero $k \geq 1$.
* El **dual** de $E$, $E^*$, es el espacio de las aplicaciones lineales continuas $\alpha: E \to \mathbb{R}$. Escribimos $\langle \alpha, v \rangle := \alpha(v)$. En $\mathbb{R}^n$, cada $\alpha$ es un vector fila y $\langle \alpha, v \rangle = \sum_i \alpha_i \cdot v_i$: es el $\vec{p} \cdot \vec{\xi}$ del apartado 7. En el apartado 10, el momento $p$ será un elemento de $E^*$.

#### La derivada

Sean $E$ y $F$ espacios normados, $U \subseteq E$ abierto, $g: U \to F$ y $a \in U$. La función $g$ es **derivable en el sentido de Fréchet** en $a$ si existe una aplicación lineal continua $Dg(a): E \to F$ tal que

$$
\begin{aligned}
&\lim_{v \to 0} \dfrac{\lVert g(a + v) - g(a) - Dg(a)\,v \rVert}{\lVert v \rVert} = 0, \\
&\text{es decir,} \qquad g(a + v) = g(a) + Dg(a)\,v + o(\lVert v \rVert).
\end{aligned}
$$

* **Es única.** Si $A$ y $B$ cumplen la definición, $(A - B)\,v = o(\lVert v \rVert)$. Con $v = t \cdot w$, para un $w$ fijo, y $t \to 0$, la linealidad da $(A - B)\,w = \dfrac{o(|t|)}{t} \to 0$, así que $A\,w = B\,w$ para todo $w$.
* **Clase $C^1$.** $g$ es de clase $C^1$ si es derivable en todo $U$ y $a \mapsto Dg(a)$ es continua, con la norma de las aplicaciones lineales.
* **En $\mathbb{R}^n$ es la matriz jacobiana.** Si $g: \mathbb{R}^n \to \mathbb{R}^l$ es derivable en $a$ y $\vec{e}_j$ es el vector $j$ de la base:

  $$
  \begin{aligned}
  Dg(a)\,\vec{e}_j \overset{(1)}{=} \lim_{t \to 0} \dfrac{Dg(a)\,(t \cdot \vec{e}_j)}{t} \overset{(2)}{=} \lim_{t \to 0} \dfrac{g(a + t \cdot \vec{e}_j) - g(a)}{t} \overset{(3)}{=} \partial_j g(a).
  \end{aligned}
  $$

  * **(1)** Linealidad: el cociente vale $Dg(a)\,\vec{e}_j$ para todo $t \neq 0$.
  * **(2)** Definición: $g(a + t \cdot \vec{e}_j) - g(a) - Dg(a)\,(t \cdot \vec{e}_j) = o(|t|)$, y dividido por $t$ tiende a $0$.
  * **(3)** Definición de derivada parcial.

  Las columnas de la matriz de $Dg(a)$ son las derivadas parciales: es la matriz jacobiana. Recíprocamente, si las derivadas parciales existen y son continuas, $g$ es derivable en el sentido de Fréchet (cálculo de varias variables). En $\mathbb{R}^n$, por tanto, «de clase $C^1$» significa lo mismo en los dos sentidos.

#### Las reglas de derivación

Se demuestran como en $\mathbb{R}^n$, con la norma en lugar del valor absoluto.

1. **Regla de la cadena.** Si $g_1: E \to F$ es derivable en $a$ y $g_2: F \to G$ lo es en $g_1(a)$, entonces $D(g_2 \circ g_1)(a) = Dg_2\big(g_1(a)\big) \circ Dg_1(a)$. Con $\delta := g_1(a + v) - g_1(a) = Dg_1(a)\,v + o(\lVert v \rVert)$ y $A := Dg_2\big(g_1(a)\big)$:

   $$
   \begin{aligned}
   g_2\big(g_1(a + v)\big) &\overset{(1)}{=} g_2\big(g_1(a) + \delta\big) \\
   &\overset{(2)}{=} g_2\big(g_1(a)\big) + A\,\delta + o(\lVert \delta \rVert) \\
   &\overset{(3)}{=} g_2\big(g_1(a)\big) + A\,Dg_1(a)\,v + A\,o(\lVert v \rVert) + o(\lVert \delta \rVert) \\
   &\overset{(4)}{=} g_2\big(g_1(a)\big) + A\,Dg_1(a)\,v + o(\lVert v \rVert).
   \end{aligned}
   $$

   * **(1)** Definición de $\delta$.
   * **(2)** Derivabilidad de $g_2$ en $g_1(a)$.
   * **(3)** Linealidad de $A$.
   * **(4)** $A$ es continua, así que $\lVert A\,o(\lVert v \rVert) \rVert \leq \lVert A \rVert \cdot o(\lVert v \rVert)$; y $\lVert \delta \rVert \leq \big(\lVert Dg_1(a) \rVert + 1\big) \cdot \lVert v \rVert$ para $v$ pequeño, así que $o(\lVert \delta \rVert) = o(\lVert v \rVert)$.
2. **Regla del producto.** Sea $B: F_1 \times F_2 \to G$ **bilineal** (lineal en cada argumento) y continua: $\lVert B(w_1, w_2) \rVert \leq C \cdot \lVert w_1 \rVert \cdot \lVert w_2 \rVert$. Si $g_1: E \to F_1$ y $g_2: E \to F_2$ son derivables en $a$,

   $$
   \begin{aligned}
   D\big[B(g_1, g_2)\big](a)\,v = B\big(Dg_1(a)\,v,\ g_2(a)\big) + B\big(g_1(a),\ Dg_2(a)\,v\big).
   \end{aligned}
   $$

   Al desarrollar $B\big(g_1(a) + \delta_1, g_2(a) + \delta_2\big)$ por la bilinealidad aparecen los dos términos de la derecha y $B(\delta_1, \delta_2)$, cuya norma es como mucho $C \cdot \lVert \delta_1 \rVert \cdot \lVert \delta_2 \rVert = o(\lVert v \rVert)$. Ejemplos de $B$: el producto de números reales, el producto escalar de $\mathbb{R}^n$ y el emparejamiento $(\alpha, w) \mapsto \langle \alpha, w \rangle$ de $E^* \times E$ en $\mathbb{R}$, que es la regla $(p \cdot \xi)' = p' \cdot \xi + p \cdot \xi'$ de los apartados 6 y 7.
3. **Desarrollo de Taylor de primer orden.** Es la propia definición.
4. **Desigualdad del valor medio.** Si $g$ es de clase $C^1$ en un abierto que contiene el segmento $S := \{z_1 + t \cdot (z_2 - z_1) : t \in [0, 1]\}$, entonces

   $$
   \begin{aligned}
   \lVert g(z_2) - g(z_1) \rVert \leq \sup_{z \in S} \lVert Dg(z) \rVert \cdot \lVert z_2 - z_1 \rVert.
   \end{aligned}
   $$

   Con valores vectoriales no hay un punto intermedio que dé la igualdad, como en una variable, pero sí esta desigualdad. Es la que usa el apartado 8.1.
5. **Derivada segunda y teorema de Schwarz.** $Dg$ es una función de $U$ en el espacio normado de las aplicaciones lineales continuas de $E$ en $F$. Su derivada en $a$, $D(Dg)(a)$, asigna a cada $v$ una de esas aplicaciones lineales, y definimos la aplicación bilineal $D^2 g(a)(v, w) := \big(D(Dg)(a)\,v\big)\,w$. Si $g$ es de clase $C^2$, es simétrica: $D^2 g(a)(v, w) = D^2 g(a)(w, v)$. En $\mathbb{R}^n$ sus elementos son las $\partial_i \partial_j g(a)$, y la simetría es el teorema de Schwarz.

**Lo que se gana.** Los apartados 5 a 8 solo usan estas cinco reglas y, para acotar los restos, que una función continua en un conjunto cerrado y acotado de $\mathbb{R}^N$ está acotada. Lo primero vale igual en un espacio de Banach; lo segundo hay que sustituirlo, porque en dimensión infinita un conjunto cerrado y acotado no tiene por qué ser compacto (apartado 10). Por otra parte, el generador del apartado 3.2 y el $D$ del apartado 5 son derivadas de funciones de una variable real, $\varepsilon$: el caso $E = \mathbb{R}$ de la derivada de Fréchet.

### 9.3. Cómo actúa la familia sobre las derivadas: la prolongación

**La derivada total como operación sobre funciones.** Para una función $G(x, y, y')$, donde $y'$ es el nombre de una variable más, definimos

$$
\begin{aligned}
d_x G := \partial_x G + y' \cdot \partial_y G + y'' \cdot \partial_{y'} G,
\end{aligned}
$$

con $y''$ el nombre de otra variable. Por la regla de la cadena, a lo largo de $f$ es la derivada de la función compuesta:

$$
\begin{aligned}
(d_x G)\big(x, f(x), f'(x), f''(x)\big) = \dfrac{d}{dx} G\big(x, f(x), f'(x)\big).
\end{aligned}
$$

Si $G$ solo depende de $(x, y)$, $d_x G = \partial_x G + y' \cdot \partial_y G$: es la prima de $\tau'$ y $\xi'$ del apartado 5. Con $m$ variables, es el $d_{x_k}$ del apartado 8.

**Definición.** La **prolongación** de $\Phi_\varepsilon$ es la transformación de los puntos $(x, y, y')$

$$
\begin{aligned}
\Phi^{(1)}_\varepsilon(x, y, y') := \big(X_\varepsilon,\ Y_\varepsilon,\ Y^{(1)}_\varepsilon\big), \qquad Y^{(1)}_\varepsilon := \dfrac{d_x Y_\varepsilon}{d_x X_\varepsilon},
\end{aligned}
$$

con $X_\varepsilon$ e $Y_\varepsilon$ evaluadas en $(x, y)$, y definida donde $d_x X_\varepsilon \neq 0$.

* **Qué hace.** Lleva un punto de la gráfica y su pendiente al punto correspondiente de la gráfica transformada y a su pendiente. Si $(x, y, y') = \big(x, f(x), f'(x)\big)$, entonces $\Phi^{(1)}_\varepsilon(x, y, y') = \big(\tilde{x}, \tilde{f}(\tilde{x}), \tilde{f}'(\tilde{x})\big)$, con $\tilde{x} = \tilde{x}(x)$, porque $\tilde{f}'\big(\tilde{x}(x)\big) = \dfrac{\tilde{y}'(x)}{\tilde{x}'(x)}$ (apartado 5, punto (1)).
* **Hereda la ley de grupo.** Si $\Phi_\varepsilon \circ \Phi_\eta = \Phi_{\varepsilon + \eta}$, también $\Phi^{(1)}_\varepsilon \circ \Phi^{(1)}_\eta = \Phi^{(1)}_{\varepsilon + \eta}$. Por cada punto $(x, y, y')$ pasa la gráfica de alguna función con esa pendiente, por ejemplo la recta $u \mapsto y + y' \cdot (u - x)$. Transformarla con $\Phi_\eta$ y después con $\Phi_\varepsilon$ es transformarla con $\Phi_{\varepsilon + \eta}$, y $\Phi^{(1)}$ solo registra el punto y la pendiente de la gráfica transformada, que no dependen de la función elegida.
* **Su generador** es $V^{(1)} := (\tau, \xi, \xi^{(1)})$, con $\xi^{(1)} := \partial_\varepsilon Y^{(1)}_\varepsilon\big|_{\varepsilon = 0}$:

  $$
  \begin{aligned}
  \xi^{(1)} &\overset{(1)}{=} \left.\dfrac{\partial_\varepsilon\big(d_x Y_\varepsilon\big) \cdot d_x X_\varepsilon - d_x Y_\varepsilon \cdot \partial_\varepsilon\big(d_x X_\varepsilon\big)}{\big(d_x X_\varepsilon\big)^2}\right|_{\varepsilon = 0} \\
  &\overset{(2)}{=} \dfrac{d_x \xi \cdot 1 - y' \cdot d_x \tau}{1^2} \\
  &\overset{(3)}{=} d_x \xi - y' \cdot d_x \tau.
  \end{aligned}
  $$

  * **(1)** Regla de derivación del cociente, respecto de $\varepsilon$.
  * **(2)** En $\varepsilon = 0$, $X_0 = x$ e $Y_0 = y$, así que $d_x X_0 = 1$ y $d_x Y_0 = y'$. Además, $\partial_\varepsilon\big(d_x Y_\varepsilon\big)\big|_{\varepsilon = 0} = d_x\big(\partial_\varepsilon Y_\varepsilon\big|_{\varepsilon = 0}\big) = d_x \xi$, porque $d_x$ solo contiene derivadas respecto de $x$ y de $y$, que conmutan con la derivada respecto de $\varepsilon$ (teorema de Schwarz); lo mismo con $X_\varepsilon$ y $\tau$.
  * **(3)** Simplificamos.

  A lo largo de $f$ es $\xi' - \tau' \cdot f'$, el coeficiente de $\varepsilon$ de la pendiente en el apartado 5, punto (2).
* **Ejemplo: el giro.** Con $(\tau, \xi) = (-y, x)$, $\xi^{(1)} = d_x x - y' \cdot d_x(-y) = 1 + y'^2$. Comprobación directa: si la pendiente es $y' = \tan\alpha$, el giro la lleva a $\tan(\alpha + \varepsilon)$, cuya derivada en $\varepsilon = 0$ es $1 + \tan^2\alpha$.
* **Con $m$ variables**, $\Phi^{(1)}_\varepsilon$ actúa sobre $(\vec{x}, \vec{y}, Z)$, con $Z \mapsto J_{\tilde{\vec{y}}} \cdot J_{\tilde{\vec{x}}}^{-1}$ (apartado 8.2), y su generador tiene las componentes $\xi^{(1)}_{il} = d_{x_l} \xi_i - \sum_k z_{ik} \cdot d_{x_l} \tau_k$.

### 9.4. La derivada de Lie

**Definición.** Sea $V$ un campo vectorial con flujo $\Phi_\varepsilon$, y $G$ una función de clase $C^1$ en el mismo espacio. La **derivada de Lie** de $G$ a lo largo de $V$ es

$$
\begin{aligned}
\mathcal{L}_V G := \left.\dfrac{\partial}{\partial \varepsilon}\big(G \circ \Phi_\varepsilon\big)\right|_{\varepsilon = 0}:
\end{aligned}
$$

lo que cambia $G$, por unidad de $\varepsilon$, para un punto que se mueve con el flujo. **Aviso:** $\mathcal{L}$, caligráfica, es la derivada de Lie; $\bsL$, en negrita, sigue siendo el lagrangiano.

* **Fórmula.** Por la regla de la cadena (apartado 9.2),

  $$
  \begin{aligned}
  \mathcal{L}_V G(P) = DG(P)\,V(P) = \tau \cdot \partial_x G + \xi \cdot \partial_y G.
  \end{aligned}
  $$

  Solo depende del valor de $V$ en $P$: cualquier familia con el mismo generador da la misma derivada de Lie, aunque no cumpla la ley de grupo.
* **Para funciones de $(x, y, y')$**, con el campo prolongado: $\mathcal{L}_{V^{(1)}} G = \tau \cdot \partial_x G + \xi \cdot \partial_y G + \xi^{(1)} \cdot \partial_{y'} G$.

**El elemento de longitud.** Al transformar la gráfica, el elemento $dx$ pasa a ser $d\tilde{x} = d_x X_\varepsilon \cdot dx$ (apartado 5, punto (1)). Su derivada de Lie es el ritmo de ese cambio, y la escribimos con el factor $dx$ para recordar que es lo que se integra:

$$
\begin{aligned}
\mathcal{L}_V(dx) := \left.\partial_\varepsilon\big(d_x X_\varepsilon\big)\right|_{\varepsilon = 0} \cdot dx = d_x \tau \cdot dx.
\end{aligned}
$$

Con $m$ variables, el factor es $\det J_{\tilde{\vec{x}}}$, y su derivada en $\varepsilon = 0$ es $\sum_k d_{x_k} \tau_k$ (apartado 8.2): el elemento de volumen cambia al ritmo de la divergencia de $\vec{\tau}$.

**El elemento lagrangiano.** Del mismo modo,

$$
\begin{aligned}
\mathcal{L}_V(\bsL \cdot dx) := \left.\partial_\varepsilon\Big(\big(\bsL \circ \Phi^{(1)}_\varepsilon\big) \cdot d_x X_\varepsilon\Big)\right|_{\varepsilon = 0} \cdot dx.
\end{aligned}
$$

El coeficiente de $dx$ es exactamente el $D$ del apartado 5:

$$
\begin{aligned}
&\left.\partial_\varepsilon\Big(\big(\bsL \circ \Phi^{(1)}_\varepsilon\big) \cdot d_x X_\varepsilon\Big)\right|_{\varepsilon = 0} \\
&\quad \overset{(1)}{=} \left.\partial_\varepsilon\big(\bsL \circ \Phi^{(1)}_\varepsilon\big)\right|_{\varepsilon = 0} \cdot d_x X_0 + \bsL \cdot \left.\partial_\varepsilon\big(d_x X_\varepsilon\big)\right|_{\varepsilon = 0} \\
&\quad \overset{(2)}{=} \mathcal{L}_{V^{(1)}} \bsL + \bsL \cdot d_x \tau \\
&\quad \overset{(3)}{=} \tau \cdot \partial_x \bsL + \xi \cdot \partial_y \bsL + \big(d_x \xi - y' \cdot d_x \tau\big) \cdot \partial_{y'} \bsL + \bsL \cdot d_x \tau.
\end{aligned}
$$

* **(1)** Regla del producto respecto de $\varepsilon$; en $\varepsilon = 0$, $\Phi^{(1)}_0$ es la identidad y $\bsL \circ \Phi^{(1)}_0 = \bsL$.
* **(2)** Definición de la derivada de Lie con el campo prolongado; $d_x X_0 = 1$ y, como en el apartado 9.3, $\partial_\varepsilon\big(d_x X_\varepsilon\big)\big|_{\varepsilon = 0} = d_x \tau$.
* **(3)** La fórmula de $\mathcal{L}_{V^{(1)}}$ y la de $\xi^{(1)}$ (apartado 9.3).

A lo largo de $f$, la última línea es la forma de cuatro términos del apartado 5, punto (2). Así, **$D$ es la derivada de Lie del elemento lagrangiano a lo largo del generador**, y la condición de simetría dice que el flujo cambia $\bsL \cdot dx$, a primer orden, en una derivada total: $\mathcal{L}_V(\bsL \cdot dx) = d_x F \cdot dx$. Con $m$ variables, $\mathcal{L}_V\big(\bsL \cdot dx_1 \cdots dx_m\big) = D \cdot dx_1 \cdots dx_m$, con el $D$ del apartado 8.3.

**El lema del apartado 6.5, leído con la derivada de Lie.** Definimos el desplazamiento en un punto fijo, $\bar{\xi} := \xi - y' \cdot \tau$, que depende de $y'$. Para toda función $G(x, y, y')$:

$$
\begin{aligned}
\mathcal{L}_{V^{(1)}} G &= \tau \cdot \partial_x G + \xi \cdot \partial_y G + \xi^{(1)} \cdot \partial_{y'} G \\
&\overset{(1)}{=} \tau \cdot \partial_x G + \big(\bar{\xi} + \tau \cdot y'\big) \cdot \partial_y G + \big(d_x \bar{\xi} + \tau \cdot y''\big) \cdot \partial_{y'} G \\
&\overset{(2)}{=} \bar{\xi} \cdot \partial_y G + d_x \bar{\xi} \cdot \partial_{y'} G + \tau \cdot \big(\partial_x G + y' \cdot \partial_y G + y'' \cdot \partial_{y'} G\big) \\
&\overset{(3)}{=} \bar{\xi} \cdot \partial_y G + d_x \bar{\xi} \cdot \partial_{y'} G + \tau \cdot d_x G.
\end{aligned}
$$

* **(1)** $\xi = \bar{\xi} + \tau \cdot y'$ y, por la regla del producto y $d_x y' = y''$, $\xi^{(1)} = d_x \xi - y' \cdot d_x \tau = d_x \bar{\xi} + \tau \cdot y'' + y' \cdot d_x \tau - y' \cdot d_x \tau = d_x \bar{\xi} + \tau \cdot y''$.
* **(2)** Agrupamos los términos con $\tau$.
* **(3)** Definición de $d_x$.

El campo prolongado se descompone en dos partes:

* **una parte evolutiva**, que cambia los valores en un punto fijo, en $\bar{\xi}$, y las pendientes, en $d_x \bar{\xi}$;
* **$\tau$ veces la derivada total**, que mueve el punto a lo largo de la gráfica.

Con $G = \bsL$ y sumando $\bsL \cdot d_x \tau$, como en el elemento lagrangiano, queda $D = \bar{\xi} \cdot \partial_y \bsL + d_x \bar{\xi} \cdot \partial_{y'} \bsL + d_x(\tau \cdot \bsL)$: el lema del apartado 6.5. La segunda parte solo añade una derivada total, $d_x(\tau \cdot \bsL)$; por eso lo que cuenta es $\bar{\xi}$. Con $m$ variables, la segunda parte es $\sum_k \tau_k \cdot d_{x_k}$, y se obtiene el lema del apartado 8.3.

### 9.5. La ley de grupo: de la condición infinitesimal a la invariancia finita

La condición de simetría solo se refiere al primer orden en $\varepsilon$. Con la ley de grupo, eso basta para todos los valores de $\varepsilon$.

**Notación.** Para una función $g$ de clase $C^2$ en un intervalo $[c, d]$, llamamos $\tilde{x}_s$ y $\tilde{g}_s$ a la variable y a la función transformadas por $\Phi_s$ (apartado 2), y

$$
\begin{aligned}
I_g(s) := \int_{\tilde{x}_s(c)}^{\tilde{x}_s(d)} \bsL(\tilde{g}_s, \tilde{g}_s')(u) \,du
\end{aligned}
$$

a la integral transformada: la del apartado 4, con $\varepsilon = s$.

**Teorema.** Sea $\Phi_\varepsilon$ una familia de clase $C^2$ con la ley de grupo (apartado 3.3), que es una simetría con la función $F(x, y)$: $D = \dfrac{dF}{dx}$ para toda función de clase $C^2$. Sean $f \in C^2([a, b])$, $[c, d] \subseteq [a, b]$ y $\varepsilon$ tal que, para todo $s$ entre $0$ y $\varepsilon$, $\tilde{x}_s$ es estrictamente creciente en $[c, d]$, de modo que existen las funciones transformadas $\tilde{f}_s$. Llamamos $I := I_f$, $P_c := \big(c, f(c)\big)$ y $P_d := \big(d, f(d)\big)$.

Entonces

$$
\begin{aligned}
I(\varepsilon) - I(0) = \int_0^\varepsilon \Big(F\big(\Phi_s(P_d)\big) - F\big(\Phi_s(P_c)\big)\Big) \,ds.
\end{aligned}
$$

En particular, si $F = 0$, $I(\varepsilon) = I(0)$: el funcional es invariante para todo $\varepsilon$, no solo a primer orden.

**Demostración.** Calculamos la derivada de $I$ en un valor $s$ cualquiera:

$$
\begin{aligned}
I'(s) &\overset{(1)}{=} \left.\dfrac{d}{d\sigma} I(s + \sigma)\right|_{\sigma = 0} \\
&\overset{(2)}{=} \left.\dfrac{d}{d\sigma} I_{\tilde{f}_s}(\sigma)\right|_{\sigma = 0} \\
&\overset{(3)}{=} \int_{\tilde{x}_s(c)}^{\tilde{x}_s(d)} D[\tilde{f}_s](u) \,du \\
&\overset{(4)}{=} \int_{\tilde{x}_s(c)}^{\tilde{x}_s(d)} \dfrac{d}{du} F\big(u, \tilde{f}_s(u)\big) \,du \\
&\overset{(5)}{=} F\Big(\tilde{x}_s(d), \tilde{f}_s\big(\tilde{x}_s(d)\big)\Big) - F\Big(\tilde{x}_s(c), \tilde{f}_s\big(\tilde{x}_s(c)\big)\Big) \\
&\overset{(6)}{=} F\big(\Phi_s(P_d)\big) - F\big(\Phi_s(P_c)\big).
\end{aligned}
$$

* **(1)** Definición de derivada.
* **(2)** Ley de grupo. La gráfica de $\tilde{f}_s$ es la imagen por $\Phi_s$ de la gráfica de $f$, y aplicarle $\Phi_\sigma$ da la imagen por $\Phi_\sigma \circ \Phi_s = \Phi_{s + \sigma}$. Por tanto, transformar $f$ con $\Phi_{s + \sigma}$ es transformar $\tilde{f}_s$, definida en $[\tilde{x}_s(c), \tilde{x}_s(d)]$, con $\Phi_\sigma$: $I_f(s + \sigma) = I_{\tilde{f}_s}(\sigma)$.
* **(3)** La derivada en $\sigma = 0$ de la integral transformada de una función es la integral de su $D$ (apartado 6.5), que para la función $\tilde{f}_s$ escribimos $D[\tilde{f}_s]$. Llevado al intervalo fijo $[\tilde{x}_s(c), \tilde{x}_s(d)]$ por el cambio de variable del apartado 5, el integrando es de clase $C^1$ en $\sigma$, y la derivada puede entrar en la integral (derivación bajo el signo integral, apartado 7.3).
* **(4)** Hipótesis de simetría, aplicada a la función $\tilde{f}_s$, que es de clase $C^2$: la hipótesis vale para toda función.
* **(5)** Regla de Barrow.
* **(6)** El extremo $\big(\tilde{x}_s(d), \tilde{f}_s(\tilde{x}_s(d))\big)$ de la gráfica transformada es la imagen por $\Phi_s$ del extremo $P_d$ de la gráfica de $f$; lo mismo con $c$.

$I'(s)$ es continua en $s$, e integrando entre $0$ y $\varepsilon$ (teorema fundamental del cálculo) se obtiene el enunciado. $\blacksquare$

**Observaciones.**

* **El recíproco es inmediato.** Si $I(\varepsilon) - I(0)$ tiene esa forma para todo $\varepsilon$, derivando en $\varepsilon = 0$ se obtiene $\int_c^d D \,dx = F(d) - F(c)$, que es la condición de simetría (apartado 5).
* **Sin la ley de grupo no basta el primer orden.** Con $\bsL = \dfrac{1}{2} \cdot y'^2$ y la familia $\Phi_\varepsilon(x, y) = (x, y + \varepsilon + \varepsilon^2 \cdot y)$, el generador es $(0, 1)$, que es una simetría con $F = 0$. Pero $\tilde{f} = f + \varepsilon + \varepsilon^2 \cdot f$, y

  $$
  \begin{aligned}
  \bsL(\tilde{f}') - \bsL(f') = \dfrac{1}{2} \cdot \Big(\big(1 + \varepsilon^2\big)^2 - 1\Big) \cdot f'^2,
  \end{aligned}
  $$

  que es de orden $\varepsilon^2$ y no se anula. La familia no es un flujo, y no es invariante más allá del primer orden.
* **Un ejemplo con $F \neq 0$: el cambio de velocidad.** Con $\bsL = \dfrac{1}{2} \cdot y'^2$, $\Phi_\varepsilon(x, y) = (x, y + \varepsilon \cdot x)$ y $F(x, y) = y$ (tercera fila de la tabla del apartado 6.4), $F\big(\Phi_s(x, y)\big) = y + s \cdot x$, y el teorema da

  $$
  \begin{aligned}
  I(\varepsilon) - I(0) &= \int_0^\varepsilon \Big(\big(f(d) + s \cdot d\big) - \big(f(c) + s \cdot c\big)\Big) \,ds \\
  &= \varepsilon \cdot \big(f(d) - f(c)\big) + \dfrac{\varepsilon^2}{2} \cdot (d - c).
  \end{aligned}
  $$

  Directamente: $\tilde{f} = f + \varepsilon \cdot x$, $\tilde{f}' = f' + \varepsilon$, y $\int_c^d \dfrac{1}{2} \cdot \big((f' + \varepsilon)^2 - f'^2\big) \,dx = \varepsilon \cdot \big(f(d) - f(c)\big) + \dfrac{\varepsilon^2}{2} \cdot (d - c)$. La fórmula es exacta, no solo de primer orden.
* **Es la razón de fondo del apartado 3.3.** Con la ley de grupo, la condición infinitesimal, que es la que se comprueba, decide lo que ocurre con las transformaciones finitas.
* **Con $n$ funciones o $m$ variables**, la demostración es la misma; con $m$ variables, el término de los extremos es el flujo de $\vec{F}$ por la frontera de la caja (apartado 8.4).

### 9.6. Simetrías cuyo generador depende de las derivadas

**Generadores generalizados.** Un generador $\bar{\xi}(x, y, y')$ que depende de la pendiente define, a primer orden, la transformación de funciones $f \mapsto f + \varepsilon \cdot \bar{\xi}\big(x, f, f'\big)$, sin mover la variable. No es una transformación de los puntos del plano: lo que se desplaza un punto depende de la pendiente de la gráfica en él, que no es una propiedad del punto. Su familia no se obtiene resolviendo un sistema de ecuaciones diferenciales ordinarias, como en el apartado 9.1, sino una ecuación en derivadas parciales para una función $u(\varepsilon, x)$:

$$
\begin{aligned}
\partial_\varepsilon u = \bar{\xi}\big(x, u, \partial_x u\big), \qquad u(0, x) = f(x).
\end{aligned}
$$

Ejemplo: con $\bar{\xi} = y'$ es $\partial_\varepsilon u = \partial_x u$, y $u(\varepsilon, x) = f(x + \varepsilon)$ es solución, porque las dos derivadas valen $f'(x + \varepsilon)$. Es la traslación de la variable de la versión anterior (apartado 6.7).

**Simetría y cantidad conservada.** Como $\bar{\xi}$ depende de $y'$, $d_x \bar{\xi}$ contiene $y''$, y la función de la condición de simetría puede depender de $y'$. Decimos que $\bar{\xi}$ es una simetría si existe $\bar{F}(x, y, y')$ de clase $C^1$ con

$$
\begin{aligned}
\bar{\xi} \cdot \partial_y \bsL + d_x \bar{\xi} \cdot \partial_{y'} \bsL = d_x \bar{F}
\end{aligned}
$$

para toda $f$. Entonces $\bar{Q} := p \cdot \bar{\xi} - \bar{F}$ es constante a lo largo de las soluciones. La demostración es la de los apartados 6.2 y 6.3, porque el lema del apartado 6.2 vale para cualquier $\eta$ de clase $C^1$, y $\bar{\xi}\big(x, f, f'\big)$ lo es si $f$ es de clase $C^2$.

**La relación con las transformaciones de los puntos.** Por el apartado 9.4, para un generador $(\tau, \xi)$ de los puntos, $D = \bar{\xi} \cdot \partial_y \bsL + d_x \bar{\xi} \cdot \partial_{y'} \bsL + d_x(\tau \cdot \bsL)$, con $\bar{\xi} = \xi - y' \cdot \tau$. Por tanto,

$$
\begin{aligned}
D = d_x F \quad \Longleftrightarrow \quad \bar{\xi} \cdot \partial_y \bsL + d_x \bar{\xi} \cdot \partial_{y'} \bsL = d_x F - d_x(\tau \cdot \bsL) = d_x\big(F - \tau \cdot \bsL\big):
\end{aligned}
$$

$(\tau, \xi)$ es una simetría con $F$ si y solo si $\bar{\xi}$ es una simetría generalizada con $\bar{F} := F - \tau \cdot \bsL$. Las cantidades conservadas coinciden:

$$
\begin{aligned}
\bar{Q} &\overset{(1)}{=} p \cdot \bar{\xi} - \bar{F} \\
&\overset{(2)}{=} p \cdot \big(\xi - \tau \cdot f'\big) - \big(F - \tau \cdot \bsL\big) \\
&\overset{(3)}{=} p \cdot \xi - \tau \cdot \big(p \cdot f' - \bsL\big) - F \\
&\overset{(4)}{=} p \cdot \xi - \tau \cdot \bsH - F = Q.
\end{aligned}
$$

* **(1)** Definición de $\bar{Q}$.
* **(2)** Sustituimos $\bar{\xi}$ y $\bar{F}$, a lo largo de $f$.
* **(3)** Agrupamos los términos con $\tau$.
* **(4)** Definición de $\bsH$ (apartado 6.5).

Es el procedimiento de la versión anterior («Reducción al caso anterior»), y explica la relación entre las dos formas de la identidad de Beltrami del apartado 6.7.

**No todo generador generalizado procede de los puntos.** $\bar{\xi}$ procede de una transformación de los puntos si y solo si es de la forma $\xi(x, y) - \tau(x, y) \cdot y'$; con $n$ funciones, $\bar{\xi}_i = \xi_i - \tau \cdot y'_i$, con el mismo $\tau$ para todas las componentes. El ejemplo clásico de lo contrario es el problema de Kepler: una partícula de masa $m$ atraída hacia el origen por una fuerza inversamente proporcional al cuadrado de la distancia, con

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 + \dfrac{k}{|\vec{q}|}, \qquad k > 0,
\end{aligned}
$$

donde el punto es la derivada respecto del tiempo y $k$ es aquí la constante de la fuerza. Además de la energía y del momento angular, $\vec{\ell} = \vec{q} \times \vec{p}$ con $\vec{p} = m \cdot \dot{\vec{q}}$, se conserva el **vector de Laplace–Runge–Lenz**,

$$
\begin{aligned}
\vec{A} := \vec{p} \times \vec{\ell} - m \cdot k \cdot \dfrac{\vec{q}}{|\vec{q}|},
\end{aligned}
$$

que apunta hacia el perihelio de la órbita, su punto más cercano al origen. Su componente $j$ procede del generador generalizado

$$
\begin{aligned}
\bar{\xi}_i = m \cdot \big(2 \cdot \dot{q}_i \cdot q_j - q_i \cdot \dot{q}_j - \delta_{ij} \cdot \vec{q} \cdot \dot{\vec{q}}\big), \qquad i = 1, 2, 3,
\end{aligned}
$$

con $\bar{F} = \vec{p} \cdot \bar{\vec{\xi}} - A_j$. Depende de las velocidades, pero no es de la forma $\xi_i - \tau \cdot \dot{q}_i$: los términos $-q_i \cdot \dot{q}_j$ y $-\delta_{ij} \cdot \vec{q} \cdot \dot{\vec{q}}$ no lo son. Ninguna transformación de los puntos da esta cantidad conservada.

Las cuentas de este apartado (los flujos, la prolongación del giro, la derivada de Lie del elemento lagrangiano y su descomposición, la invariancia finita, el contraejemplo sin ley de grupo, la fórmula exacta del cambio de velocidad y el vector de Laplace–Runge–Lenz) están comprobadas con SymPy en Teorema-de-Noether-v2-comprobaciones.py.

## 10. Guía: dimensión infinita

Este apartado es una guía: recoge resultados establecidos, sin derivaciones, con las referencias del apartado 10.6. Trata dos generalizaciones: funciones con valores en un espacio de dimensión infinita (apartados 10.1 a 10.4) y variables independientes en espacios más generales (apartado 10.5). La conclusión es asimétrica. Las variables dependientes admiten dimensión infinita casi sin cambios, porque la teoría es puntual en $x$: solo usa derivadas y emparejamientos. Las independientes, no, porque hay que integrar sobre ellas.

### 10.1. Valores en un espacio de Banach o de Hilbert

**El planteamiento.** Sean $E$ un espacio de Banach (apartado 9.2), $f: [a, b] \to E$ de clase $C^2$ y $\bsL: E \times E \times [a, b] \to \mathbb{R}$ de clase $C^2$, con las derivadas de Fréchet del apartado 9.2.

* **Derivadas parciales.** $D_y \bsL(y, y', x) \in E^*$ es la derivada de Fréchet de $\bsL$ respecto de su primer argumento, con los otros dos fijos, y $D_{y'} \bsL(y, y', x) \in E^*$, la derivada respecto del segundo. En $E = \mathbb{R}^n$ son los vectores fila de las $\partial_{y_i} \bsL$ y de las $\partial_{y'_i} \bsL$.
* **Momento, expresión de Euler–Lagrange y $\bsH$**, a lo largo de $f$:

  $$
  \begin{aligned}
  p &:= D_{y'} \bsL(f, f', x) \in E^*, \qquad \varphi := D_y \bsL(f, f', x) - p' \in E^*, \\
  \bsH &:= \langle p, f' \rangle - \bsL.
  \end{aligned}
  $$

* **Estacionariedad.** $f$ hace estacionario a $\bsS$ con los extremos fijos si y solo si $\varphi = 0$ en todo $[a, b]$. El lema fundamental del cálculo de variaciones sigue valiendo: si $\varphi$ es continua y $\int_a^b \langle \varphi, h \rangle \,dx = 0$ para toda $h$ de clase $C^2$ con $h(a) = h(b) = 0$, se toma $h(x) = \lambda(x) \cdot e$, con $e \in E$ fijo y $\lambda$ una función real, y se aplica el lema de una variable a $x \mapsto \langle \varphi(x), e \rangle$. Como $e$ es cualquiera, $\varphi(x) = 0$.
* **Las transformaciones** actúan sobre los puntos de $\mathbb{R} \times E$, con generador $(\tau, \xi)$, $\tau(x, y) \in \mathbb{R}$ y $\xi(x, y) \in E$. La condición de simetría es la del apartado 4, con $F(x, y)$ real.
* **El resultado.** Para toda $f$ de clase $C^2$,

  $$
  \begin{aligned}
  \dfrac{d}{dx}\big(\langle p, \xi \rangle - \tau \cdot \bsH - F\big) = -\big\langle \varphi,\ \xi - \tau \cdot f' \big\rangle,
  \end{aligned}
  $$

  y sobre las soluciones $Q := \langle p, \xi \rangle - \tau \cdot \bsH - F$ es constante. La demostración es la de los apartados 6.5 y 7.4: solo usa las cinco reglas del apartado 9.2, con el emparejamiento $\langle \cdot, \cdot \rangle$ en el papel de la suma $\sum_i p_i \cdot \xi_i$, y la cota de los restos, con la precaución del apartado 10.2, punto 1. Las condiciones de integrabilidad del apartado 7.3 y el lema de Poincaré también valen en espacios de Banach (Lang, 1999).

**Espacios de Hilbert.**

* Un **producto escalar** en un espacio vectorial real $E$ es una aplicación $(u, v) \mapsto \langle u, v \rangle \in \mathbb{R}$, bilineal, simétrica y con $\langle u, u \rangle > 0$ si $u \neq 0$. Define la norma $\lVert u \rVert := \sqrt{\langle u, u \rangle}$. Un **espacio de Hilbert** es un espacio con producto escalar que, con esa norma, es de Banach.
* **Ejemplos.** $\mathbb{R}^n$, con el producto escalar habitual. El espacio $\ell^2$ de las sucesiones reales $(a_1, a_2, \dots)$ con $\sum_k a_k^2$ finita, con $\langle a, b \rangle := \sum_k a_k \cdot b_k$, que tiene dimensión infinita.
* **Teorema de representación de Riesz.** En un espacio de Hilbert, para cada $\alpha \in E^*$ existe un único $u_\alpha \in E$ con $\alpha(v) = \langle u_\alpha, v \rangle$ para todo $v$, y $\lVert \alpha \rVert = \lVert u_\alpha \rVert$ (Brezis, 2011). Así, el momento $p$ se identifica con un vector de $E$, y el emparejamiento $\langle p, \xi \rangle$, con el producto escalar; por eso se usa la misma notación para los dos.
* **Espacios de Hilbert complejos.** En mecánica cuántica los vectores son complejos. Un producto escalar complejo $\langle u, v \rangle \in \mathbb{C}$ es lineal en $v$, cumple $\langle v, u \rangle = \overline{\langle u, v \rangle}$, donde la barra indica el conjugado, y $\langle u, u \rangle > 0$ si $u \neq 0$; es, por tanto, antilineal en $u$: $\langle \lambda \cdot u, v \rangle = \bar{\lambda} \cdot \langle u, v \rangle$. Como $\bsL$ tiene que ser real, el espacio complejo $\mathcal{H}$ se ve como un espacio real, en el que los vectores solo se multiplican por números reales, con el producto escalar real $\operatorname{Re}\langle u, v \rangle$, que lo hace un espacio de Hilbert real. Por ejemplo, $\mathbb{C}^N$, con $\langle u, v \rangle = \sum_j \bar{u}_j \cdot v_j$, es $\mathbb{R}^{2 \cdot N}$ con el producto escalar habitual, separando las partes real e imaginaria de las componentes.

### 10.2. Lo que necesita cuidado

1. **Compacidad.** Un conjunto de un espacio normado es **compacto** si toda sucesión de sus puntos tiene una subsucesión que converge a un punto del conjunto. En $\mathbb{R}^N$, los compactos son los cerrados y acotados; en dimensión infinita, no: la bola unidad cerrada de un espacio normado es compacta si y solo si la dimensión es finita (lema de Riesz; Brezis, 2011). En $\ell^2$, los vectores $e_k$, con un $1$ en el lugar $k$ y $0$ en los demás, están en la bola unidad y cumplen $\lVert e_k - e_l \rVert = \sqrt{2}$ si $k \neq l$, así que ninguna subsucesión converge. La cota uniforme del apartado 5, punto (2), se mantiene por otra razón: la imagen de un compacto por una función continua es compacta en cualquier espacio normado, y el conjunto donde se evalúan las derivadas de $\bsL$ es la imagen continua de un compacto de $\mathbb{R}^N$, como $[c, d] \times [-\varepsilon_0, \varepsilon_0]$.
2. **La matriz $W$.** Su análogo es la derivada segunda $D^2_{y'} \bsL$, una aplicación bilineal continua de $E \times E$ en $\mathbb{R}$, que define una aplicación lineal continua de $E$ en $E^*$. Para que la transformada de Legendre, $y' \mapsto p$, sea invertible y lleve al formalismo hamiltoniano, no basta con que esa aplicación sea inyectiva (se dice **débilmente no degenerada**): hace falta que sea biyectiva con inversa continua (**fuertemente no degenerada**). En dimensión finita las dos condiciones coinciden; en dimensión infinita, no (Abraham et al., 1988; Marsden y Ratiu, 1999). La identidad de Noether no usa $W$ (apartado 7.4), así que no le afecta.
3. **Generadores no acotados.** Es la dificultad de fondo de la mecánica cuántica.
   * Un **operador lineal** $\hat{A}$ en un espacio de Hilbert $\mathcal{H}$ es una aplicación lineal definida en un subespacio $D(\hat{A})$, su **dominio**, con valores en $\mathcal{H}$. Es **acotado** si existe $C$ con $\lVert \hat{A}u \rVert \leq C \cdot \lVert u \rVert$ para todo $u \in D(\hat{A})$, es decir, si es continuo (apartado 9.2); si no, es **no acotado**, como la derivada (apartado 9.2). El dominio es **denso** si todo vector de $\mathcal{H}$ es límite de vectores del dominio.
   * El **adjunto** $\hat{A}^*$ de un operador con dominio denso está definido en los $v$ para los que existe un $w$ con $\langle v, \hat{A}u \rangle = \langle w, u \rangle$ para todo $u \in D(\hat{A})$, y vale $\hat{A}^* v := w$. $\hat{A}$ es **autoadjunto** si $\hat{A}^* = \hat{A}$, con el mismo dominio. En $\mathbb{C}^N$, el adjunto es la matriz traspuesta conjugada, y autoadjunto quiere decir **hermítico**: igual a su traspuesta conjugada.
   * Un operador $\hat{U}$ definido en todo $\mathcal{H}$ es **unitario** si es biyectivo y conserva el producto escalar: $\langle \hat{U}u, \hat{U}v \rangle = \langle u, v \rangle$.
   * Un **grupo unitario uniparamétrico fuertemente continuo** es una familia de operadores unitarios $\hat{U}(\varepsilon)$ con la ley de grupo, $\hat{U}(\varepsilon + \eta) = \hat{U}(\varepsilon)\hat{U}(\eta)$, con $\hat{U}(0)$ igual a la identidad y con $\varepsilon \mapsto \hat{U}(\varepsilon)\,u$ continua para cada $u$.
   * **Teorema de Stone.** Esos grupos se corresponden uno a uno con los operadores autoadjuntos. Cada uno es $\hat{U}(\varepsilon) = e^{-i \cdot \varepsilon \cdot \hat{A}}$ para un único $\hat{A}$ autoadjunto, su generador; la exponencial se define con el teorema espectral y, para matrices, es la de «El teorema de Noether: anexos». Además, $\hat{A}u = i \cdot \left.\dfrac{d}{d\varepsilon} \hat{U}(\varepsilon)\,u\right|_{\varepsilon = 0}$ para los $u$ en los que existe esa derivada, que son exactamente los de $D(\hat{A})$ (Reed y Simon, 1980, cap. VIII).
   * **Consecuencia para el teorema de Noether.** El generador de la transformación, $\xi(\psi) = -i \cdot \hat{A}\psi$, solo está definido en $D(\hat{A})$, y la familia no es de clase $C^2$ en todo $\mathcal{H}$, como pide el apartado 3.1. Los tratamientos rigurosos trabajan en el dominio, con la norma $\lVert u \rVert + \lVert \hat{A}u \rVert$, que lo hace un espacio de Banach cuando $\hat{A}$ es autoadjunto (Chernoff y Marsden, 1974).

### 10.3. Ejemplo: la ecuación de Schrödinger

**Avisos de notación.** En este apartado, $i$ es la unidad imaginaria; $\mathcal{H}$, caligráfica, es el espacio de Hilbert; $\hat{H}$, con gorro, un operador (el hamiltoniano cuántico); y $\bsH$, en negrita, la función del apartado 6.5. $\hbar$ es la constante de Planck reducida, $\dfrac{h_{\mathrm{P}}}{2 \cdot \pi} \approx 1{,}055 \cdot 10^{-34}\ \mathrm{J \cdot s}$, con $h_{\mathrm{P}}$ la constante de Planck. La variable $x$ es el tiempo, $t$, y el punto indica $\dfrac{d}{dt}$.

**El planteamiento.** $\mathcal{H}$ es un espacio de Hilbert complejo visto como real (apartado 10.1), y $\hat{H}$ un operador autoadjunto. Para que todo sea riguroso con lo ya visto, se puede tomar $\mathcal{H} = \mathbb{C}^N$ y $\hat{H}$ una matriz hermítica: entonces es el apartado 7 con $2 \cdot N$ funciones reales, las partes real e imaginaria de las componentes de $\psi(t)$. El lagrangiano es

$$
\begin{aligned}
\bsL(\psi, \dot{\psi}) = \operatorname{Re}\big\langle \psi, i \cdot \hbar \cdot \dot{\psi} \big\rangle - \big\langle \psi, \hat{H}\psi \big\rangle,
\end{aligned}
$$

real porque $\hat{H}$ es autoadjunto.

* **La ecuación de Euler–Lagrange** es la **ecuación de Schrödinger**, $i \cdot \hbar \cdot \dot{\psi} = \hat{H}\psi$. En componentes reales, las expresiones de Euler–Lagrange de las partes real e imaginaria de $\psi_j$ son el doble de la parte real y de la parte imaginaria de $i \cdot \hbar \cdot \dot{\psi}_j - (\hat{H}\psi)_j$.
* **El momento** es $p(\eta) = \operatorname{Re}\langle \psi, i \cdot \hbar \cdot \eta \rangle$, para cada $\eta \in \mathcal{H}$.
* **Tres simetrías**, todas con $F = 0$. $[\hat{A}, \hat{H}] := \hat{A}\hat{H} - \hat{H}\hat{A}$ es el **conmutador**:

| Simetría | Generador | $Q$ |
| ---------------------------------------- | ------------------------ | ------------------------------------ |
| Fase, $\psi \mapsto e^{i \cdot \varepsilon} \cdot \psi$ | $\xi = i \cdot \psi$ | $-\hbar \cdot \lVert \psi \rVert^2$ |
| $\psi \mapsto e^{-i \cdot \varepsilon \cdot \hat{A}}\psi$, con $\hat{A}$ autoadjunto y $[\hat{A}, \hat{H}] = 0$ | $\xi = -i \cdot \hat{A}\psi$ | $\hbar \cdot \langle \psi, \hat{A}\psi \rangle$ |
| Traslación en el tiempo | $\tau = 1$, $\xi = 0$ | $-\bsH = -\langle \psi, \hat{H}\psi \rangle$ |

Table: Simetrías del lagrangiano de Schrödinger.

**Observaciones.**

* **$\bsL$ es lineal en $\dot{\psi}$**, así que $W = 0$ y la transformada de Legendre es degenerada. La identidad de Noether vale igual, porque no usa $W$ (apartado 7.4, «Qué no hemos usado»).
* **Interpretación.** Si $\lVert \psi \rVert = 1$, $\langle \psi, \hat{A}\psi \rangle$ es el **valor esperado** del observable representado por $\hat{A}$. La regla de la mecánica cuántica «si $\hat{A}$ conmuta con $\hat{H}$, su valor esperado se conserva» es el teorema de Noether para este lagrangiano. La conservación de la norma, que es la de la probabilidad total, procede de la simetría de fase, y la de $\langle \psi, \hat{H}\psi \rangle$, el valor esperado de la energía, de la traslación en el tiempo.
* **En dimensión infinita**, $\hat{H}$ suele ser no acotado; para una partícula contiene una derivada segunda. El resultado vale para $\psi(t)$ en $D(\hat{H})$, con las precauciones del apartado 10.2, punto 3 (Chernoff y Marsden, 1974). La ecuación de Schrödinger como sistema hamiltoniano en un espacio de Hilbert se estudia en Kibble (1979).
* **Comprobación.** Con $N = 2$, una matriz hermítica cualquiera y $\hat{A} = \hat{H}^2$, que conmuta con $\hat{H}$, las tres filas de la tabla, la ecuación de Schrödinger y $W = 0$ están comprobadas con SymPy en Teorema-de-Noether-v2-comprobaciones.py.

### 10.4. Los campos como curvas en un espacio de funciones

* **La cuerda del apartado 8.8, otra vez.** Para cada $t$, $q(t) := f(t, \cdot)$ es una función de $x$ en $[a_1, b_1]$. Con el producto escalar $\langle g_1, g_2 \rangle := \int_{a_1}^{b_1} g_1 \cdot g_2 \,dx$ entre funciones continuas, el lagrangiano del apartado 8.8, integrado en $x$, es

  $$
  \begin{aligned}
  \bsL(q, \dot{q}) = \dfrac{1}{2} \cdot \lVert \dot{q} \rVert^2 - \dfrac{c^2}{2} \cdot \lVert \partial_x q \rVert^2.
  \end{aligned}
  $$

  El apartado 8 con una variable espacial es el apartado 7 con valores en un espacio de funciones, y la energía de la cuerda, que en el apartado 8.8 procede de la traslación en $t$, es aquí la $\bsH$ de la traslación en el tiempo.
* **Tres obstáculos:**
  * las funciones continuas con esa norma no forman un espacio completo; su completado es el espacio $L^2(a_1, b_1)$ de las funciones de cuadrado integrable, que necesita la integral de Lebesgue (Brezis, 2011);
  * $\lVert \partial_x q \rVert$ solo está definida para las $q$ derivables, que forman un subespacio denso: $\bsL$ no está definida en todo el espacio;
  * la traslación en $x$, $q \mapsto q(\cdot - \varepsilon)$, con condiciones periódicas para que lleve el intervalo en sí mismo, tiene el generador $\xi(q) = -\partial_x q$, que no es acotado (apartado 9.2).
* **Por eso**, en la práctica, los campos se tratan con el apartado 8, y la visión como curva en un espacio de funciones se usa sobre todo para su estructura hamiltoniana (Marsden y Ratiu, 1999; Chernoff y Marsden, 1974).

### 10.5. Variables independientes más generales

#### Variedades: el marco geométrico

* Una **variedad diferenciable** de dimensión $m$ es un conjunto en el que cada punto tiene un entorno que se describe con $m$ coordenadas reales, una **carta**, de modo que, donde dos cartas se solapan, el cambio de coordenadas es un difeomorfismo (apartado 6.5). Ejemplo: la esfera, con las coordenadas esféricas fuera de los polos y otras cartas cerca de ellos.
* En el marco general (Olver, 1993; Saunders, 1989), las variables recorren una variedad $M$ y los valores, otra variedad $N$; por ejemplo, un campo de vectores unitarios toma valores en la esfera. Los puntos $(x, y)$ son los de $M \times N$ o, más en general, los de un **fibrado**, un espacio que alrededor de cada punto es un producto de ese tipo.
* El espacio de los puntos $(x, y, y')$ del apartado 9.3, o $(\vec{x}, \vec{y}, Z)$ del apartado 8.2, se llama **espacio de jets de primer orden**; la prolongación actúa sobre él.
* **Formas de grado $m$.** En coordenadas se escriben $g(\vec{x}) \cdot dx_1 \wedge \dots \wedge dx_m$. El símbolo $\wedge$, el **producto exterior**, es antisimétrico, $dx_k \wedge dx_l = -dx_l \wedge dx_k$, y por eso, al cambiar de coordenadas, una forma de grado $m$ se multiplica por el determinante jacobiano, el factor del apartado 8.2. El elemento lagrangiano $\bsL \cdot dx_1 \wedge \dots \wedge dx_m$ es una forma de grado $m$.
* **Formas de grado $m - 1$ y derivada exterior.** La corriente $\vec{Q}$ del apartado 8.6 se escribe como la forma $\sum_k (-1)^{k-1} \cdot Q_k \cdot dx_1 \wedge \dots \wedge dx_{k-1} \wedge dx_{k+1} \wedge \dots \wedge dx_m$. Su **derivada exterior** es $\big(\sum_k d_{x_k} Q_k\big) \cdot dx_1 \wedge \dots \wedge dx_m$: la divergencia.
* **Teorema de Stokes.** La integral de la derivada exterior de una forma de grado $m - 1$ sobre una región es la integral de la forma sobre su frontera. Sustituye al teorema de la divergencia en una caja del apartado 8.4.
* **El teorema de Noether en este lenguaje.** $D \cdot dx_1 \wedge \dots \wedge dx_m$ es la derivada de Lie de la forma lagrangiana a lo largo del generador prolongado (apartado 9.4); la condición de simetría pide que sea la derivada exterior de una forma de grado $m - 1$; y la corriente es una forma de grado $m - 1$ con derivada exterior nula sobre las soluciones.

#### Infinitas variables independientes

* Una **medida** asigna a ciertos conjuntos, al menos a los abiertos y a los que se obtienen de ellos con uniones numerables y complementos (los **conjuntos de Borel**), un número en $[0, \infty]$, de modo que la medida de una unión numerable de conjuntos disjuntos es la suma de sus medidas. En $\mathbb{R}^m$, la de Lebesgue es el volumen, y es **invariante por traslaciones**: la de $A + \vec{v}$ es la de $A$.
* **Teorema.** En un espacio de Banach separable (con un subconjunto numerable denso) de dimensión infinita, toda medida de Borel invariante por traslaciones que dé medida finita a alguna bola es nula (Bogachev, 1998). La idea: por el **lema de Riesz** (para cada subespacio cerrado distinto de todo el espacio y cada $\theta \in (0, 1)$ hay un vector de norma $1$ a distancia al menos $\theta$ del subespacio), hay vectores $e_k$ de norma $1$ con $\lVert e_k - e_l \rVert \geq \dfrac{1}{2}$. Las bolas abiertas de radio $\dfrac{r}{8}$ centradas en los $\dfrac{r}{2} \cdot e_k$ son disjuntas, están dentro de la bola de radio $r$ y tienen todas la misma medida, que tiene que ser nula; por la separabilidad, el espacio es una unión numerable de bolas de ese radio.
* **Consecuencia.** No hay un $dx_1 \cdots dx_m$ con infinitas variables, y con él desaparecen el determinante jacobiano y el teorema de Fubini del apartado 8.
* **Lo que existe.** Las **medidas gaussianas**, como la **medida de Wiener** sobre los caminos continuos, que describe el movimiento browniano, no son invariantes por traslaciones, pero sí **cuasiinvariantes** en las direcciones de un subespacio, el **espacio de Cameron–Martin**: trasladarlas en esas direcciones las multiplica por una densidad, que hace el papel del determinante jacobiano; en las demás direcciones, la medida trasladada no tiene densidad respecto de la original. La integración por partes en estos espacios es el **cálculo de Malliavin**, con una divergencia propia (Bogachev, 1998; Nualart, 2006). Son análogos parciales; no hay una teoría de Noether estándar con infinitas variables independientes.
* **La integral de camino.** En la teoría cuántica de campos se integra, de forma no rigurosa en general, sobre todas las funciones $f$, es decir, sobre las variables dependientes, con un peso que depende de $\bsS[f]$. Como la identidad de Noether vale para toda $f$, y no solo para las soluciones, integrada así da las **identidades de Ward–Takahashi**: la corriente se conserva dentro de las **funciones de correlación**, los promedios de productos de valores de $f$ con ese peso, salvo unos términos de contacto que proceden de $-\sum_i \varphi_i \cdot \bar{\xi}_i$ (Peskin y Schroeder, 1995, cap. 9).

### 10.6. Referencias

* Abraham, R., Marsden, J. E. y Ratiu, T. (1988). *Manifolds, tensor analysis, and applications* (2.ª ed.). Springer.
* Bogachev, V. I. (1998). *Gaussian measures*. American Mathematical Society.
* Brezis, H. (2011). *Functional analysis, Sobolev spaces and partial differential equations*. Springer.
* Chernoff, P. R. y Marsden, J. E. (1974). *Properties of infinite dimensional Hamiltonian systems*. Springer.
* Kibble, T. W. B. (1979). Geometrization of quantum mechanics. *Communications in Mathematical Physics*, *65*(2), 189–201.
* Lang, S. (1999). *Fundamentals of differential geometry*. Springer.
* Marsden, J. E. y Ratiu, T. S. (1999). *Introduction to mechanics and symmetry* (2.ª ed.). Springer.
* Noether, E. (1918). Invariante Variationsprobleme. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 235–257.
* Nualart, D. (2006). *The Malliavin calculus and related topics* (2.ª ed.). Springer.
* Olver, P. J. (1993). *Applications of Lie groups to differential equations* (2.ª ed.). Springer.
* Peskin, M. E. y Schroeder, D. V. (1995). *An introduction to quantum field theory*. Addison-Wesley.
* Reed, M. y Simon, B. (1980). *Methods of modern mathematical physics: Vol. 1. Functional analysis* (ed. rev.). Academic Press.
* Saunders, D. J. (1989). *The geometry of jet bundles*. Cambridge University Press.

## Resumen

| Situación | Generador | $F$ | Cantidad conservada | Apartado |
| ------------------------------ | ---------------------- | ------------------ | -------------------------------- | ------------------ |
| La variable no se mueve | $(0, \xi)$ | $F(x, y)$ | $p \cdot \xi - F$ | 6.3 |
| La variable también se mueve | $(\tau, \xi)$ | $F(x, y)$ | $p \cdot \xi - \tau \cdot \bsH - F$ | 6.5 |
| $\bsL$ no depende de $y$ | $(0, 1)$ | $0$ | $p$ | 6.7 |
| $\bsL$ no depende de $x$ | $(1, 0)$ | $0$ | $-\bsH$ | 6.7 |
| Varias funciones | $(\tau, \vec{\xi})$ | $F(x, \vec{y})$ | $\vec{p} \cdot \vec{\xi} - \tau \cdot \bsH - F$ | 7.4 |
| Una función arbitraria $\tau(x)$ | $(\tau, \vec{0})$ | $0$ | ninguna: una relación entre las ecuaciones | 7.5 |
| Varias variables | $(\vec{\tau}, \vec{\xi})$ | $\vec{F}$ | la corriente $\vec{Q}$, de divergencia nula | 8.6 |
| Generador que depende de las derivadas | $\bar{\xi}$ | $\bar{F}$ | $p \cdot \bar{\xi} - \bar{F}$ | 9.6 |
| Valores en un espacio de Banach | $(\tau, \xi)$, con $\xi \in E$ | $F(x, y)$ | $\langle p, \xi \rangle - \tau \cdot \bsH - F$ | 10.1 |

Table: Casos del teorema de Noether.

En todos los casos la identidad de Noether vale para toda función, y el teorema se obtiene al anularse las expresiones de Euler–Lagrange. Con la ley de grupo, la condición infinitesimal da la invariancia para todo $\varepsilon$ (apartado 9.5).

## Mapa de la notación

Cómo cambia cada objeto en las generalizaciones de los apartados 7, 8 y 10. $E$ es un espacio de Banach y $E^*$, su dual (apartado 9.2).

| Objeto | Una función (2 a 6) | $n$ funciones (7) | $m$ variables (8) | Valores en $E$ (10) |
| ------------------------------------ | -------------------- | -------------------------- | -------------------------------- | ---------------------- |
| Variable | $x \in [a, b]$ | $x \in [a, b]$ | $\vec{x} \in \Omega = \prod_k [a_k, b_k]$ | $x \in [a, b]$ |
| Función | $f$ | $\vec{f} = (f_1, \dots, f_n)$ | $\vec{f}(\vec{x})$ | $f$, con valores en $E$ |
| Puntos que se transforman | $\mathbb{R} \times \mathbb{R}$ | $\mathbb{R} \times \mathbb{R}^n$ | $\mathbb{R}^m \times \mathbb{R}^n$ | $\mathbb{R} \times E$ |
| Generador | $(\tau, \xi)$ | $(\tau, \vec{\xi})$ | $(\vec{\tau}, \vec{\xi})$ | $(\tau, \xi)$, $\xi \in E$ |
| Derivada a lo largo de $f$ | $'$, o $d_x$ (9.3) | $'$ | $d_{x_k}$ | $'$ |
| Derivadas de $f$ | $f'$ | $\vec{f}'$ | $J_{\vec{f}} = (\partial_k f_i)$ | $f'$ |
| Factor de $d\tilde{x}$ | $\tilde{x}'$ | $\tilde{x}'$ | $\det J_{\tilde{\vec{x}}}$ | $\tilde{x}'$ |
| Subdominio | $[c, d]$ | $[c, d]$ | caja $B = \prod_k [c_k, d_k]$ | $[c, d]$ |
| Momento | $p$ | $p_i$ | $u_{ik}$ | $p$, en $E^*$ |
| Expresión de Euler–Lagrange | $\varphi$ | $\varphi_i$ | $\varphi_i$ | $\varphi$, en $E^*$ |
| Hamiltoniano | $\bsH$ | $\bsH$ | $T_{kl}$ | $\bsH$ |
| Término de borde | $F(x, y)$ | $F(x, \vec{y})$ | $\vec{F}$, con $F_k(\vec{x}, \vec{y})$ | $F(x, y)$ |
| Cantidad conservada | $Q$ | $Q$ | corriente $\vec{Q}$ | $Q$ |

Table: Cómo cambia la notación en cada generalización.

**Otros documentos.** En la versión anterior de «El teorema de Noether: parte matemática», la familia se escribe $\bsT_\epsilon$, con el parámetro $\epsilon$, y el generador puede depender de las derivadas (apartado 9.6); en el Tema 1, apartado 4.4, el parámetro se llama $s$ y el campo, $(\xi^t, \xi^x)$. Aquí usamos $\Phi_\varepsilon$, $\varepsilon$ y $(\tau, \xi)$, como en el trabajo «La importancia de las simetrías en física».
