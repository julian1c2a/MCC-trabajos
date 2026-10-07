---
author: "Julián Calderón Almendros"
---

# El teorema de Noether: parte matemática

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-07
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

Esta serie continúa «El formalismo lagrangiano». Allí se buscaban las funciones que hacen estacionario un funcional; aquí se estudian las transformaciones que no cambian el funcional y lo que se deduce de ellas: cantidades que no cambian a lo largo de las soluciones. Como aquella serie, estos documentos son un superconjunto de lo que entra en el trabajo «La importancia de las simetrías en física».

La serie consta de cinco documentos y de la versión para el trabajo:

* «El teorema de Noether: parte matemática» (este documento): transformaciones, simetrías de un funcional y el teorema, en una variable y en varias.
* «El teorema de Noether: ejemplos matemáticos»: el camino más corto, las ecuaciones con la estructura de las de Newton y la ecuación de Laplace.
* «El teorema de Noether: parte física»: las simetrías de los sistemas de partículas de «El formalismo lagrangiano: parte física», etapa por etapa, y el grupo de Galileo.
* «El teorema de Noether: ejemplos físicos»: la partícula libre, el campo uniforme, el campo central, dos partículas, una carga en un campo magnético y la cuerda vibrante.
* «El teorema de Noether: anexos»: rotaciones, grupo de Galileo y exponencial de una matriz.
* «El teorema de Noether (versión para el trabajo)»: lo que entra en los apartados 4.2 y 4.3 del trabajo, con su procedencia.

## Planteamiento y notación

Usamos la notación de «El formalismo lagrangiano: parte matemática» en el caso de una variable y $n$ funciones, que es el que necesita la mecánica de partículas. El caso de varias variables se trata al final.

* $\vec{f} = (f_1, \dots, f_n): [a, b] \to \mathbb{R}^n$ es una función de clase $C^2$, y $f'_i$ es la derivada de su componente $f_i$. Los índices $i, j = 1, \dots, n$ recorren las componentes.
* $\bsL(\vec{f}, \vec{f}', x)$ es una función de $2 \cdot n + 1$ variables reales con derivadas parciales segundas continuas. A lo largo de una función $\vec{f}$ escribimos $\bsL(\vec{f}, \vec{f}')(x) := \bsL\big(\vec{f}(x), \vec{f}'(x), x\big)$, y lo mismo para sus derivadas parciales.
* Para cada subintervalo $[c, d] \subseteq [a, b]$, el funcional es
  $$
  \begin{aligned}
  \bsS_{[c,d]}[\vec{f}] := \int_c^d \bsL(\vec{f}, \vec{f}')(x) \,dx,
  \end{aligned}
  $$
  y $\bsS := \bsS_{[a,b]}$.
* A lo largo de $\vec{f}$ definimos, para cada $i$,
  $$
  \begin{aligned}
  p_i(x) := \partial_{f'_i} \bsL(\vec{f}, \vec{f}')(x), \qquad \varphi_i(x) := \partial_{f_i} \bsL(\vec{f}, \vec{f}')(x) - \dfrac{d}{dx} p_i(x).
  \end{aligned}
  $$
  $\varphi_i$ es la expresión de Euler–Lagrange de la componente $i$, la misma que en «El formalismo lagrangiano». Como $\bsL$ es de clase $C^2$ y $\vec{f}$ de clase $C^2$, $p_i$ es de clase $C^1$ y $\varphi_i$ es continua.
* Las **soluciones** son las funciones $\vec{f}_0$ que cumplen las ecuaciones de Euler–Lagrange, $\varphi_i = 0$ para $i = 1, \dots, n$, en todo $[a, b]$, sean cuales sean sus valores en los extremos.
* Definimos también, a lo largo de $\vec{f}$,
  $$
  \begin{aligned}
  \bsH(x) := \sum_{i=1}^{n} p_i(x) \cdot f'_i(x) - \bsL(\vec{f}, \vec{f}')(x).
  \end{aligned}
  $$
  En la parte física, $\bsH$ será el hamiltoniano.

Una diferencia con «El formalismo lagrangiano» es importante: allí todas las funciones del conjunto de partida tenían los mismos valores en los extremos, porque se buscaban las estacionarias con los extremos fijos. Aquí no se impone ninguna condición de contorno. La definición de simetría se refiere a todas las funciones de clase $C^2$, y el teorema, a todas las soluciones.

## Transformaciones de las funciones

### Tres ejemplos

Una transformación asigna a cada función $\vec{f}$ otra función. Tres ejemplos, cada uno dependiente de un parámetro real $\epsilon$:

1. **Desplazar una componente:** $f_k \to f_k + \epsilon$, sin cambiar las demás.
2. **Desplazar la variable:** $\vec{f}(x) \to \vec{f}(x + \epsilon)$. La gráfica de cada componente se desplaza una distancia $\epsilon$ hacia la izquierda.
3. **Girar dos componentes:** $(f_1, f_2) \to (f_1 \cdot \cos\epsilon - f_2 \cdot \sin\epsilon,\ f_1 \cdot \sin\epsilon + f_2 \cdot \cos\epsilon)$, sin cambiar las demás.

En los tres casos, $\epsilon = 0$ da la identidad. Escribimos la familia como $\bsT_\epsilon$, de modo que $\bsT_0(\vec{f}) = \vec{f}$.

### El generador

Desarrollando cada ejemplo en $\epsilon$ hasta el primer orden:

1. $f_k + \epsilon$ ya es de primer orden: el cambio es $\epsilon \cdot 1$ en la componente $k$ y nulo en las demás.
2. Por el desarrollo de Taylor de cada componente, que es de clase $C^2$, $f_i(x + \epsilon) = f_i(x) + \epsilon \cdot f'_i(x) + O(\epsilon^2)$.
3. Como $\cos\epsilon = 1 + O(\epsilon^2)$ y $\sin\epsilon = \epsilon + O(\epsilon^2)$, queda $(f_1 - \epsilon \cdot f_2,\ f_2 + \epsilon \cdot f_1) + O(\epsilon^2)$.

En los tres casos, $\bsT_\epsilon(\vec{f})(x) = \vec{f}(x) + \epsilon \cdot \vec{\xi}(x) + O(\epsilon^2)$, donde el vector $\vec{\xi}(x)$ solo depende de los valores de $\vec{f}$ y de $\vec{f}'$ en el mismo punto $x$, y de $x$:

| Transformación | $\vec{\xi}$ |
| --- | --- |
| Desplazar la componente $k$ | $\xi_k = 1$, y $\xi_i = 0$ si $i \neq k$ |
| Desplazar la variable | $\xi_i = f'_i$ |
| Girar las componentes $1$ y $2$ | $\xi_1 = -f_2$, $\xi_2 = f_1$, y $\xi_i = 0$ si $i > 2$ |

Esto lleva a la definición general. Un **generador** es una lista de $n$ funciones $\xi_i(\vec{f}, \vec{f}', x)$ de $2 \cdot n + 1$ variables reales, de clase $C^1$. A lo largo de una función $\vec{f}$ escribimos $\xi_i(x) := \xi_i\big(\vec{f}(x), \vec{f}'(x), x\big)$, que es una función de clase $C^1$ de $x$, y $\xi'_i(x)$ es su derivada. Si $\xi_i$ depende de $\vec{f}'$, la derivada $\xi'_i$ contiene $\vec{f}''$; por ejemplo, para el desplazamiento de la variable, $\xi'_i = f''_i$.

La **transformación infinitesimal** de generador $\vec{\xi}$ es

$$
\begin{aligned}
\vec{f} \to \vec{f} + \epsilon \cdot \vec{\xi}, \qquad \vec{f}' \to \vec{f}' + \epsilon \cdot \vec{\xi}'.
\end{aligned}
$$

El teorema de Noether solo usa este primer orden. Dos diferencias con la variación $\vec{h}$ de «El formalismo lagrangiano»: $\vec{h}$ era una función cualquiera, independiente de $\vec{f}$ y nula en los extremos, mientras que $\vec{\xi}$ es una regla fija que se calcula a partir de $\vec{f}$, y no tiene por qué anularse en los extremos.

### Familias de un parámetro y flujos

En los ejemplos 1 y 3, además, $\bsT_\epsilon \circ \bsT_\eta = \bsT_{\epsilon + \eta}$: desplazar $\eta$ y después $\epsilon$ es desplazar $\epsilon + \eta$, y lo mismo con los giros. En el ejemplo 2 también se cumple. Una familia con esta propiedad es un flujo, en el sentido del Tema 1, apartado 4.4, de los apuntes públicos: cuando el generador solo depende de $\vec{f}$, la familia se recupera de él resolviendo $\dfrac{d}{d\epsilon} \bsT_\epsilon(\vec{f}) = \vec{\xi}\big(\bsT_\epsilon(\vec{f})\big)$ con $\bsT_0(\vec{f}) = \vec{f}$. Las rotaciones y las transformaciones de Galileo son de este tipo, y se estudian en los anexos.

## Simetría de un funcional

### La variación de $\bsL$ en la dirección de un generador

Como en «El formalismo lagrangiano», el desarrollo de Taylor de $\bsL$ en sus $2 \cdot n$ primeros argumentos, con $x$ fijo, da

$$
\begin{aligned}
\bsL(\vec{f} + \epsilon \cdot \vec{\xi}, \vec{f}' + \epsilon \cdot \vec{\xi}')(x) - \bsL(\vec{f}, \vec{f}')(x) = \epsilon \cdot \bsdelta_{\vec{\xi}} \bsL(x) + O(\epsilon^2),
\end{aligned}
$$

con la variación primera de $\bsL$ en la dirección de $\vec{\xi}$:

$$
\begin{aligned}
\bsdelta_{\vec{\xi}} \bsL(x) := \sum_{i=1}^{n} \Big( \partial_{f_i} \bsL(\vec{f}, \vec{f}')(x) \cdot \xi_i(x) + p_i(x) \cdot \xi'_i(x) \Big).
\end{aligned}
$$

Es la misma $\bsdelta_{\vec{f}} \bsL$ de «El formalismo lagrangiano», con $\vec{\xi}$ en el lugar de $\vec{h}$.

### Definición

El generador $\vec{\xi}$ es una **simetría** de $\bsS$ (o de $\bsL$) si existe una función $F(\vec{f}, \vec{f}', x)$ de clase $C^1$ tal que, para **toda** función $\vec{f}$ de clase $C^2$ en $[a, b]$ y todo $x \in [a, b]$,

$$
\begin{aligned}
\bsdelta_{\vec{\xi}} \bsL(x) = \dfrac{d}{dx} F(x),
\end{aligned}
$$

donde $F(x) := F\big(\vec{f}(x), \vec{f}'(x), x\big)$. Si se puede tomar $F = 0$, decimos que $\bsL$ es **invariante** bajo la transformación.

La definición no menciona las soluciones: la igualdad tiene que cumplirse para toda función. Por eso la simetría es una propiedad de $\bsL$, y no de una función particular.

### Lo que significa para el funcional

Integrando la definición sobre un subintervalo $[c, d]$, por la regla de Barrow,

$$
\begin{aligned}
\bsS_{[c,d]}[\vec{f} + \epsilon \cdot \vec{\xi}] - \bsS_{[c,d]}[\vec{f}] = \epsilon \cdot \big(F(d) - F(c)\big) + O(\epsilon^2).
\end{aligned}
$$

El resto es $O(\epsilon^2)$ uniformemente en $[c, d]$ por el mismo argumento que en «El formalismo lagrangiano»: las derivadas segundas de $\bsL$ son continuas y se evalúan en un conjunto cerrado y acotado. A primer orden, el funcional solo cambia en una cantidad que depende de lo que ocurre en los extremos del intervalo.

El recíproco también es cierto. Si esa igualdad se cumple para todo subintervalo, dividiendo por $\epsilon$ y haciendo $\epsilon \to 0$ queda $\int_c^d \left(\bsdelta_{\vec{\xi}} \bsL - \dfrac{dF}{dx}\right) dx = 0$ para todo $[c, d]$. El integrando es continuo; derivando respecto de $d$ la integral, por el teorema fundamental del cálculo, el integrando es nulo en cada punto. Las dos formulaciones son, por tanto, equivalentes.

Cuando $F$ solo depende de $\vec{f}$ y de $x$, sumar $\dfrac{dF}{dx}$ a $\bsL$ no cambia las ecuaciones de Euler–Lagrange («El formalismo lagrangiano: anexos», «Requisito matemático previo»). Por eso no se exige $F = 0$: lo que importa son las ecuaciones, y una derivada total no las cambia.

### Simetría y estacionariedad

Las dos ideas usan la variación primera, pero responden a preguntas distintas:

| | Estacionariedad | Simetría |
| --- | --- | --- |
| Qué se fija | una función $\vec{f}_0$ | un generador $\vec{\xi}$ |
| Qué se recorre | todas las $\vec{h}$ admisibles, nulas en los extremos | todas las funciones $\vec{f}$, sin condiciones de contorno |
| Qué se exige | $\bsdelta\bsS[\vec{f}_0] = 0$ | $\bsdelta_{\vec{\xi}} \bsL = \dfrac{dF}{dx}$ |
| De qué es propiedad | de la función $\vec{f}_0$ | de $\bsL$ |
| Para qué sirve | seleccionar las soluciones | obtener cantidades constantes en las soluciones |

### Cómo se reconoce que no hay simetría

Para demostrar que un generador **no** es una simetría hay que ver que ninguna $F$ cumple la definición. Es fácil cuando el generador solo depende de $\vec{f}$ y de $x$, que es el caso de los giros y las traslaciones. Entonces $\xi'_i = \sum_j \partial_{f_j} \xi_i \cdot f'_j + \partial_x \xi_i$ no contiene $\vec{f}''$, y tampoco $\bsdelta_{\vec{\xi}} \bsL$.

En un punto $x_0$, los valores de $\vec{f}$, $\vec{f}'$ y $\vec{f}''$ pueden elegirse con independencia: la función $\vec{f}(x) = \vec{y} + \vec{y}\,' \cdot (x - x_0) + \dfrac{1}{2} \cdot \vec{y}\,'' \cdot (x - x_0)^2$ es de clase $C^2$ y toma en $x_0$ los valores $\vec{y}$, $\vec{y}\,'$ e $\vec{y}\,''$ que se quiera. Por la regla de la cadena,

$$
\begin{aligned}
\dfrac{dF}{dx} = \sum_{j=1}^{n} \partial_{f_j} F \cdot f'_j + \sum_{j=1}^{n} \partial_{f'_j} F \cdot f''_j + \partial_x F.
\end{aligned}
$$

Si el lado izquierdo de la definición no contiene $\vec{f}''$, la igualdad para todos los valores de $\vec{y}\,''$ obliga a que $\partial_{f'_j} F = 0$ para todo $j$: $F$ solo depende de $\vec{f}$ y de $x$, y $\dfrac{dF}{dx}$ es una función afín de $\vec{f}'$. En particular:

* **Criterio.** Si $\bsdelta_{\vec{\xi}} \bsL$ no depende de $\vec{f}'$, la igualdad para todos los valores de $\vec{y}\,'$ obliga a que $\partial_{f_j} F = 0$ para todo $j$, así que $F$ solo depende de $x$. Entonces $\bsdelta_{\vec{\xi}} \bsL = F'(x)$ tiene que depender solo de $x$. Si depende de $\vec{f}$, el generador no es una simetría.

## El teorema de Noether

### Enunciado

**Teorema (primer teorema de Noether, una variable).** Sea $\vec{\xi}$ una simetría de $\bsS$, con la función $F$ de la definición. Entonces, a lo largo de toda solución $\vec{f}_0$ de las ecuaciones de Euler–Lagrange, la función

$$
\begin{aligned}
Q(x) := \sum_{i=1}^{n} p_i(x) \cdot \xi_i(x) - F(x)
\end{aligned}
$$

es constante en $[a, b]$.

$Q$ se llama la **cantidad conservada** de la simetría, o integral primera de las ecuaciones.

### Demostración

Sea $\vec{f}$ una función cualquiera de clase $C^2$, no necesariamente una solución. Por la regla de derivación del producto, para cada $i$,

$$
\begin{aligned}
\dfrac{d}{dx}\big(p_i \cdot \xi_i\big) = \dfrac{dp_i}{dx} \cdot \xi_i + p_i \cdot \xi'_i.
\end{aligned}
$$

Despejando $p_i \cdot \xi'_i$ y sustituyendo en la definición de $\bsdelta_{\vec{\xi}} \bsL$:

$$
\begin{aligned}
\bsdelta_{\vec{\xi}} \bsL &= \sum_{i=1}^{n} \left( \partial_{f_i} \bsL \cdot \xi_i + \dfrac{d}{dx}\big(p_i \cdot \xi_i\big) - \dfrac{dp_i}{dx} \cdot \xi_i \right) \\
&= \sum_{i=1}^{n} \varphi_i \cdot \xi_i + \dfrac{d}{dx}\left( \sum_{i=1}^{n} p_i \cdot \xi_i \right).
\end{aligned}
$$

Como $\vec{\xi}$ es una simetría, el lado izquierdo es $\dfrac{dF}{dx}$. Pasando el último término al otro lado:

$$
\begin{aligned}
\dfrac{d}{dx}\left( \sum_{i=1}^{n} p_i \cdot \xi_i - F \right) = -\sum_{i=1}^{n} \varphi_i \cdot \xi_i.
\end{aligned}
$$

Esta igualdad vale para toda función $\vec{f}$ de clase $C^2$; la llamaremos **identidad de Noether**. Si $\vec{f} = \vec{f}_0$ es una solución, todas las $\varphi_i$ son nulas, y $Q' = 0$ en $[a, b]$. Por el teorema del valor medio, $Q$ es constante. $\blacksquare$

Las funciones que intervienen son derivables con continuidad: $p_i$ y $\xi_i$ son de clase $C^1$ a lo largo de $\vec{f}$, y $F(x)$ también, por ser composición de funciones de clase $C^1$.

### Observaciones

* **El valor de $Q$ depende de la solución.** El teorema dice que $Q$ no cambia a lo largo de cada solución, no que valga lo mismo en todas.
* **La identidad de Noether dice más que el teorema:** vale para toda función, y expresa $Q'$ como una combinación de las expresiones de Euler–Lagrange con coeficientes $\xi_i$.
* **Linealidad.** $\bsdelta_{\vec{\xi}} \bsL$ es lineal en $\vec{\xi}$. Si $\vec{\xi}$ y $\vec{\eta}$ son simetrías con funciones $F$ y $G$, $\alpha \cdot \vec{\xi} + \beta \cdot \vec{\eta}$ es una simetría con $\alpha \cdot F + \beta \cdot G$, y su cantidad conservada es $\alpha \cdot Q_{\vec{\xi}} + \beta \cdot Q_{\vec{\eta}}$. Una familia de transformaciones con $k$ parámetros independientes da $k$ cantidades conservadas, una por parámetro.
* **$F$ y $Q$ están definidas salvo una constante aditiva**, porque $F + c$ tiene la misma derivada que $F$.
* **Puede ocurrir que $Q$ sea constante para toda función**, no solo para las soluciones. Entonces el teorema no da información, y la identidad de Noether se reduce a $\sum_i \varphi_i \cdot \xi_i = 0$ para toda $\vec{f}$: una relación entre las ecuaciones de Euler–Lagrange, que no son independientes. Ocurre con el camino más corto en forma paramétrica (ejemplos matemáticos).

## Dos casos particulares

### Una componente que no aparece en $\bsL$

Sea $\vec{\xi} = \vec{e}_k$: $\xi_k = 1$ y las demás componentes nulas. Entonces $\vec{\xi}' = \vec{0}$ y $\bsdelta_{\vec{\xi}} \bsL = \partial_{f_k} \bsL$.

* **Si $\bsL$ no depende de $f_k$**, es una simetría con $F = 0$, y se conserva $Q = p_k = \partial_{f'_k} \bsL$. Se ve también directamente en la ecuación de Euler–Lagrange de $f_k$, que se reduce a $\dfrac{dp_k}{dx} = 0$.
* **Si $\partial_{f_k} \bsL$ solo depende de $x$**, digamos $\partial_{f_k} \bsL = c(x)$ con $c$ continua, también es una simetría, con $F(x) := \int_a^x c(s) \,ds$. Se conserva $Q = p_k - \int_a^x c(s) \,ds$, que es la ecuación de Euler–Lagrange de $f_k$, $\dfrac{dp_k}{dx} = c(x)$, integrada una vez. En la parte física es el caso de una partícula en un campo uniforme.
* **Si $\partial_{f_k} \bsL$ no depende de $\vec{f}'$ pero sí de $\vec{f}$**, no es una simetría, por el criterio del apartado anterior. Es el caso habitual en la parte física, donde $\bsL$ es la suma de un término que solo depende de $\vec{f}'$ y otro que solo depende de $\vec{f}$ y de $x$. Si $\partial_{f_k} \bsL$ depende de $\vec{f}'$, hay que aplicar el razonamiento completo de ese apartado.

### Cuando $\bsL$ no depende de la variable: la identidad de Beltrami

Sea la transformación $\vec{f}(x) \to \vec{f}(x + \epsilon)$, de generador $\xi_i = f'_i$, con $\xi'_i = f''_i$. Por la regla de la cadena,

$$
\begin{aligned}
\bsdelta_{\vec{\xi}} \bsL = \sum_{i=1}^{n} \Big( \partial_{f_i} \bsL \cdot f'_i + \partial_{f'_i} \bsL \cdot f''_i \Big) = \dfrac{d}{dx}\bsL(\vec{f}, \vec{f}')(x) - \partial_x \bsL(\vec{f}, \vec{f}')(x).
\end{aligned}
$$

Es la diferencial total de «El formalismo lagrangiano: parte matemática» menos el término de la dependencia explícita en $x$. Si $\bsL$ no depende explícitamente de $x$, $\partial_x \bsL = 0$, y el generador es una simetría con $F = \bsL$. La cantidad conservada es

$$
\begin{aligned}
Q = \sum_{i=1}^{n} p_i \cdot f'_i - \bsL = \bsH.
\end{aligned}
$$

Es la **identidad de Beltrami**: si $\bsL$ no depende de $x$, $\bsH$ es constante a lo largo de las soluciones. En la parte física, con $x = t$, es la conservación de la energía.

Si $\bsL$ depende de $x$, la identidad de Noether con este generador sigue valiendo. Con $\dfrac{d}{dx}\left(\sum_i p_i \cdot f'_i\right) - \bsdelta_{\vec{\xi}} \bsL = \dfrac{d\bsH}{dx} + \partial_x \bsL$, queda

$$
\begin{aligned}
\dfrac{d\bsH}{dx} = -\partial_x \bsL - \sum_{i=1}^{n} \varphi_i \cdot f'_i,
\end{aligned}
$$

y sobre las soluciones, $\dfrac{d\bsH}{dx} = -\partial_x \bsL$: la dependencia explícita de $x$ es exactamente lo que impide que $\bsH$ se conserve.

## Transformaciones que también mueven la variable

### La transformación y su definición de simetría

En algunas transformaciones cambia también la variable: un desplazamiento en el tiempo o un cambio de parámetro de una curva. Sea $\tau(x)$ una función de clase $C^1$ en $[a, b]$ y $\vec{\xi}$ un generador. La transformación lleva el punto $x$ a

$$
\begin{aligned}
\tilde{x}(x) := x + \epsilon \cdot \tau(x),
\end{aligned}
$$

y la función $\vec{f}$ a la función $\tilde{\vec{f}}$ definida por

$$
\begin{aligned}
\tilde{\vec{f}}\big(\tilde{x}(x)\big) := \vec{f}(x) + \epsilon \cdot \vec{\xi}(x).
\end{aligned}
$$

Está bien definida para $|\epsilon|$ pequeño: $\tilde{x}'(x) = 1 + \epsilon \cdot \tau'(x)$ es positiva si $|\epsilon| \cdot \max|\tau'| < 1$, así que $\tilde{x}$ es estrictamente creciente y tiene inversa. El intervalo $[c, d]$ pasa a ser $[\tilde{x}(c), \tilde{x}(d)]$.

**Definición.** La transformación es una simetría si existe $F(\vec{f}, \vec{f}', x)$ de clase $C^1$ tal que, para toda $\vec{f}$ de clase $C^2$ y todo subintervalo $[c, d]$,

$$
\begin{aligned}
\bsS_{[\tilde{x}(c), \tilde{x}(d)]}[\tilde{\vec{f}}] - \bsS_{[c,d]}[\vec{f}] = \epsilon \cdot \big(F(d) - F(c)\big) + O(\epsilon^2).
\end{aligned}
$$

Con $\tau = 0$ es la definición anterior en forma integral.

### La condición en cada punto

Cambiamos de variable en la primera integral, $y = \tilde{x}(x)$, con $dy = \tilde{x}'(x) \,dx$:

$$
\begin{aligned}
\bsS_{[\tilde{x}(c), \tilde{x}(d)]}[\tilde{\vec{f}}] = \int_c^d \bsL\Big(\tilde{\vec{f}}\big(\tilde{x}(x)\big), \tilde{\vec{f}}\,'\big(\tilde{x}(x)\big), \tilde{x}(x)\Big) \cdot \tilde{x}'(x) \,dx.
\end{aligned}
$$

El primer argumento es $\vec{f}(x) + \epsilon \cdot \vec{\xi}(x)$, por definición. Para el segundo, derivamos esa definición respecto de $x$ con la regla de la cadena: $\tilde{\vec{f}}\,'\big(\tilde{x}(x)\big) \cdot \tilde{x}'(x) = \vec{f}'(x) + \epsilon \cdot \vec{\xi}'(x)$. Despejando y desarrollando $\dfrac{1}{1 + \epsilon \cdot \tau'} = 1 - \epsilon \cdot \tau' + O(\epsilon^2)$:

$$
\begin{aligned}
\tilde{\vec{f}}\,'\big(\tilde{x}(x)\big) = \dfrac{\vec{f}' + \epsilon \cdot \vec{\xi}'}{1 + \epsilon \cdot \tau'} = \vec{f}' + \epsilon \cdot \big(\vec{\xi}' - \tau' \cdot \vec{f}'\big) + O(\epsilon^2).
\end{aligned}
$$

El tercer argumento es $x + \epsilon \cdot \tau$, y el factor, $1 + \epsilon \cdot \tau'$. Desarrollando $\bsL$ por Taylor en sus $2 \cdot n + 1$ argumentos, el integrando es $\bsL(\vec{f}, \vec{f}')(x) + \epsilon \cdot D(x) + O(\epsilon^2)$, con

$$
\begin{aligned}
D := \sum_{i=1}^{n} \Big( \partial_{f_i} \bsL \cdot \xi_i + p_i \cdot \big(\xi'_i - \tau' \cdot f'_i\big) \Big) + \partial_x \bsL \cdot \tau + \bsL \cdot \tau'.
\end{aligned}
$$

Con el argumento de los subintervalos del apartado anterior, la transformación es una simetría si y solo si $D = \dfrac{dF}{dx}$ en cada punto, para toda $\vec{f}$.

### Reducción al caso anterior

Definimos el generador **a variable fija** y la función

$$
\begin{aligned}
\bar{\xi}_i := \xi_i - \tau \cdot f'_i, \qquad \bar{F} := F - \tau \cdot \bsL.
\end{aligned}
$$

$\bar{\xi}_i$ es el cambio de $f_i$ en un mismo punto: el valor nuevo se toma en $\tilde{x}$, que está desplazado $\epsilon \cdot \tau$, y eso resta $\epsilon \cdot \tau \cdot f'_i$. Calculamos $\bsdelta_{\bar{\vec{\xi}}} \bsL$, con $\bar{\xi}'_i = \xi'_i - \tau' \cdot f'_i - \tau \cdot f''_i$:

$$
\begin{aligned}
\bsdelta_{\bar{\vec{\xi}}} \bsL &= \sum_{i=1}^{n} \Big( \partial_{f_i} \bsL \cdot \xi_i + p_i \cdot \big(\xi'_i - \tau' \cdot f'_i\big) \Big) - \tau \cdot \sum_{i=1}^{n} \Big( \partial_{f_i} \bsL \cdot f'_i + p_i \cdot f''_i \Big) \\
&= \big(D - \partial_x \bsL \cdot \tau - \bsL \cdot \tau'\big) - \tau \cdot \left( \dfrac{d\bsL}{dx} - \partial_x \bsL \right) \\
&= D - \dfrac{d}{dx}\big(\tau \cdot \bsL\big).
\end{aligned}
$$

En la segunda igualdad se usan la definición de $D$ y la regla de la cadena del apartado de Beltrami; en la tercera, la regla del producto. Por tanto, $D = \dfrac{dF}{dx}$ si y solo si $\bsdelta_{\bar{\vec{\xi}}} \bsL = \dfrac{d\bar{F}}{dx}$: la transformación es una simetría si y solo si $\bar{\vec{\xi}}$ lo es, en el sentido del apartado anterior, con la función $\bar{F}$. $\bar{\xi}_i$ y $\bar{F}$ dependen de $\vec{f}'$ aunque $\xi_i$ y $F$ no dependan, y la definición general de generador lo permite.

### La cantidad conservada

Aplicando el teorema a $\bar{\vec{\xi}}$ y $\bar{F}$:

$$
\begin{aligned}
Q = \sum_{i=1}^{n} p_i \cdot \big(\xi_i - \tau \cdot f'_i\big) - F + \tau \cdot \bsL = \sum_{i=1}^{n} p_i \cdot \xi_i - \tau \cdot \bsH - F.
\end{aligned}
$$

Es la fórmula que se usa en la parte física para el grupo de Galileo, con $x = t$.

**Dos ejemplos:**

* **Desplazamiento puro de la variable:** $\tau = 1$ y $\vec{\xi} = \vec{0}$. Entonces $D = \partial_x \bsL$, y si $\bsL$ no depende de $x$, es una simetría con $F = 0$ y $Q = -\bsH$. Coincide, salvo el signo, con la identidad de Beltrami del apartado anterior: allí la gráfica se desplazaba $\epsilon$ hacia la izquierda, y aquí, hacia la derecha, porque $\tilde{\vec{f}}(x + \epsilon) = \vec{f}(x)$.
* **Cambio de parámetro con $\tau$ cualquiera:** $\vec{\xi} = \vec{0}$, $\bsL$ independiente de $x$ y homogénea de grado $1$ en las derivadas, es decir, $\bsL(\vec{f}, \lambda \cdot \vec{f}') = \lambda \cdot \bsL(\vec{f}, \vec{f}')$ para todo $\lambda > 0$. Derivando esta igualdad respecto de $\lambda$ en $\lambda = 1$ se obtiene $\sum_i f'_i \cdot \partial_{f'_i} \bsL = \bsL$, es decir, $\bsH = 0$ para toda función. Entonces $D = \tau' \cdot \left(\bsL - \sum_i p_i \cdot f'_i\right) = -\tau' \cdot \bsH = 0$: es una simetría con $F = 0$ para **toda** función $\tau$, y la cantidad conservada, $Q = -\tau \cdot \bsH$, es idénticamente nula. Una simetría que depende de una función arbitraria no da una cantidad conservada, sino una relación entre las ecuaciones de Euler–Lagrange. Es el caso más sencillo del segundo teorema de Noether; se desarrolla con el camino más corto en los ejemplos matemáticos.

## Varias variables: corrientes que se conservan

### Planteamiento en varias variables

Volvemos al marco general de «El formalismo lagrangiano: parte matemática»: $\vec{f} = (f_1, \dots, f_n): \Omega \to \mathbb{R}^n$ de clase $C^2$ en la caja $\Omega = [a_1, b_1] \times \dots \times [a_m, b_m]$, con $\bsL(\vec{f}, J_{\vec{f}}, \vec{x})$ de clase $C^2$ y los índices $k, l = 1, \dots, m$ para las variables. Como allí, a lo largo de $\vec{f}$ escribimos

$$
\begin{aligned}
u_{ik}(\vec{x}) := \partial_{\partial_{x_k} f_i} \bsL(\vec{f}, J_{\vec{f}})(\vec{x}), \qquad \varphi_i := \partial_{f_i} \bsL - \sum_{k=1}^{m} \dfrac{\partial u_{ik}}{\partial x_k},
\end{aligned}
$$

donde $\dfrac{\partial u_{ik}}{\partial x_k}$ es la derivada de la función compuesta, que es continua (el excurso de aquel documento). Las ecuaciones de Euler–Lagrange son $\varphi_i = 0$.

Un generador es ahora una lista de funciones $\xi_i(\vec{f}, J_{\vec{f}}, \vec{x})$ de clase $C^1$, y $\partial_{x_k} \xi_i$ es la derivada respecto de $x_k$ de la función compuesta $\xi_i(\vec{x})$. La variación primera de $\bsL$ en la dirección de $\vec{\xi}$ es

$$
\begin{aligned}
\bsdelta_{\vec{\xi}} \bsL := \sum_{i=1}^{n} \left( \partial_{f_i} \bsL \cdot \xi_i + \sum_{k=1}^{m} u_{ik} \cdot \partial_{x_k} \xi_i \right).
\end{aligned}
$$

**Definición.** $\vec{\xi}$ es una simetría si existen $m$ funciones $F_1, \dots, F_m$ de $(\vec{f}, J_{\vec{f}}, \vec{x})$, de clase $C^1$, tales que, para toda $\vec{f}$ de clase $C^2$,

$$
\begin{aligned}
\bsdelta_{\vec{\xi}} \bsL = \sum_{k=1}^{m} \partial_{x_k} F_k,
\end{aligned}
$$

donde $\partial_{x_k} F_k$ es la derivada de la función compuesta. El lado derecho es la divergencia del campo $(F_1, \dots, F_m)$; con $m = 1$ es la derivada $\dfrac{dF}{dx}$ del caso de una variable.

### El teorema

**Teorema.** Si $\vec{\xi}$ es una simetría, las $m$ funciones

$$
\begin{aligned}
Q_k := \sum_{i=1}^{n} u_{ik} \cdot \xi_i - F_k, \qquad k = 1, \dots, m,
\end{aligned}
$$

cumplen, a lo largo de toda solución,

$$
\begin{aligned}
\sum_{k=1}^{m} \partial_{x_k} Q_k = 0.
\end{aligned}
$$

**Demostración.** La misma que en una variable, con una regla del producto para cada $k$: $\partial_{x_k}(u_{ik} \cdot \xi_i) = \dfrac{\partial u_{ik}}{\partial x_k} \cdot \xi_i + u_{ik} \cdot \partial_{x_k} \xi_i$. Despejando $u_{ik} \cdot \partial_{x_k} \xi_i$ y sumando en $i$ y en $k$,

$$
\begin{aligned}
\bsdelta_{\vec{\xi}} \bsL = \sum_{i=1}^{n} \varphi_i \cdot \xi_i + \sum_{k=1}^{m} \partial_{x_k}\left( \sum_{i=1}^{n} u_{ik} \cdot \xi_i \right),
\end{aligned}
$$

y con la definición de simetría, $\sum_k \partial_{x_k} Q_k = -\sum_i \varphi_i \cdot \xi_i$ para toda $\vec{f}$, que es nulo sobre las soluciones. $\blacksquare$

$(Q_1, \dots, Q_m)$ se llama **corriente conservada**: lo que se conserva ya no es un número, sino que la corriente tiene divergencia nula.

### Cuando una variable es el tiempo: la ley de conservación integral

Si las variables son el tiempo, $x_0 := t \in [t_1, t_2]$, y $m$ coordenadas espaciales en la caja $\Omega$, la corriente tiene $m + 1$ componentes y la ley se escribe

$$
\begin{aligned}
\partial_t Q_0 + \sum_{k=1}^{m} \partial_{x_k} Q_k = 0.
\end{aligned}
$$

Es una ecuación de continuidad: $Q_0$ es una densidad y $(Q_1, \dots, Q_m)$, su flujo. Integramos en $\Omega$ para un $t$ fijo. $Q_0$ y $\partial_t Q_0$ son continuas en el conjunto cerrado y acotado $[t_1, t_2] \times \Omega$, así que la derivada respecto de $t$ puede entrar en la integral. Por el teorema de Fubini, cada término $\partial_{x_k} Q_k$ se integra primero en $x_k$, con la regla de Barrow, como en la integración por partes de «El formalismo lagrangiano»:

$$
\begin{aligned}
\dfrac{d}{dt} \int_\Omega Q_0 \,dx_1 \cdots dx_m = -\sum_{k=1}^{m} \int_{\Omega_k} \Big[ Q_k \Big]_{x_k = a_k}^{x_k = b_k} d\hat{x}_k,
\end{aligned}
$$

con $\Omega_k$ y $d\hat{x}_k$ como en aquel documento. El lado derecho solo depende de los valores de la corriente en la frontera $\operatorname{Fr}(\Omega)$: es lo que entra o sale por las caras. Si las condiciones de contorno lo anulan, la cantidad total $\int_\Omega Q_0 \,dx_1 \cdots dx_m$ se conserva. Si no, cambia exactamente en lo que atraviesa la frontera. La cuerda vibrante de los ejemplos físicos muestra los dos casos.

## Resumen

| Situación | Generador | $F$ | Cantidad conservada |
| --- | --- | --- | --- |
| $\bsL$ no depende de $f_k$ | $\vec{\xi} = \vec{e}_k$ | $0$ | $p_k$ |
| $\partial_{f_k} \bsL = c(x)$ | $\vec{\xi} = \vec{e}_k$ | $\int_a^x c(s) \,ds$ | $p_k - \int_a^x c(s) \,ds$ |
| $\bsL$ no depende de $x$ | $\xi_i = f'_i$ | $\bsL$ | $\bsH$ |
| La variable también se mueve | $\vec{\xi}$ y $\tau$ | $F$ | $\sum_i p_i \cdot \xi_i - \tau \cdot \bsH - F$ |
| Varias variables | $\vec{\xi}$ | $F_1, \dots, F_m$ | corriente $Q_k$, con $\sum_k \partial_{x_k} Q_k = 0$ |

Table: Casos particulares del teorema de Noether.
