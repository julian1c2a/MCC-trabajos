---
author: "Julián Calderón Almendros"
---

# El formalismo lagrangiano: anexos

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-03
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

Resultados matemáticos auxiliares de la serie: el lema fundamental del cálculo de variaciones, que usa la parte matemática, y dos resultados que usa la parte física: que sumar una derivada total o cambiar de coordenadas no altera las ecuaciones de Euler–Lagrange, y la forma más general del potencial en $\bsL = T - V$.

## Lema fundamental del cálculo de variaciones

**Lema.** Sea $\varphi: [a,b] \to \mathbb{R}$ una función continua tal que

$$
\begin{aligned}
\int_a^b \varphi(x) \cdot h(x) \,dx = 0
\end{aligned}
$$

para toda función $h: [a,b] \to \mathbb{R}$ dos veces derivable con continuidad con $h(a) = h(b) = 0$. Entonces $\varphi(x) = 0$ para todo $x \in [a,b]$.

**Demostración.** Por reducción al absurdo. Supongamos que existe un punto $x_0 \in (a,b)$ con $\varphi(x_0) \neq 0$. Podemos suponer que $\varphi(x_0) > 0$: si fuera negativo, el mismo razonamiento se aplica a $-\varphi$, que cumple la misma hipótesis.

1. **Un intervalo donde $\varphi$ es positiva.** Como $\varphi$ es continua en $x_0$, existe $\eta > 0$ tal que $\varphi(x) > \dfrac{\varphi(x_0)}{2} > 0$ siempre que $|x - x_0| < \eta$. Elegimos $\alpha$ y $\beta$ con $\max(a, x_0 - \eta) < \alpha < x_0 < \beta < \min(b, x_0 + \eta)$. Así, $[\alpha, \beta] \subset (a,b)$ y $\varphi(x) > 0$ en todo $[\alpha, \beta]$.

2. **Una función $h$ que solo es distinta de cero en $(\alpha, \beta)$.** Definimos

   $$
   \begin{aligned}
   h(x) := \begin{cases} (x - \alpha)^3 \cdot (\beta - x)^3 & \text{si } \alpha \leq x \leq \beta, \\ 0 & \text{en otro caso.} \end{cases}
   \end{aligned}
   $$

3. **$h$ es admisible.** Como $a < \alpha$ y $\beta < b$, se cumple $h(a) = h(b) = 0$. Falta ver que $h$ es dos veces derivable con continuidad. Dentro de $(\alpha, \beta)$, $h$ es un polinomio, y fuera de $[\alpha, \beta]$ es la función nula, así que solo hay que comprobar los puntos $\alpha$ y $\beta$. A la derecha de $\alpha$ escribimos $h(x) = (x - \alpha)^3 \cdot p(x)$, con $p(x) := (\beta - x)^3$, y derivamos:

   $$
   \begin{aligned}
   h'(x) &= 3 \cdot (x - \alpha)^2 \cdot p(x) + (x - \alpha)^3 \cdot p'(x), \\
   h''(x) &= 6 \cdot (x - \alpha) \cdot p(x) + 6 \cdot (x - \alpha)^2 \cdot p'(x) + (x - \alpha)^3 \cdot p''(x).
   \end{aligned}
   $$

   A la izquierda de $\alpha$, $h$, $h'$ y $h''$ son nulas. Por la derecha, los cocientes $\dfrac{h(x) - h(\alpha)}{x - \alpha} = (x - \alpha)^2 \cdot p(x)$ y $\dfrac{h'(x) - 0}{x - \alpha} = 3 \cdot (x - \alpha) \cdot p(x) + (x - \alpha)^2 \cdot p'(x)$ tienden a $0$, así que $h'(\alpha) = 0$ y $h''(\alpha) = 0$. Además, $h''(x) \to 0$ cuando $x \to \alpha$ por la derecha, porque cada término contiene el factor $(x - \alpha)$. Por tanto, $h''$ es continua en $\alpha$. En $\beta$ se razona igual, con el factor $(\beta - x)^3$ y $q(x) := (x - \alpha)^3$. Por eso el exponente es $3$: con exponente $2$, $h''$ saltaría en $\alpha$ de $0$ a $2 \cdot (\beta - \alpha)^3$.

4. **La contradicción.** En $(\alpha, \beta)$ son positivas tanto $\varphi$ como $h$, porque $x - \alpha > 0$ y $\beta - x > 0$. Fuera de $[\alpha, \beta]$, $h = 0$. Por tanto,

   $$
   \begin{aligned}
   \int_a^b \varphi(x) \cdot h(x) \,dx = \int_\alpha^\beta \varphi(x) \cdot h(x) \,dx > 0,
   \end{aligned}
   $$

   porque es la integral de una función continua y positiva en $(\alpha, \beta)$. Esto contradice la hipótesis, así que $\varphi(x_0) = 0$ para todo $x_0 \in (a,b)$.

5. **Los extremos.** Por la continuidad de $\varphi$, $\varphi(a) = \lim_{x \to a^+} \varphi(x) = 0$ y $\varphi(b) = \lim_{x \to b^-} \varphi(x) = 0$. $\blacksquare$

### El lema en dos variables

**Lema.** Sea $\varphi: \Omega \to \mathbb{R}$ una función continua en el rectángulo $\Omega = [x_1,x_2] \times [t_1,t_2]$ tal que

$$
\begin{aligned}
\int_{t_1}^{t_2} \int_{x_1}^{x_2} \varphi(x,t) \cdot h(x,t) \,dx \,dt = 0
\end{aligned}
$$

para toda función $h: \Omega \to \mathbb{R}$ de clase $C^2(\Omega)$ con $h = 0$ en $\operatorname{Fr}(\Omega)$. Entonces $\varphi(x,t) = 0$ para todo $(x,t) \in \Omega$.

**Demostración.** Es la misma idea que en una variable, con una «joroba» en un rectángulo pequeño. Supongamos que existe un punto $(x_0, t_0)$ del interior de $\Omega$, es decir, con $x_1 < x_0 < x_2$ y $t_1 < t_0 < t_2$, tal que $\varphi(x_0, t_0) \neq 0$. Como antes, podemos suponer que $\varphi(x_0, t_0) > 0$; si fuera negativo, el razonamiento se aplica a $-\varphi$.

1. **Un rectángulo donde $\varphi$ es positiva.** Como $\varphi$ es continua en $(x_0, t_0)$, existe $\eta > 0$ tal que $\varphi(x,t) > \dfrac{\varphi(x_0,t_0)}{2} > 0$ siempre que $|x - x_0| < \eta$ y $|t - t_0| < \eta$. Elegimos $\alpha_x$, $\beta_x$, $\alpha_t$ y $\beta_t$ con $\max(x_1, x_0 - \eta) < \alpha_x < x_0 < \beta_x < \min(x_2, x_0 + \eta)$ y $\max(t_1, t_0 - \eta) < \alpha_t < t_0 < \beta_t < \min(t_2, t_0 + \eta)$. Así, el rectángulo $[\alpha_x, \beta_x] \times [\alpha_t, \beta_t]$ está en el interior de $\Omega$, y en él $\varphi > 0$.

2. **La joroba.** Sean $\psi_1$ y $\psi_2$ las funciones del paso 2 del caso de una variable, construidas con los intervalos $[\alpha_x, \beta_x]$ y $[\alpha_t, \beta_t]$:

   $$
   \begin{aligned}
   \psi_1(x) &:= \begin{cases} (x - \alpha_x)^3 \cdot (\beta_x - x)^3 & \text{si } \alpha_x \leq x \leq \beta_x, \\ 0 & \text{en otro caso,} \end{cases} \\
   \psi_2(t) &:= \begin{cases} (t - \alpha_t)^3 \cdot (\beta_t - t)^3 & \text{si } \alpha_t \leq t \leq \beta_t, \\ 0 & \text{en otro caso.} \end{cases}
   \end{aligned}
   $$

   Definimos $h(x,t) := \psi_1(x) \cdot \psi_2(t)$.

3. **$h$ es admisible.** Por el paso 3 del caso de una variable, $\psi_1$ y $\psi_2$ son dos veces derivables con continuidad. Las derivadas parciales de $h$ hasta el segundo orden son productos de derivadas de $\psi_1$ y de $\psi_2$ hasta el segundo orden; por ejemplo, $\partial^2_{xt} h(x,t) = \psi_1'(x) \cdot \psi_2'(t)$ y $\partial^2_x h(x,t) = \psi_1''(x) \cdot \psi_2(t)$. Por tanto, existen y son continuas, y $h$ es de clase $C^2(\Omega)$. Además, $h$ se anula fuera del rectángulo $[\alpha_x, \beta_x] \times [\alpha_t, \beta_t]$, que está en el interior de $\Omega$; en particular, $h = 0$ en $\operatorname{Fr}(\Omega)$.

4. **La contradicción.** En el interior del rectángulo pequeño son positivas tanto $\varphi$ como $h$, y fuera de él $h = 0$. Por tanto,

   $$
   \begin{aligned}
   \int_{t_1}^{t_2} \int_{x_1}^{x_2} \varphi(x,t) \cdot h(x,t) \,dx \,dt = \int_{\alpha_t}^{\beta_t} \int_{\alpha_x}^{\beta_x} \varphi(x,t) \cdot h(x,t) \,dx \,dt > 0,
   \end{aligned}
   $$

   porque es la integral de una función continua y positiva en el interior del rectángulo pequeño. Esto contradice la hipótesis, así que $\varphi = 0$ en todo el interior de $\Omega$.

5. **La frontera.** Todo punto de $\operatorname{Fr}(\Omega)$ es límite de puntos del interior de $\Omega$. Como $\varphi$ es continua, también se anula en $\operatorname{Fr}(\Omega)$. $\blacksquare$

### El lema en $m$ variables

**Lema.** Sea $\varphi: \Omega \to \mathbb{R}$ una función continua en la caja $\Omega = [a_1, b_1] \times \dots \times [a_m, b_m]$ tal que

$$
\begin{aligned}
\int_\Omega \varphi(\vec{x}) \cdot h(\vec{x}) \,dx_1 \cdots dx_m = 0
\end{aligned}
$$

para toda función $h: \Omega \to \mathbb{R}$ de clase $C^2(\Omega)$ con $h = 0$ en $\operatorname{Fr}(\Omega)$. Entonces $\varphi(\vec{x}) = 0$ para todo $\vec{x} \in \Omega$.

**Demostración.** Es la del caso de dos variables, con $m$ factores en lugar de dos. Supongamos que existe un punto $\vec{c} = (c_1, \dots, c_m)$ del interior de $\Omega$, es decir, con $a_k < c_k < b_k$ para todo $k$, tal que $\varphi(\vec{c}) > 0$; si fuera negativo, el razonamiento se aplica a $-\varphi$.

1. **Una caja donde $\varphi$ es positiva.** Como $\varphi$ es continua en $\vec{c}$, existe $\eta > 0$ tal que $\varphi(\vec{x}) > \dfrac{\varphi(\vec{c})}{2} > 0$ siempre que $|x_k - c_k| < \eta$ para todo $k$. Elegimos, para cada $k$, $\alpha_k$ y $\beta_k$ con $\max(a_k, c_k - \eta) < \alpha_k < c_k < \beta_k < \min(b_k, c_k + \eta)$. Así, la caja $[\alpha_1, \beta_1] \times \dots \times [\alpha_m, \beta_m]$ está en el interior de $\Omega$, y en ella $\varphi > 0$.

2. **La joroba.** Sea $\psi_k$ la función del paso 2 del caso de una variable construida con el intervalo $[\alpha_k, \beta_k]$, y definimos

   $$
   \begin{aligned}
   h(\vec{x}) := \psi_1(x_1) \cdot \psi_2(x_2) \cdots \psi_m(x_m).
   \end{aligned}
   $$

3. **$h$ es admisible.** Por el paso 3 del caso de una variable, cada $\psi_k$ es dos veces derivable con continuidad. Cada derivada parcial de $h$ hasta el segundo orden es un producto de $m$ factores, en el que uno o dos de ellos están derivados; por ejemplo, $\partial^2_{x_k x_l} h(\vec{x}) = \psi_k'(x_k) \cdot \psi_l'(x_l) \cdot \prod_{r \neq k, l} \psi_r(x_r)$ si $k \neq l$. Por tanto, existen y son continuas, y $h$ es de clase $C^2(\Omega)$. Además, $h$ se anula fuera de la caja pequeña, que está en el interior de $\Omega$; en particular, $h = 0$ en $\operatorname{Fr}(\Omega)$.

4. **La contradicción.** En el interior de la caja pequeña son positivas tanto $\varphi$ como $h$, y fuera de ella $h = 0$. La integral de $\varphi \cdot h$ sobre $\Omega$ es, por tanto, la integral de una función continua, no negativa y positiva en el interior de la caja pequeña, y es positiva. Esto contradice la hipótesis, así que $\varphi = 0$ en todo el interior de $\Omega$.

5. **La frontera.** Todo punto de $\operatorname{Fr}(\Omega)$ es límite de puntos del interior de $\Omega$. Como $\varphi$ es continua, también se anula en $\operatorname{Fr}(\Omega)$. $\blacksquare$

## Requisito matemático previo: derivadas totales y cambios de coordenadas

Dos resultados sobre las ecuaciones de Euler–Lagrange de un funcional $\bsS[\vec{q}] = \int_{t_1}^{t_2} \bsL(\vec{q}, \dot{\vec{q}}, t) \,dt$, con $\vec{q} = (q_1, \dots, q_n)$ y extremos fijos. Los usa la parte física: para fijar $\bsL$, para la libertad de elegir el potencial vector y para cambiar de coordenadas en los ejemplos.

### Sumar una derivada total no cambia las ecuaciones

Sea $G(\vec{q}, t)$ de clase $C^3$ y $\bsL' := \bsL + \dfrac{d}{dt} G$, donde $\dfrac{d}{dt} G = \sum_{a} \partial_{q_a} G \cdot \dot{q}_a + \partial_t G$ (aquí $a$ recorre las $n$ coordenadas). Las ecuaciones de Euler–Lagrange de $\bsL'$ y de $\bsL$ son las mismas. Dos demostraciones:

* **Directa:** para el término $\dfrac{d}{dt} G$, $\partial_{\dot{q}_a}\left(\dfrac{d}{dt} G\right) = \partial_{q_a} G$, cuya derivada respecto de $t$ es $\sum_b \partial_{q_b} \partial_{q_a} G \cdot \dot{q}_b + \partial_t \partial_{q_a} G$; y $\partial_{q_a}\left(\dfrac{d}{dt} G\right) = \sum_b \partial_{q_a} \partial_{q_b} G \cdot \dot{q}_b + \partial_{q_a} \partial_t G$. Por el teorema de Schwarz son iguales, así que la expresión de Euler–Lagrange de $\dfrac{d}{dt} G$ es idénticamente nula.
* **Variacional:** $\int_{t_1}^{t_2} \dfrac{d}{dt} G \,dt = G(\vec{q}(t_2), t_2) - G(\vec{q}(t_1), t_1)$ vale lo mismo para todas las trayectorias admisibles, que tienen los extremos fijos. Sumarlo a $\bsS$ no cambia qué trayectorias son estacionarias.

Multiplicar $\bsL$ por una constante $\lambda \neq 0$ tampoco cambia las ecuaciones, porque son lineales en $\bsL$.

### Las ecuaciones mantienen su forma al cambiar de coordenadas

Sea $\vec{q} = \vec{Q}(\vec{s}, t)$ un cambio de coordenadas de clase $C^3$, con $\vec{s} = (s_1, \dots, s_n)$ las nuevas coordenadas y la matriz jacobiana $\left(\partial_{s_b} Q_a\right)_{a,b}$ invertible. Definimos el lagrangiano en las nuevas coordenadas,

$$
\begin{aligned}
\tilde{\bsL}(\vec{s}, \dot{\vec{s}}, t) := \bsL\big(\vec{Q}(\vec{s}, t), \dot{\vec{Q}}, t\big), \qquad \dot{Q}_a = \sum_{b=1}^{n} \partial_{s_b} Q_a \cdot \dot{s}_b + \partial_t Q_a.
\end{aligned}
$$

**Resultado:** $\vec{q}(t)$ cumple las ecuaciones de Euler–Lagrange de $\bsL$ si y solo si $\vec{s}(t)$ cumple las de $\tilde{\bsL}$.

**Demostración:**

1. $\partial_{\dot{s}_b} \dot{Q}_a = \partial_{s_b} Q_a$, así que $\partial_{\dot{s}_b} \tilde{\bsL} = \sum_a \partial_{\dot{q}_a} \bsL \cdot \partial_{s_b} Q_a$.
2. Por el teorema de Schwarz, $\partial_{s_b} \dot{Q}_a = \dfrac{d}{dt}\left(\partial_{s_b} Q_a\right)$.
3. Por la regla de la cadena, $\partial_{s_b} \tilde{\bsL} = \sum_a \left(\partial_{q_a} \bsL \cdot \partial_{s_b} Q_a + \partial_{\dot{q}_a} \bsL \cdot \partial_{s_b} \dot{Q}_a\right)$. Derivando respecto de $t$ la igualdad del paso 1, restando y usando el paso 2, los términos con $\partial_{\dot{q}_a} \bsL$ se cancelan y queda
   $$
   \begin{aligned}
   \partial_{s_b} \tilde{\bsL} - \dfrac{d}{dt}\Big(\partial_{\dot{s}_b} \tilde{\bsL}\Big) = \sum_{a=1}^{n} \left( \partial_{q_a} \bsL - \dfrac{d}{dt}\Big(\partial_{\dot{q}_a} \bsL\Big) \right) \cdot \partial_{s_b} Q_a.
   \end{aligned}
   $$
4. Como la matriz jacobiana es invertible, las $n$ expresiones de la izquierda son nulas si y solo si lo son las $n$ de la derecha.

Se aplica en los ejemplos físicos a las coordenadas polares y al centro de masas.

## La forma más general del potencial en $\bsL = T - V$

### La pregunta

Escribimos todas las coordenadas de las partículas con un solo índice, $a, b = 1, \dots, n$, con $n = 3 \cdot N$, y $m_a$ para la masa de la partícula a la que pertenece la coordenada $a$, de modo que $T = \sum_a \dfrac{1}{2} \cdot m_a \cdot \dot{q}_a^2$. Sea $\bsL = T - V(\vec{q}, \dot{\vec{q}}, t)$. ¿De qué puede depender $V$ para que cada ecuación de Euler–Lagrange sea, tal cual, una ecuación de Newton, $m_a \cdot \ddot{q}_a = F_a(\vec{q}, \dot{\vec{q}}, t)$, con fuerzas que no dependen de las aceleraciones? Dicho de otro modo: que en la ecuación $a$ la única aceleración que aparezca sea $\ddot{q}_a$, multiplicada por la masa $m_a$.

### El resultado: $V$ es, como mucho, lineal en las velocidades

En la forma desarrollada de las ecuaciones, el coeficiente de $\ddot{q}_b$ en la ecuación $a$ es la entrada $(a,b)$ de la matriz $W$:

$$
\begin{aligned}
W_{ab} = \partial_{\dot{q}_b} \partial_{\dot{q}_a} \bsL = m_a \cdot [a = b] - \partial_{\dot{q}_b} \partial_{\dot{q}_a} V,
\end{aligned}
$$

donde $[a = b]$ vale $1$ si $a = b$ y $0$ si no. Para que la ecuación $a$ sea $m_a \cdot \ddot{q}_a = F_a$ para cualquier movimiento, $W$ tiene que ser la matriz de masas, es decir, las derivadas segundas de $V$ respecto de las velocidades tienen que ser nulas. Equivalentemente, el momento canónico $\partial_{\dot{q}_a} \bsL$ difiere de $m_a \cdot \dot{q}_a$ en una función que solo depende de las posiciones y del tiempo: es la forma que toma la condición (A) de la parte física cuando hay fuerzas que dependen de la velocidad. Como el espacio de las velocidades es conexo, $V$ es entonces una función afín de las velocidades:

$$
\begin{aligned}
V(\vec{q}, \dot{\vec{q}}, t) = \phi(\vec{q}, t) - \sum_{a=1}^{n} A_a(\vec{q}, t) \cdot \dot{q}_a.
\end{aligned}
$$

Si $W$ fuera invertible pero distinta de la matriz de masas, las ecuaciones podrían despejarse para las aceleraciones, pero cada ecuación mezclaría las aceleraciones de varias coordenadas y la «masa efectiva» dependería del estado del sistema. Es lo que excluye la pregunta.

### Las fuerzas que resultan

Con este $V$, $\partial_{\dot{q}_a} \bsL = m_a \cdot \dot{q}_a + A_a$ y $\partial_{q_a} \bsL = -\partial_{q_a} \phi + \sum_b \partial_{q_a} A_b \cdot \dot{q}_b$, y las ecuaciones de Euler–Lagrange dan

$$
\begin{aligned}
m_a \cdot \ddot{q}_a = -\partial_{q_a} \phi - \partial_t A_a + \sum_{b=1}^{n} \left(\partial_{q_a} A_b - \partial_{q_b} A_a\right) \cdot \dot{q}_b.
\end{aligned}
$$

* **El término lineal en las velocidades no realiza trabajo:** al multiplicarlo por $\dot{q}_a$ y sumar en $a$ se anula, porque el coeficiente $\partial_{q_a} A_b - \partial_{q_b} A_a$ cambia de signo al intercambiar $a$ y $b$.
* **Para una partícula en $\mathbb{R}^3$:** $\sum_b \left(\partial_{q_a} A_b - \partial_{q_b} A_a\right) \cdot \dot{q}_b$ es la componente $a$ de $\dot{\vec{q}} \times (\nabla \times \vec{A})$, y la fuerza es
  $$
  \begin{aligned}
  \vec{F} = -\nabla \phi - \partial_t \vec{A} + \dot{\vec{q}} \times (\nabla \times \vec{A}),
  \end{aligned}
  $$
  que es la forma de la fuerza de Lorentz por unidad de carga, con $\vec{E} = -\nabla \phi - \partial_t \vec{A}$ y $\vec{B} = \nabla \times \vec{A}$. La estructura del electromagnetismo aparece como la única posible.
* **$\phi$ y $\vec{A}$ no son únicos:** $\phi - \partial_t \chi$ y $\vec{A} + \nabla \chi$ dan las mismas fuerzas, y cambian $\bsL$ en la derivada total $\dfrac{d}{dt} \chi(\vec{q}, t)$ (apartado anterior).

### Clasificación según las dependencias de $V$

| $V$ depende de | Fuerzas | Qué se conserva | Dónde aparece |
| --- | --- | --- | --- |
| $\vec{q}$ | conservativas | $E = T + V$ | primera a tercera etapas de la parte física |
| $\vec{q}$ y $t$ | dependientes del tiempo | en general, nada | campos que varían con el tiempo |
| $\vec{q}$, $t$, y linealmente $\dot{\vec{q}}$ | además, de tipo magnético | $T + \phi$, si no depende de $t$ | cuarta etapa de la parte física |
| $\dot{\vec{q}}$ de forma no lineal | la ecuación deja de ser $m \cdot \ddot{q} = F$: cambia $W$ | depende del caso | fuera de este esquema |

**Fuerzas sin potencial.** No toda fuerza que dependa de la velocidad se obtiene así. El rozamiento viscoso en una dimensión, $F = -\beta \cdot \dot{q}$, no lo admite: por el resultado anterior, $V$ tendría que ser $\phi(q,t) - A(q,t) \cdot \dot{q}$, y entonces la fuerza sería $-\partial_q \phi - \partial_t A$, que no depende de $\dot{q}$ (en una dimensión, el término antisimétrico es nulo). Para tratar el rozamiento hacen falta otras herramientas, como la función de disipación de Rayleigh.
