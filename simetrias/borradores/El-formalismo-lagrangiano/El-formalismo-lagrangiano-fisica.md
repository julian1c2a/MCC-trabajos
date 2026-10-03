---
author: "Julián Calderón Almendros"
---

# El formalismo lagrangiano: parte física

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-03
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

Este documento aplica la parte matemática («El formalismo lagrangiano: parte matemática») a masas puntuales que se mueven en el espacio tridimensional, y determina $\bsL(\vec{q}, \dot{\vec{q}}, t)$ a partir de las leyes de Newton: $\vec{p} = m \cdot \dot{\vec{q}}$ y $\vec{F} = m \cdot \vec{a}$. Se hace en cuatro etapas de complejidad creciente:

1. una partícula en un campo central;
2. $N$ partículas en el mismo campo, sin interacción entre ellas;
3. dos o tres partículas con interacciones que dependen de las distancias;
4. dos o tres cargas con interacción de Coulomb en un campo magnético exterior, que introduce una fuerza dependiente de la velocidad.

Los ejemplos están en «El formalismo lagrangiano: ejemplos físicos», y los resultados matemáticos auxiliares (que sumar una derivada total o cambiar de coordenadas no altera las ecuaciones de Euler–Lagrange, y la forma más general del potencial), en «El formalismo lagrangiano: anexos». Las leyes físicas se introducen en la primera etapa; hasta entonces todo es matemática.

## Diccionario y notación

Las funciones solo dependen del tiempo: hay una sola variable, que ahora se llama $t$ y recorre $[t_1, t_2]$. Cada partícula tiene tres coordenadas.

| Parte matemática | Sistema de partículas |
| --- | --- |
| variable $x$, en $[a, b]$ | tiempo $t$, en $[t_1, t_2]$ |
| $\vec{f} = (f_1, \dots, f_n)$ | $\vec{q} = (\vec{q}_1, \dots, \vec{q}_N)$, con $n = 3 \cdot N$ |
| componente $f_i$ | coordenada $q_{i,\alpha}$ de la partícula $i$ |
| derivada $f'_i$ | componente de la velocidad, $\dot{q}_{i,\alpha} := \dfrac{d q_{i,\alpha}}{dt}$ |
| solución $\vec{f}_0$ | trayectoria real del sistema |
| matriz $W$ | matriz de masas |

**Notación:**

* $i, j = 1, \dots, N$ numeran las partículas, y $\alpha = 1, 2, 3$, las componentes espaciales: $\vec{q}_i = (q_{i,1}, q_{i,2}, q_{i,3})$.
* $m_i > 0$ es la masa de la partícula $i$ (en la primera etapa, simplemente $m$). En la parte física, $m$ es siempre una masa: el número de variables de la parte matemática vale $1$ y no se escribe.
* $e_i$ es la carga de la partícula $i$ respecto del campo que actúa sobre ella (en la primera etapa, $e$). No se usa $q$ para la carga, porque $\vec{q}$ es la posición. Si el campo es gravitatorio, la carga es la masa: $e_i = m_i$.
* $r_i := |\vec{q}_i|$ es la distancia de la partícula $i$ al centro del campo, y $r_{ij} := |\vec{q}_i - \vec{q}_j|$, la distancia entre las partículas $i$ y $j$.
* $\nabla_{\vec{q}_i} \bsL := \left(\partial_{q_{i,1}} \bsL, \partial_{q_{i,2}} \bsL, \partial_{q_{i,3}} \bsL\right)$, y lo mismo $\nabla_{\dot{\vec{q}}_i} \bsL$ con las velocidades.
* $\vec{\ell}_i := \vec{q}_i \times \vec{p}_i$ es el momento angular de la partícula $i$ respecto del origen.

**Las ecuaciones de Euler–Lagrange, todavía sin física.** Por el caso particular de curvas en $\mathbb{R}^n$ de la parte matemática, con $n = 3 \cdot N$, la trayectoria hace estacionario a $\bsS[\vec{q}] = \int_{t_1}^{t_2} \bsL(\vec{q}, \dot{\vec{q}}, t) \,dt$ si y solo si

$$
\begin{aligned}
\nabla_{\vec{q}_i} \bsL - \dfrac{d}{dt}\Big(\nabla_{\dot{\vec{q}}_i} \bsL\Big) = \vec{0}, \qquad i = 1, \dots, N,
\end{aligned}
$$

que son tres ecuaciones por partícula, una por componente.

## Primera etapa: una partícula en un campo central

### Las leyes físicas y las hipótesis

**Hipótesis:** la masa $m > 0$ y la carga $e$ son constantes; trabajamos en un sistema de referencia inercial, con el origen en el centro del campo, que está en reposo; la partícula no pasa por el centro, $|\vec{q}(t)| > 0$.

**Leyes:**

$$
\begin{aligned}
\vec{p} := m \cdot \dot{\vec{q}}, \qquad \dfrac{d\vec{p}}{dt} = \vec{F}.
\end{aligned}
$$

La primera define la cantidad de movimiento, y la segunda es la segunda ley de Newton. Como $m$ es constante, juntas dan $m \cdot \ddot{\vec{q}} = \vec{F}$.

### El campo central y su potencial

La intensidad del campo es la fuerza por unidad de carga. Solo depende de la posición, tiene la dirección de la recta que une el punto con el centro y su módulo solo depende de la distancia $r = |\vec{q}|$:

$$
\begin{aligned}
\vec{g}(\vec{q}) = g(r) \cdot \dfrac{\vec{q}}{r}, \qquad r := |\vec{q}| > 0,
\end{aligned}
$$

con $g: (0, \infty) \to \mathbb{R}$ de clase $C^1$. La fuerza sobre la partícula es $\vec{F} = e \cdot \vec{g}(\vec{q})$. Ejemplos:

* **Campo gravitatorio** de una masa $M$ fija en el origen: $g(r) = -\dfrac{G \cdot M}{r^2}$, y la carga es la masa, $e = m$. Entonces $m \cdot \ddot{\vec{q}} = m \cdot \vec{g}$ y la masa se simplifica: el movimiento no depende de ella. Es la igualdad entre masa inercial y masa gravitatoria.
* **Campo eléctrico** de una carga $Q$ fija en el origen: $g(r) = \dfrac{Q}{4 \cdot \pi \cdot \varepsilon_0 \cdot r^2}$. Aquí la carga $e$ y la masa $m$ son independientes.

**El campo deriva de un potencial.** Fijamos $r_0 > 0$ y definimos $U(r) := -\int_{r_0}^{r} g(\rho) \,d\rho$, de modo que $U'(r) = -g(r)$. Como $\partial_{q_\alpha} |\vec{q}| = \dfrac{q_\alpha}{r}$, la regla de la cadena da

$$
\begin{aligned}
\nabla U(|\vec{q}|) = U'(r) \cdot \dfrac{\vec{q}}{r} = -\vec{g}(\vec{q}).
\end{aligned}
$$

Con la energía potencial $V(\vec{q}) := e \cdot U(|\vec{q}|)$, la fuerza es $\vec{F} = -\nabla V$. En los ejemplos, salvo una constante aditiva que no afecta a la fuerza, $U(r) = -\dfrac{G \cdot M}{r}$ y $U(r) = \dfrac{Q}{4 \cdot \pi \cdot \varepsilon_0 \cdot r}$.

### La determinación de $\bsL$

Las ecuaciones de Newton y las de Euler–Lagrange tienen la misma forma:

$$
\begin{aligned}
\dfrac{d}{dt}\big(m \cdot \dot{\vec{q}}\big) = -\nabla V, \qquad \dfrac{d}{dt}\Big(\nabla_{\dot{\vec{q}}} \bsL\Big) = \nabla_{\vec{q}} \bsL.
\end{aligned}
$$

Para que coincidan basta con que coincidan término a término:

* **(A)** $\nabla_{\dot{\vec{q}}} \bsL = m \cdot \dot{\vec{q}} = \vec{p}$. Aquí entra la ley $\vec{p} = m \cdot \dot{\vec{q}}$: la cantidad de movimiento es la derivada de $\bsL$ respecto de la velocidad.
* **(B)** $\nabla_{\vec{q}} \bsL = -\nabla V = \vec{F}$. Aquí entra el campo: la fuerza es la derivada de $\bsL$ respecto de la posición.

**De (A):** la función $\bsL - \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$ tiene derivadas nulas respecto de las tres velocidades, y como $\mathbb{R}^3$ es conexo, no depende de ellas: $\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 + \Phi(\vec{q}, t)$.

**De (B):** $\nabla \Phi = -\nabla V$, así que $\Phi + V$ tiene gradiente nulo en $\mathbb{R}^3 \setminus \{\vec{0}\}$, que es conexo: $\Phi = -V + c(t)$. La función $c(t)$ es la derivada total de una primitiva suya, que no cambia las ecuaciones (anexos, «Requisito matemático previo»), y tomamos $c = 0$:

$$
\begin{aligned}
\bsL(\vec{q}, \dot{\vec{q}}, t) = T - V = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 - e \cdot U(|\vec{q}|).
\end{aligned}
$$

**$\bsL$ no es única.** Las condiciones (A) y (B) son suficientes, no necesarias: $\lambda \cdot \bsL$, con $\lambda \neq 0$ constante, y $\bsL + \dfrac{d}{dt} G(\vec{q}, t)$ dan las mismas ecuaciones (anexos, «Requisito matemático previo»). Lo que fija $\bsL = T - V$ es exigir (A).

### Comprobación y problema de valores iniciales

Con $\bsL = T - V$, las ecuaciones de Euler–Lagrange son $m \cdot \ddot{\vec{q}} = e \cdot g(r) \cdot \dfrac{\vec{q}}{r}$. La matriz $W$ es $m$ por la identidad, que es invertible. El principio variacional fija $\vec{q}(t_1)$ y $\vec{q}(t_2)$, pero el problema físico se plantea con la posición y la velocidad iniciales; como $g$ es de clase $C^1$, el teorema de Picard–Lindelöf (Tema 1, apartado 4.4.2) da solución única, al menos en un intervalo alrededor de $t_1$.

### Energía y momento angular

* **Energía:** $\bsL$ no depende explícitamente de $t$, y $E := T + V$ se conserva: $\dfrac{dE}{dt} = \dot{\vec{q}} \cdot \big(m \cdot \ddot{\vec{q}} + \nabla V\big) = 0$.
* **Momento angular:** $\vec{\ell}$ se conserva, porque $\dfrac{d\vec{\ell}}{dt} = \dot{\vec{q}} \times (m \cdot \dot{\vec{q}}) + \vec{q} \times \vec{F} = \vec{0}$, ya que $\vec{F}$ es paralela a $\vec{q}$. Si $\vec{\ell} \neq \vec{0}$, el movimiento es plano: ocurre en el plano que pasa por el centro y es perpendicular a $\vec{\ell}$.

Las dos leyes corresponden a dos simetrías de $\bsL$: no depende de $t$, y $U$ solo depende de $|\vec{q}|$, es decir, no cambia al girar alrededor del centro. Es lo que el teorema de Noether hará general. En el plano del movimiento, con coordenadas polares, el problema se reduce a una sola variable; se desarrolla en los ejemplos físicos («Coordenadas polares, potencial efectivo y órbitas de Kepler»).

## Segunda etapa: $N$ partículas sin interacción

Las mismas hipótesis, para cada partícula. La fuerza sobre la partícula $i$ es la del campo, $\vec{F}_i = e_i \cdot \vec{g}(\vec{q}_i) = -\nabla_{\vec{q}_i} V$, con

$$
\begin{aligned}
V(\vec{q}_1, \dots, \vec{q}_N) := \sum_{i=1}^{N} e_i \cdot U(r_i),
\end{aligned}
$$

porque solo el sumando $i$ depende de $\vec{q}_i$. El razonamiento de la primera etapa, con (A) y (B) para cada partícula y el dominio $\left(\mathbb{R}^3 \setminus \{\vec{0}\}\right)^N$, que es conexo, da

$$
\begin{aligned}
\bsL = T - V = \sum_{i=1}^{N} \left( \dfrac{1}{2} \cdot m_i \cdot |\dot{\vec{q}}_i|^2 - e_i \cdot U(r_i) \right).
\end{aligned}
$$

**Lo nuevo es poco:** $\bsL$ es una suma de lagrangianos de una partícula, cada uno con sus propias variables. Las ecuaciones de la partícula $i$ solo contienen $\vec{q}_i$: están desacopladas, y cada partícula se mueve como en la primera etapa. La matriz $W$ es diagonal, con cada $m_i$ repetida tres veces. Se conservan la energía total y, además, la energía y el momento angular de cada partícula por separado.

## Tercera etapa: interacciones que dependen de las distancias

### La tercera ley de Newton

Sea $\vec{F}_{ij}$ la fuerza que la partícula $j$ ejerce sobre la $i$. Suponemos que cumple la tercera ley de Newton, $\vec{F}_{ji} = -\vec{F}_{ij}$, que tiene la dirección de la recta que une las dos partículas y que su módulo solo depende de la distancia entre ellas:

$$
\begin{aligned}
\vec{F}_{ij} = F_{ij}(r_{ij}) \cdot \dfrac{\vec{q}_i - \vec{q}_j}{r_{ij}}, \qquad F_{ij} = F_{ji},
\end{aligned}
$$

con $F_{ij}: (0, \infty) \to \mathbb{R}$ de clase $C^1$, positiva si la fuerza es repulsiva. La fuerza total sobre la partícula $i$ es $\vec{F}_i = e_i \cdot \vec{g}(\vec{q}_i) + \sum_{j \neq i} \vec{F}_{ij}$. Hipótesis adicional: no hay choques, $r_{ij}(t) > 0$. Consideramos dos o tres partículas.

### El potencial de interacción y $\bsL$

Para cada pareja definimos $V_{ij}(r) := -\int_{r_0}^{r} F_{ij}(\rho) \,d\rho$, que cumple $V_{ij} = V_{ji}$. Por la regla de la cadena, $\nabla_{\vec{q}_i} V_{ij}(r_{ij}) = -\vec{F}_{ij}$ y $\nabla_{\vec{q}_j} V_{ij}(r_{ij}) = -\vec{F}_{ji}$. Con la energía potencial total

$$
\begin{aligned}
V := \sum_{i=1}^{N} e_i \cdot U(r_i) + \sum_{i<j} V_{ij}(r_{ij}),
\end{aligned}
$$

se cumple $\vec{F}_i = -\nabla_{\vec{q}_i} V$ para cada $i$, y el razonamiento de la primera etapa da otra vez $\bsL = T - V$. El dominio de las posiciones, sin el centro y sin los choques, sigue siendo conexo, porque se le quitan conjuntos de dimensión $3 \cdot N - 3$.

**Ahora las ecuaciones están acopladas:** la de la partícula $i$ contiene las posiciones de todas las demás. La matriz $W$ sigue siendo diagonal, porque la interacción no depende de las velocidades.

Ejemplos: la gravitación mutua, $V_{ij}(r) = -\dfrac{G \cdot m_i \cdot m_j}{r}$, y la interacción de Coulomb, $V_{ij}(r) = \dfrac{e_i \cdot e_j}{4 \cdot \pi \cdot \varepsilon_0 \cdot r}$. Con dos partículas y sin campo exterior, el problema se reduce a la primera etapa mediante el centro de masas y la masa reducida; se desarrolla en los ejemplos físicos («Dos partículas: centro de masas y masa reducida»).

### Cantidades conservadas

Con tres partículas no hay una solución general en forma cerrada (el problema de los tres cuerpos), pero sí cantidades conservadas:

* **la energía** $E = T + V$, porque $\bsL$ no depende de $t$;
* **el momento angular total**, $\sum_i \vec{\ell}_i$, porque las fuerzas del campo son centrales y, en cada pareja, $\vec{q}_i \times \vec{F}_{ij} + \vec{q}_j \times \vec{F}_{ji} = (\vec{q}_i - \vec{q}_j) \times \vec{F}_{ij} = \vec{0}$;
* **la cantidad de movimiento total**, $\sum_i \vec{p}_i$, solo si no hay campo exterior: las fuerzas internas se cancelan por parejas por la tercera ley.

En términos de simetrías: sin campo exterior, $V$ solo depende de las distancias $r_{ij}$ y no cambia al trasladar todas las partículas a la vez; con campo central, solo queda la simetría de los giros alrededor del centro.

## Cuarta etapa: cargas con interacción de Coulomb en un campo magnético exterior

### Una fuerza que depende de la velocidad

Un campo magnético estático $\vec{B}(\vec{q})$ ejerce sobre una carga $e$ la fuerza de Lorentz $\vec{F} = e \cdot \dot{\vec{q}} \times \vec{B}(\vec{q})$, que depende de la velocidad. La condición (B) no puede cumplirse con un $V$ que solo dependa de las posiciones. Se escribe $\vec{B} = \nabla \times \vec{A}$, con $\vec{A}$ el potencial vector, y se toma un potencial que depende linealmente de la velocidad, $V = -e \cdot \dot{\vec{q}} \cdot \vec{A}(\vec{q})$. En los anexos («La forma más general del potencial en $\bsL = T - V$») se demuestra que esta es, esencialmente, la única dependencia de la velocidad compatible con la forma $m \cdot \ddot{\vec{q}} = \vec{F}$.

### Una carga en el campo magnético

$$
\begin{aligned}
\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 + e \cdot \dot{\vec{q}} \cdot \vec{A}(\vec{q}).
\end{aligned}
$$

**Comprobación:** $\nabla_{\dot{\vec{q}}} \bsL = m \cdot \dot{\vec{q}} + e \cdot \vec{A}$, cuya derivada respecto de $t$ es $m \cdot \ddot{\vec{q}} + e \cdot (\dot{\vec{q}} \cdot \nabla) \vec{A}$, y $\nabla_{\vec{q}} \bsL = e \cdot \nabla(\dot{\vec{q}} \cdot \vec{A})$. Con la identidad $\nabla(\vec{v} \cdot \vec{A}) - (\vec{v} \cdot \nabla)\vec{A} = \vec{v} \times (\nabla \times \vec{A})$, para $\vec{v}$ fijo, queda $m \cdot \ddot{\vec{q}} = e \cdot \dot{\vec{q}} \times \vec{B}$.

**Observaciones:**

* **$\vec{p} = m \cdot \dot{\vec{q}}$ deja de ser la derivada de $\bsL$.** $\nabla_{\dot{\vec{q}}} \bsL = m \cdot \dot{\vec{q}} + e \cdot \vec{A}$ es el momento canónico (Tema 1, apartado 7.5). En las tres primeras etapas coincidía con la cantidad de movimiento; aquí no, y la condición (A) deja de valer tal cual.
* **$\vec{A}$ no es único:** $\vec{A} + \nabla \chi$ da el mismo $\vec{B}$, y cambia $\bsL$ en $e \cdot \dot{\vec{q}} \cdot \nabla \chi = \dfrac{d}{dt}\big(e \cdot \chi(\vec{q})\big)$, una derivada total que no altera las ecuaciones (anexos, «Requisito matemático previo»).
* **La fuerza magnética no realiza trabajo:** $\dot{\vec{q}} \cdot (\dot{\vec{q}} \times \vec{B}) = 0$, y se conserva $\dot{\vec{q}} \cdot \nabla_{\dot{\vec{q}}} \bsL - \bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$.
* **Con $\vec{B}$ uniforme**, la trayectoria es una hélice cuyo eje es paralelo a $\vec{B}$; se desarrolla en los ejemplos físicos («Una carga en un campo magnético uniforme»).

### Dos o tres cargas

Juntando la interacción de Coulomb de la tercera etapa y el campo magnético:

$$
\begin{aligned}
\bsL = \sum_{i=1}^{N} \dfrac{1}{2} \cdot m_i \cdot |\dot{\vec{q}}_i|^2 - \sum_{i<j} \dfrac{e_i \cdot e_j}{4 \cdot \pi \cdot \varepsilon_0 \cdot r_{ij}} + \sum_{i=1}^{N} e_i \cdot \dot{\vec{q}}_i \cdot \vec{A}(\vec{q}_i),
\end{aligned}
$$

con $N = 2$ o $N = 3$. Las ecuaciones de Euler–Lagrange son

$$
\begin{aligned}
m_i \cdot \ddot{\vec{q}}_i = \sum_{j \neq i} \dfrac{e_i \cdot e_j}{4 \cdot \pi \cdot \varepsilon_0} \cdot \dfrac{\vec{q}_i - \vec{q}_j}{r_{ij}^3} + e_i \cdot \dot{\vec{q}}_i \times \vec{B}(\vec{q}_i), \qquad i = 1, \dots, N.
\end{aligned}
$$

**Estructura:** las ecuaciones están acopladas por las posiciones (Coulomb), pero no por las aceleraciones: el término magnético es lineal en las velocidades, y $W$ sigue siendo la matriz de masas, diagonal (anexos, «La forma más general del potencial en $\bsL = T - V$»).

**Cantidades conservadas:**

* $T + \sum_{i<j} \dfrac{e_i \cdot e_j}{4 \cdot \pi \cdot \varepsilon_0 \cdot r_{ij}}$, porque $\bsL$ no depende de $t$ y la fuerza magnética no realiza trabajo.
* La cantidad de movimiento total no se conserva, porque la fuerza magnética es exterior. Con $\vec{B}$ uniforme y constante se conserva en su lugar la combinación $\vec{K} := \sum_i \left(m_i \cdot \dot{\vec{q}}_i - e_i \cdot \vec{q}_i \times \vec{B}\right)$, asociada a las traslaciones; se estudiará con el teorema de Noether.
