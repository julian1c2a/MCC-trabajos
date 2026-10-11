---
author: "Julián Calderón Almendros"
---

# El teorema de Noether: ejemplos físicos

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-11
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

**Versión 1.** Este documento pertenece a la versión 1 de la serie, que se conserva. La versión 2, en los documentos con sufijo -v2 de este mismo directorio, es la que se mantiene al día: usa la familia $\Phi_\varepsilon$ en lugar de $\bsT_\epsilon$, transformaciones de los puntos con generador $(\tau, \xi)$ y apartados numerados, y añade, entre otras cosas, los grupos de Lorentz y de Poincaré y la mecánica cuántica no relativista. Las líneas «Fuente:» de la versión para el trabajo remiten a la versión 2.

Ejemplos de «El teorema de Noether: parte física», con la notación de aquel documento. Van de más a menos simétricos: la partícula libre tiene las diez simetrías de Galileo; el campo uniforme rompe algunas; el campo central, otras. Después vienen dos partículas, una carga en un campo magnético y la cuerda vibrante, un ejemplo con varias variables.

En cada ejemplo se siguen los cuatro pasos de la parte física: generador, $\bsdelta_{\vec{\xi}} \bsL$ y $F$, cantidad conservada $Q$, y **comprobación sobre la solución explícita**. Esta comprobación no usa el teorema: deriva $Q$ a lo largo del movimiento real y ve que se anula. Si el teorema estuviera mal aplicado, la comprobación fallaría.

Todas las cuentas de este documento están comprobadas con SymPy en `Teorema-de-Noether-comprobaciones.py`, en el mismo directorio.

## Ejemplo: la partícula libre

Una partícula de masa $m$ sin fuerzas: $\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$ y $\vec{p} = m \cdot \dot{\vec{q}}$. La ecuación de Euler–Lagrange es $m \cdot \ddot{\vec{q}} = \vec{0}$, cuya solución es el movimiento uniforme

$$
\begin{aligned}
\vec{q}(t) = \vec{q}_0 + \vec{v}_0 \cdot t,
\end{aligned}
$$

con $\vec{q}_0$ y $\vec{v}_0$ la posición y la velocidad en $t = 0$.

| Transformación | $\vec{\xi}$ | $\bsdelta_{\vec{\xi}} \bsL$ | $F$ | $Q$ |
| ---------------------- | ---------- | ---------------------------- | -------------- | ---------- |
| Traslación $\vec{a}$ | $\vec{a}$ | $0$ | $0$ | $\vec{a} \cdot \vec{p}$ |
| Giro alrededor de $\vec{n}$ | $\vec{n} \times \vec{q}$ | $m \cdot \dot{\vec{q}} \cdot (\vec{n} \times \dot{\vec{q}}) = 0$ | $0$ | $\vec{n} \cdot \vec{\ell}$ |
| Cambio de velocidad $\vec{u}$ | $\vec{u} \cdot t$ | $m \cdot \dot{\vec{q}} \cdot \vec{u}$ | $m \cdot \vec{u} \cdot \vec{q}$ | $-\vec{u} \cdot \vec{g}$ |
| Traslación en el tiempo | $\dot{\vec{q}}$ | $\dfrac{d\bsL}{dt}$ | $\bsL$ | $E$ |

Table: Las diez simetrías de la partícula libre.

Con $\vec{\ell} = \vec{q} \times \vec{p}$, $\vec{g} = m \cdot \vec{q} - \vec{p} \cdot t$ y $E = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$. Las cuentas de $\bsdelta_{\vec{\xi}} \bsL$ y de $Q$ están en la parte física («Primera etapa › La partícula libre»).

**Comprobación sobre la solución.** Con $\dot{\vec{q}} = \vec{v}_0$:

* $\vec{p} = m \cdot \vec{v}_0$, constante.
* $\vec{\ell} = (\vec{q}_0 + \vec{v}_0 \cdot t) \times m \cdot \vec{v}_0 = m \cdot \vec{q}_0 \times \vec{v}_0$, porque $\vec{v}_0 \times \vec{v}_0 = \vec{0}$. Constante.
* $\vec{g} = m \cdot (\vec{q}_0 + \vec{v}_0 \cdot t) - m \cdot \vec{v}_0 \cdot t = m \cdot \vec{q}_0$, constante: es la masa por la posición inicial.
* $E = \dfrac{1}{2} \cdot m \cdot |\vec{v}_0|^2$, constante.

**Qué muestra el ejemplo.** Es el caso más sencillo del teorema y el único en que las diez transformaciones son simetrías. Cada cantidad conservada responde a una pregunta sobre el movimiento: hacia dónde va y con qué rapidez ($\vec{p}$), de dónde salió ($\vec{g}$), y dos combinaciones de ellas, $\vec{\ell} = \dfrac{1}{m} \cdot \vec{g} \times \vec{p}$ y $E = \dfrac{|\vec{p}|^2}{2 \cdot m}$. La primera ley de Newton aparece como consecuencia de que el espacio no tiene puntos privilegiados.

## Ejemplo: una partícula en un campo uniforme (el tiro parabólico)

Una partícula de masa $m$ cerca de la superficie de la Tierra, con el eje $z$ vertical hacia arriba y $\vec{q} = (x, y, z)$:

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot m \cdot \left(\dot{x}^2 + \dot{y}^2 + \dot{z}^2\right) - m \cdot g \cdot z.
\end{aligned}
$$

Es el campo uniforme de la parte física con $e = m$ y $\vec{g} = (0, 0, -g)$. Las ecuaciones de Euler–Lagrange son $\ddot{x} = \ddot{y} = 0$ y $\ddot{z} = -g$, con solución

$$
\begin{aligned}
x = x_0 + v_x \cdot t, \qquad y = y_0 + v_y \cdot t, \qquad z = z_0 + v_z \cdot t - \dfrac{1}{2} \cdot g \cdot t^2.
\end{aligned}
$$

### Traslaciones horizontales

**1.** $x \to x + \epsilon$: $\vec{\xi} = (1, 0, 0)$, y lo mismo en $y$.

**2.** $\bsL$ no depende de $x$ ni de $y$: $\bsdelta_{\vec{\xi}} \bsL = 0$, simetría con $F = 0$.

**3.** Se conservan $p_x = m \cdot \dot{x}$ y $p_y = m \cdot \dot{y}$.

**4.** $p_x = m \cdot v_x$ y $p_y = m \cdot v_y$: constantes.

### Traslación vertical

**1.** $z \to z + \epsilon$: $\vec{\xi} = (0, 0, 1)$.

**2.** Solo cambia la energía potencial: $\bsdelta_{\vec{\xi}} \bsL = \partial_z \bsL = -m \cdot g$. No es nula, pero es constante, y una constante es la derivada de una función del tiempo: $-m \cdot g = \dfrac{d}{dt}(-m \cdot g \cdot t)$. Es una simetría con $F = -m \cdot g \cdot t$.

**3.** Se conserva $Q = p_z - F = p_z + m \cdot g \cdot t$.

**4.** $p_z = m \cdot \dot{z} = m \cdot (v_z - g \cdot t)$, así que $Q = m \cdot v_z$: constante.

**Qué significa.** La cantidad de movimiento vertical, $p_z$, no se conserva: la gravedad la cambia a ritmo constante. Pero la traslación vertical sigue siendo una simetría en el sentido del teorema: una parábola desplazada hacia arriba sigue siendo una solución, porque la gravedad es la misma a todas las alturas. Lo que se conserva es $p_z + m \cdot g \cdot t$, que depende explícitamente del tiempo. No dice nada que no diga ya la ecuación $\dot{p}_z = -m \cdot g$, integrada una vez, pero muestra que la energía potencial $m \cdot g \cdot z$ distingue unas alturas de otras solo en una constante aditiva, que no afecta al movimiento.

### Giros: solo alrededor de la vertical

**1.** Alrededor del eje $z$: $\vec{\xi} = \vec{e}_z \times \vec{q} = (-y, x, 0)$. Alrededor del eje $x$: $\vec{\xi} = \vec{e}_x \times \vec{q} = (0, -z, y)$.

**2.** El término cinético no cambia (parte física). El potencial cambia en $-m \cdot g \cdot \xi_z$:

* alrededor de $z$, $\xi_z = 0$: $\bsdelta_{\vec{\xi}} \bsL = 0$, simetría con $F = 0$;
* alrededor de $x$, $\xi_z = y$: $\bsdelta_{\vec{\xi}} \bsL = -m \cdot g \cdot y$. No depende de las velocidades y depende de la posición: por el criterio de la parte matemática, **no** es una simetría. Lo mismo alrededor de $y$.

**3.** Se conserva $\ell_z = m \cdot (x \cdot \dot{y} - y \cdot \dot{x})$.

**4.** $\ell_z = m \cdot \big((x_0 + v_x \cdot t) \cdot v_y - (y_0 + v_y \cdot t) \cdot v_x\big) = m \cdot (x_0 \cdot v_y - y_0 \cdot v_x)$: constante. En cambio, $\ell_x = m \cdot (y \cdot \dot{z} - z \cdot \dot{y})$ cumple

$$
\begin{aligned}
\dfrac{d\ell_x}{dt} = m \cdot (\dot{y} \cdot \dot{z} + y \cdot \ddot{z} - \dot{z} \cdot \dot{y} - z \cdot \ddot{y}) = -m \cdot g \cdot y,
\end{aligned}
$$

que es el momento de la fuerza de la gravedad respecto del eje $x$, y no es nulo.

### Traslación en el tiempo

$\bsL$ no depende de $t$, y se conserva $\bsH = E = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 + m \cdot g \cdot z$. Con la solución, $\dot{z} = v_z - g \cdot t$:

$$
\begin{aligned}
E &= \dfrac{1}{2} \cdot m \cdot \left(v_x^2 + v_y^2 + (v_z - g \cdot t)^2\right) + m \cdot g \cdot \left(z_0 + v_z \cdot t - \dfrac{1}{2} \cdot g \cdot t^2\right) \\
&= \dfrac{1}{2} \cdot m \cdot \left(v_x^2 + v_y^2 + v_z^2\right) + m \cdot g \cdot z_0.
\end{aligned}
$$

Los términos $-m \cdot g \cdot v_z \cdot t$ y $\dfrac{1}{2} \cdot m \cdot g^2 \cdot t^2$ de la energía cinética se cancelan con los de la potencial.

### Cambios de velocidad

**1.** $\vec{\xi} = \vec{u} \cdot t$, con $\vec{u}$ constante.

**2.** $\bsdelta_{\vec{\xi}} \bsL = m \cdot \dot{\vec{q}} \cdot \vec{u} - m \cdot g \cdot u_z \cdot t = \dfrac{d}{dt}\left(m \cdot \vec{u} \cdot \vec{q} - \dfrac{1}{2} \cdot m \cdot g \cdot u_z \cdot t^2\right)$. Simetría con $F = m \cdot \vec{u} \cdot \vec{q} - \dfrac{1}{2} \cdot m \cdot g \cdot u_z \cdot t^2$.

**3.** $Q = \vec{p} \cdot \vec{u} \cdot t - F$.

**4.** Sobre la solución, $\vec{p} = m \cdot (v_x, v_y, v_z - g \cdot t)$, y restando $m \cdot \vec{q}$ los términos en $t$ se cancelan salvo uno: $\vec{p} \cdot t - m \cdot \vec{q} = -m \cdot \vec{q}_0 + \left(0, 0, -\dfrac{1}{2} \cdot m \cdot g \cdot t^2\right)$, con $\vec{q}_0 = (x_0, y_0, z_0)$. Entonces

$$
\begin{aligned}
Q = \vec{u} \cdot (\vec{p} \cdot t - m \cdot \vec{q}) + \dfrac{1}{2} \cdot m \cdot g \cdot u_z \cdot t^2 = -m \cdot \vec{u} \cdot \vec{q}_0,
\end{aligned}
$$

constante.

### Qué muestra el ejemplo

| Transformación | ¿Simetría? | $F$ | Cantidad conservada |
| --- | --- | --- | --- |
| Traslaciones horizontales | sí | $0$ | $p_x$, $p_y$ |
| Traslación vertical | sí | $-m \cdot g \cdot t$ | $p_z + m \cdot g \cdot t$ (no $p_z$) |
| Giro alrededor de la vertical | sí | $0$ | $\ell_z$ |
| Giros alrededor de ejes horizontales | no | — | — ($\ell_x$ y $\ell_y$ cambian) |
| Cambios de velocidad | sí | $m \cdot \vec{u} \cdot \vec{q} - \dfrac{1}{2} \cdot m \cdot g \cdot u_z \cdot t^2$ | $-m \cdot \vec{u} \cdot \vec{q}_0$ |
| Traslación en el tiempo | sí | $\bsL$ | $E$ |

Table: Simetrías del tiro parabólico.

La gravedad uniforme rompe dos de las diez simetrías de la partícula libre: los giros alrededor de ejes horizontales. Lo que distingue es una **dirección**, la vertical, no un punto. Por eso hay que precisar la expresión habitual «la gravedad rompe la simetría vertical»: lo que se pierde es la conservación de $p_z$ y la isotropía del espacio, no la posibilidad de desplazar la trayectoria en vertical.

## Ejemplo: una partícula en un campo central

Una partícula de masa $m$ y carga $e$ en un campo central: $\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 - e \cdot U(r)$, con $r = |\vec{q}| > 0$. La ecuación del movimiento es $m \cdot \ddot{\vec{q}} = -e \cdot U'(r) \cdot \dfrac{\vec{q}}{r}$.

### Giros alrededor del centro

**1.** Alrededor de un eje $\vec{n}$ que pasa por el centro: $\vec{\xi} = \vec{n} \times \vec{q}$.

**2.** A primer orden, $|\vec{q}|^2$ cambia en $2 \cdot \epsilon \cdot \vec{q} \cdot (\vec{n} \times \vec{q}) = 0$, así que $U(r)$ no cambia; el término cinético tampoco. Simetría con $F = 0$.

**3.** Se conserva $\vec{n} \cdot \vec{\ell}$ para todo $\vec{n}$: el vector $\vec{\ell}$.

**4.** Sin resolver la ecuación: $\dfrac{d\vec{\ell}}{dt} = \dot{\vec{q}} \times m \cdot \dot{\vec{q}} + \vec{q} \times m \cdot \ddot{\vec{q}} = \vec{0} - \dfrac{e \cdot U'(r)}{r} \cdot \vec{q} \times \vec{q} = \vec{0}$.

### El mismo giro en coordenadas polares

Si $\vec{\ell} \neq \vec{0}$, el movimiento ocurre en el plano perpendicular a $\vec{\ell}$ por el centro. Con ese plano como $q_3 = 0$ y coordenadas polares, $q_1 = r \cdot \cos\theta$ y $q_2 = r \cdot \sin\theta$,

$$
\begin{aligned}
\tilde{\bsL} = \dfrac{1}{2} \cdot m \cdot \left(\dot{r}^2 + r^2 \cdot \dot{\theta}^2\right) - e \cdot U(r).
\end{aligned}
$$

El giro alrededor del eje $q_3$ es ahora $\theta \to \theta + \epsilon$, con generador $(\xi_r, \xi_\theta) = (0, 1)$: $\theta$ es una coordenada cíclica, y se conserva $p_\theta = m \cdot r^2 \cdot \dot{\theta}$. Es la misma cantidad que en cartesianas:

$$
\begin{aligned}
p_1 \cdot (-q_2) + p_2 \cdot q_1 = m \cdot (q_1 \cdot \dot{q}_2 - q_2 \cdot \dot{q}_1) = m \cdot r^2 \cdot \dot{\theta},
\end{aligned}
$$

porque $\dot{q}_1 = \dot{r} \cdot \cos\theta - r \cdot \dot{\theta} \cdot \sin\theta$ y $\dot{q}_2 = \dot{r} \cdot \sin\theta + r \cdot \dot{\theta} \cdot \cos\theta$, y los términos con $\dot{r}$ se cancelan. El generador $(-q_2, q_1)$ en cartesianas y $(0, 1)$ en polares es el mismo campo vectorial, escrito en dos sistemas de coordenadas, y la cantidad $\sum_i p_i \cdot \xi_i$ no depende de las coordenadas. Una coordenada es cíclica cuando las coordenadas están adaptadas a la simetría.

### Traslaciones

**1.** $\vec{\xi} = \vec{a}$.

**2.** $\bsdelta_{\vec{\xi}} \bsL = -e \cdot U'(r) \cdot \dfrac{\vec{q} \cdot \vec{a}}{r}$, que depende de la posición y no de la velocidad. Por el criterio de la parte matemática, salvo que $U' = 0$, **no** es una simetría: el centro es un punto privilegiado.

**3 y 4.** No hay cantidad conservada, y en efecto $\dot{\vec{p}} = -e \cdot U'(r) \cdot \dfrac{\vec{q}}{r} \neq \vec{0}$.

### La simetría ayuda a resolver

Con $\ell := p_\theta$ y la energía, que se conserva porque $\bsL$ no depende de $t$,

$$
\begin{aligned}
E = \dfrac{1}{2} \cdot m \cdot \dot{r}^2 + \dfrac{\ell^2}{2 \cdot m \cdot r^2} + e \cdot U(r).
\end{aligned}
$$

Despejando, $\dot{r} = \pm\sqrt{\dfrac{2}{m} \cdot \left(E - e \cdot U(r) - \dfrac{\ell^2}{2 \cdot m \cdot r^2}\right)}$: una ecuación de primer orden en una sola variable, que se resuelve separando variables, $dt = \dfrac{dr}{\dot{r}(r)}$, en cada tramo en que $\dot{r}$ no cambia de signo. Dos cantidades conservadas reducen un problema de seis condiciones iniciales a integrales de una variable. La órbita de Kepler, con $U(r) = -\dfrac{G \cdot M}{r}$ y $e = m$, se obtiene así en «El formalismo lagrangiano: ejemplos físicos».

## Ejemplo: dos partículas

Dos partículas con una interacción que solo depende de su distancia, sin campo exterior:

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot m_1 \cdot |\dot{\vec{q}}_1|^2 + \dfrac{1}{2} \cdot m_2 \cdot |\dot{\vec{q}}_2|^2 - V_{12}(r_{12}).
\end{aligned}
$$

Por la tercera etapa de la parte física, se conservan las diez cantidades: $\vec{P}$, $\vec{G}$, $\vec{J}$ y $E$.

**El centro de masas, resuelto por las simetrías.** Con $M = m_1 + m_2$, $\vec{X}(t) = \dfrac{\vec{G} + \vec{P} \cdot t}{M}$: las traslaciones y los cambios de velocidad dan el movimiento del centro de masas sin resolver ninguna ecuación.

**El movimiento relativo.** Con $\vec{r} := \vec{q}_1 - \vec{q}_2$ y la masa reducida $\bar{m} := \dfrac{m_1 \cdot m_2}{M}$, «El formalismo lagrangiano: ejemplos físicos» escribe $\vec{q}_1 = \vec{X} + \dfrac{m_2}{M} \cdot \vec{r}$ y $\vec{q}_2 = \vec{X} - \dfrac{m_1}{M} \cdot \vec{r}$. Sustituyendo en $\vec{J}$ y en $E$, los términos cruzados se cancelan por la misma razón que en $T$ (aparecen con los coeficientes $m_1 \cdot \dfrac{m_2}{M}$ y $-m_2 \cdot \dfrac{m_1}{M}$):

$$
\begin{aligned}
\vec{J} &= M \cdot \vec{X} \times \dot{\vec{X}} + \bar{m} \cdot \vec{r} \times \dot{\vec{r}}, \\
E &= \dfrac{1}{2} \cdot M \cdot |\dot{\vec{X}}|^2 + \dfrac{1}{2} \cdot \bar{m} \cdot |\dot{\vec{r}}|^2 + V_{12}(|\vec{r}|).
\end{aligned}
$$

Como $\vec{X} \times \dot{\vec{X}} = \dfrac{1}{M^2} \cdot (\vec{G} + \vec{P} \cdot t) \times \vec{P} = \dfrac{1}{M^2} \cdot \vec{G} \times \vec{P}$ y $|\dot{\vec{X}}|^2 = \dfrac{|\vec{P}|^2}{M^2}$ son constantes, también lo son el momento angular y la energía del movimiento relativo, $\bar{m} \cdot \vec{r} \times \dot{\vec{r}}$ y $\dfrac{1}{2} \cdot \bar{m} \cdot |\dot{\vec{r}}|^2 + V_{12}(|\vec{r}|)$. El movimiento relativo es el de una partícula de masa $\bar{m}$ en un campo central, y se resuelve como en el ejemplo anterior.

**El sistema del centro de masas.** Como los cambios de velocidad y las traslaciones son simetrías, el sistema de referencia que se mueve con el centro de masas es tan válido como el de partida, y en él $\vec{P} = \vec{0}$ y $\vec{G} = \vec{0}$.

## Ejemplo: una carga en un campo magnético uniforme

Una partícula de masa $m$ y carga $e$ en $\vec{B} = (0, 0, B)$, con $\vec{A} = \dfrac{1}{2} \cdot \vec{B} \times \vec{q}$ (cuarta etapa de la parte física). Con $\omega_c := \dfrac{e \cdot B}{m}$, «El formalismo lagrangiano: ejemplos físicos» obtiene la hélice

$$
\begin{aligned}
q_1 &= c_1 - \dfrac{v_\perp}{\omega_c} \cdot \sin(\gamma - \omega_c \cdot t), \\
q_2 &= c_2 + \dfrac{v_\perp}{\omega_c} \cdot \cos(\gamma - \omega_c \cdot t), \\
q_3 &= c_3 + v_\parallel \cdot t,
\end{aligned}
$$

cuya proyección sobre el plano $q_1 q_2$ es una circunferencia de centro $\vec{c} := (c_1, c_2, 0)$ y radio $R := \dfrac{v_\perp}{|\omega_c|}$.

### Traslaciones: el centro de la circunferencia

**1 a 3.** Por la parte física, todas las traslaciones son simetrías, con $F = \dfrac{e}{2} \cdot \vec{q} \cdot (\vec{B} \times \vec{a})$, y se conserva $\vec{K} = m \cdot \dot{\vec{q}} - e \cdot \vec{q} \times \vec{B}$. Con $\vec{q} \times \vec{B} = (B \cdot q_2, -B \cdot q_1, 0)$:

$$
\begin{aligned}
\vec{K} = \big(m \cdot \dot{q}_1 - e \cdot B \cdot q_2,\ m \cdot \dot{q}_2 + e \cdot B \cdot q_1,\ m \cdot \dot{q}_3\big).
\end{aligned}
$$

**4.** Sobre la hélice, $\dot{q}_1 = v_\perp \cdot \cos(\gamma - \omega_c \cdot t)$ y $\dot{q}_2 = v_\perp \cdot \sin(\gamma - \omega_c \cdot t)$. En la primera componente, $e \cdot B \cdot \dfrac{v_\perp}{\omega_c} = m \cdot v_\perp$, y

$$
\begin{aligned}
K_1 = m \cdot v_\perp \cdot \cos(\gamma - \omega_c \cdot t) - e \cdot B \cdot c_2 - m \cdot v_\perp \cdot \cos(\gamma - \omega_c \cdot t) = -e \cdot B \cdot c_2.
\end{aligned}
$$

Del mismo modo, $K_2 = e \cdot B \cdot c_1$ y $K_3 = m \cdot v_\parallel$. Por tanto,

$$
\begin{aligned}
\vec{K} = e \cdot \vec{B} \times \vec{c} + m \cdot v_\parallel \cdot \vec{e}_3.
\end{aligned}
$$

**Qué significa.** La componente de $\vec{K}$ paralela a $\vec{B}$ es la cantidad de movimiento en esa dirección. Las perpendiculares no son cantidad de movimiento: dan la **posición del centro** de la circunferencia, $\vec{c}$. Trasladar la hélice da otra hélice, con otro centro, y la cantidad asociada a esa simetría es precisamente el centro. La cantidad de movimiento perpendicular, en cambio, gira con la partícula y no se conserva.

### Giro alrededor del eje $q_3$

Por la parte física se conserva el momento angular canónico, $Q = \ell^{\mathrm{cin}}_3 + \dfrac{e \cdot B}{2} \cdot \rho^2$, con $\ell^{\mathrm{cin}}_3 = m \cdot (q_1 \cdot \dot{q}_2 - q_2 \cdot \dot{q}_1)$ y $\rho^2 = q_1^2 + q_2^2$. Sobre la hélice, sustituyendo y usando $\omega_c \cdot R^2 = \dfrac{v_\perp^2}{\omega_c}$, los términos que dependen de $t$ se cancelan y queda

$$
\begin{aligned}
Q = \dfrac{e \cdot B}{2} \cdot \left(c_1^2 + c_2^2 - R^2\right),
\end{aligned}
$$

constante: solo depende de la distancia del centro de la circunferencia al eje y del radio. El momento angular cinético, $\ell^{\mathrm{cin}}_3$, no es constante si el centro no está en el eje.

### Energía y cambio de velocidad paralelo a $\vec{B}$

* $\bsH = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 = \dfrac{1}{2} \cdot m \cdot \left(v_\perp^2 + v_\parallel^2\right)$: constante.
* El cambio de velocidad $\vec{u} = \vec{e}_3$ es una simetría con $F = m \cdot q_3$, y da $Q = -(m \cdot q_3 - p_3 \cdot t)$, con $p_3 = m \cdot \dot{q}_3$ porque $A_3 = 0$. Sobre la hélice, $m \cdot q_3 - m \cdot v_\parallel \cdot t = m \cdot c_3$: constante.

## Ejemplo: la cuerda vibrante

Un ejemplo con dos variables, el de «El formalismo lagrangiano: ejemplos físicos»: el desplazamiento transversal $f(x, t)$ de una cuerda de extremos fijos en $x_1$ y $x_2$, con densidad $\mu$ y tensión $\tau$ constantes,

$$
\begin{aligned}
\bsL &= \dfrac{1}{2} \cdot \mu \cdot (\partial_t f)^2 - \dfrac{1}{2} \cdot \tau \cdot (\partial_x f)^2, \\
u_t &:= \partial_{\partial_t f} \bsL = \mu \cdot \partial_t f, \qquad u_x := \partial_{\partial_x f} \bsL = -\tau \cdot \partial_x f.
\end{aligned}
$$

Aquí $\tau$ es la tensión, como en aquel documento; no aparece el desplazamiento del tiempo de la parte matemática. La ecuación de Euler–Lagrange es la de ondas, $\mu \cdot \partial^2_t f = \tau \cdot \partial^2_x f$. Usamos el teorema de varias variables de la parte matemática, con la ley integral en $[x_1, x_2]$.

### Traslación en el tiempo: la energía de la onda

**1.** $f(x, t) \to f(x, t + \epsilon)$: generador $\xi = \partial_t f$.

**2.** Como $\bsL$ no depende explícitamente de $t$, por la regla de la cadena, $\bsdelta_{\xi} \bsL = u_t \cdot \partial_t(\partial_t f) + u_x \cdot \partial_x(\partial_t f) = \partial_t\big[\bsL\big]$. Simetría con $F_t = \bsL$ y $F_x = 0$.

**3.** La corriente conservada es

$$
\begin{aligned}
Q_t &= u_t \cdot \partial_t f - \bsL = \dfrac{1}{2} \cdot \mu \cdot (\partial_t f)^2 + \dfrac{1}{2} \cdot \tau \cdot (\partial_x f)^2, \\
Q_x &= u_x \cdot \partial_t f = -\tau \cdot \partial_x f \cdot \partial_t f.
\end{aligned}
$$

$Q_t$ es la densidad de energía, cinética más elástica, y $Q_x$ su flujo: la componente transversal de la tensión, $-\tau \cdot \partial_x f$, por la velocidad del punto, $\partial_t f$, es la potencia que una parte de la cuerda transmite a la siguiente.

**4.** La ley integral de la parte matemática da

$$
\begin{aligned}
\dfrac{d}{dt} \int_{x_1}^{x_2} Q_t \,dx = -\Big[ Q_x \Big]_{x = x_1}^{x = x_2} = \tau \cdot \Big[ \partial_x f \cdot \partial_t f \Big]_{x = x_1}^{x = x_2} = 0,
\end{aligned}
$$

porque en los extremos fijos $\partial_t f = 0$. La energía total de la cuerda se conserva. Con la onda estacionaria $f = A \cdot \sin\big(k \cdot (x - x_1)\big) \cdot \cos(\omega \cdot t)$, con $k = \dfrac{n \cdot \pi}{x_2 - x_1}$ y $\omega^2 = \dfrac{\tau}{\mu} \cdot k^2$, el cuadrado de un seno o de un coseno integrado en un número entero de semiperiodos da la mitad del intervalo, y

$$
\begin{aligned}
\int_{x_1}^{x_2} Q_t \,dx &= \dfrac{A^2 \cdot (x_2 - x_1)}{4} \cdot \left(\mu \cdot \omega^2 \cdot \sin^2(\omega \cdot t) + \tau \cdot k^2 \cdot \cos^2(\omega \cdot t)\right) \\
&= \dfrac{A^2 \cdot (x_2 - x_1) \cdot \tau \cdot k^2}{4},
\end{aligned}
$$

porque $\mu \cdot \omega^2 = \tau \cdot k^2$: no depende de $t$.

### Desplazamiento transversal: una simetría que rompen los extremos

**1.** $f \to f + \epsilon$: generador $\xi = 1$.

**2.** $\bsL$ no depende de $f$: simetría con $F_t = F_x = 0$.

**3.** La corriente es $Q_t = \mu \cdot \partial_t f$, la densidad de cantidad de movimiento transversal, y $Q_x = -\tau \cdot \partial_x f$. La ley de conservación es la propia ecuación de ondas.

**4.** La ley integral da

$$
\begin{aligned}
\dfrac{d}{dt} \int_{x_1}^{x_2} \mu \cdot \partial_t f \,dx = \tau \cdot \Big[ \partial_x f \Big]_{x = x_1}^{x = x_2},
\end{aligned}
$$

que en general no es nulo: los soportes de los extremos ejercen fuerzas transversales sobre la cuerda. Con la onda estacionaria y $n$ impar, $\int_{x_1}^{x_2} \sin\big(k \cdot (x - x_1)\big) \,dx = \dfrac{2}{k}$, y la cantidad de movimiento transversal total, $-\dfrac{2 \cdot \mu \cdot A \cdot \omega}{k} \cdot \sin(\omega \cdot t)$, cambia con el tiempo.

**Qué muestra el ejemplo.** $\bsL$ es simétrica, pero las condiciones de contorno no: desplazar la cuerda entera incumple $f(x_1, t) = f(x_2, t) = 0$. El teorema da la ley local, $\partial_t Q_t + \partial_x Q_x = 0$, sin condiciones; que la cantidad total se conserve depende además del flujo en la frontera. Con la energía, los extremos fijos anulan el flujo; con la cantidad de movimiento transversal, no.
