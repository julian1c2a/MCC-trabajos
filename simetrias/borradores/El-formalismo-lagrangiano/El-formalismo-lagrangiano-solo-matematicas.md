---
author: "Julián Calderón Almendros"
---

# El formalismo lagrangiano: parte matemática

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-03
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

En esta serie de documentos voy a desarrollar un primer borrador del formalismo lagrangiano.

La forma en que lo voy a desarrollar es personal y no va a coincidir con la propuesta para María y para mí, sino que estos documentos deben ser un superconjunto de lo que vamos a presentar.

La serie consta de cinco documentos:

* «El formalismo lagrangiano: parte matemática» (este documento): el cálculo de variaciones, desde una función de una variable hasta funciones vectoriales de varias variables.
* «El formalismo lagrangiano: ejemplos matemáticos».
* «El formalismo lagrangiano: parte física»: de las ecuaciones de Euler–Lagrange a la mecánica de partículas, a partir de las leyes de Newton.
* «El formalismo lagrangiano: ejemplos físicos».
* «El formalismo lagrangiano: anexos»: el lema fundamental del cálculo de variaciones y otros resultados matemáticos auxiliares.

## Optimizar una función de una variable según un funcional que caracteriza el objetivo

Supongamos que tenemos un conjunto de funciones que sean dos veces derivables con continuidad, que tienen un dominio en el intervalo $[a,b] \subseteq \mathbb{R}$, y cuya imagen es un real en cada punto del dominio. Le vamos a exigir también a ese conjunto de funciones, siendo $f$ y $g$ dos cualesquiera de ellas, que $f(a)=g(a)$ y que $f(b)=g(b)$. Con estas condiciones, lo que tenemos que optimizar (en realidad, encontrar una función en la que el funcional sea estacionario) es:

$$
\begin{aligned}
\bsS[f] := \int_a^b \bsL(f,f',x) \,dx.
\end{aligned}
$$

Claro está que no hemos definido $\bsL$. Al pasarle $f$ al operador $\bsL$, este nos devuelve una función de la variable $x$.

Lo primero que quiero hacer es ver si existe algo como una derivada de $\bsS$. Para esto vamos a inventar otra función auxiliar, $h$. Esta función es cualquier función dos veces derivable con continuidad en el mismo dominio antes definido, pero con las condiciones de contorno $h(a) = h(b) = 0$. Por lo demás, consideraremos la función $(\delta_f \bsL)(f,f',x) := \bsL (f + \epsilon \cdot h,f'+\epsilon \cdot h', x) - \bsL (f, f', x)$.

No lo he dicho, pero $\epsilon$ es un número real tan pequeño como se quiera, pero distinto de $0$, de forma que nos ayude a que la aportación que hace $h$ sea también infinitesimal en cada punto.

El problema ahora es ¿cuánto vale $(\delta_f \bsL)(f,f',x)$? Antes conviene distinguir dos cambios de $\bsL$ que no son lo mismo:

* **La diferencial total, $d\bsL$:** cuánto cambia $\bsL(f(x), f'(x), x)$ al pasar de $x$ a $x + dx$ a lo largo de la **misma** función $f$. Por la regla de la cadena de Leibniz,

  $$
  \begin{aligned}
  d\bsL = \dfrac {\partial \bsL}{\partial f}(f,f',x) \cdot f'(x) \cdot dx &+ \dfrac {\partial \bsL}{\partial f'}(f,f',x) \cdot f''(x) \cdot dx \\
  &+ \dfrac {\partial \bsL}{\partial x}(f,f',x) \cdot dx.
  \end{aligned}
  $$

  La derivada total $\dfrac{d\bsL}{dx}$ aparecerá más adelante (al integrar por partes y en la identidad de Beltrami), pero no es lo que buscamos ahora.

* **La variación, $\delta_f \bsL$:** cuánto cambia $\bsL$ al cambiar la **función**, de $f$ a $f + \epsilon \cdot h$, en el **mismo** punto $x$. Aquí $x$ no se mueve: solo cambian el primer y el segundo argumento de $\bsL$. Por eso en la variación no puede aparecer ningún término con $\dfrac{\partial \bsL}{\partial x}$.

Recordemos que $\bsL$ es una función de tres variables reales, y que $\dfrac{\partial \bsL}{\partial f}$ y $\dfrac{\partial \bsL}{\partial f'}$ son sus derivadas parciales respecto de su primer y su segundo argumento. Para calcular la variación aplicamos un desarrollo de Taylor de $\bsL$ en esos dos argumentos, alrededor de $(f(x), f'(x))$ y con $x$ fijo:

$$
\begin{aligned}
\bsL (f + \epsilon \cdot h,\ f' + \epsilon \cdot h',\ x) = \bsL (f, f', x) &+ \dfrac {\partial \bsL}{\partial f}(f, f', x) \cdot \epsilon \cdot h(x) \\
&+ \dfrac {\partial \bsL}{\partial f'}(f, f', x) \cdot \epsilon \cdot h'(x) + O(\epsilon^2).
\end{aligned}
$$

De aquí sale la variación:

$$
\begin{aligned}
(\delta_f \bsL)(f,f',x) &= \bsL (f + \epsilon \cdot h,\ f' + \epsilon \cdot h',\ x) - \bsL (f, f', x) \\
&= \dfrac {\partial \bsL}{\partial f}(f,f',x) \cdot \epsilon \cdot h(x) + \dfrac {\partial \bsL}{\partial f'}(f,f',x) \cdot \epsilon \cdot h'(x) + O(\epsilon^2).
\end{aligned}
$$

Dividiendo por $\epsilon$ y haciendo $\epsilon \to 0$:

$$
\begin{aligned}
\lim_{\epsilon \to 0} \dfrac{(\delta_f \bsL)(f,f',x)}{\epsilon} = \dfrac {\partial \bsL}{\partial f}(f,f',x) \cdot h(x) + \dfrac {\partial \bsL}{\partial f'}(f,f',x) \cdot h'(x).
\end{aligned}
$$

Esta expresión es exacta. Si $\bsL$ tiene derivadas segundas continuas, el resto del desarrollo de Taylor es de orden $\epsilon^2$; al dividirlo por $\epsilon$ queda un término de orden $\epsilon$, que tiende a $0$.

A este límite lo llamaremos variación primera de $\bsL$, y lo escribiremos con $\bsdelta$ en negrita:

$$
\begin{aligned}
\bsdelta_f \bsL(f,f',x) := \lim_{\epsilon \to 0} \dfrac{(\delta_f \bsL)(f,f',x)}{\epsilon}.
\end{aligned}
$$

La $\delta_f$ normal es la diferencia completa, que contiene el factor $\epsilon$ y términos de orden $\epsilon^2$; la $\bsdelta_f$ en negrita es solo su parte de primer orden, dividida por $\epsilon$.

Hacemos lo mismo con el funcional. Su diferencia completa es $\bsS[f + \epsilon \cdot h] - \bsS[f]$, y su variación primera en $f$, en la dirección de $h$, es:

$$
\begin{aligned}
\bsdelta\bsS[f] := \lim_{\epsilon \to 0} \dfrac{\bsS[f + \epsilon \cdot h] - \bsS[f]}{\epsilon}.
\end{aligned}
$$

$\bsdelta\bsS[f]$ depende de $f$ y también de $h$, aunque no lo indiquemos en la notación. Para relacionarla con $\bsdelta_f \bsL$, observamos que las dos integrales tienen el mismo intervalo, así que su diferencia es la integral de la diferencia:

$$
\begin{aligned}
\bsS[f + \epsilon \cdot h] - \bsS[f] &= \int_a^b (\delta_f \bsL)(f,f',x)\,dx \\
&= \epsilon \cdot \int_a^b \bsdelta_f \bsL(f,f',x)\,dx + \int_a^b R(x,\epsilon)\,dx,
\end{aligned}
$$

donde $R(x,\epsilon)$ es el resto del desarrollo de Taylor (el término $O(\epsilon^2)$). Las derivadas segundas de $\bsL$ son continuas y, como $f$, $f'$, $h$ y $h'$ son continuas en el intervalo cerrado y acotado $[a,b]$, se evalúan en un conjunto cerrado y acotado, donde están acotadas. Por eso existe una constante $C$, que no depende de $x$, tal que $|R(x,\epsilon)| \leq C \cdot \epsilon^2$ para $|\epsilon| \leq 1$. Dividiendo por $\epsilon$:

$$
\begin{aligned}
\left|\dfrac{\bsS[f + \epsilon \cdot h] - \bsS[f]}{\epsilon} - \int_a^b \bsdelta_f \bsL(f,f',x)\,dx\right| &= \left|\int_a^b \dfrac{R(x,\epsilon)}{\epsilon}\,dx\right| \\
&\leq (b - a) \cdot C \cdot |\epsilon|,
\end{aligned}
$$

que tiende a $0$ con $\epsilon$. Por tanto, el límite puede entrar en la integral:

$$
\begin{aligned}
\bsdelta\bsS[f] = \int_a^b \bsdelta_f \bsL(f,f',x)\,dx.
\end{aligned}
$$

Ahora lo que queremos es resolver $\bsdelta \bsS [f] = \bsdelta_f \int_a^b \bsL(f,f',x) \,dx = 0$. Esto quiere decir que estamos buscando una función $f_0$ tal que:

$$
\begin{aligned}
\forall (h: [a,b] &\to \mathbb{R}) \qquad \dfrac{d^2h}{dx^2} \text{ es continua} \land h(a)=h(b)=0 \implies \\
\bsdelta \bsS[f_0] &= \bsdelta_f \int_a^b \bsL(f_0,f'_0,x) \,dx \\
                   &= \int_a^b \bsdelta_f\bsL(f_0,f'_0,x) \,dx \\
                   &= \int_a^b \bigg(\dfrac {\partial \bsL}{\partial f}(f_0,f'_0,x) \cdot h(x) \\
                   &\qquad + \dfrac {\partial \bsL}{\partial f'}(f_0,f'_0,x) \cdot h'(x)\bigg) \,dx = 0.
\end{aligned}
$$

Un excurso antes de integrar por partes. Al integrar por partes el término con $h'$ aparecerá la derivada respecto de $x$ de la función $x \mapsto \dfrac{\partial \bsL}{\partial f'}(f(x), f'(x), x)$. Como $\bsL$ tiene derivadas parciales segundas continuas y $f$ es dos veces derivable con continuidad, la regla de la cadena da:

$$
\begin{aligned}
&\dfrac{d}{dx}\left(\dfrac{\partial \bsL}{\partial f'}(f(x), f'(x), x)\right) \\
&\qquad = \dfrac{\partial^2 \bsL}{\partial f \partial f'} \cdot \dfrac{df}{dx} + \dfrac{\partial^2 \bsL}{\partial f'^2} \cdot \dfrac{df'}{dx} + \dfrac{\partial^2 \bsL}{\partial x \partial f'} \cdot \dfrac{dx}{dx} \\
&\qquad = \dfrac{\partial^2 \bsL}{\partial f \partial f'} \cdot f'(x) + \dfrac{\partial^2 \bsL}{\partial f'^2} \cdot f''(x) + \dfrac{\partial^2 \bsL}{\partial x \partial f'},
\end{aligned}
$$

donde las derivadas segundas de $\bsL$ se evalúan en $(f(x), f'(x), x)$. Por el teorema de Schwarz, al ser continuas, el orden de las derivadas cruzadas no importa: $\dfrac{\partial^2 \bsL}{\partial f \partial f'} = \dfrac{\partial^2 \bsL}{\partial f' \partial f}$. El resultado es una función continua de $x$, porque lo son las derivadas segundas de $\bsL$, $f'$ y $f''$. Esto justifica la integración por partes que viene a continuación, y el término con $f''(x)$ es el que hará que la ecuación final sea de segundo orden.

Para encontrar esa función $f_0$ que buscamos, lo primero que vamos a hacer es integrar por partes. Por la linealidad de la integral, separamos los dos términos:

$$
\begin{aligned}
\bsdelta \bsS[f_0] = \int_a^b \dfrac{\partial \bsL}{\partial f}(f_0,f'_0,x) \cdot h(x) \,dx + \int_a^b \dfrac{\partial \bsL}{\partial f'}(f_0,f'_0,x) \cdot h'(x) \,dx.
\end{aligned}
$$

Recordemos la regla de integración por partes: si $u$ y $v$ son funciones con derivada continua en $[a,b]$,

$$
\begin{aligned}
\int_a^b u(x) \cdot v'(x) \,dx = \Big[u(x) \cdot v(x)\Big]_a^b - \int_a^b u'(x) \cdot v(x) \,dx.
\end{aligned}
$$

La aplicamos al segundo término con $u(x) := \dfrac{\partial \bsL}{\partial f'}(f_0(x),f'_0(x),x)$ y $v(x) := h(x)$. Por el excurso anterior, aplicado a $f = f_0$, $u$ tiene derivada continua, y $h$ también la tiene. Por tanto:

$$
\begin{aligned}
\int_a^b \dfrac{\partial \bsL}{\partial f'}(f_0,f'_0,x) \cdot h'(x) \,dx &= \left[\dfrac{\partial \bsL}{\partial f'}(f_0,f'_0,x) \cdot h(x)\right]_a^b \\
&\quad - \int_a^b \dfrac{d}{dx}\left(\dfrac{\partial \bsL}{\partial f'}(f_0,f'_0,x)\right) \cdot h(x) \,dx.
\end{aligned}
$$

El término de contorno es nulo, porque $h(a) = h(b) = 0$:

$$
\begin{aligned}
\left[\dfrac{\partial \bsL}{\partial f'}(f_0,f'_0,x) \cdot h(x)\right]_a^b &= \dfrac{\partial \bsL}{\partial f'}(f_0(b),f'_0(b),b) \cdot h(b) - \dfrac{\partial \bsL}{\partial f'}(f_0(a),f'_0(a),a) \cdot h(a) \\
&= 0.
\end{aligned}
$$

Aquí es donde se usan las condiciones de contorno de $h$, y por eso las exigimos. Sustituyendo en $\bsdelta \bsS[f_0]$ y volviendo a juntar las dos integrales:

$$
\begin{aligned}
\bsdelta \bsS[f_0] = \int_a^b \left(\dfrac{\partial \bsL}{\partial f}(f_0,f'_0,x) - \dfrac{d}{dx}\left(\dfrac{\partial \bsL}{\partial f'}(f_0,f'_0,x)\right)\right) \cdot h(x) \,dx.
\end{aligned}
$$

Por último, aplicamos el excurso con $f = f_0$ para desarrollar la derivada total:

$$
\begin{aligned}
\bsdelta \bsS[f_0] = \int_a^b \bigg(&\dfrac{\partial \bsL}{\partial f} - \dfrac{\partial^2 \bsL}{\partial f \partial f'} \cdot f'_0(x) \\
&- \dfrac{\partial^2 \bsL}{\partial f'^2} \cdot f''_0(x) - \dfrac{\partial^2 \bsL}{\partial x \partial f'}\bigg) \cdot h(x) \,dx,
\end{aligned}
$$

donde las derivadas de $\bsL$ se evalúan en $(f_0(x), f'_0(x), x)$.

El paréntesis ya no contiene a $h$: es una función de $x$ que solo depende de $f_0$, y es continua, porque lo son las derivadas de $\bsL$ hasta el segundo orden, $f'_0$ y $f''_0$. Llamándola

$$
\begin{aligned}
\varphi(x) := \dfrac{\partial \bsL}{\partial f}(f_0,f'_0,x) - \dfrac{d}{dx}\left(\dfrac{\partial \bsL}{\partial f'}(f_0,f'_0,x)\right),
\end{aligned}
$$

hemos pasado de una condición con $h$ y $h'$ a esta otra: $\int_a^b \varphi(x) \cdot h(x) \,dx = 0$ para toda $h$ dos veces derivable con continuidad con $h(a) = h(b) = 0$. Por el lema fundamental del cálculo de variaciones, que se demuestra en el documento de anexos, esto obliga a que $\varphi(x) = 0$ en todo $[a,b]$. Es decir, $f_0$ tiene que cumplir, para todo $x \in [a,b]$:

$$
\begin{aligned}
\dfrac{\partial \bsL}{\partial f}(f_0,f'_0,x) - \dfrac{d}{dx}\left(\dfrac{\partial \bsL}{\partial f'}(f_0,f'_0,x)\right) = 0.
\end{aligned}
$$

Es la ecuación de Euler–Lagrange. El recíproco también es cierto: el cálculo que lleva de $\bsdelta \bsS[f_0]$ a $\int_a^b \varphi(x) \cdot h(x) \,dx$ vale para cualquier función del conjunto de partida, así que si $f_0$ cumple la ecuación, entonces $\varphi = 0$ y $\bsdelta \bsS[f_0] = 0$ para toda $h$ admisible. Por tanto, dentro del conjunto de partida, $f_0$ hace estacionario a $\bsS$ si y solo si cumple la ecuación de Euler–Lagrange.

Desarrollando la derivada total con el excurso, la ecuación de Euler–Lagrange es una ecuación diferencial ordinaria de segundo orden para $f_0$:

$$
\begin{aligned}
\dfrac{\partial^2 \bsL}{\partial f'^2} \cdot f''_0(x) + \dfrac{\partial^2 \bsL}{\partial f \partial f'} \cdot f'_0(x) + \dfrac{\partial^2 \bsL}{\partial x \partial f'} - \dfrac{\partial \bsL}{\partial f} = 0,
\end{aligned}
$$

con las derivadas de $\bsL$ evaluadas en $(f_0(x), f'_0(x), x)$. Sus dos constantes de integración se fijan con los valores $f_0(a)$ y $f_0(b)$, que son los que comparten todas las funciones del conjunto de partida. Es un problema de contorno, no de valores iniciales: según cuál sea $\bsL$, puede tener una solución, ninguna o infinitas.

## Generalizando la anterior optimización a funciones de dos variables

En el primer apartado hemos tratado con funciones $f: [a,b] \to \mathbb{R}$, tales que $f''(x)$ existe y es continua en el dominio especificado, además de cumplir con las condiciones de contorno en $f(a)$ y $f(b)$. ¿Qué ocurre si consideramos funciones de dos variables, $f: \Omega \to \mathbb{R}$, definidas en el rectángulo $\Omega := [x_1,x_2] \times [t_1,t_2] \subseteq \mathbb{R} \times \mathbb{R}$? Les exigiremos que sean de clase $C^2(\Omega)$: que existan y sean continuas, como funciones de $x$ y de $t$, todas sus derivadas parciales hasta el segundo orden, $\dfrac{\partial f}{\partial x}$, $\dfrac{\partial f}{\partial t}$, $\dfrac{\partial^2 f}{\partial x^2}$, $\dfrac{\partial^2 f}{\partial x \partial t}$, $\dfrac{\partial^2 f}{\partial t \partial x}$ y $\dfrac{\partial^2 f}{\partial t^2}$. Por el teorema de Schwarz, al ser continuas, las derivadas cruzadas coinciden: $\dfrac{\partial^2 f}{\partial x \partial t} = \dfrac{\partial^2 f}{\partial t \partial x}$.

Las condiciones de contorno pasan de los dos extremos del intervalo a la frontera del rectángulo, que escribiremos $\operatorname{Fr}(\Omega)$ (y no $\partial\Omega$, para no confundirla con las derivadas parciales). Está formada por sus cuatro lados: $x = x_1$, $x = x_2$, $t = t_1$ y $t = t_2$. Exigimos que todas las funciones del conjunto tomen los mismos valores en $\operatorname{Fr}(\Omega)$: esos valores pueden variar de un punto a otro de la frontera, pero no al cambiar de función. Es decir, si $f$ y $g$ son dos funciones cualesquiera del conjunto, $f(x,t) = g(x,t)$ para todo $(x,t) \in \operatorname{Fr}(\Omega)$.

Ahora $\bsL$ toma una forma algo diferente: es una función de cinco variables reales, $\bsL\left(f, \dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial t}, x, t\right)$, con derivadas parciales segundas continuas. El funcional es ahora una integral doble sobre $\Omega$:

$$
\begin{aligned}
\bsS[f] := \int_{t_1}^{t_2} \int_{x_1}^{x_2} \bsL\left(f, \dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial t}, x, t\right) \,dx \,dt.
\end{aligned}
$$

Por comodidad, a partir de ahora definiremos los símbolos ${\partial_x f} := {\dfrac {\partial f}{\partial x}}$, y ${\partial_t f} := {\dfrac {\partial f}{\partial t}}$. Las segundas parciales quedan así, ${\partial^2_x f} := {\dfrac {\partial^2 f}{\partial x^2}}$, ${\partial^2_t f} := {\dfrac {\partial^2 f}{\partial t^2}}$ y por último ${\partial^2_{xt} f} := {\dfrac {\partial^2 f}{\partial x \partial t}} = {\dfrac {\partial^2 f}{\partial t \partial x}} =: {\partial^2_{tx} f}$.

De esta forma $\bsL\left(f, \dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial t}, x, t\right)$ pasa a ser $\bsL(f, \partial_x f, \partial_t f, x, t)$. Cuando $\bsL$ se evalúa a lo largo de una función $f$, escribiremos además

$$
\begin{aligned}
\bsL(f, \partial_x f, \partial_t f)(x,t) := \bsL\big(f(x,t), \partial_x f(x,t), \partial_t f(x,t), x, t\big),
\end{aligned}
$$

y lo mismo con sus derivadas parciales. Esta notación separa los argumentos respecto de los que se deriva ($f$, $\partial_x f$ y $\partial_t f$) del punto en el que se evalúa, $(x,t)$. La dependencia explícita de $\bsL$ respecto de $x$ y de $t$ sigue presente, aunque ya no aparezca entre los argumentos. Con ella, $\bsS$ pasa a escribirse

$$
\begin{aligned}
\bsS[f] \equiv \int_{t_1}^{t_2} \int_{x_1}^{x_2} \bsL(f, \partial_x f, \partial_t f)(x,t) \,dx \,dt.
\end{aligned}
$$

Como en el caso de una variable, para variar $f$ tomamos una función auxiliar $h: \Omega \to \mathbb{R}$ de clase $C^2(\Omega)$ que se anula en la frontera: $h(x,t) = 0$ para todo $(x,t) \in \operatorname{Fr}(\Omega)$. Así, $f + \epsilon \cdot h$ también es de clase $C^2(\Omega)$ y toma en $\operatorname{Fr}(\Omega)$ los mismos valores que $f$, de modo que sigue en el conjunto de partida.

Recordemos que ahora $\bsL$ es una función de cinco variables reales, y que $\partial_f \bsL$, $\partial_{\partial_x f} \bsL$ y $\partial_{\partial_t f} \bsL$ son sus derivadas parciales respecto de su primer, su segundo y su tercer argumento. Para calcular la variación aplicamos un desarrollo de Taylor de $\bsL$ en esos tres argumentos, alrededor de $(f(x,t), \partial_x f(x,t), \partial_t f(x,t))$ y con $(x,t)$ fijo:

$$
\begin{aligned}
&\bsL(f + \epsilon \cdot h,\ \partial_x f + \epsilon \cdot \partial_x h,\ \partial_t f + \epsilon \cdot \partial_t h)(x,t) \\
&\quad = \bsL(f, \partial_x f, \partial_t f)(x,t) \\
&\qquad + \partial_f \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot \epsilon \cdot h(x,t) \\
&\qquad + \partial_{\partial_x f} \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot \epsilon \cdot \partial_x h(x,t) \\
&\qquad + \partial_{\partial_t f} \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot \epsilon \cdot \partial_t h(x,t) \\
&\qquad + O(\epsilon^2).
\end{aligned}
$$

Llamamos, como antes, $\delta_f \bsL$ a la diferencia completa, con lo que:

$$
\begin{aligned}
&(\delta_f \bsL)(f, \partial_x f, \partial_t f)(x,t) \\
&\quad := \bsL(f + \epsilon \cdot h,\ \partial_x f + \epsilon \cdot \partial_x h,\ \partial_t f + \epsilon \cdot \partial_t h)(x,t) \\
&\qquad - \bsL(f, \partial_x f, \partial_t f)(x,t) \\
&\quad = \partial_f \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot \epsilon \cdot h(x,t) \\
&\qquad + \partial_{\partial_x f} \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot \epsilon \cdot \partial_x h(x,t) \\
&\qquad + \partial_{\partial_t f} \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot \epsilon \cdot \partial_t h(x,t) \\
&\qquad + O(\epsilon^2).
\end{aligned}
$$

La variación primera de $\bsL$ es, como en el caso de una variable, la parte de primer orden de esa diferencia, dividida por $\epsilon$:

$$
\begin{aligned}
&\bsdelta_f \bsL(f, \partial_x f, \partial_t f)(x,t) := \lim_{\epsilon \to 0} \dfrac{(\delta_f \bsL)(f, \partial_x f, \partial_t f)(x,t)}{\epsilon} \\
&\quad = \partial_f \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot h(x,t) \\
&\qquad + \partial_{\partial_x f} \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot \partial_x h(x,t) \\
&\qquad + \partial_{\partial_t f} \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot \partial_t h(x,t).
\end{aligned}
$$

Esta expresión es exacta: si $\bsL$ tiene derivadas segundas continuas, el resto del desarrollo de Taylor es de orden $\epsilon^2$, y al dividirlo por $\epsilon$ queda un término de orden $\epsilon$, que tiende a $0$.

La variación primera de $\bsS$ se define igual que en el caso de una variable:

$$
\begin{aligned}
\bsdelta\bsS[f] := \lim_{\epsilon \to 0} \dfrac{\bsS[f + \epsilon \cdot h] - \bsS[f]}{\epsilon}.
\end{aligned}
$$

Como las dos integrales dobles tienen el mismo dominio $\Omega$, su diferencia es la integral doble de la diferencia:

$$
\begin{aligned}
\bsS[f + \epsilon \cdot h] - \bsS[f] &= \int_{t_1}^{t_2} \int_{x_1}^{x_2} (\delta_f \bsL)(f, \partial_x f, \partial_t f)(x,t) \,dx \,dt \\
&= \epsilon \cdot \int_{t_1}^{t_2} \int_{x_1}^{x_2} \bsdelta_f \bsL(f, \partial_x f, \partial_t f)(x,t) \,dx \,dt \\
&\quad + \int_{t_1}^{t_2} \int_{x_1}^{x_2} R(x,t,\epsilon) \,dx \,dt,
\end{aligned}
$$

donde $R(x,t,\epsilon)$ es el resto del desarrollo de Taylor (el término $O(\epsilon^2)$). Las derivadas segundas de $\bsL$ son continuas y, como $f$, $\partial_x f$, $\partial_t f$, $h$, $\partial_x h$ y $\partial_t h$ son continuas en el rectángulo cerrado y acotado $\Omega$, se evalúan en un conjunto cerrado y acotado, donde están acotadas. Por eso existe una constante $C$, que no depende de $(x,t)$, tal que $|R(x,t,\epsilon)| \leq C \cdot \epsilon^2$ para $|\epsilon| \leq 1$. Dividiendo por $\epsilon$:

$$
\begin{aligned}
&\left|\dfrac{\bsS[f + \epsilon \cdot h] - \bsS[f]}{\epsilon} - \int_{t_1}^{t_2} \int_{x_1}^{x_2} \bsdelta_f \bsL(f, \partial_x f, \partial_t f)(x,t) \,dx \,dt\right| \\
&\quad = \left|\int_{t_1}^{t_2} \int_{x_1}^{x_2} \dfrac{R(x,t,\epsilon)}{\epsilon} \,dx \,dt\right| \\
&\quad \leq (x_2 - x_1) \cdot (t_2 - t_1) \cdot C \cdot |\epsilon|,
\end{aligned}
$$

que tiende a $0$ con $\epsilon$. Por tanto, el límite puede entrar en la integral:

$$
\begin{aligned}
\bsdelta\bsS[f] &= \int_{t_1}^{t_2} \int_{x_1}^{x_2} \bsdelta_f \bsL(f, \partial_x f, \partial_t f)(x,t) \,dx \,dt \\
&= \int_{t_1}^{t_2} \int_{x_1}^{x_2} \bigg(\partial_f \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot h(x,t) \\
&\qquad + \partial_{\partial_x f} \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot \partial_x h(x,t) \\
&\qquad + \partial_{\partial_t f} \bsL(f, \partial_x f, \partial_t f)(x,t) \cdot \partial_t h(x,t)\bigg) \,dx \,dt.
\end{aligned}
$$

Ahora lo que queremos es resolver $\bsdelta\bsS[f] = 0$. Es decir, buscamos una función $f_0$ del conjunto de partida tal que $\bsdelta\bsS[f_0] = 0$ para toda $h: \Omega \to \mathbb{R}$ de clase $C^2(\Omega)$ con $h = 0$ en $\operatorname{Fr}(\Omega)$. Como en el caso de una variable, el camino es eliminar $\partial_x h$ y $\partial_t h$ integrando por partes, y antes conviene saber derivar las funciones que las acompañan.

Un excurso antes de integrar por partes. Al integrar por partes el término con $\partial_x h$ aparecerá la derivada respecto de $x$, con $t$ fijo, de la función compuesta $(x,t) \mapsto \partial_{\partial_x f} \bsL(f, \partial_x f, \partial_t f)(x,t)$, y al integrar el término con $\partial_t h$, la derivada respecto de $t$, con $x$ fijo, de $(x,t) \mapsto \partial_{\partial_t f} \bsL(f, \partial_x f, \partial_t f)(x,t)$. Ahora hay dos derivadas distintas que se escriben con $\partial$, y conviene no confundirlas:

* $\dfrac{\partial}{\partial x}\Big(\partial_{\partial_x f} \bsL(f, \partial_x f, \partial_t f)(x,t)\Big)$ es la derivada de la función compuesta: al cambiar $x$ cambian $f(x,t)$, $\partial_x f(x,t)$ y $\partial_t f(x,t)$, y también el cuarto argumento de $\bsL$. Es el análogo de la derivada total $\dfrac{d}{dx}$ del caso de una variable.
* $\partial_x \bsL$ es la derivada parcial de $\bsL$ respecto de su cuarto argumento, con los otros cuatro fijos, y $\partial_t \bsL$, respecto del quinto. Son el análogo de $\dfrac{\partial \bsL}{\partial x}$ en el caso de una variable.

Para las derivadas segundas de $\bsL$ escribimos, por ejemplo, $\partial_f \partial_{\partial_x f} \bsL$ para la derivada de $\partial_{\partial_x f} \bsL$ respecto del primer argumento. Como $\bsL$ tiene derivadas parciales segundas continuas, por el teorema de Schwarz el orden en que se deriva no importa. Con $t$ fijo, la regla de la cadena da:

$$
\begin{aligned}
&\dfrac{\partial}{\partial x}\Big(\partial_{\partial_x f} \bsL(f, \partial_x f, \partial_t f)(x,t)\Big) \\
&\quad = \partial_f \partial_{\partial_x f} \bsL \cdot \dfrac{\partial f}{\partial x} + \partial_{\partial_x f} \partial_{\partial_x f} \bsL \cdot \dfrac{\partial (\partial_x f)}{\partial x} \\
&\qquad + \partial_{\partial_t f} \partial_{\partial_x f} \bsL \cdot \dfrac{\partial (\partial_t f)}{\partial x} + \partial_x \partial_{\partial_x f} \bsL \cdot \dfrac{\partial x}{\partial x} + \partial_t \partial_{\partial_x f} \bsL \cdot \dfrac{\partial t}{\partial x} \\
&\quad = \partial_f \partial_{\partial_x f} \bsL \cdot \partial_x f(x,t) + \partial_{\partial_x f} \partial_{\partial_x f} \bsL \cdot \partial^2_x f(x,t) \\
&\qquad + \partial_{\partial_t f} \partial_{\partial_x f} \bsL \cdot \partial^2_{xt} f(x,t) + \partial_x \partial_{\partial_x f} \bsL,
\end{aligned}
$$

donde las derivadas segundas de $\bsL$ se evalúan en $(f, \partial_x f, \partial_t f)(x,t)$. Se ha usado que $\dfrac{\partial x}{\partial x} = 1$ y que $\dfrac{\partial t}{\partial x} = 0$, porque $t$ está fijo; por eso desaparece el término con $\partial_t \partial_{\partial_x f} \bsL$. Del mismo modo, con $x$ fijo:

$$
\begin{aligned}
&\dfrac{\partial}{\partial t}\Big(\partial_{\partial_t f} \bsL(f, \partial_x f, \partial_t f)(x,t)\Big) \\
&\quad = \partial_f \partial_{\partial_t f} \bsL \cdot \dfrac{\partial f}{\partial t} + \partial_{\partial_x f} \partial_{\partial_t f} \bsL \cdot \dfrac{\partial (\partial_x f)}{\partial t} \\
&\qquad + \partial_{\partial_t f} \partial_{\partial_t f} \bsL \cdot \dfrac{\partial (\partial_t f)}{\partial t} + \partial_x \partial_{\partial_t f} \bsL \cdot \dfrac{\partial x}{\partial t} + \partial_t \partial_{\partial_t f} \bsL \cdot \dfrac{\partial t}{\partial t} \\
&\quad = \partial_f \partial_{\partial_t f} \bsL \cdot \partial_t f(x,t) + \partial_{\partial_x f} \partial_{\partial_t f} \bsL \cdot \partial^2_{tx} f(x,t) \\
&\qquad + \partial_{\partial_t f} \partial_{\partial_t f} \bsL \cdot \partial^2_t f(x,t) + \partial_t \partial_{\partial_t f} \bsL.
\end{aligned}
$$

Los dos resultados son funciones continuas de $(x,t)$, porque lo son las derivadas segundas de $\bsL$ y las derivadas de $f$ hasta el segundo orden. Esto justifica la integración por partes que viene a continuación.

Para encontrar $f_0$, separamos $\bsdelta\bsS[f_0]$ en tres integrales, por la linealidad de la integral. En ellas, $\partial_{\partial_x f} \bsL$ y $\partial_{\partial_t f} \bsL$ siguen indicando las derivadas respecto del segundo y del tercer argumento de $\bsL$, aunque se evalúen en $f_0$:

$$
\begin{aligned}
&\bsdelta\bsS[f_0] \\
&\quad = \int_{t_1}^{t_2} \int_{x_1}^{x_2} \partial_f \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \cdot h(x,t) \,dx \,dt \\
&\qquad + \int_{t_1}^{t_2} \int_{x_1}^{x_2} \partial_{\partial_x f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \cdot \partial_x h(x,t) \,dx \,dt \\
&\qquad + \int_{t_1}^{t_2} \int_{x_1}^{x_2} \partial_{\partial_t f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \cdot \partial_t h(x,t) \,dx \,dt.
\end{aligned}
$$

**El término con $\partial_x h$.** Para cada $t$ fijo, la integral interior es una integral en $x$ de una sola variable. La integramos por partes con

$$
\begin{aligned}
u(x) := \partial_{\partial_x f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t), \qquad v(x) := h(x,t),
\end{aligned}
$$

que tienen derivada continua (la de $u$, por el excurso aplicado a $f = f_0$):

$$
\begin{aligned}
&\int_{x_1}^{x_2} \partial_{\partial_x f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \cdot \partial_x h(x,t) \,dx \\
&\quad = \Big[\partial_{\partial_x f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \cdot h(x,t)\Big]_{x = x_1}^{x = x_2} \\
&\qquad - \int_{x_1}^{x_2} \dfrac{\partial}{\partial x}\Big(\partial_{\partial_x f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t)\Big) \cdot h(x,t) \,dx.
\end{aligned}
$$

El término de contorno es nulo, porque los puntos $(x_1,t)$ y $(x_2,t)$ están en los lados $x = x_1$ y $x = x_2$ de $\operatorname{Fr}(\Omega)$, donde $h$ se anula: $h(x_1,t) = h(x_2,t) = 0$.

**El término con $\partial_t h$.** Primero intercambiamos el orden de integración, lo que permite el teorema de Fubini porque el integrando es continuo en el rectángulo $\Omega$:

$$
\begin{aligned}
&\int_{t_1}^{t_2} \int_{x_1}^{x_2} \partial_{\partial_t f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \cdot \partial_t h(x,t) \,dx \,dt \\
&\quad = \int_{x_1}^{x_2} \int_{t_1}^{t_2} \partial_{\partial_t f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \cdot \partial_t h(x,t) \,dt \,dx.
\end{aligned}
$$

Para cada $x$ fijo, la integral interior es una integral en $t$, y la integramos por partes igual que antes:

$$
\begin{aligned}
&\int_{t_1}^{t_2} \partial_{\partial_t f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \cdot \partial_t h(x,t) \,dt \\
&\quad = \Big[\partial_{\partial_t f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \cdot h(x,t)\Big]_{t = t_1}^{t = t_2} \\
&\qquad - \int_{t_1}^{t_2} \dfrac{\partial}{\partial t}\Big(\partial_{\partial_t f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t)\Big) \cdot h(x,t) \,dt.
\end{aligned}
$$

El término de contorno vuelve a ser nulo, porque $(x,t_1)$ y $(x,t_2)$ están en los lados $t = t_1$ y $t = t_2$ de la frontera: $h(x,t_1) = h(x,t_2) = 0$. Aquí es donde se usa que $h$ se anula en toda la frontera: los lados $x = x_1$ y $x = x_2$ eliminan el término de contorno en $x$, y los lados $t = t_1$ y $t = t_2$, el término de contorno en $t$.

Sustituyendo, volviendo al orden de integración $dx \,dt$ (otra vez por el teorema de Fubini) y juntando las tres integrales, queda

$$
\begin{aligned}
\bsdelta\bsS[f_0] = \int_{t_1}^{t_2} \int_{x_1}^{x_2} \varphi(x,t) \cdot h(x,t) \,dx \,dt,
\end{aligned}
$$

donde

$$
\begin{aligned}
&\varphi(x,t) := \partial_f \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \\
&\qquad - \dfrac{\partial}{\partial x}\Big(\partial_{\partial_x f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t)\Big) \\
&\qquad - \dfrac{\partial}{\partial t}\Big(\partial_{\partial_t f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t)\Big).
\end{aligned}
$$

Como en el caso de una variable, $\varphi$ ya no contiene a $h$: es una función de $(x,t)$ que solo depende de $f_0$, y es continua, por el excurso. Hemos pasado de una condición con $h$, $\partial_x h$ y $\partial_t h$ a esta otra: $\int_{t_1}^{t_2} \int_{x_1}^{x_2} \varphi(x,t) \cdot h(x,t) \,dx \,dt = 0$ para toda $h$ de clase $C^2(\Omega)$ con $h = 0$ en $\operatorname{Fr}(\Omega)$. Por el lema fundamental del cálculo de variaciones en dos variables, que se demuestra en el documento de anexos, esto obliga a que $\varphi(x,t) = 0$ en todo $\Omega$. Es decir, $f_0$ tiene que cumplir, para todo $(x,t) \in \Omega$:

$$
\begin{aligned}
&\partial_f \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t) \\
&\qquad - \dfrac{\partial}{\partial x}\Big(\partial_{\partial_x f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t)\Big) \\
&\qquad - \dfrac{\partial}{\partial t}\Big(\partial_{\partial_t f} \bsL(f_0, \partial_x f_0, \partial_t f_0)(x,t)\Big) = 0.
\end{aligned}
$$

Es la ecuación de Euler–Lagrange en dos variables. El recíproco también es cierto, por el mismo argumento que en el caso de una variable: el cálculo que lleva de $\bsdelta\bsS[f_0]$ a $\int_{t_1}^{t_2} \int_{x_1}^{x_2} \varphi(x,t) \cdot h(x,t) \,dx \,dt$ vale para cualquier función del conjunto de partida, así que, si $f_0$ cumple la ecuación, entonces $\varphi = 0$ y $\bsdelta\bsS[f_0] = 0$ para toda $h$ admisible. Por tanto, dentro del conjunto de partida, $f_0$ hace estacionario a $\bsS$ si y solo si cumple la ecuación de Euler–Lagrange.

Desarrollando las dos derivadas con el excurso y agrupando, la ecuación de Euler–Lagrange es una ecuación en derivadas parciales de segundo orden para $f_0$:

$$
\begin{aligned}
&\partial_{\partial_x f} \partial_{\partial_x f} \bsL \cdot \partial^2_x f_0 + 2 \cdot \partial_{\partial_x f} \partial_{\partial_t f} \bsL \cdot \partial^2_{xt} f_0 + \partial_{\partial_t f} \partial_{\partial_t f} \bsL \cdot \partial^2_t f_0 \\
&\quad + \partial_f \partial_{\partial_x f} \bsL \cdot \partial_x f_0 + \partial_f \partial_{\partial_t f} \bsL \cdot \partial_t f_0 \\
&\quad + \partial_x \partial_{\partial_x f} \bsL + \partial_t \partial_{\partial_t f} \bsL - \partial_f \bsL = 0,
\end{aligned}
$$

con las derivadas de $\bsL$ evaluadas en $(f_0, \partial_x f_0, \partial_t f_0)(x,t)$ y las de $f_0$ en $(x,t)$. Los dos términos cruzados, $\partial_{\partial_t f} \partial_{\partial_x f} \bsL \cdot \partial^2_{xt} f_0$ (del primer excurso) y $\partial_{\partial_x f} \partial_{\partial_t f} \bsL \cdot \partial^2_{tx} f_0$ (del segundo), son iguales por el teorema de Schwarz, aplicado a $\bsL$ y a $f_0$; por eso aparece el factor $2$.

Las condiciones de contorno son los valores de $f_0$ en $\operatorname{Fr}(\Omega)$, que son los que comparten todas las funciones del conjunto de partida. Como en el caso de una variable, según cuál sea $\bsL$, el problema puede tener una solución, ninguna o infinitas. Cuando $t$ es el tiempo, en física no se suele plantear así: se dan la configuración y la velocidad iniciales, $f_0(x,t_1)$ y $\partial_t f_0(x,t_1)$, junto con las condiciones en los lados $x = x_1$ y $x = x_2$. Las condiciones en $t_1$ y en $t_2$ sirven para deducir la ecuación; después, la ecuación se resuelve con las condiciones iniciales.

## Generalización a funciones vectoriales de varias variables

En los apartados anteriores, la función buscada era escalar y dependía de una o de dos variables. Ahora buscamos una función vectorial de un vector de variables. Los pasos son los mismos que en el caso de dos variables. Las novedades son tres: las sumas sobre índices, la separación de las componentes de la función y que la ecuación de Euler–Lagrange pasa a ser un sistema de ecuaciones acopladas.

### Planteamiento y notación

Las variables forman un vector $\vec{x} = (x_1, \dots, x_m)$ de $\mathbb{R}^m$, sin distinguir ninguna, y el dominio es la caja

$$
\begin{aligned}
\Omega := [a_1, b_1] \times \dots \times [a_m, b_m] \subset \mathbb{R}^m.
\end{aligned}
$$

Así redefinimos $\Omega$, que en el apartado de dos variables era el rectángulo $[x_1, x_2] \times [t_1, t_2]$. Atención: aquí $x_1$ y $x_2$ son las dos primeras componentes de $\vec{x}$, no los extremos de un intervalo. La frontera $\operatorname{Fr}(\Omega)$ está formada por las caras $x_k = a_k$ y $x_k = b_k$, para $k = 1, \dots, m$.

Las funciones del conjunto de partida son funciones vectoriales $\vec{f} := (f_1, \dots, f_n): \Omega \to \mathbb{R}^n$ de clase $C^2(\Omega)$, es decir, con todas sus componentes de clase $C^2(\Omega)$. Todas toman los mismos valores en la frontera: si $\vec{f}$ y $\vec{g}$ son dos funciones del conjunto, $\vec{f}(\vec{x}) = \vec{g}(\vec{x})$ para todo $\vec{x} \in \operatorname{Fr}(\Omega)$.

Usaremos los índices $i, j = 1, \dots, n$ para las componentes de $\vec{f}$, y $k, l = 1, \dots, m$ para las variables. Las derivadas parciales de las componentes se escriben

$$
\begin{aligned}
\partial_{x_k} f_i := \dfrac{\partial f_i}{\partial x_k}, \qquad \partial^2_{x_k x_l} f_i := \dfrac{\partial^2 f_i}{\partial x_k \partial x_l},
\end{aligned}
$$

y, por el teorema de Schwarz, $\partial^2_{x_k x_l} f_i = \partial^2_{x_l x_k} f_i$. Las $n \cdot m$ derivadas primeras forman la matriz jacobiana de $\vec{f}$, de $n$ filas y $m$ columnas:

$$
\begin{aligned}
J_{\vec{f}} := \begin{pmatrix} \partial_{x_1} f_1 & \cdots & \partial_{x_m} f_1 \\ \vdots & & \vdots \\ \partial_{x_1} f_n & \cdots & \partial_{x_m} f_n \end{pmatrix}.
\end{aligned}
$$

Ahora $\bsL$ es una función de $n + n \cdot m + m$ variables reales: las $n$ componentes de $\vec{f}$, las $n \cdot m$ entradas del jacobiano y las $m$ variables. La escribimos $\bsL(\vec{f}, J_{\vec{f}}, \vec{x})$ y le exigimos derivadas parciales segundas continuas. Como en el apartado de dos variables, cuando $\bsL$ se evalúa a lo largo de una función $\vec{f}$ escribimos

$$
\begin{aligned}
\bsL(\vec{f}, J_{\vec{f}})(\vec{x}) := \bsL\big(\vec{f}(\vec{x}), J_{\vec{f}}(\vec{x}), \vec{x}\big),
\end{aligned}
$$

y lo mismo con sus derivadas parciales. Estas se nombran por el argumento respecto del que se deriva: $\partial_{f_i} \bsL$ es la derivada respecto del argumento $f_i$; $\partial_{\partial_{x_k} f_i} \bsL$, la derivada respecto del argumento que ocupa la entrada $(i,k)$ del jacobiano; y $\partial_{x_k} \bsL$, la derivada respecto de la variable explícita $x_k$. Para las derivadas segundas escribimos, por ejemplo, $\partial_{f_j} \partial_{\partial_{x_k} f_i} \bsL$; como son continuas, por el teorema de Schwarz el orden en que se deriva no importa.

El funcional es una integral múltiple sobre la caja $\Omega$:

$$
\begin{aligned}
\bsS[\vec{f}] := \int_\Omega \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) \,dx_1 \cdots dx_m.
\end{aligned}
$$

Como el integrando es continuo, por el teorema de Fubini la integral puede calcularse como $m$ integrales iteradas, en cualquier orden.

### La variación primera

Para variar $\vec{f}$ tomamos una función auxiliar $\vec{h} := (h_1, \dots, h_n): \Omega \to \mathbb{R}^n$ de clase $C^2(\Omega)$ que se anula en la frontera: $\vec{h}(\vec{x}) = \vec{0}$ para todo $\vec{x} \in \operatorname{Fr}(\Omega)$. Así, $\vec{f} + \epsilon \cdot \vec{h}$ sigue en el conjunto de partida, y su jacobiano es $J_{\vec{f}} + \epsilon \cdot J_{\vec{h}}$. El desarrollo de Taylor de $\bsL$ en sus $n + n \cdot m$ primeros argumentos, con $\vec{x}$ fijo, da para la diferencia completa:

$$
\begin{aligned}
&(\delta_{\vec{f}} \bsL)(\vec{f}, J_{\vec{f}})(\vec{x}) \\
&\quad := \bsL(\vec{f} + \epsilon \cdot \vec{h}, J_{\vec{f}} + \epsilon \cdot J_{\vec{h}})(\vec{x}) - \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) \\
&\quad = \epsilon \cdot \sum_{i=1}^{n} \bigg( \partial_{f_i} \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) \cdot h_i(\vec{x}) \\
&\qquad + \sum_{k=1}^{m} \partial_{\partial_{x_k} f_i} \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) \cdot \partial_{x_k} h_i(\vec{x}) \bigg) + O(\epsilon^2).
\end{aligned}
$$

Como en los apartados anteriores, la variación primera de $\bsL$ es la parte de primer orden de esa diferencia, dividida por $\epsilon$:

$$
\begin{aligned}
\bsdelta_{\vec{f}} \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) := \lim_{\epsilon \to 0} \dfrac{(\delta_{\vec{f}} \bsL)(\vec{f}, J_{\vec{f}})(\vec{x})}{\epsilon} = \sum_{i=1}^{n} \bigg( \partial_{f_i} \bsL \cdot h_i + \sum_{k=1}^{m} \partial_{\partial_{x_k} f_i} \bsL \cdot \partial_{x_k} h_i \bigg),
\end{aligned}
$$

con las derivadas de $\bsL$ evaluadas en $(\vec{f}, J_{\vec{f}})(\vec{x})$ y las de $\vec{h}$, en $\vec{x}$. La variación primera de $\bsS$ se define igual que en los casos anteriores:

$$
\begin{aligned}
\bsdelta\bsS[\vec{f}] := \lim_{\epsilon \to 0} \dfrac{\bsS[\vec{f} + \epsilon \cdot \vec{h}] - \bsS[\vec{f}]}{\epsilon}.
\end{aligned}
$$

El límite puede entrar en la integral por el mismo argumento que en el caso de una variable. Las derivadas segundas de $\bsL$ son continuas y se evalúan en un conjunto cerrado y acotado, porque $\Omega$ lo es y las funciones $\vec{f}$, $J_{\vec{f}}$, $\vec{h}$ y $J_{\vec{h}}$ son continuas en $\Omega$. Por eso existe una constante $C$, que no depende de $\vec{x}$, tal que el resto del desarrollo de Taylor cumple $|R(\vec{x}, \epsilon)| \leq C \cdot \epsilon^2$ para $|\epsilon| \leq 1$. Al dividir por $\epsilon$ e integrar, la diferencia entre el cociente que define $\bsdelta\bsS[\vec{f}]$ y la integral de $\bsdelta_{\vec{f}} \bsL$ queda acotada, en valor absoluto, por $\operatorname{vol}(\Omega) \cdot C \cdot |\epsilon|$, donde $\operatorname{vol}(\Omega) := (b_1 - a_1) \cdots (b_m - a_m)$, y tiende a $0$ con $\epsilon$. Por tanto:

$$
\begin{aligned}
\bsdelta\bsS[\vec{f}] &= \int_\Omega \bsdelta_{\vec{f}} \bsL(\vec{f}, J_{\vec{f}})(\vec{x}) \,dx_1 \cdots dx_m \\
&= \int_\Omega \sum_{i=1}^{n} \bigg( \partial_{f_i} \bsL \cdot h_i + \sum_{k=1}^{m} \partial_{\partial_{x_k} f_i} \bsL \cdot \partial_{x_k} h_i \bigg) \,dx_1 \cdots dx_m.
\end{aligned}
$$

Ahora lo que queremos es resolver $\bsdelta\bsS[\vec{f}] = 0$: buscamos una función $\vec{f}_0 = (f_{0,1}, \dots, f_{0,n})$ del conjunto de partida tal que $\bsdelta\bsS[\vec{f}_0] = 0$ para toda $\vec{h}$ de clase $C^2(\Omega)$ que se anule en $\operatorname{Fr}(\Omega)$.

### Un excurso: la regla de la cadena en varias variables

Al integrar por partes el término con $\partial_{x_k} h_i$ aparecerá la derivada respecto de $x_k$, con las demás variables fijas, de la función compuesta $\vec{x} \mapsto \partial_{\partial_{x_k} f_i} \bsL(\vec{f}, J_{\vec{f}})(\vec{x})$. Como en el apartado de dos variables, no hay que confundirla con la derivada parcial explícita $\partial_{x_k} \bsL$. Al cambiar $x_k$ cambian todos los argumentos de $\bsL$:

* cada componente $f_j(\vec{x})$, con derivada $\partial_{x_k} f_j(\vec{x})$;
* cada entrada $\partial_{x_l} f_j(\vec{x})$ del jacobiano, con derivada $\partial^2_{x_k x_l} f_j(\vec{x})$;
* la variable explícita $x_k$, con $\dfrac{\partial x_k}{\partial x_k} = 1$; las demás variables explícitas no cambian, porque $\dfrac{\partial x_l}{\partial x_k} = 0$ si $l \neq k$.

Para cada $i$ y cada $k$ fijos (aquí no se suma en $k$), la regla de la cadena da:

$$
\begin{aligned}
&\dfrac{\partial}{\partial x_k}\Big(\partial_{\partial_{x_k} f_i} \bsL(\vec{f}, J_{\vec{f}})(\vec{x})\Big) \\
&\quad = \sum_{j=1}^{n} \partial_{f_j} \partial_{\partial_{x_k} f_i} \bsL \cdot \partial_{x_k} f_j(\vec{x}) \\
&\qquad + \sum_{j=1}^{n} \sum_{l=1}^{m} \partial_{\partial_{x_l} f_j} \partial_{\partial_{x_k} f_i} \bsL \cdot \partial^2_{x_k x_l} f_j(\vec{x}) \\
&\qquad + \partial_{x_k} \partial_{\partial_{x_k} f_i} \bsL,
\end{aligned}
$$

donde las derivadas segundas de $\bsL$ se evalúan en $(\vec{f}, J_{\vec{f}})(\vec{x})$. El resultado es una función continua de $\vec{x}$, porque lo son las derivadas segundas de $\bsL$ y las derivadas de $\vec{f}$ hasta el segundo orden. Esto justifica la integración por partes que viene a continuación.

### La integración por partes en varias variables

Por la linealidad de la integral, $\bsdelta\bsS[\vec{f}_0]$ es la suma de las integrales de cada término. Fijemos $i$ y $k$, y llamemos

$$
\begin{aligned}
u_{ik}(\vec{x}) := \partial_{\partial_{x_k} f_i} \bsL(\vec{f}_0, J_{\vec{f}_0})(\vec{x}),
\end{aligned}
$$

que tiene derivada continua respecto de $x_k$, por el excurso aplicado a $\vec{f} = \vec{f}_0$. Por el teorema de Fubini, la integral del término con $\partial_{x_k} h_i$ puede calcularse integrando primero en $x_k$, con las demás variables fijas:

$$
\begin{aligned}
\int_\Omega u_{ik} \cdot \partial_{x_k} h_i \,dx_1 \cdots dx_m = \int_{\Omega_k} \left( \int_{a_k}^{b_k} u_{ik} \cdot \partial_{x_k} h_i \,dx_k \right) d\hat{x}_k,
\end{aligned}
$$

donde $\Omega_k$ es la caja formada por los intervalos de las otras $m - 1$ variables y $d\hat{x}_k$ indica el producto de sus diferenciales. La integral interior es una integral de una sola variable, y la integramos por partes:

$$
\begin{aligned}
\int_{a_k}^{b_k} u_{ik} \cdot \partial_{x_k} h_i \,dx_k = \Big[u_{ik} \cdot h_i\Big]_{x_k = a_k}^{x_k = b_k} - \int_{a_k}^{b_k} \dfrac{\partial u_{ik}}{\partial x_k} \cdot h_i \,dx_k.
\end{aligned}
$$

El término de contorno es nulo, porque los puntos con $x_k = a_k$ o $x_k = b_k$ están en la frontera, donde $h_i$ se anula. Aquí se usa que $\vec{h}$ se anula en toda la frontera: las caras $x_k = a_k$ y $x_k = b_k$ eliminan el término de contorno de la variable $x_k$.

Haciendo lo mismo para todos los $i$ y $k$, volviendo a escribir las integrales sobre $\Omega$ y juntando los términos de cada $h_i$, queda

$$
\begin{aligned}
\bsdelta\bsS[\vec{f}_0] = \int_\Omega \sum_{i=1}^{n} \varphi_i(\vec{x}) \cdot h_i(\vec{x}) \,dx_1 \cdots dx_m,
\end{aligned}
$$

donde, para cada $i$,

$$
\begin{aligned}
\varphi_i(\vec{x}) := \partial_{f_i} \bsL(\vec{f}_0, J_{\vec{f}_0})(\vec{x}) &- \sum_{k=1}^{m} \dfrac{\partial}{\partial x_k}\Big(\partial_{\partial_{x_k} f_i} \bsL(\vec{f}_0, J_{\vec{f}_0})(\vec{x})\Big).
\end{aligned}
$$

Cada $\varphi_i$ es continua, por el excurso, y no depende de $\vec{h}$.

### La separación de las componentes

La novedad respecto de los casos anteriores es que hay $n$ funciones $h_i$ y $n$ funciones $\varphi_i$. La condición $\bsdelta\bsS[\vec{f}_0] = 0$ vale para toda $\vec{h}$ admisible; en particular, para las que solo tienen una componente distinta de cero. Fijado $i$, tomamos $\vec{h} = (0, \dots, 0, h, 0, \dots, 0)$, con $h$ en la posición $i$, donde $h: \Omega \to \mathbb{R}$ es de clase $C^2(\Omega)$ y se anula en $\operatorname{Fr}(\Omega)$. La suma se reduce entonces a un solo término:

$$
\begin{aligned}
\int_\Omega \varphi_i(\vec{x}) \cdot h(\vec{x}) \,dx_1 \cdots dx_m = 0 \quad \text{para toda } h \text{ admisible}.
\end{aligned}
$$

Por el lema fundamental del cálculo de variaciones en $m$ variables, que se demuestra en el documento de anexos, $\varphi_i = 0$ en todo $\Omega$. Como $i$ es cualquiera, $\vec{f}_0$ tiene que cumplir, para todo $\vec{x} \in \Omega$, las $n$ ecuaciones

$$
\begin{aligned}
\partial_{f_i} \bsL(\vec{f}_0, J_{\vec{f}_0})(\vec{x}) &- \sum_{k=1}^{m} \dfrac{\partial}{\partial x_k}\Big(\partial_{\partial_{x_k} f_i} \bsL(\vec{f}_0, J_{\vec{f}_0})(\vec{x})\Big) = 0, \qquad i = 1, \dots, n.
\end{aligned}
$$

Son las ecuaciones de Euler–Lagrange de una función vectorial de varias variables: una por cada componente de $\vec{f}$. El recíproco también es cierto, por el mismo argumento que en los casos anteriores: el cálculo que lleva de $\bsdelta\bsS[\vec{f}_0]$ a $\int_\Omega \sum_i \varphi_i \cdot h_i \,dx_1 \cdots dx_m$ vale para cualquier función del conjunto de partida, así que, si $\vec{f}_0$ cumple las $n$ ecuaciones, todas las $\varphi_i$ son nulas y $\bsdelta\bsS[\vec{f}_0] = 0$ para toda $\vec{h}$ admisible. Por tanto, dentro del conjunto de partida, $\vec{f}_0$ hace estacionario a $\bsS$ si y solo si cumple las $n$ ecuaciones de Euler–Lagrange.

### La forma desarrollada: un sistema acoplado

Desarrollando las derivadas con el excurso y sumando en $k$, la ecuación $i$ queda:

$$
\begin{aligned}
&\sum_{j=1}^{n} \sum_{k,l=1}^{m} \partial_{\partial_{x_l} f_j} \partial_{\partial_{x_k} f_i} \bsL \cdot \partial^2_{x_k x_l} f_{0,j} \\
&\quad + \sum_{j=1}^{n} \sum_{k=1}^{m} \partial_{f_j} \partial_{\partial_{x_k} f_i} \bsL \cdot \partial_{x_k} f_{0,j} \\
&\quad + \sum_{k=1}^{m} \partial_{x_k} \partial_{\partial_{x_k} f_i} \bsL - \partial_{f_i} \bsL = 0,
\end{aligned}
$$

con las derivadas de $\bsL$ evaluadas en $(\vec{f}_0, J_{\vec{f}_0})(\vec{x})$ y las de $\vec{f}_0$, en $\vec{x}$. En la ecuación $i$ aparecen las derivadas segundas de todas las componentes $f_{0,j}$, no solo las de $f_{0,i}$: es un sistema de $n$ ecuaciones en derivadas parciales de segundo orden, acopladas. Sus coeficientes son las derivadas segundas de $\bsL$ respecto de las entradas del jacobiano, $\partial_{\partial_{x_l} f_j} \partial_{\partial_{x_k} f_i} \bsL$.

### Cuando una de las variables es el tiempo

Cuando las variables son el tiempo y $m$ coordenadas espaciales, se llama $x_0 := t$, el vector $\vec{x} = (x_1, \dots, x_m)$ reúne solo las coordenadas espaciales y el dominio pasa a ser $[t_1, t_2] \times \Omega$, que es otra caja, ahora de $m + 1$ dimensiones. Su frontera está formada por las caras $t = t_1$ y $t = t_2$, donde se fija la configuración inicial y la final, y por $[t_1, t_2] \times \operatorname{Fr}(\Omega)$, donde se fijan los valores en el borde espacial en todo instante. Los índices $\mu, \nu = 0, \dots, m$ recorren todas las variables, con $\partial_{x_0} = \partial_t$. Todo lo anterior vale igual, con $\sum_{\mu=0}^{m}$ en lugar de $\sum_{k=1}^{m}$:

$$
\begin{aligned}
\partial_{f_i} \bsL - \sum_{\mu=0}^{m} \dfrac{\partial}{\partial x_\mu}\Big(\partial_{\partial_{x_\mu} f_i} \bsL\Big) = 0, \qquad i = 1, \dots, n.
\end{aligned}
$$

Separando el término de $t$:

$$
\begin{aligned}
\partial_{f_i} \bsL - \dfrac{\partial}{\partial t}\Big(\partial_{\partial_t f_i} \bsL\Big) - \sum_{k=1}^{m} \dfrac{\partial}{\partial x_k}\Big(\partial_{\partial_{x_k} f_i} \bsL\Big) = 0, \qquad i = 1, \dots, n,
\end{aligned}
$$

con $\bsL$ y sus derivadas evaluadas en $(\vec{f}_0, J_{\vec{f}_0})(t, \vec{x})$, donde ahora el jacobiano incluye la columna de las derivadas $\partial_t f_{0,i}$.

### Casos particulares

Con $m = 1$ hay una sola variable. Escribimos $[a, b] := [a_1, b_1]$, $x := x_1$ y $f'_i := \partial_{x_1} f_i$, y la derivada de la función compuesta respecto de $x$ es la derivada total $\dfrac{d}{dx}$. Las fórmulas generales contienen las de los apartados anteriores:

| Caso | Ecuación de Euler–Lagrange | Dónde está |
| --- | --- | --- |
| $n = 1$, $m = 1$ | $\partial_f \bsL - \dfrac{d}{dx}\left(\partial_{f'} \bsL\right) = 0$ | primer apartado |
| $n = 1$, $m = 2$, con $(x_1, x_2) = (x, t)$ | la de dos variables, con el factor $2$ de los términos cruzados | apartado de dos variables |
| $n$ cualquiera, $m = 1$ | $\partial_{f_i} \bsL - \dfrac{d}{dx}\left(\partial_{f'_i} \bsL\right) = 0$, con $i = 1, \dots, n$ | nuevo: curvas en $\mathbb{R}^n$ |

En el caso $n = 1$, $m = 2$, la suma doble $\sum_{k,l}$ de la forma desarrollada contiene los dos términos cruzados, $(k,l) = (1,2)$ y $(k,l) = (2,1)$, que son iguales por el teorema de Schwarz; de ahí el factor $2$.

En el último caso, $\vec{f}$ describe una curva en $\mathbb{R}^n$, y la forma desarrollada es

$$
\begin{aligned}
\sum_{j=1}^{n} W_{ij} \cdot f''_{0,j} + \sum_{j=1}^{n} \partial_{f_j} \partial_{f'_i} \bsL \cdot f'_{0,j} + \partial_x \partial_{f'_i} \bsL - \partial_{f_i} \bsL = 0, \qquad W_{ij} := \partial_{f'_j} \partial_{f'_i} \bsL.
\end{aligned}
$$

La matriz $W$, de $n$ filas y $n$ columnas, es simétrica por el teorema de Schwarz. Si es invertible en cada punto, el sistema puede resolverse para las derivadas segundas $f''_{0,j}$, y se obtiene un sistema de ecuaciones diferenciales ordinarias de la forma $\vec{f}''_0 = \dots$. Si no lo es, las ecuaciones no determinan todas las derivadas segundas. Esta condición reaparecerá al construir el hamiltoniano con la transformada de Legendre (Tema 1, apartados 5 y 6).
