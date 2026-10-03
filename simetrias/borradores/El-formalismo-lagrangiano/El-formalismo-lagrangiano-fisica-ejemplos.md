---
author: "Julián Calderón Almendros"
---

# El formalismo lagrangiano: ejemplos físicos

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-03
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

Ejemplos de la parte física («El formalismo lagrangiano: parte física»). Los tres primeros son sistemas de partículas: usan $\bsL = T - V$, deducido allí de las leyes de Newton, y el resultado de los anexos según el cual las ecuaciones de Euler–Lagrange mantienen su forma al cambiar de coordenadas. Los dos últimos son medios continuos, la cuerda y la membrana: para ellos se toma $\bsL$ como la energía cinética menos la potencial por unidad de longitud o de superficie, por analogía con el caso de las partículas.

## Ejemplo: coordenadas polares, potencial efectivo y órbitas de Kepler

Una partícula de masa $m$ y carga $e$ en un campo central (primera etapa de la parte física). Como el momento angular $\vec{\ell}$ se conserva, si $\vec{\ell} \neq \vec{0}$ el movimiento es plano, y podemos elegir los ejes de modo que ocurra en el plano $q_3 = 0$. En ese plano usamos coordenadas polares, $q_1 = r \cdot \cos\theta$ y $q_2 = r \cdot \sin\theta$, con $r > 0$. El cambio es de clase $C^\infty$ y su matriz jacobiana tiene determinante $r \neq 0$, así que, por los anexos («Requisito matemático previo»), las ecuaciones de Euler–Lagrange pueden escribirse en las variables $(r, \theta)$. Como $\dot{q}_1^2 + \dot{q}_2^2 = \dot{r}^2 + r^2 \cdot \dot{\theta}^2$, el lagrangiano es

$$
\begin{aligned}
\tilde{\bsL}(r, \theta, \dot{r}, \dot{\theta}) = \dfrac{1}{2} \cdot m \cdot \left(\dot{r}^2 + r^2 \cdot \dot{\theta}^2\right) - e \cdot U(r).
\end{aligned}
$$

La variable $\theta$ no aparece en $\tilde{\bsL}$ (es una variable cíclica), así que su ecuación se reduce a $\dfrac{d}{dt}\left(m \cdot r^2 \cdot \dot{\theta}\right) = 0$: la cantidad $\ell := m \cdot r^2 \cdot \dot{\theta}$, que es la componente del momento angular perpendicular al plano, es constante. La ecuación de $r$ es

$$
\begin{aligned}
m \cdot \ddot{r} = m \cdot r \cdot \dot{\theta}^2 - e \cdot U'(r).
\end{aligned}
$$

Sustituyendo $\dot{\theta} = \dfrac{\ell}{m \cdot r^2}$, el término $m \cdot r \cdot \dot{\theta}^2 = \dfrac{\ell^2}{m \cdot r^3}$ es la derivada de $-\dfrac{\ell^2}{2 \cdot m \cdot r^2}$ respecto de $r$, y queda

$$
\begin{aligned}
m \cdot \ddot{r} = -\dfrac{d}{dr}\left(e \cdot U(r) + \dfrac{\ell^2}{2 \cdot m \cdot r^2}\right).
\end{aligned}
$$

Es un problema de una sola variable, con el potencial efectivo $e \cdot U(r) + \dfrac{\ell^2}{2 \cdot m \cdot r^2}$: el segundo término es la barrera centrífuga, que impide que la partícula llegue al centro si $\ell \neq 0$. Con el campo gravitatorio, $e = m$ y $U(r) = -\dfrac{G \cdot M}{r}$, se obtienen las órbitas de Kepler.

## Ejemplo: dos partículas, centro de masas y masa reducida

Dos partículas con una interacción que solo depende de la distancia y sin campo exterior (tercera etapa de la parte física), de modo que $\bsL = \dfrac{1}{2} \cdot m_1 \cdot |\dot{\vec{q}}_1|^2 + \dfrac{1}{2} \cdot m_2 \cdot |\dot{\vec{q}}_2|^2 - V_{12}(r_{12})$. Con $m_{12} := m_1 + m_2$, definimos el centro de masas y la posición relativa:

$$
\begin{aligned}
\vec{R} := \dfrac{m_1 \cdot \vec{q}_1 + m_2 \cdot \vec{q}_2}{m_{12}}, \qquad \vec{r} := \vec{q}_1 - \vec{q}_2.
\end{aligned}
$$

El cambio es lineal e invertible: $\vec{q}_1 = \vec{R} + \dfrac{m_2}{m_{12}} \cdot \vec{r}$ y $\vec{q}_2 = \vec{R} - \dfrac{m_1}{m_{12}} \cdot \vec{r}$. Al sustituir en $T$, los términos cruzados $\dot{\vec{R}} \cdot \dot{\vec{r}}$ se cancelan, porque aparecen con los coeficientes $m_1 \cdot \dfrac{m_2}{m_{12}}$ y $-m_2 \cdot \dfrac{m_1}{m_{12}}$, y la energía cinética se separa:

$$
\begin{aligned}
T = \dfrac{1}{2} \cdot m_{12} \cdot |\dot{\vec{R}}|^2 + \dfrac{1}{2} \cdot \bar{m} \cdot |\dot{\vec{r}}|^2, \qquad \bar{m} := \dfrac{m_1 \cdot m_2}{m_{12}}.
\end{aligned}
$$

Por los anexos («Requisito matemático previo»), las ecuaciones de Euler–Lagrange pueden escribirse en las nuevas variables, con

$$
\begin{aligned}
\tilde{\bsL} = \dfrac{1}{2} \cdot m_{12} \cdot |\dot{\vec{R}}|^2 + \dfrac{1}{2} \cdot \bar{m} \cdot |\dot{\vec{r}}|^2 - V_{12}(|\vec{r}|).
\end{aligned}
$$

$\vec{R}$ no aparece en $\tilde{\bsL}$, así que $m_{12} \cdot \ddot{\vec{R}} = \vec{0}$: el centro de masas se mueve con velocidad constante. La ecuación de $\vec{r}$ es $\bar{m} \cdot \ddot{\vec{r}} = -\nabla V_{12}(|\vec{r}|)$: la posición relativa se mueve como una partícula de masa $\bar{m}$ en un campo central. El problema de dos cuerpos se reduce así a la primera etapa y, con la gravitación, a las órbitas de Kepler del ejemplo anterior.

## Ejemplo: una carga en un campo magnético uniforme

Una partícula de masa $m$ y carga $e$ en un campo magnético uniforme y constante (cuarta etapa de la parte física). Elegimos los ejes de modo que $\vec{B} = (0, 0, B)$, y tomamos $\vec{A} = \dfrac{1}{2} \cdot \vec{B} \times \vec{q}$, que cumple $\nabla \times \vec{A} = \vec{B}$. Como $\dot{\vec{q}} \times \vec{B} = (B \cdot \dot{q}_2, -B \cdot \dot{q}_1, 0)$, las ecuaciones $m \cdot \ddot{\vec{q}} = e \cdot \dot{\vec{q}} \times \vec{B}$ son, con $\omega_c := \dfrac{e \cdot B}{m}$,

$$
\begin{aligned}
\ddot{q}_1 = \omega_c \cdot \dot{q}_2, \qquad \ddot{q}_2 = -\omega_c \cdot \dot{q}_1, \qquad \ddot{q}_3 = 0.
\end{aligned}
$$

La tercera da un movimiento uniforme a lo largo de $\vec{B}$: $q_3(t) = q_3(0) + v_\parallel \cdot t$. Las dos primeras tienen por solución, como se comprueba derivando,

$$
\begin{aligned}
\dot{q}_1(t) = v_\perp \cdot \cos(\gamma - \omega_c \cdot t), \qquad \dot{q}_2(t) = v_\perp \cdot \sin(\gamma - \omega_c \cdot t),
\end{aligned}
$$

donde $v_\perp \geq 0$ y $\gamma$ se fijan con la velocidad inicial. Integrando,

$$
\begin{aligned}
q_1(t) = c_1 - \dfrac{v_\perp}{\omega_c} \cdot \sin(\gamma - \omega_c \cdot t), \qquad q_2(t) = c_2 + \dfrac{v_\perp}{\omega_c} \cdot \cos(\gamma - \omega_c \cdot t),
\end{aligned}
$$

con $c_1$ y $c_2$ constantes. La proyección sobre el plano perpendicular a $\vec{B}$ es una circunferencia de centro $(c_1, c_2)$ y radio $\dfrac{v_\perp}{|\omega_c|}$, recorrida con frecuencia angular $|\omega_c|$ (la frecuencia de ciclotrón); junto con el movimiento uniforme a lo largo de $\vec{B}$, la trayectoria es una hélice. Comprobación: el módulo de la velocidad, $\sqrt{v_\perp^2 + v_\parallel^2}$, es constante, como debe ser, porque se conserva $\dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$.

## Ejemplo: la cuerda vibrante y la ecuación de ondas

En este ejemplo, $t$ es el tiempo. Una cuerda tensa ocupa en reposo el segmento $[x_1, x_2]$ del eje $x$, con los extremos fijos, y $f(x,t)$ es su desplazamiento transversal en el punto $x$ y en el instante $t$: la $y(x,t)$ del Tema 1, apartado 1.2. Suponemos que la masa por unidad de longitud, $\mu$, y la tensión, $\tau$, son constantes, y que las pendientes son pequeñas. Escribimos $\tau$ para la tensión, como en el Tema 1, porque $T$ suele reservarse para la energía cinética.

### La densidad lagrangiana

Un trozo de cuerda de longitud $dx$ tiene masa $\mu \cdot dx$ y velocidad transversal $\partial_t f$, así que su energía cinética es $\dfrac{1}{2} \cdot \mu \cdot (\partial_t f)^2 \cdot dx$. Su energía potencial es el trabajo necesario para estirarlo contra la tensión. Deformado, el trozo mide $\sqrt{1 + (\partial_x f)^2} \cdot dx \approx \left(1 + \dfrac{1}{2} \cdot (\partial_x f)^2\right) \cdot dx$, es decir, se ha alargado $\dfrac{1}{2} \cdot (\partial_x f)^2 \cdot dx$, y su energía potencial es $\dfrac{1}{2} \cdot \tau \cdot (\partial_x f)^2 \cdot dx$.

Por analogía con la parte física, donde $\bsL = T - V$ se deduce para partículas, tomamos como $\bsL$ la energía cinética menos la potencial, por unidad de longitud:

$$
\begin{aligned}
\bsL(f, \partial_x f, \partial_t f, x, t) = \dfrac{1}{2} \cdot \mu \cdot (\partial_t f)^2 - \dfrac{1}{2} \cdot \tau \cdot (\partial_x f)^2.
\end{aligned}
$$

En este contexto, $\bsL$ se llama densidad lagrangiana, y $\bsS$, acción. Las unidades de $\bsL$ son de energía por unidad de longitud: $\mu \cdot (\partial_t f)^2$ tiene unidades de $\dfrac{\text{kg}}{\text{m}} \cdot \dfrac{\text{m}^2}{\text{s}^2} = \dfrac{\text{J}}{\text{m}}$, y $\tau \cdot (\partial_x f)^2$, de newtons por un número adimensional, también $\dfrac{\text{J}}{\text{m}}$.

### La ecuación de ondas

Las derivadas parciales de $\bsL$ son $\partial_f \bsL = 0$, $\partial_{\partial_x f} \bsL = -\tau \cdot \partial_x f$ y $\partial_{\partial_t f} \bsL = \mu \cdot \partial_t f$. La ecuación de Euler–Lagrange queda

$$
\begin{aligned}
-\dfrac{\partial}{\partial x}\Big(-\tau \cdot \partial_x f_0(x,t)\Big) - \dfrac{\partial}{\partial t}\Big(\mu \cdot \partial_t f_0(x,t)\Big) &= \tau \cdot \partial^2_x f_0 - \mu \cdot \partial^2_t f_0 \\
&= 0,
\end{aligned}
$$

es decir,

$$
\begin{aligned}
\partial^2_x f_0 = \dfrac{1}{v^2} \cdot \partial^2_t f_0, \qquad v^2 := \dfrac{\tau}{\mu}.
\end{aligned}
$$

Es la ecuación de ondas del Tema 1, apartado 1.4.1. Comprobación de unidades: $\dfrac{\tau}{\mu}$ tiene unidades de $\dfrac{\text{N}}{\text{kg}/\text{m}} = \dfrac{\text{m}^2}{\text{s}^2}$, las de una velocidad al cuadrado.

**Ejemplo computacional:** [cuadernos/tema1/ondas.py](https://github.com/julian1c2a/MCC/blob/main/cuadernos/tema1/ondas.py). Obtiene con SymPy esta misma ecuación como ecuación de Euler–Lagrange de la densidad lagrangiana de la cuerda, y comprueba la solución de d'Alembert y las ondas estacionarias.

### Las ondas estacionarias

Las ondas estacionarias del Tema 1, apartado 1.2.1, son soluciones:

$$
\begin{aligned}
f_0(x,t) = A \cdot \sin\big(k \cdot (x - x_1)\big) \cdot \cos(\omega \cdot t), \qquad \omega = v \cdot k,
\end{aligned}
$$

donde $A$ es la amplitud. En efecto, $\partial^2_x f_0 = -k^2 \cdot f_0$ y $\partial^2_t f_0 = -\omega^2 \cdot f_0$, y la ecuación se cumple porque $k^2 = \dfrac{\omega^2}{v^2}$. Los extremos fijos, $f_0(x_1,t) = f_0(x_2,t) = 0$, exigen $\sin\big(k \cdot (x_2 - x_1)\big) = 0$, es decir, $k = \dfrac{n \cdot \pi}{x_2 - x_1}$ con $n$ entero positivo.

### No es un mínimo

Como en el ejemplo de la membrana casi plana (ejemplos matemáticos), $\bsL$ es cuadrático, y el término de primer orden se anula porque $f_0$ es estacionaria. Para cualquier $h$ de clase $C^2(\Omega)$ que se anule en $\operatorname{Fr}(\Omega)$:

$$
\begin{aligned}
\bsS[f_0 + h] - \bsS[f_0] = \dfrac{1}{2} \cdot \int_{t_1}^{t_2} \int_{x_1}^{x_2} \Big(\mu \cdot \big(\partial_t h(x,t)\big)^2 - \tau \cdot \big(\partial_x h(x,t)\big)^2\Big) \,dx \,dt.
\end{aligned}
$$

Ahora los dos términos tienen signos opuestos, y la diferencia puede ser positiva o negativa. Lo vemos con las funciones

$$
\begin{aligned}
h(x,t) = \sin\left(\dfrac{n \cdot \pi \cdot (x - x_1)}{x_2 - x_1}\right) \cdot \sin\left(\dfrac{j \cdot \pi \cdot (t - t_1)}{t_2 - t_1}\right),
\end{aligned}
$$

con $n$ y $j$ enteros positivos, que se anulan en los cuatro lados de la frontera. El cuadrado de un seno o de un coseno, integrado sobre un número entero de semiperiodos, da la mitad de la longitud del intervalo. Con eso se obtiene

$$
\begin{aligned}
\bsS[f_0 + h] - \bsS[f_0] &= \dfrac{\pi^2 \cdot (x_2 - x_1) \cdot (t_2 - t_1)}{8} \\
&\quad \cdot \left(\mu \cdot \dfrac{j^2}{(t_2 - t_1)^2} - \tau \cdot \dfrac{n^2}{(x_2 - x_1)^2}\right).
\end{aligned}
$$

Con $n = 1$ y $j$ grande, $h$ oscila deprisa en el tiempo, domina el término cinético y la diferencia es positiva. Con $j = 1$ y $n$ grande, $h$ oscila deprisa en el espacio, domina el término elástico y la diferencia es negativa. Lo mismo ocurre con $\epsilon \cdot h$ para $\epsilon$ tan pequeño como se quiera, porque la diferencia queda multiplicada por $\epsilon^2$. Por tanto, $f_0$ no es ni un mínimo ni un máximo de $\bsS$, sino un punto de silla: la acción de la cuerda es estacionaria, pero no mínima. Por eso hablamos siempre de funciones que hacen estacionario el funcional.

### Las condiciones de contorno de la cuerda

Este ejemplo ilustra también la observación de la parte matemática, en el apartado de dos variables, sobre las condiciones de contorno. Con $f = 0$ en toda la frontera, $f_0 = 0$ es solución. Pero si la duración $t_2 - t_1$ cumple $\omega \cdot (t_2 - t_1) = j \cdot \pi$ para algún entero positivo $j$, con $k = \dfrac{n \cdot \pi}{x_2 - x_1}$ y $\omega = v \cdot k$, la función

$$
\begin{aligned}
f_0(x,t) = A \cdot \sin\big(k \cdot (x - x_1)\big) \cdot \sin\big(\omega \cdot (t - t_1)\big)
\end{aligned}
$$

también cumple la ecuación de ondas y se anula en los cuatro lados, para cualquier amplitud $A$: hay infinitas soluciones. Por eso, en física, la ecuación de ondas se resuelve con la posición y la velocidad iniciales, y no con los valores en $t_1$ y en $t_2$.

## Comparación: la membrana casi plana y la cuerda

| | Membrana casi plana (ejemplos matemáticos) | Cuerda vibrante |
| --- | --- | --- |
| $\bsL$ | $\dfrac{1}{2} \cdot \left((\partial_x f)^2 + (\partial_t f)^2\right)$ | $\dfrac{1}{2} \cdot \mu \cdot (\partial_t f)^2 - \dfrac{1}{2} \cdot \tau \cdot (\partial_x f)^2$ |
| Ecuación de Euler–Lagrange | Laplace | ondas |
| Carácter de $f_0$ | mínimo global y único | punto de silla |
| Datos con los que se resuelve | valores en toda la frontera | posición y velocidad iniciales |

La única diferencia entre los dos funcionales es el signo del término con $(\partial_x f)^2$, y ese signo cambia tanto el tipo de ecuación como el carácter de la función que hace estacionario el funcional.

## Ejemplo: la membrana vibrante

Tomamos el tiempo y $m = 2$ coordenadas espaciales, con $n = 1$: $f(t, x_1, x_2)$ es el desplazamiento transversal de una membrana tensa que en reposo ocupa el rectángulo $\Omega = [a_1, b_1] \times [a_2, b_2]$, con el borde fijo. Suponemos constantes la masa por unidad de superficie, $\rho$, y la tensión por unidad de longitud, $\sigma$, y pequeñas las pendientes. No usamos $\mu$ ni $\tau$, como en la cuerda, porque $\mu$ es ahora un índice.

Como en la cuerda, la energía cinética de un trozo de área $dx_1 \cdot dx_2$ es $\dfrac{1}{2} \cdot \rho \cdot (\partial_t f)^2 \cdot dx_1 \cdot dx_2$. La energía potencial es la tensión por el aumento de área, que, por el ejemplo de la membrana casi plana (ejemplos matemáticos), es aproximadamente $\dfrac{1}{2} \cdot \left((\partial_{x_1} f)^2 + (\partial_{x_2} f)^2\right) \cdot dx_1 \cdot dx_2$. La densidad lagrangiana es, por tanto,

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot \rho \cdot (\partial_t f)^2 - \dfrac{1}{2} \cdot \sigma \cdot \left((\partial_{x_1} f)^2 + (\partial_{x_2} f)^2\right).
\end{aligned}
$$

Sus derivadas parciales son $\partial_f \bsL = 0$, $\partial_{\partial_t f} \bsL = \rho \cdot \partial_t f$ y $\partial_{\partial_{x_k} f} \bsL = -\sigma \cdot \partial_{x_k} f$, y la ecuación de Euler–Lagrange, en la forma con el tiempo separado de la parte matemática, queda

$$
\begin{aligned}
-\dfrac{\partial}{\partial t}\big(\rho \cdot \partial_t f_0\big) - \sum_{k=1}^{2} \dfrac{\partial}{\partial x_k}\big(-\sigma \cdot \partial_{x_k} f_0\big) = 0,
\end{aligned}
$$

es decir,

$$
\begin{aligned}
\partial^2_t f_0 = v^2 \cdot \left(\partial^2_{x_1} f_0 + \partial^2_{x_2} f_0\right),
\end{aligned}
$$

con $v^2 := \dfrac{\sigma}{\rho}$. Es la ecuación de ondas bidimensional del Tema 1, apartado 1.4.5, con $(x, z) = (x_1, x_2)$. Comprobación de unidades: $\dfrac{\sigma}{\rho}$ tiene unidades de $\dfrac{\text{N}/\text{m}}{\text{kg}/\text{m}^2} = \dfrac{\text{m}^2}{\text{s}^2}$, las de una velocidad al cuadrado.

Los modos normales del Tema 1 son soluciones: con $k_1 := \dfrac{n_1 \cdot \pi}{b_1 - a_1}$ y $k_2 := \dfrac{n_2 \cdot \pi}{b_2 - a_2}$, siendo $n_1$ y $n_2$ enteros positivos,

$$
\begin{aligned}
f_0(t, x_1, x_2) &= A \cdot \sin\big(k_1 \cdot (x_1 - a_1)\big) \cdot \sin\big(k_2 \cdot (x_2 - a_2)\big) \cdot \cos(\omega \cdot t), \\
\omega^2 &= v^2 \cdot \left(k_1^2 + k_2^2\right).
\end{aligned}
$$

En efecto, $\partial^2_t f_0 = -\omega^2 \cdot f_0$, $\partial^2_{x_1} f_0 = -k_1^2 \cdot f_0$ y $\partial^2_{x_2} f_0 = -k_2^2 \cdot f_0$, y $f_0$ se anula en el borde del rectángulo. Como en la cuerda, la acción de la membrana es estacionaria, pero no mínima: las perturbaciones que oscilan deprisa en el tiempo la aumentan, y las que oscilan deprisa en el espacio la disminuyen.
