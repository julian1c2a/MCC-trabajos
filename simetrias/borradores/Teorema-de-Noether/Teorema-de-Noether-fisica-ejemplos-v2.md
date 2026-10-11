---
author: "Julián Calderón Almendros"
---

# El teorema de Noether: ejemplos físicos (versión 2)

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-11
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

Ejemplos de «El teorema de Noether: parte física (versión 2)», con la notación de aquel documento, que aquí se cita como «parte física». Los seis primeros son de la mecánica de Newton y van de más a menos simétricos: la partícula libre tiene las diez simetrías de Galileo, el campo uniforme rompe algunas y el campo central, otras; después vienen dos partículas, una carga en un campo magnético y la cuerda vibrante, que tiene dos variables. Los dos últimos salen de la mecánica de Newton: la partícula relativista, libre y en un campo uniforme, y la partícula cuántica en un potencial central.

La versión 2 de la serie consta de cinco documentos:

* «El teorema de Noether: parte matemática (versión 2)»: la teoría, con una función, varias funciones y varias variables, los flujos, las derivadas de Fréchet y de Lie, y una guía de dimensión infinita.
* «El teorema de Noether: ejemplos matemáticos (versión 2)»: el camino más corto, como gráfica y en forma paramétrica, las ecuaciones con la estructura de las de Newton y la ecuación de Laplace.
* «El teorema de Noether: parte física (versión 2)»: los sistemas de partículas, el grupo de Galileo, el grupo de Lorentz y el de Poincaré, y la mecánica cuántica no relativista.
* «El teorema de Noether: ejemplos físicos (versión 2)», este documento.
* «El teorema de Noether: anexos (versión 2)»: las rotaciones, la exponencial de una matriz y los grupos de Galileo, de Lorentz y de Poincaré en forma de matrices, con la contracción de Poincaré a Galileo y la carga central.

**Diferencias con la versión 1**, cuyos documentos se conservan:

* la versión 1 escribe la familia de transformaciones $\bsT_\epsilon$, con el parámetro $\epsilon$; la versión 2 usa $\Phi_\varepsilon$ y $\varepsilon$, como el trabajo «La importancia de las simetrías en física»;
* las transformaciones actúan sobre los puntos $(t, \vec{q})$, con un generador $(\tau, \vec{\xi})$, y la traslación en el tiempo se describe con $\tau = 1$, con cantidad conservada $-\bsH$, en lugar del generador $\dot{\vec{q}}$ con $F = \bsL$;
* la cantidad de los cambios de velocidad de una partícula es $\vec{G}$, el tiro parabólico usa las coordenadas $(q_1, q_2, q_3)$, la fase de la hélice es $\chi$ y la tensión de la cuerda es $T_0$ (en la versión 1, $\vec{g}$, $(x, y, z)$, $\gamma$ y $\tau$);
* son nuevos los apartados 3.1, 3.2 en esféricas y 3.4 (procedentes de los comentarios del borrador de la versión 2), 6.3 a 6.5, 7 y 8;
* las comprobaciones están en Teorema-de-Noether-v2-comprobaciones.py, y las de la versión 1, en Teorema-de-Noether-comprobaciones.py.

**Los cuatro pasos.** En cada ejemplo clásico se siguen los de la parte física, apartado 2:

1. la transformación y su generador $(\tau, \vec{\xi})$;
2. el término $D$, con la forma de cuatro términos, y la función $F$, si existe;
3. la cantidad conservada, $Q = \sum_i \vec{p}_i \cdot \vec{\xi}_i - \tau \cdot \bsH - F$;
4. la **comprobación sobre la solución explícita**, que no usa el teorema: deriva $Q$ a lo largo del movimiento real y ve que se anula. Si el teorema estuviera mal aplicado, la comprobación fallaría.

Las transformaciones son activas, como en la parte física (apartado 2): el cambio de velocidad suma $\varepsilon \cdot \vec{u} \cdot t$ a la trayectoria, y la traslación en el tiempo, con $\tau = 1$, da $Q = -\bsH$.

**Avisos de notación**, además de los de la parte física, apartado 1.3:

* $\phi$ es el ángulo azimutal de las coordenadas esféricas; $\vec{\varphi}_i$ siguen siendo las expresiones de Euler–Lagrange.
* $\chi$ es la fase de la hélice del apartado 5.
* $c$ es la velocidad de propagación de las ondas en el apartado 6 y la de la luz en el 7.
* $\mu$ es la densidad lineal de masa de la cuerda, $T_0$ su tensión y $\mathcal{E}$ su densidad de energía (apartado 6). La masa reducida de dos partículas se escribe $\bar{m}$ (apartado 4).
* $\kappa$ es una fuerza constante (apartado 7), como en la parte física, apartado 4.2.
* $k$ es el número de onda en el apartado 6 y la constante del potencial de Coulomb en el 8.5. $n$ es el número del modo de la cuerda (apartado 6) y el número cuántico principal (apartado 8.5); $\vec{n}$, con flecha, el eje de un giro.
* En el apartado 8, $i$ es la unidad imaginaria, $\ell$ y $m_\ell$ son números enteros que etiquetan los valores propios del momento angular, y $m$ sigue siendo la masa.

## 1. La partícula libre

Una partícula de masa $m$ sin fuerzas: $\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$ y $\vec{p} = m \cdot \dot{\vec{q}}$. La ecuación de Euler–Lagrange es $m \cdot \ddot{\vec{q}} = \vec{0}$, cuya solución es el movimiento uniforme

$$
\begin{aligned}
\vec{q}(t) = \vec{q}_0 + \vec{v}_0 \cdot t,
\end{aligned}
$$

con $\vec{q}_0$ y $\vec{v}_0$ la posición y la velocidad en $t = 0$.

| Transformación | $(\tau, \vec{\xi})$ | $D$ | $F$ | $Q$ |
| ------------------------ | ------------------------ | ---------------------------- | -------------- | ---------- |
| Traslación $\vec{a}$ | $(0, \vec{a})$ | $0$ | $0$ | $\vec{a} \cdot \vec{p}$ |
| Giro alrededor de $\vec{n}$ | $(0, \vec{n} \times \vec{q})$ | $m \cdot \dot{\vec{q}} \cdot (\vec{n} \times \dot{\vec{q}}) = 0$ | $0$ | $\vec{n} \cdot \vec{\ell}$ |
| Cambio de velocidad $\vec{u}$ | $(0, \vec{u} \cdot t)$ | $m \cdot \dot{\vec{q}} \cdot \vec{u}$ | $m \cdot \vec{u} \cdot \vec{q}$ | $-\vec{u} \cdot \vec{G}$ |
| Traslación en el tiempo | $(1, \vec{0})$ | $0$ | $0$ | $-E$ |

Table: Las diez simetrías de la partícula libre.

Con $\vec{\ell} = \vec{q} \times \vec{p}$, $\vec{G} = m \cdot \vec{q} - \vec{p} \cdot t$ y $E = \bsH = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$. Las cuentas de $D$ y de $Q$ están en la parte física, apartado 4.1.

**Comprobación sobre la solución.** Con $\dot{\vec{q}} = \vec{v}_0$:

* $\vec{p} = m \cdot \vec{v}_0$, constante.
* $\vec{\ell} = (\vec{q}_0 + \vec{v}_0 \cdot t) \times m \cdot \vec{v}_0 = m \cdot \vec{q}_0 \times \vec{v}_0$, porque $\vec{v}_0 \times \vec{v}_0 = \vec{0}$. Constante.
* $\vec{G} = m \cdot (\vec{q}_0 + \vec{v}_0 \cdot t) - m \cdot \vec{v}_0 \cdot t = m \cdot \vec{q}_0$, constante: es la masa por la posición inicial.
* $E = \dfrac{1}{2} \cdot m \cdot |\vec{v}_0|^2$, constante.

**Qué muestra el ejemplo.** Es el caso más sencillo del teorema y el único de la mecánica de Newton en que las diez transformaciones son simetrías. Cada cantidad conservada responde a una pregunta sobre el movimiento: hacia dónde va y con qué rapidez ($\vec{p}$), de dónde salió ($\vec{G}$), y dos combinaciones de ellas, $\vec{\ell} = \dfrac{1}{m} \cdot \vec{G} \times \vec{p}$ y $E = \dfrac{|\vec{p}|^2}{2 \cdot m}$. La primera ley de Newton aparece como consecuencia de que el espacio no tiene puntos privilegiados.

## 2. Una partícula en un campo uniforme: el tiro parabólico

Una partícula de masa $m$ cerca de la superficie de la Tierra, con el eje $q_3$ vertical hacia arriba y $g > 0$ la aceleración de la gravedad:

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 - m \cdot g \cdot q_3.
\end{aligned}
$$

Es el campo uniforme de la parte física, apartado 4.2, con $e = m$ y $\vec{g} = (0, 0, -g)$. Las ecuaciones de Euler–Lagrange son $\ddot{q}_1 = \ddot{q}_2 = 0$ y $\ddot{q}_3 = -g$, con solución

$$
\begin{aligned}
\vec{q}(t) = \vec{q}_0 + \vec{v}_0 \cdot t - \dfrac{1}{2} \cdot g \cdot t^2 \cdot \vec{e}_3,
\end{aligned}
$$

donde $\vec{e}_3 = (0, 0, 1)$ y $\vec{v}_0 = (v_{0,1}, v_{0,2}, v_{0,3})$ es la velocidad inicial. $\bsL$ no depende de $t$, así que $\partial_t \bsL = 0$ en la forma de cuatro términos.

### 2.1. Traslaciones horizontales

**1.** $q_1 \mapsto q_1 + \varepsilon$: $\tau = 0$ y $\vec{\xi} = (1, 0, 0)$, y lo mismo en $q_2$.

**2.** $\bsL$ no depende de $q_1$ ni de $q_2$: $D = 0$, simetría con $F = 0$.

**3.** Se conservan $p_1 = m \cdot \dot{q}_1$ y $p_2 = m \cdot \dot{q}_2$.

**4.** $p_1 = m \cdot v_{0,1}$ y $p_2 = m \cdot v_{0,2}$: constantes.

### 2.2. Traslación vertical

**1.** $q_3 \mapsto q_3 + \varepsilon$: $\tau = 0$ y $\vec{\xi} = \vec{e}_3$.

**2.** Solo cambia la energía potencial: $D = \partial_{q_3} \bsL = -m \cdot g$. No es nula, pero es constante, y una constante es la derivada de una función del tiempo: $-m \cdot g = \dfrac{d}{dt}(-m \cdot g \cdot t)$. Es una simetría con $F = -m \cdot g \cdot t$.

**3.** Se conserva $Q = p_3 - F = p_3 + m \cdot g \cdot t$.

**4.** $p_3 = m \cdot \dot{q}_3 = m \cdot (v_{0,3} - g \cdot t)$, así que $Q = m \cdot v_{0,3}$: constante.

**Qué significa.** La cantidad de movimiento vertical, $p_3$, no se conserva: la gravedad la cambia a ritmo constante. Pero la traslación vertical sigue siendo una simetría en el sentido del teorema: una parábola desplazada hacia arriba sigue siendo una solución, porque la gravedad es la misma a todas las alturas. Lo que se conserva es $p_3 + m \cdot g \cdot t$, que depende explícitamente del tiempo. No dice nada que no diga ya la ecuación $\dot{p}_3 = -m \cdot g$, integrada una vez, pero muestra que la energía potencial $m \cdot g \cdot q_3$ distingue unas alturas de otras solo en una constante aditiva, que no afecta al movimiento. En la mecánica cuántica, esta $F$ se convierte en la fase $e^{i \cdot \varepsilon \cdot F/\hbar}$ de la parte física, apartado 10.5.

### 2.3. Giros: solo alrededor de la vertical

**1.** Alrededor del eje $q_3$: $\vec{\xi} = \vec{e}_3 \times \vec{q} = (-q_2, q_1, 0)$. Alrededor del eje $q_1$: $\vec{\xi} = (1, 0, 0) \times \vec{q} = (0, -q_3, q_2)$.

**2.** El término cinético no cambia (parte física, apartado 4.1). El potencial aporta $-m \cdot g \cdot \xi_3$:

* alrededor de $q_3$, $\xi_3 = 0$: $D = 0$, simetría con $F = 0$;
* alrededor de $q_1$, $\xi_3 = q_2$: $D = -m \cdot g \cdot q_2$. No depende de las velocidades y depende de la posición: por el criterio de la parte física, apartado 2, **no** es una simetría. Lo mismo alrededor de $q_2$.

**3.** Se conserva $\ell_3 = m \cdot (q_1 \cdot \dot{q}_2 - q_2 \cdot \dot{q}_1)$.

**4.** $\ell_3 = m \cdot \big((q_{0,1} + v_{0,1} \cdot t) \cdot v_{0,2} - (q_{0,2} + v_{0,2} \cdot t) \cdot v_{0,1}\big) = m \cdot (q_{0,1} \cdot v_{0,2} - q_{0,2} \cdot v_{0,1})$: constante. En cambio, $\ell_1 = m \cdot (q_2 \cdot \dot{q}_3 - q_3 \cdot \dot{q}_2)$ cumple

$$
\begin{aligned}
\dfrac{d\ell_1}{dt} = m \cdot (\dot{q}_2 \cdot \dot{q}_3 + q_2 \cdot \ddot{q}_3 - \dot{q}_3 \cdot \dot{q}_2 - q_3 \cdot \ddot{q}_2) = -m \cdot g \cdot q_2,
\end{aligned}
$$

que es el momento de la fuerza de la gravedad respecto del eje $q_1$, y no es nulo.

### 2.4. Traslación en el tiempo

**1 a 3.** $\tau = 1$ y $\vec{\xi} = \vec{0}$: $D = \partial_t \bsL = 0$, $F = 0$, y se conserva $Q = -\bsH$, con $\bsH = E = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 + m \cdot g \cdot q_3$.

**4.** Con la solución, $\dot{q}_3 = v_{0,3} - g \cdot t$:

$$
\begin{aligned}
E &= \dfrac{1}{2} \cdot m \cdot \left(v_{0,1}^2 + v_{0,2}^2 + (v_{0,3} - g \cdot t)^2\right) + m \cdot g \cdot \left(q_{0,3} + v_{0,3} \cdot t - \dfrac{1}{2} \cdot g \cdot t^2\right) \\
&= \dfrac{1}{2} \cdot m \cdot |\vec{v}_0|^2 + m \cdot g \cdot q_{0,3}.
\end{aligned}
$$

Los términos $-m \cdot g \cdot v_{0,3} \cdot t$ y $\dfrac{1}{2} \cdot m \cdot g^2 \cdot t^2$ de la energía cinética se cancelan con los de la potencial.

### 2.5. Cambios de velocidad

**1.** $\tau = 0$ y $\vec{\xi} = \vec{u} \cdot t$, con $\vec{u}$ constante.

**2.** $D = m \cdot \dot{\vec{q}} \cdot \vec{u} - m \cdot g \cdot u_3 \cdot t = \dfrac{d}{dt}\left(m \cdot \vec{u} \cdot \vec{q} - \dfrac{1}{2} \cdot m \cdot g \cdot u_3 \cdot t^2\right)$. Simetría con $F = m \cdot \vec{u} \cdot \vec{q} - \dfrac{1}{2} \cdot m \cdot g \cdot u_3 \cdot t^2$.

**3.** $Q = \vec{p} \cdot \vec{u} \cdot t - F$.

**4.** Sobre la solución, $\vec{p} = m \cdot (\vec{v}_0 - g \cdot t \cdot \vec{e}_3)$, y en $\vec{p} \cdot t - m \cdot \vec{q}$ los términos en $t$ se cancelan salvo uno: $\vec{p} \cdot t - m \cdot \vec{q} = -m \cdot \vec{q}_0 - \dfrac{1}{2} \cdot m \cdot g \cdot t^2 \cdot \vec{e}_3$. Entonces

$$
\begin{aligned}
Q = \vec{u} \cdot (\vec{p} \cdot t - m \cdot \vec{q}) + \dfrac{1}{2} \cdot m \cdot g \cdot u_3 \cdot t^2 = -m \cdot \vec{u} \cdot \vec{q}_0,
\end{aligned}
$$

constante.

### 2.6. Qué muestra el ejemplo

| Transformación | ¿Simetría? | $F$ | Cantidad conservada |
| ---------------------------- | ------------------ | ---------------------------------- | ---------------------------- |
| Traslaciones horizontales | sí | $0$ | $p_1$, $p_2$ |
| Traslación vertical | sí | $-m \cdot g \cdot t$ | $p_3 + m \cdot g \cdot t$ (no $p_3$) |
| Giro alrededor de la vertical | sí | $0$ | $\ell_3$ |
| Giros alrededor de ejes horizontales | no | — | — ($\ell_1$ y $\ell_2$ cambian) |
| Cambios de velocidad | sí | $m \cdot \vec{u} \cdot \vec{q} - \dfrac{1}{2} \cdot m \cdot g \cdot u_3 \cdot t^2$ | $-\vec{u} \cdot \vec{G} + \dfrac{1}{2} \cdot m \cdot g \cdot u_3 \cdot t^2$ |
| Traslación en el tiempo | sí | $0$ | $-E$ |

Table: Simetrías del tiro parabólico.

La gravedad uniforme rompe dos de las diez simetrías de la partícula libre: los giros alrededor de ejes horizontales. Lo que distingue es una **dirección**, la vertical, no un punto. Por eso hay que precisar la expresión habitual «la gravedad rompe la simetría vertical»: lo que se pierde es la conservación de $p_3$ y la isotropía del espacio, no la posibilidad de desplazar la trayectoria en vertical.

## 3. Una partícula en un campo central

Una partícula de masa $m$ con energía potencial $V(r)$, de clase $C^2$ para $r := |\vec{q}| > 0$ (en la parte física, $V = e \cdot U$):

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 - V(r), \qquad m \cdot \ddot{\vec{q}} = -V'(r) \cdot \dfrac{\vec{q}}{r}.
\end{aligned}
$$

$V'$ es la derivada de $V$ respecto de $r$, y por la regla de la cadena, $\nabla V = V'(r) \cdot \dfrac{\vec{q}}{r}$. El apartado 3.1 trata una cuestión previa: si la cantidad conservada depende de las coordenadas con que se escriba el movimiento.

### 3.1. La cantidad conservada no depende de las coordenadas

Sea $\vec{q} = \vec{h}(\vec{w})$ un cambio de coordenadas que no depende de $t$: $\vec{h}$ es un difeomorfismo (parte matemática, apartado 6.5) entre un abierto de las nuevas coordenadas $\vec{w} = (w_1, w_2, w_3)$ y uno del espacio, y $J_{\vec{h}}$ es su matriz jacobiana.

* **Velocidades.** Por la regla de la cadena, $\dot{\vec{q}} = J_{\vec{h}} \cdot \dot{\vec{w}}$.
* **Momentos.** Con $\vec{p}_{\vec{w}} := \nabla_{\dot{\vec{w}}} \bsL$ y $\vec{p} = \nabla_{\dot{\vec{q}}} \bsL$, la regla de la cadena da $\vec{p}_{\vec{w}} = J_{\vec{h}}^{\mathsf{T}} \cdot \vec{p}$, donde $\mathsf{T}$ indica la matriz traspuesta.
* **Generadores.** Un desplazamiento infinitesimal se transforma como una velocidad: $\vec{\xi} = J_{\vec{h}} \cdot \vec{\xi}_{\vec{w}}$. Entonces

  $$
  \begin{aligned}
  \vec{p}_{\vec{w}} \cdot \vec{\xi}_{\vec{w}} = \big(J_{\vec{h}}^{\mathsf{T}} \cdot \vec{p}\big) \cdot \vec{\xi}_{\vec{w}} = \vec{p} \cdot \big(J_{\vec{h}} \cdot \vec{\xi}_{\vec{w}}\big) = \vec{p} \cdot \vec{\xi},
  \end{aligned}
  $$

  por la propiedad de la traspuesta, $(J^{\mathsf{T}} \cdot \vec{a}) \cdot \vec{b} = \vec{a} \cdot (J \cdot \vec{b})$.
* **$\bsH$ y $F$** son también los mismos en las dos coordenadas: $\vec{p}_{\vec{w}} \cdot \dot{\vec{w}} = \vec{p} \cdot \dot{\vec{q}}$ por el mismo argumento, y $F$ es una función de los puntos.

Las coordenadas deciden qué cantidades se ven con facilidad, no cuáles existen.

**Coordenadas esféricas.** $q_1 = r \cdot \sin\theta \cdot \cos\phi$, $q_2 = r \cdot \sin\theta \cdot \sin\phi$ y $q_3 = r \cdot \cos\theta$, con $r > 0$ y $0 < \theta < \pi$ (fuera del eje $q_3$, donde son singulares). Entonces

$$
\begin{aligned}
\bsL &= \dfrac{1}{2} \cdot m \cdot \big(\dot{r}^2 + r^2 \cdot \dot{\theta}^2 + r^2 \cdot \sin^2\theta \cdot \dot{\phi}^2\big) - V(r), \\
p_r &= m \cdot \dot{r}, \qquad p_\theta = m \cdot r^2 \cdot \dot{\theta}, \qquad p_\phi = m \cdot r^2 \cdot \sin^2\theta \cdot \dot{\phi}.
\end{aligned}
$$

### 3.2. Giros

**1 a 3, en cartesianas.** Alrededor de un eje $\vec{n}$ que pasa por el centro: $\tau = 0$ y $\vec{\xi} = \vec{n} \times \vec{q}$. A primer orden, $|\vec{q}|^2$ cambia en $2 \cdot \varepsilon \cdot \vec{q} \cdot (\vec{n} \times \vec{q}) = 0$, así que $V(r)$ no cambia; el término cinético tampoco:

$$
\begin{aligned}
D = -\dfrac{V'(r)}{r} \cdot \vec{q} \cdot (\vec{n} \times \vec{q}) + m \cdot \dot{\vec{q}} \cdot (\vec{n} \times \dot{\vec{q}}) = 0,
\end{aligned}
$$

porque un producto mixto con un vector repetido es nulo. Simetría con $F = 0$, y se conserva $Q = \vec{p} \cdot (\vec{n} \times \vec{q}) = \vec{n} \cdot \vec{\ell}$ para todo $\vec{n}$: el vector $\vec{\ell}$.

**4.** Sin resolver la ecuación: $\dfrac{d\vec{\ell}}{dt} = \dot{\vec{q}} \times m \cdot \dot{\vec{q}} + \vec{q} \times m \cdot \ddot{\vec{q}} = \vec{0} - \dfrac{V'(r)}{r} \cdot \vec{q} \times \vec{q} = \vec{0}$.

**En esféricas, alrededor del eje $q_3$.** El giro es $\phi \mapsto \phi + \varepsilon$, con generador $(\xi_r, \xi_\theta, \xi_\phi) = (0, 0, 1)$. $\bsL$ no depende de $\phi$, que es una coordenada **cíclica**: $D = \partial_\phi \bsL = 0$, y se conserva $Q = p_\phi = m \cdot r^2 \cdot \sin^2\theta \cdot \dot{\phi} = \ell_3$. Es la regla de la parte matemática, apartado 6.7, «la función no aparece en $\bsL$»: el momento de una coordenada cíclica se conserva.

**En esféricas, alrededor de los ejes $q_1$ y $q_2$.** No desplazan una sola coordenada esférica. Para el eje $q_1$, el generador cartesiano es $(0, -q_3, q_2)$, que no cambia $r$; con $r$ fijo, se derivan en esa dirección las relaciones $\cos\theta = \dfrac{q_3}{r}$ y $\tan\phi = \dfrac{q_2}{q_1}$:

* $-\sin\theta \cdot \xi_\theta = \dfrac{\xi_3}{r} = \dfrac{q_2}{r} = \sin\theta \cdot \sin\phi$, así que $\xi_\theta = -\sin\phi$;
* $\dfrac{\xi_\phi}{\cos^2\phi} = \dfrac{\xi_2}{q_1} = -\dfrac{q_3}{q_1} = -\dfrac{\cos\theta}{\sin\theta \cdot \cos\phi}$, así que $\xi_\phi = -\cot\theta \cdot \cos\phi$.

Del mismo modo para el eje $q_2$, con el generador cartesiano $(q_3, 0, -q_1)$:

$$
\begin{aligned}
\text{eje } q_1&: \quad (\xi_r, \xi_\theta, \xi_\phi) = (0, -\sin\phi, -\cot\theta \cdot \cos\phi), \\
\text{eje } q_2&: \quad (\xi_r, \xi_\theta, \xi_\phi) = (0, \cos\phi, -\cot\theta \cdot \sin\phi).
\end{aligned}
$$

Con $Q = p_\theta \cdot \xi_\theta + p_\phi \cdot \xi_\phi$ (apartado 3.1):

$$
\begin{aligned}
\ell_1 &= -m \cdot r^2 \cdot \big(\sin\phi \cdot \dot{\theta} + \sin\theta \cdot \cos\theta \cdot \cos\phi \cdot \dot{\phi}\big), \\
\ell_2 &= m \cdot r^2 \cdot \big(\cos\phi \cdot \dot{\theta} - \sin\theta \cdot \cos\theta \cdot \sin\phi \cdot \dot{\phi}\big).
\end{aligned}
$$

Se conservan aunque ninguna coordenada esférica sea cíclica para ellos; con el eje polar en la dirección $q_1$, $\ell_1$ sería el momento de un ángulo cíclico. Además, $|\vec{\ell}|^2 = p_\theta^2 + \dfrac{p_\phi^2}{\sin^2\theta}$.

### 3.3. Traslación en el tiempo

**1 a 3.** $\tau = 1$, $\vec{\xi} = \vec{0}$, $D = \partial_t \bsL = 0$ y $F = 0$. Se conserva $Q = -\bsH$, con

$$
\begin{aligned}
\bsH &= p_r \cdot \dot{r} + p_\theta \cdot \dot{\theta} + p_\phi \cdot \dot{\phi} - \bsL \\
&= \dfrac{1}{2} \cdot m \cdot \big(\dot{r}^2 + r^2 \cdot \dot{\theta}^2 + r^2 \cdot \sin^2\theta \cdot \dot{\phi}^2\big) + V(r) = E,
\end{aligned}
$$

la energía, que en cartesianas es $\dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 + V(r)$, como dice el apartado 3.1.

### 3.4. Traslaciones y cambios de velocidad: no son simetrías

* **Traslación en la dirección $\vec{a}$:** $\tau = 0$, $\vec{\xi} = \vec{a}$ y $\dot{\vec{\xi}} = \vec{0}$, así que $D = -\nabla V \cdot \vec{a} = -\dfrac{V'(r)}{r} \cdot (\vec{a} \cdot \vec{q})$. No depende de las velocidades, así que, por el criterio de la parte física, apartado 2, solo podría depender de $t$. Pero se anula en el plano $\vec{a} \cdot \vec{q} = 0$, así que sería nula en todo punto, y eso obliga a $V'(r) \cdot (\vec{a} \cdot \vec{q}) = 0$ para todo $\vec{q}$, es decir, $V' = 0$. Salvo en la partícula libre, **no** es una simetría, y en efecto $\dot{\vec{p}} = -V'(r) \cdot \dfrac{\vec{q}}{r} \neq \vec{0}$.
* **Cambio de velocidad $\vec{u}$:** $\tau = 0$ y $\vec{\xi} = \vec{u} \cdot t$, así que
  $$
  \begin{aligned}
  D = m \cdot \vec{u} \cdot \dot{\vec{q}} - t \cdot \dfrac{V'(r)}{r} \cdot (\vec{u} \cdot \vec{q}).
  \end{aligned}
  $$
  Es afín en las velocidades, con término independiente $\alpha = -t \cdot \dfrac{V'(r)}{r} \cdot (\vec{u} \cdot \vec{q})$ y coeficientes constantes, $\vec{\beta} = m \cdot \vec{u}$. Las condiciones de integrabilidad (parte matemática, apartado 7.3), $\partial_{q_i} \alpha = \partial_t \beta_i = 0$, exigen que $\alpha$ no dependa de $\vec{q}$; como se anula en el plano $\vec{u} \cdot \vec{q} = 0$, tendría que ser nulo, y otra vez $V' = 0$. Para la partícula libre, $D = \dfrac{d}{dt}\big(m \cdot \vec{u} \cdot \vec{q}\big)$ y se conserva $-\vec{u} \cdot \vec{G}$ (apartado 1).
* **El motivo.** $V(r)$ distingue el origen, el centro de fuerzas: desplazar la trayectoria cambia su distancia a él, y el observador que se mueve con velocidad constante ve moverse el centro, con un potencial que depende explícitamente del tiempo. El apartado 4 muestra dónde están las simetrías perdidas.

### 3.5. La simetría ayuda a resolver

Si $\vec{\ell} \neq \vec{0}$, el movimiento ocurre en el plano perpendicular a $\vec{\ell}$ por el centro, porque $\vec{q} \cdot \vec{\ell} = 0$ en todo instante. Con ese plano como $q_3 = 0$ (es decir, $\theta = \dfrac{\pi}{2}$) y $\ell := p_\phi = m \cdot r^2 \cdot \dot{\phi}$, la energía es

$$
\begin{aligned}
E = \dfrac{1}{2} \cdot m \cdot \dot{r}^2 + \dfrac{\ell^2}{2 \cdot m \cdot r^2} + V(r).
\end{aligned}
$$

Despejando, $\dot{r} = \pm\sqrt{\dfrac{2}{m} \cdot \left(E - V(r) - \dfrac{\ell^2}{2 \cdot m \cdot r^2}\right)}$: una ecuación de primer orden en una sola variable, que se resuelve separando variables, $dt = \dfrac{dr}{\dot{r}(r)}$, en cada tramo en que $\dot{r}$ no cambia de signo. Dos cantidades conservadas reducen un problema de seis condiciones iniciales a integrales de una variable. El término $\dfrac{\ell^2}{2 \cdot m \cdot r^2}$ reaparece en la mecánica cuántica, con $\ell^2$ sustituido por $\hbar^2 \cdot \ell \cdot (\ell + 1)$ (apartado 8.4).

## 4. Dos partículas

Dos partículas con una interacción que solo depende de su distancia, sin campo exterior:

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot m_1 \cdot |\dot{\vec{q}}_1|^2 + \dfrac{1}{2} \cdot m_2 \cdot |\dot{\vec{q}}_2|^2 - V_{12}(r_{12}).
\end{aligned}
$$

Por la tercera etapa de la parte física (apartado 6), se conservan las diez cantidades: $\vec{P}$, $\vec{G}$, $\vec{J}$ y $E$. El cambio de velocidad de las dos partículas, $\vec{\xi}_1 = \vec{\xi}_2 = \vec{u} \cdot t$, no cambia $r_{12}$, y su $F$ es $\vec{u} \cdot (m_1 \cdot \vec{q}_1 + m_2 \cdot \vec{q}_2) = M \cdot \vec{u} \cdot \vec{X}$.

**El centro de masas, resuelto por las simetrías.** Con $M = m_1 + m_2$, $\vec{X}(t) = \dfrac{\vec{G} + \vec{P} \cdot t}{M}$: las traslaciones y los cambios de velocidad dan el movimiento del centro de masas sin resolver ninguna ecuación.

**El movimiento relativo.** Con $\vec{r} := \vec{q}_1 - \vec{q}_2$ y la masa reducida $\bar{m} := \dfrac{m_1 \cdot m_2}{M}$, «El formalismo lagrangiano: ejemplos físicos» escribe $\vec{q}_1 = \vec{X} + \dfrac{m_2}{M} \cdot \vec{r}$ y $\vec{q}_2 = \vec{X} - \dfrac{m_1}{M} \cdot \vec{r}$. Sustituyendo en $\vec{J}$ y en $E$, los términos cruzados se cancelan, porque aparecen con los coeficientes $m_1 \cdot \dfrac{m_2}{M}$ y $-m_2 \cdot \dfrac{m_1}{M}$:

$$
\begin{aligned}
\vec{J} &= M \cdot \vec{X} \times \dot{\vec{X}} + \bar{m} \cdot \vec{r} \times \dot{\vec{r}}, \\
E &= \dfrac{1}{2} \cdot M \cdot |\dot{\vec{X}}|^2 + \dfrac{1}{2} \cdot \bar{m} \cdot |\dot{\vec{r}}|^2 + V_{12}(|\vec{r}|).
\end{aligned}
$$

Como $\vec{X} \times \dot{\vec{X}} = \dfrac{1}{M^2} \cdot (\vec{G} + \vec{P} \cdot t) \times \vec{P} = \dfrac{1}{M^2} \cdot \vec{G} \times \vec{P}$ y $|\dot{\vec{X}}|^2 = \dfrac{|\vec{P}|^2}{M^2}$ son constantes, también lo son el momento angular y la energía del movimiento relativo, $\bar{m} \cdot \vec{r} \times \dot{\vec{r}}$ y $\dfrac{1}{2} \cdot \bar{m} \cdot |\dot{\vec{r}}|^2 + V_{12}(|\vec{r}|)$. El movimiento relativo es el de una partícula de masa $\bar{m}$ en el campo central $V_{12}$, y se resuelve como en el apartado 3.

**Dónde están las simetrías perdidas.** El campo central del apartado 3 es lo que queda de este problema al fijarse en el movimiento relativo. Las traslaciones y los cambios de velocidad de las dos partículas a la vez son simetrías del sistema completo, pero mueven el centro de masas, no $\vec{r}$: en el problema reducido solo quedan los giros y la traslación en el tiempo. Para el potencial de Kepler hay además el vector de Laplace–Runge–Lenz (parte matemática, apartado 9.6), cuyo generador depende de la velocidad.

**El sistema del centro de masas.** Como los cambios de velocidad y las traslaciones son simetrías, el sistema de referencia que se mueve con el centro de masas es tan válido como el de partida, y en él $\vec{P} = \vec{0}$ y $\vec{G} = \vec{0}$.

## 5. Una carga en un campo magnético uniforme

Una partícula de masa $m$ y carga $e$ en $\vec{B} = (0, 0, B)$, con $\vec{A} = \dfrac{1}{2} \cdot \vec{B} \times \vec{q}$ (cuarta etapa de la parte física, apartado 7). Con $\omega_c := \dfrac{e \cdot B}{m}$, «El formalismo lagrangiano: ejemplos físicos» obtiene la hélice

$$
\begin{aligned}
q_1 &= c_1 - \dfrac{v_\perp}{\omega_c} \cdot \sin(\chi - \omega_c \cdot t), \\
q_2 &= c_2 + \dfrac{v_\perp}{\omega_c} \cdot \cos(\chi - \omega_c \cdot t), \\
q_3 &= c_3 + v_\parallel \cdot t,
\end{aligned}
$$

cuya proyección sobre el plano $q_1 q_2$ es una circunferencia de centro $\vec{c} := (c_1, c_2, 0)$ y radio $R := \dfrac{v_\perp}{|\omega_c|}$; $v_\perp$ y $v_\parallel$ son las velocidades perpendicular y paralela a $\vec{B}$, y $\chi$ es una fase constante.

### 5.1. Traslaciones: el centro de la circunferencia

**1 a 3.** Por la parte física, apartado 7, todas las traslaciones son simetrías, con $F = \dfrac{e}{2} \cdot \vec{q} \cdot (\vec{B} \times \vec{a})$, y se conserva $\vec{K} = m \cdot \dot{\vec{q}} - e \cdot \vec{q} \times \vec{B}$. Con $\vec{q} \times \vec{B} = (B \cdot q_2, -B \cdot q_1, 0)$:

$$
\begin{aligned}
\vec{K} = \big(m \cdot \dot{q}_1 - e \cdot B \cdot q_2,\ m \cdot \dot{q}_2 + e \cdot B \cdot q_1,\ m \cdot \dot{q}_3\big).
\end{aligned}
$$

**4.** Sobre la hélice, $\dot{q}_1 = v_\perp \cdot \cos(\chi - \omega_c \cdot t)$ y $\dot{q}_2 = v_\perp \cdot \sin(\chi - \omega_c \cdot t)$. En la primera componente, $e \cdot B \cdot \dfrac{v_\perp}{\omega_c} = m \cdot v_\perp$, y

$$
\begin{aligned}
K_1 = m \cdot v_\perp \cdot \cos(\chi - \omega_c \cdot t) - e \cdot B \cdot c_2 - m \cdot v_\perp \cdot \cos(\chi - \omega_c \cdot t) = -e \cdot B \cdot c_2.
\end{aligned}
$$

Del mismo modo, $K_2 = e \cdot B \cdot c_1$ y $K_3 = m \cdot v_\parallel$. Por tanto,

$$
\begin{aligned}
\vec{K} = e \cdot \vec{B} \times \vec{c} + m \cdot v_\parallel \cdot \vec{e}_3.
\end{aligned}
$$

**Qué significa.** La componente de $\vec{K}$ paralela a $\vec{B}$ es la cantidad de movimiento en esa dirección. Las perpendiculares no son cantidad de movimiento: dan la **posición del centro** de la circunferencia, $\vec{c}$. Trasladar la hélice da otra hélice, con otro centro, y la cantidad asociada a esa simetría es precisamente el centro. La cantidad de movimiento perpendicular, en cambio, gira con la partícula y no se conserva.

### 5.2. Giro alrededor del eje $q_3$

Por la parte física, apartado 7, se conserva el momento angular canónico, $Q = \ell^{\mathrm{cin}}_3 + \dfrac{e \cdot B}{2} \cdot \rho^2$, con $\ell^{\mathrm{cin}}_3 = m \cdot (q_1 \cdot \dot{q}_2 - q_2 \cdot \dot{q}_1)$ y $\rho^2 = q_1^2 + q_2^2$. Sobre la hélice, sustituyendo y usando $\omega_c \cdot R^2 = \dfrac{v_\perp^2}{\omega_c}$, los términos que dependen de $t$ se cancelan y queda

$$
\begin{aligned}
Q = \dfrac{e \cdot B}{2} \cdot \left(c_1^2 + c_2^2 - R^2\right),
\end{aligned}
$$

constante: solo depende de la distancia del centro de la circunferencia al eje y del radio. El momento angular cinético, $\ell^{\mathrm{cin}}_3$, no es constante si el centro no está en el eje.

### 5.3. Energía y cambio de velocidad paralelo a $\vec{B}$

* **Traslación en el tiempo:** $\tau = 1$, $D = \partial_t \bsL = 0$ y $Q = -\bsH$, con $\bsH = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 = \dfrac{1}{2} \cdot m \cdot \left(v_\perp^2 + v_\parallel^2\right)$ sobre la hélice: constante.
* **Cambio de velocidad $\vec{u} = \vec{e}_3$:** es una simetría con $F = m \cdot q_3$, porque $\vec{A}$ no tiene componente $q_3$ y no depende de $q_3$, y da $Q = p_3 \cdot t - m \cdot q_3 = -(m \cdot q_3 - p_3 \cdot t)$, con $p_3 = m \cdot \dot{q}_3$. Sobre la hélice, $m \cdot q_3 - m \cdot v_\parallel \cdot t = m \cdot c_3$: constante.

## 6. La cuerda vibrante

Un ejemplo con dos variables, el de la parte matemática, apartado 8.8, con la densidad lineal de masa $\mu$ y la tensión $T_0$ sin fijar a $1$: $f(t, x)$ es el desplazamiento transversal del punto de la cuerda que está en reposo en $x \in [a_1, b_1]$. Con $(x_0, x_1) = (t, x)$ y una sola función,

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot \mu \cdot (\partial_t f)^2 - \dfrac{1}{2} \cdot T_0 \cdot (\partial_x f)^2, \qquad u_0 = \mu \cdot \partial_t f, \qquad u_1 = -T_0 \cdot \partial_x f.
\end{aligned}
$$

La ecuación de Euler–Lagrange es la de ondas, $\partial_t^2 f = c^2 \cdot \partial_x^2 f$, con $c := \sqrt{T_0/\mu}$, la velocidad de propagación. El tensor de energía-momento (parte matemática, apartado 8.7), con elementos $T_{kl} = u_k \cdot \partial_l f - \delta_{kl} \cdot \bsL$ para $k, l = 0, 1$, es

$$
\begin{aligned}
T &= \begin{pmatrix} \mathcal{E} & \mu \cdot \partial_t f \cdot \partial_x f \\ -T_0 \cdot \partial_x f \cdot \partial_t f & -\mathcal{E} \end{pmatrix}, \\
\mathcal{E} &:= \dfrac{1}{2} \cdot \mu \cdot (\partial_t f)^2 + \dfrac{1}{2} \cdot T_0 \cdot (\partial_x f)^2,
\end{aligned}
$$

donde $\mathcal{E}$ es la densidad de energía, cinética más elástica. La corriente de una simetría es $Q_k = u_k \cdot \xi - \sum_l T_{kl} \cdot \tau_l - F_k$ (parte matemática, apartado 8.6), y la ley integral (apartado 8.7) es $\dfrac{d}{dt} \int_{a_1}^{b_1} Q_0 \,dx = -\Big[Q_1\Big]_{x = a_1}^{x = b_1}$.

### 6.1. Traslación en el tiempo: la energía de la onda

**1.** $\vec{\tau} = (1, 0)$ y $\xi = 0$.

**2.** $\bsL$ no depende de $t$: $D = \partial_t \bsL = 0$, simetría con $\vec{F} = \vec{0}$.

**3.** La corriente es $Q_k = -T_{k0}$:

$$
\begin{aligned}
Q_0 = -\mathcal{E}, \qquad Q_1 = T_0 \cdot \partial_x f \cdot \partial_t f.
\end{aligned}
$$

$-Q_1 = -T_0 \cdot \partial_x f \cdot \partial_t f$ es el flujo de energía: la componente transversal de la tensión, $-T_0 \cdot \partial_x f$, por la velocidad del punto, $\partial_t f$, es la potencia que una parte de la cuerda transmite a la siguiente.

**4.** Con los extremos fijos, $\partial_t f = 0$ en $a_1$ y en $b_1$, y la ley integral da $\dfrac{d}{dt} \int_{a_1}^{b_1} \mathcal{E} \,dx = 0$. Con la onda estacionaria $f = A \cdot \sin\big(k \cdot (x - a_1)\big) \cdot \cos(\omega \cdot t)$, con $k = \dfrac{n \cdot \pi}{b_1 - a_1}$, $n$ entero positivo, y $\omega = c \cdot k$, el cuadrado de un seno o de un coseno integrado en un número entero de semiperiodos da la mitad del intervalo, y

$$
\begin{aligned}
\int_{a_1}^{b_1} \mathcal{E} \,dx &= \dfrac{A^2 \cdot (b_1 - a_1)}{4} \cdot \left(\mu \cdot \omega^2 \cdot \sin^2(\omega \cdot t) + T_0 \cdot k^2 \cdot \cos^2(\omega \cdot t)\right) \\
&= \dfrac{A^2 \cdot (b_1 - a_1) \cdot T_0 \cdot k^2}{4},
\end{aligned}
$$

porque $\mu \cdot \omega^2 = \mu \cdot c^2 \cdot k^2 = T_0 \cdot k^2$: no depende de $t$.

### 6.2. Desplazamiento transversal: una simetría que rompen los extremos

**1.** $f \mapsto f + \varepsilon$: $\vec{\tau} = \vec{0}$ y $\xi = 1$.

**2.** $\bsL$ no depende de $f$: simetría con $\vec{F} = \vec{0}$.

**3.** La corriente es $Q_0 = \mu \cdot \partial_t f$, la densidad de cantidad de movimiento transversal, y $Q_1 = -T_0 \cdot \partial_x f$. La ley local es la propia ecuación de ondas.

**4.** La ley integral da

$$
\begin{aligned}
\dfrac{d}{dt} \int_{a_1}^{b_1} \mu \cdot \partial_t f \,dx = T_0 \cdot \Big[ \partial_x f \Big]_{x = a_1}^{x = b_1},
\end{aligned}
$$

que en general no es nulo: los soportes de los extremos ejercen fuerzas transversales sobre la cuerda. Con la onda estacionaria y $n$ impar, $\int_{a_1}^{b_1} \sin\big(k \cdot (x - a_1)\big) \,dx = \dfrac{2}{k}$, y la cantidad de movimiento transversal total, $-\dfrac{2 \cdot \mu \cdot A \cdot \omega}{k} \cdot \sin(\omega \cdot t)$, cambia con el tiempo.

### 6.3. Traslación en $x$

Es la de la parte matemática, apartado 8.8: la densidad es $Q_0 = -T_{01} = -\mu \cdot \partial_t f \cdot \partial_x f$, la de la cantidad de movimiento de la onda a lo largo de la cuerda, y su flujo, $Q_1 = -T_{11} = \mathcal{E}$, no se anula en los extremos fijos. La ley local se cumple, pero el total no se conserva: $\bsL$ es invariante por traslaciones en $x$, y los extremos no.

### 6.4. El cambio de velocidad de Lorentz

La ecuación de ondas tiene una simetría que no tienen las ecuaciones de Newton: el cambio de velocidad de Lorentz de la parte física, apartado 9.1, en las variables $(t, x)$ y con $c$ la velocidad de las ondas.

**1.** A primer orden, $t \mapsto t + \varepsilon \cdot \dfrac{x}{c^2}$ y $x \mapsto x + \varepsilon \cdot t$, con $f$ sin cambiar: $\vec{\tau} = \left(\dfrac{x}{c^2}, t\right)$ y $\xi = 0$.

**2.** $\bsL$ no depende de $t$, de $x$ ni de $f$, y $\xi = 0$. En la forma de cuatro términos de la parte matemática, apartado 8.3, quedan los términos de las pendientes y el del factor de volumen:

$$
\begin{aligned}
D &\overset{(1)}{=} -\sum_{l=0}^{1} u_l \cdot \sum_{k=0}^{1} \partial_k f \cdot \partial_l \tau_k + \bsL \cdot \sum_{k=0}^{1} \partial_k \tau_k \\
&\overset{(2)}{=} -u_0 \cdot \partial_x f \cdot 1 - u_1 \cdot \partial_t f \cdot \dfrac{1}{c^2} + \bsL \cdot 0 \\
&\overset{(3)}{=} -\mu \cdot \partial_t f \cdot \partial_x f + \dfrac{T_0}{c^2} \cdot \partial_x f \cdot \partial_t f \overset{(4)}{=} 0.
\end{aligned}
$$

**(1)** Forma de cuatro términos con $\xi = 0$, $\partial_f \bsL = 0$ y $\partial_{x_k} \bsL = 0$; los índices $0$ y $1$ son $t$ y $x$. **(2)** Las únicas derivadas no nulas de $\vec{\tau}$ son $\partial_x \tau_0 = \dfrac{1}{c^2}$ y $\partial_t \tau_1 = 1$, y la divergencia, $\partial_t \tau_0 + \partial_x \tau_1$, es nula. **(3)** $u_0 = \mu \cdot \partial_t f$ y $u_1 = -T_0 \cdot \partial_x f$. **(4)** $\dfrac{T_0}{c^2} = \mu$, por la definición de $c$.

Es una simetría con $\vec{F} = \vec{0}$.

**3.** La corriente es $Q_k = -T_{k0} \cdot \dfrac{x}{c^2} - T_{k1} \cdot t$:

$$
\begin{aligned}
Q_0 = -\left(\dfrac{x \cdot \mathcal{E}}{c^2} + t \cdot \mu \cdot \partial_t f \cdot \partial_x f\right), \qquad Q_1 = \mu \cdot x \cdot \partial_x f \cdot \partial_t f + t \cdot \mathcal{E}.
\end{aligned}
$$

**El total.** Si la perturbación no llega a los extremos durante el intervalo de tiempo considerado (por ejemplo, un pulso en una cuerda larga), $f$ y sus derivadas son nulas cerca de $a_1$ y de $b_1$, los flujos de esta corriente y de la de la traslación en $x$ se anulan allí, y se conservan

$$
\begin{aligned}
\mathcal{G} := \int_{a_1}^{b_1} \left(\dfrac{x \cdot \mathcal{E}}{c^2} + t \cdot \mu \cdot \partial_t f \cdot \partial_x f\right) \,dx = \dfrac{E_{\mathrm{c}}}{c^2} \cdot X_{\mathcal{E}} - P_{\mathrm{c}} \cdot t
\end{aligned}
$$

y $P_{\mathrm{c}} := -\int_{a_1}^{b_1} \mu \cdot \partial_t f \cdot \partial_x f \,dx$, la cantidad de movimiento de la onda a lo largo de la cuerda, junto con la energía $E_{\mathrm{c}} := \int_{a_1}^{b_1} \mathcal{E} \,dx$. $X_{\mathcal{E}} := \dfrac{1}{E_{\mathrm{c}}} \cdot \int_{a_1}^{b_1} x \cdot \mathcal{E} \,dx$ es el **centro de energía** de la onda, que se mueve con la velocidad constante $\dfrac{c^2 \cdot P_{\mathrm{c}}}{E_{\mathrm{c}}}$. Es la misma estructura que $\vec{G}_{\mathrm{rel}}$ en la parte física, apartado 9.5.

**4.** Con un pulso que viaja hacia la derecha, $f(t, x) = g(x - c \cdot t)$, con $g$ de clase $C^2$ y nula fuera de un intervalo: $\partial_t f = -c \cdot g'$ y $\partial_x f = g'$, evaluadas en $x - c \cdot t$. Entonces $\mathcal{E} = \dfrac{1}{2} \cdot \mu \cdot c^2 \cdot g'^2 + \dfrac{1}{2} \cdot T_0 \cdot g'^2 = \mu \cdot c^2 \cdot g'^2$, y el integrando de $\mathcal{G}$ es

$$
\begin{aligned}
x \cdot \mu \cdot g'^2 - t \cdot \mu \cdot c \cdot g'^2 = \mu \cdot (x - c \cdot t) \cdot g'(x - c \cdot t)^2.
\end{aligned}
$$

Con el cambio de variable $s = x - c \cdot t$, $\mathcal{G} = \mu \cdot \int s \cdot g'(s)^2 \,ds$, que no depende de $t$. Además, $E_{\mathrm{c}} = \mu \cdot c^2 \cdot \int g'^2 \,ds$ y $P_{\mathrm{c}} = \mu \cdot c \cdot \int g'^2 \,ds$, así que el centro de energía se mueve con velocidad $\dfrac{c^2 \cdot P_{\mathrm{c}}}{E_{\mathrm{c}}} = c$, la del pulso.

### 6.5. El cambio de velocidad de Galileo no es una simetría de la cuerda

**1.** $x \mapsto x + \varepsilon \cdot t$, con $t$ y $f$ sin cambiar: $\vec{\tau} = (0, t)$ y $\xi = 0$.

**2.** La única derivada no nula de $\vec{\tau}$ es $\partial_t \tau_1 = 1$, y $D = -u_0 \cdot \partial_x f = -\mu \cdot \partial_t f \cdot \partial_x f$. Es cuadrática en las derivadas, y la divergencia de un $\vec{F}(t, x, f)$ es afín en ellas (parte matemática, apartado 8.5): **no** es una simetría.

**Qué muestra el ejemplo.** La ecuación de ondas es invariante bajo las transformaciones de Lorentz con $c$ la velocidad de las ondas, y no bajo las de Galileo. Es una simetría matemática de la ecuación, no un cambio de observador: la cuerda en reposo define un sistema de referencia privilegiado, y un observador que se mueve respecto de ella, en la mecánica de Newton, la ve con otra ecuación. Lo mismo ocurre con el sonido. Con la luz no hay medio, y la invariancia de Lorentz de las ecuaciones de Maxwell sí es un cambio de observador (parte física, apartado 9.1). La energía, por su parte, se conserva con los extremos fijos; la cantidad de movimiento transversal y la longitudinal, no. Que la cantidad total se conserve depende del flujo en la frontera, no solo de la simetría de $\bsL$.

## 7. La partícula relativista

### 7.1. Libre

Con $\bsL = -m \cdot c^2 \cdot \sqrt{1 - |\dot{\vec{q}}|^2/c^2}$ (parte física, apartado 9.2), la solución es $\vec{q}(t) = \vec{q}_0 + \vec{v}_0 \cdot t$, con $|\vec{v}_0| < c$. El factor de Lorentz $\gamma_0 := \dfrac{1}{\sqrt{1 - |\vec{v}_0|^2/c^2}}$ es constante, y también $\vec{p} = \gamma_0 \cdot m \cdot \vec{v}_0$, $E = \gamma_0 \cdot m \cdot c^2$ y $\vec{\ell} = \vec{q}_0 \times \vec{p}$. Para el cambio de velocidad (parte física, apartado 9.3),

$$
\begin{aligned}
\vec{G}_{\mathrm{rel}} = \dfrac{E \cdot (\vec{q}_0 + \vec{v}_0 \cdot t)}{c^2} - \gamma_0 \cdot m \cdot \vec{v}_0 \cdot t = \dfrac{E \cdot \vec{q}_0}{c^2},
\end{aligned}
$$

porque $\dfrac{E}{c^2} = \gamma_0 \cdot m$: constante, la energía por la posición inicial, dividida por $c^2$.

### 7.2. En un campo uniforme

Una partícula relativista sometida a una fuerza constante $\kappa > 0$ en la dirección $\vec{e}_1 = (1, 0, 0)$; por ejemplo, una carga $e$ en un campo eléctrico uniforme, con $\kappa$ igual a la carga por la intensidad del campo. La energía potencial es $-\kappa \cdot q_1$ y

$$
\begin{aligned}
\bsL = -m \cdot c^2 \cdot \sqrt{1 - \dfrac{|\dot{\vec{q}}|^2}{c^2}} + \kappa \cdot q_1, \qquad \vec{p} = \gamma \cdot m \cdot \dot{\vec{q}}, \qquad \bsH = \gamma \cdot m \cdot c^2 - \kappa \cdot q_1,
\end{aligned}
$$

con $\gamma$ el factor de Lorentz de la partícula. Las ecuaciones de Euler–Lagrange son $\dot{\vec{p}} = \kappa \cdot \vec{e}_1$. $D$ es lineal en $\bsL$, así que se calcula sumando lo que aporta la parte libre, que es lo del apartado 9.3 de la parte física, y lo que aporta el término $\kappa \cdot q_1$.

* **Traslaciones perpendiculares** a $\vec{e}_1$: $D = 0$, y se conservan $p_2$ y $p_3$.
* **Traslación en la dirección $\vec{e}_1$:** $D = \kappa$, simetría con $F = \kappa \cdot t$, y se conserva $p_1 - \kappa \cdot t$.
* **Giro alrededor del eje $q_1$:** $\bsL$ solo depende de $|\dot{\vec{q}}|$ y de $q_1$, que no cambian. Se conserva $\ell_1$.
* **Traslación en el tiempo:** se conserva $\bsH = \gamma \cdot m \cdot c^2 - \kappa \cdot q_1$, la energía relativista más la potencial.
* **Cambio de velocidad paralelo a la fuerza,** $\tau = \dfrac{u \cdot q_1}{c^2}$ y $\vec{\xi} = u \cdot t \cdot \vec{e}_1$, con $u$ constante. La parte libre aporta $0$ (parte física, apartado 9.3). El término $\kappa \cdot q_1$ aporta, en la forma de cuatro términos, $\partial_{q_1}(\kappa \cdot q_1) \cdot \xi_1 + \kappa \cdot q_1 \cdot \dot{\tau}$:
  $$
  \begin{aligned}
  D = \kappa \cdot u \cdot t + \kappa \cdot q_1 \cdot \dfrac{u \cdot \dot{q}_1}{c^2} = \dfrac{d}{dt}\left(\kappa \cdot u \cdot \left(\dfrac{t^2}{2} + \dfrac{q_1^2}{2 \cdot c^2}\right)\right).
  \end{aligned}
  $$
  Es una simetría con $F = \kappa \cdot u \cdot \left(\dfrac{t^2}{2} + \dfrac{q_1^2}{2 \cdot c^2}\right)$: el análogo relativista del cambio de velocidad del tiro parabólico. Con $Q = p_1 \cdot u \cdot t - \tau \cdot \bsH - F$, y agrupando,
  $$
  \begin{aligned}
  \dfrac{Q}{u} = p_1 \cdot t - \gamma \cdot m \cdot q_1 + \dfrac{\kappa \cdot q_1^2}{2 \cdot c^2} - \dfrac{\kappa \cdot t^2}{2}.
  \end{aligned}
  $$
* **Cambio de velocidad perpendicular a la fuerza,** por ejemplo $\tau = \dfrac{u \cdot q_2}{c^2}$ y $\vec{\xi} = u \cdot t \cdot \vec{e}_2$. La parte libre aporta $0$ y el término $\kappa \cdot q_1$ aporta $D = \kappa \cdot q_1 \cdot \dot{\tau} = \dfrac{\kappa \cdot u}{c^2} \cdot q_1 \cdot \dot{q}_2$. Es afín en las velocidades, con $\alpha = 0$, $\beta_1 = 0$ y $\beta_2 = \dfrac{\kappa \cdot u}{c^2} \cdot q_1$, y la condición de integrabilidad $\partial_{q_1} \beta_2 = \partial_{q_2} \beta_1$ no se cumple, porque el primer lado vale $\dfrac{\kappa \cdot u}{c^2}$ y el segundo, $0$: **no** es una simetría. Si la fuerza es la de un campo eléctrico, un observador que se mueve perpendicularmente al campo mide además un campo magnético.

**Comprobación sobre la solución.** Partiendo del reposo en el origen en $t = 0$, la solución es el **movimiento hiperbólico**:

$$
\begin{aligned}
q_1(t) = \dfrac{m \cdot c^2}{\kappa} \cdot \left(\sqrt{1 + \left(\dfrac{\kappa \cdot t}{m \cdot c}\right)^2} - 1\right), \qquad q_2 = q_3 = 0.
\end{aligned}
$$

* De $\dot{p}_1 = \kappa$ y $p_1(0) = 0$, $p_1 = \kappa \cdot t$: se conserva $p_1 - \kappa \cdot t = 0$.
* Elevando al cuadrado $q_1 + \dfrac{m \cdot c^2}{\kappa} = \dfrac{m \cdot c^2}{\kappa} \cdot \sqrt{1 + \left(\dfrac{\kappa \cdot t}{m \cdot c}\right)^2}$ se obtiene $q_1^2 + \dfrac{2 \cdot m \cdot c^2}{\kappa} \cdot q_1 = c^2 \cdot t^2$, y multiplicando por $\dfrac{\kappa}{2 \cdot c^2}$,
  $$
  \begin{aligned}
  \dfrac{\kappa \cdot q_1^2}{2 \cdot c^2} + m \cdot q_1 = \dfrac{\kappa \cdot t^2}{2}.
  \end{aligned}
  $$
* La energía: $\gamma \cdot m \cdot c^2 = \sqrt{p_1^2 \cdot c^2 + m^2 \cdot c^4} = m \cdot c^2 \cdot \sqrt{1 + \left(\dfrac{\kappa \cdot t}{m \cdot c}\right)^2} = m \cdot c^2 + \kappa \cdot q_1$, y $\bsH = m \cdot c^2$: constante.
* El cambio de velocidad: con $\gamma \cdot m = m + \dfrac{\kappa \cdot q_1}{c^2}$ y $p_1 = \kappa \cdot t$,
  $$
  \begin{aligned}
  \dfrac{Q}{u} &= \kappa \cdot t^2 - m \cdot q_1 - \dfrac{\kappa \cdot q_1^2}{c^2} + \dfrac{\kappa \cdot q_1^2}{2 \cdot c^2} - \dfrac{\kappa \cdot t^2}{2} \\
  &= \dfrac{\kappa \cdot t^2}{2} - m \cdot q_1 - \dfrac{\kappa \cdot q_1^2}{2 \cdot c^2} = 0,
  \end{aligned}
  $$
  por la igualdad anterior: constante.

**El límite de Galileo.** Cuando $c \to \infty$, $\gamma \cdot m \to m$ y $\dfrac{\kappa \cdot q_1^2}{2 \cdot c^2} \to 0$, y $\dfrac{Q}{u} \to p_1 \cdot t - m \cdot q_1 - \dfrac{\kappa \cdot t^2}{2}$: la cantidad del cambio de velocidad del tiro parabólico (apartado 2.5), con la fuerza $\kappa$ en la dirección $q_1$ en lugar de $-m \cdot g$ en la dirección $q_3$. Como en la parte física, apartado 9.4, el término $m \cdot \vec{u} \cdot \vec{q}$ de la $F$ de Galileo procede de $-\tau \cdot \bsH$. Y el cambio de velocidad perpendicular, que falla por un término de orden $\dfrac{1}{c^2}$, es una simetría en el límite, como en el apartado 2.5.

**Qué muestra el ejemplo.** De las diez simetrías de Poincaré, el campo uniforme conserva seis: las tres traslaciones (una con $F \neq 0$), un giro, un cambio de velocidad (con $F \neq 0$) y la traslación en el tiempo. En la mecánica de Newton conservaba ocho (apartado 2): la relatividad pierde los dos cambios de velocidad perpendiculares a la fuerza.

## 8. La partícula cuántica en un potencial central

El análogo cuántico del apartado 3, con la parte física, apartado 10: una partícula de masa $m$ con

$$
\begin{aligned}
\hat{H} = -\dfrac{\hbar^2}{2 \cdot m} \cdot \nabla^2 + V(r).
\end{aligned}
$$

### 8.1. Lo que conmuta con $\hat{H}$

* **Las componentes del momento angular.** $[\hat{H}, \hat{\ell}_k] = 0$ para $k = 1, 2, 3$ (parte física, apartado 10.4), y se conserva $\langle \hat{\vec{\ell}} \rangle$.
* **Su cuadrado**, $\hat{\vec{\ell}}^{\,2} := \hat{\ell}_1^2 + \hat{\ell}_2^2 + \hat{\ell}_3^2$, conmuta con $\hat{H}$, por la regla de Leibniz, y con cada componente. Para $\hat{\ell}_3$, con $[\hat{\ell}_1, \hat{\ell}_3] = -i \cdot \hbar \cdot \hat{\ell}_2$ y $[\hat{\ell}_2, \hat{\ell}_3] = i \cdot \hbar \cdot \hat{\ell}_1$ (las relaciones de la parte física, apartado 10.4, con los índices permutados cíclicamente):
  $$
  \begin{aligned}
  {[\hat{\ell}_1^2, \hat{\ell}_3]} &= \hat{\ell}_1[\hat{\ell}_1, \hat{\ell}_3] + [\hat{\ell}_1, \hat{\ell}_3]\hat{\ell}_1 = -i \cdot \hbar \cdot (\hat{\ell}_1\hat{\ell}_2 + \hat{\ell}_2\hat{\ell}_1), \\
  {[\hat{\ell}_2^2, \hat{\ell}_3]} &= \hat{\ell}_2[\hat{\ell}_2, \hat{\ell}_3] + [\hat{\ell}_2, \hat{\ell}_3]\hat{\ell}_2 = i \cdot \hbar \cdot (\hat{\ell}_2\hat{\ell}_1 + \hat{\ell}_1\hat{\ell}_2),
  \end{aligned}
  $$
  que se cancelan, y $[\hat{\ell}_3^2, \hat{\ell}_3] = 0$.
* **Números cuánticos.** $\hat{H}$, $\hat{\vec{\ell}}^{\,2}$ y $\hat{\ell}_3$ conmutan dos a dos, y los estados estacionarios se pueden elegir funciones propias de los tres (parte física, apartado 10.4). Las componentes $\hat{\ell}_1$ y $\hat{\ell}_2$ no conmutan con $\hat{\ell}_3$, y no pueden tener a la vez valores definidos: de las tres cantidades conservadas del momento angular solo se usan dos, $\hat{\vec{\ell}}^{\,2}$ y una componente.
* **$\hat{\ell}_3$ en esféricas.** Para una función $h(r, \theta, \phi)$, por la regla de la cadena, $\partial_\phi h = \partial_1 h \cdot \partial_\phi q_1 + \partial_2 h \cdot \partial_\phi q_2 = -q_2 \cdot \partial_1 h + q_1 \cdot \partial_2 h$, porque $q_3$ no depende de $\phi$. Por tanto, $\hat{\ell}_3 = -i \cdot \hbar \cdot (q_1 \cdot \partial_2 - q_2 \cdot \partial_1) = -i \cdot \hbar \cdot \partial_\phi$: la versión cuántica de que $\phi$ es cíclica (apartado 3.2). Sus funciones propias son $e^{i \cdot m_\ell \cdot \phi}$, por funciones de $r$ y $\theta$, con valor propio $\hbar \cdot m_\ell$. Como $\phi$ y $\phi + 2 \cdot \pi$ son el mismo punto, la función tiene que tomar el mismo valor en los dos, y $m_\ell$ es un número entero.

### 8.2. Los valores propios del momento angular

Los valores posibles de $\hat{\vec{\ell}}^{\,2}$ y de $\hat{\ell}_3$ se obtienen solo con las relaciones de conmutación (Sakurai y Napolitano, 2017, cap. 3). Definimos los **operadores escalera**, $\hat{\ell}_\pm := \hat{\ell}_1 \pm i \cdot \hat{\ell}_2$.

1. **Suben y bajan $m_\ell$.** Con las relaciones de conmutación, $[\hat{\ell}_3, \hat{\ell}_\pm] = \pm\hbar \cdot \hat{\ell}_\pm$. Si $\hat{\ell}_3 \varphi = \hbar \cdot m_\ell \cdot \varphi$, entonces $\hat{\ell}_3(\hat{\ell}_\pm\varphi) = \hat{\ell}_\pm\hat{\ell}_3\varphi \pm \hbar \cdot \hat{\ell}_\pm\varphi = \hbar \cdot (m_\ell \pm 1) \cdot \hat{\ell}_\pm\varphi$: $\hat{\ell}_\pm\varphi$ es nula o es función propia de $\hat{\ell}_3$ con $m_\ell \pm 1$. (Aquí $\varphi$ es una función propia, no una expresión de Euler–Lagrange.)
2. **No cambian $\hat{\vec{\ell}}^{\,2}$**, porque conmuta con $\hat{\ell}_1$ y con $\hat{\ell}_2$: si $\hat{\vec{\ell}}^{\,2}\varphi = \hbar^2 \cdot \lambda \cdot \varphi$, también $\hat{\vec{\ell}}^{\,2}(\hat{\ell}_\pm\varphi) = \hbar^2 \cdot \lambda \cdot \hat{\ell}_\pm\varphi$.
3. **$m_\ell$ está acotado.** $\langle \varphi, (\hat{\vec{\ell}}^{\,2} - \hat{\ell}_3^2)\varphi \rangle = \lVert \hat{\ell}_1\varphi \rVert^2 + \lVert \hat{\ell}_2\varphi \rVert^2 \geq 0$, porque $\hat{\ell}_1$ y $\hat{\ell}_2$ son autoadjuntos, así que $m_\ell^2 \leq \lambda$. Aplicando $\hat{\ell}_+$ repetidamente, $m_\ell$ crece de uno en uno, y la escalera tiene que terminar: hay un valor máximo $j$ con $\hat{\ell}_+\varphi_j = 0$.
4. **El valor de $\lambda$.** Desarrollando el producto y usando $[\hat{\ell}_1, \hat{\ell}_2] = i \cdot \hbar \cdot \hat{\ell}_3$,
   $$
   \begin{aligned}
   \hat{\ell}_-\hat{\ell}_+ = \hat{\ell}_1^2 + \hat{\ell}_2^2 + i \cdot [\hat{\ell}_1, \hat{\ell}_2] = \hat{\vec{\ell}}^{\,2} - \hat{\ell}_3^2 - \hbar \cdot \hat{\ell}_3.
   \end{aligned}
   $$
   Aplicado a $\varphi_j$, el lado izquierdo es nulo, y el derecho es $\hbar^2 \cdot (\lambda - j^2 - j) \cdot \varphi_j$: $\lambda = j \cdot (j + 1)$. Del mismo modo, con $\hat{\ell}_+\hat{\ell}_- = \hat{\vec{\ell}}^{\,2} - \hat{\ell}_3^2 + \hbar \cdot \hat{\ell}_3$, el valor mínimo $j'$ cumple $\lambda = j'^2 - j'$, y $j' = -j$.
5. **Conclusión.** $m_\ell$ va de $-j$ a $j$ de uno en uno, así que $2 \cdot j$ es un número entero. Para el momento angular orbital, $m_\ell$ es entero (apartado 8.1), y $j$ también. Escribiendo $\ell := j$:
   $$
   \begin{aligned}
   \hat{\vec{\ell}}^{\,2}\varphi &= \hbar^2 \cdot \ell \cdot (\ell + 1) \cdot \varphi, \qquad \hat{\ell}_3\varphi = \hbar \cdot m_\ell \cdot \varphi, \\
   \ell &= 0, 1, 2, \dots, \qquad m_\ell = -\ell, \dots, \ell.
   \end{aligned}
   $$

Los valores semienteros de $j$ no aparecen en el momento angular orbital, pero sí en el **espín**, un momento angular interno de las partículas que no procede de $\hat{\vec{q}} \times \hat{\vec{p}}$. El argumento es formal: supone que las funciones propias están en los dominios de los operadores (parte matemática, apartado 10.2).

### 8.3. Funciones propias

Como $\hat{\vec{\ell}}$ solo deriva en las direcciones que no cambian $r$, sus funciones propias pueden tomarse de los ángulos. Algunas, escritas en cartesianas y en esféricas, salvo constantes multiplicativas:

| $\ell$ | $m_\ell$ | Función propia | En esféricas |
| ------ | ------ | ------------------------------------------ | ------------------------------------ |
| $0$ | $0$ | $1$ | $1$ |
| $1$ | $0$ | $\dfrac{q_3}{r}$ | $\cos\theta$ |
| $1$ | $1$ | $\dfrac{q_1 + i \cdot q_2}{r}$ | $\sin\theta \cdot e^{i \cdot \phi}$ |
| $2$ | $0$ | $\dfrac{3 \cdot q_3^2 - r^2}{r^2}$ | $3 \cdot \cos^2\theta - 1$ |
| $2$ | $1$ | $\dfrac{(q_1 + i \cdot q_2) \cdot q_3}{r^2}$ | $\sin\theta \cdot \cos\theta \cdot e^{i \cdot \phi}$ |
| $2$ | $2$ | $\dfrac{(q_1 + i \cdot q_2)^2}{r^2}$ | $\sin^2\theta \cdot e^{2 \cdot i \cdot \phi}$ |

Table: Funciones propias de $\hat{\vec{\ell}}^{\,2}$ y de $\hat{\ell}_3$.

Son los **armónicos esféricos** de esos valores, sin normalizar. Los de $m_\ell$ negativo se obtienen con $\hat{\ell}_-$, y son los conjugados, con $q_1 - i \cdot q_2$. Que cada fila es función propia con los valores indicados está comprobado con SymPy, aplicando $\hat{\vec{\ell}}^{\,2}$ y $\hat{\ell}_3$ en cartesianas.

### 8.4. La ecuación radial

**El laplaciano y $\hat{\vec{\ell}}^{\,2}$.** Con la derivada radial, $r \cdot \partial_r = \sum_k q_k \cdot \partial_k$, se cumple la identidad

$$
\begin{aligned}
\hat{\vec{\ell}}^{\,2} = -\hbar^2 \cdot \Big(r^2 \cdot \nabla^2 - (r \cdot \partial_r)^2 - r \cdot \partial_r\Big),
\end{aligned}
$$

que se obtiene desarrollando $\sum_k \hat{\ell}_k^2$ con la relación canónica (Sakurai y Napolitano, 2017, cap. 3) y está comprobada con SymPy. Como $(r \cdot \partial_r)^2 + r \cdot \partial_r = r^2 \cdot \partial_r^2 + 2 \cdot r \cdot \partial_r$, por la regla del producto, despejando:

$$
\begin{aligned}
\nabla^2 = \partial_r^2 + \dfrac{2}{r} \cdot \partial_r - \dfrac{\hat{\vec{\ell}}^{\,2}}{\hbar^2 \cdot r^2}.
\end{aligned}
$$

**La separación.** Con $\psi = R(r) \cdot Y$, donde $Y$ es una de las funciones propias del apartado 8.3 (que no depende de $r$, así que $\partial_r Y = 0$), $\hat{H}\psi = E \cdot \psi$ se reduce a una ecuación diferencial ordinaria para $R$:

$$
\begin{aligned}
-\dfrac{\hbar^2}{2 \cdot m} \cdot \left(R'' + \dfrac{2}{r} \cdot R'\right) + \left(V(r) + \dfrac{\hbar^2 \cdot \ell \cdot (\ell + 1)}{2 \cdot m \cdot r^2}\right) \cdot R = E \cdot R.
\end{aligned}
$$

* **El paralelo clásico.** El término $\dfrac{\hbar^2 \cdot \ell \cdot (\ell + 1)}{2 \cdot m \cdot r^2}$ es el $\dfrac{\ell^2}{2 \cdot m \cdot r^2}$ de la energía efectiva del apartado 3.5, con $\ell^2$ sustituido por el valor propio de $\hat{\vec{\ell}}^{\,2}$. En los dos casos, la simetría de rotación reduce un problema de tres variables a uno de la variable $r$.
* **Degeneración.** $\hat{\ell}_\pm$ conmutan con $\hat{H}$, porque $\hat{\ell}_1$ y $\hat{\ell}_2$ lo hacen, y llevan una solución con $m_\ell$ a otra con $m_\ell \pm 1$ y la misma energía. Cada nivel de energía con un $\ell$ dado contiene al menos $2 \cdot \ell + 1$ estados independientes: la **degeneración** que impone la simetría de rotación.

### 8.5. El átomo de hidrógeno y su simetría adicional

Con $V(r) = -\dfrac{k}{r}$, donde $k = \dfrac{e^2}{4 \cdot \pi \cdot \varepsilon_0}$ para el electrón del átomo de hidrógeno y $m$ es su masa (en rigor, la masa reducida del electrón y el protón, apartado 4), los niveles de energía son

$$
\begin{aligned}
E_n = -\dfrac{m \cdot k^2}{2 \cdot \hbar^2 \cdot n^2}, \qquad n = 1, 2, 3, \dots, \qquad \ell = 0, 1, \dots, n - 1.
\end{aligned}
$$

La energía no depende de $\ell$, y el nivel $n$ contiene $\sum_{\ell=0}^{n-1} (2 \cdot \ell + 1) = n^2$ estados, más de los $2 \cdot \ell + 1$ que impone la simetría de rotación. La degeneración adicional procede de otra cantidad conservada: la versión cuántica del vector de Laplace–Runge–Lenz (parte matemática, apartado 9.6), un operador que conmuta con $\hat{H}$. Pauli (1926) obtuvo los niveles de energía del hidrógeno con él, antes de que se resolviera la ecuación de Schrödinger, y Fock (1935) mostró que, junto con $\hat{\vec{\ell}}$, genera una simetría mayor que la de rotación, la de las rotaciones de un espacio de cuatro dimensiones. Como en el caso clásico, esa simetría no procede de ninguna transformación de los puntos $(t, \vec{q})$.

## Referencias

* Fock, V. (1935). Zur Theorie des Wasserstoffatoms. *Zeitschrift für Physik*, *98*(3–4), 145–154.
* Pauli, W. (1926). Über das Wasserstoffspektrum vom Standpunkt der neuen Quantenmechanik. *Zeitschrift für Physik*, *36*(5), 336–363.
* Sakurai, J. J. y Napolitano, J. (2017). *Modern quantum mechanics* (2.ª ed.). Cambridge University Press.

Todas las cuentas de este documento están comprobadas con SymPy en Teorema-de-Noether-v2-comprobaciones.py, en el mismo directorio: para cada ejemplo, $D$, $F$, la cantidad conservada y su comprobación sobre la solución explícita; los generadores en esféricas; las relaciones de conmutación del momento angular, las funciones propias de la tabla del apartado 8.3 y la separación del laplaciano.
