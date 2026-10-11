---
author: "Julián Calderón Almendros"
---

# El teorema de Noether: parte física

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-11
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

**Versión 1.** Este documento pertenece a la versión 1 de la serie, que se conserva. La versión 2, en los documentos con sufijo -v2 de este mismo directorio, es la que se mantiene al día: usa la familia $\Phi_\varepsilon$ en lugar de $\bsT_\epsilon$, transformaciones de los puntos con generador $(\tau, \xi)$ y apartados numerados, y añade, entre otras cosas, los grupos de Lorentz y de Poincaré y la mecánica cuántica no relativista. Las líneas «Fuente:» de la versión para el trabajo remiten a la versión 2.

Este documento aplica «El teorema de Noether: parte matemática» a los sistemas de partículas de «El formalismo lagrangiano: parte física», en sus mismas cuatro etapas:

1. una partícula, libre o en un campo exterior;
2. $N$ partículas sin interacción;
3. partículas con interacciones que dependen de las distancias;
4. cargas en un campo magnético uniforme.

En cada etapa se pregunta qué transformaciones del espacio y del tiempo son simetrías y qué cantidades conservadas dan. Al final, las diez transformaciones se reúnen en el grupo de Galileo. Las cuentas completas de cada caso, con la comprobación sobre la solución explícita, están en «El teorema de Noether: ejemplos físicos», y las rotaciones y el grupo de Galileo, en «El teorema de Noether: anexos».

## Diccionario y notación

| Parte matemática | Sistema de partículas |
| --- | --- |
| variable $x$, en $[a, b]$ | tiempo $t$, en $[t_1, t_2]$ |
| $\vec{f} = (f_1, \dots, f_n)$ | posiciones $(\vec{q}_1, \dots, \vec{q}_N)$, con $n = 3 \cdot N$ |
| $p_i = \partial_{f'_i} \bsL$ | momento canónico $\vec{p}_i := \nabla_{\dot{\vec{q}}_i} \bsL$ |
| $\bsH = \sum_i p_i \cdot f'_i - \bsL$ | hamiltoniano $\bsH = \sum_i \vec{p}_i \cdot \dot{\vec{q}}_i - \bsL$ |
| generador $\vec{\xi}$ | desplazamiento infinitesimal $\vec{\xi}_i$ de cada partícula |
| $\tau$ | desplazamiento infinitesimal del tiempo |
| solución | movimiento real del sistema |
| cantidad conservada $Q$ | ley de conservación |

Table: Diccionario entre la parte matemática y la física.

**Notación**, la de «El formalismo lagrangiano: parte física», y además:

* $i, j = 1, \dots, N$ numeran las partículas; $m_i$ es la masa y $e_i$ la carga de la partícula $i$ respecto del campo exterior ($e_i = m_i$ si el campo es gravitatorio).
* $\vec{\ell}_i := \vec{q}_i \times \vec{p}_i$ es el momento angular de la partícula $i$ respecto del origen.
* Totales: $M := \sum_i m_i$, $\vec{P} := \sum_i \vec{p}_i$, $\vec{J} := \sum_i \vec{\ell}_i$, el centro de masas $\vec{X} := \dfrac{1}{M} \cdot \sum_i m_i \cdot \vec{q}_i$, y $E := T + V$.
* $\vec{G} := M \cdot \vec{X} - \vec{P} \cdot t$ es la cantidad asociada a los cambios de velocidad. No tiene relación con la constante de la gravitación, que en este documento no aparece.
* Para las transformaciones: $\vec{a}$ es un vector constante (dirección de una traslación), $\vec{n}$ un vector unitario constante (eje de un giro que pasa por el origen) y $\vec{u}$ un vector constante (cambio de velocidad).
* $F$ es la función de la definición de simetría. No es una fuerza: las fuerzas llevan siempre flecha, $\vec{F}$.

## El teorema en mecánica

Con el diccionario, la definición y el teorema de la parte matemática se leen así. Un generador asigna a cada partícula un desplazamiento infinitesimal $\vec{\xi}_i$, que puede depender de las posiciones, de las velocidades y del tiempo. Es una **simetría** si existe $F$ tal que, para **toda** trayectoria, real o no,

$$
\begin{aligned}
\bsdelta_{\vec{\xi}} \bsL = \sum_{i=1}^{N} \left( \nabla_{\vec{q}_i} \bsL \cdot \vec{\xi}_i + \vec{p}_i \cdot \dot{\vec{\xi}}_i \right) = \dfrac{dF}{dt}.
\end{aligned}
$$

Entonces, a lo largo de todo **movimiento real**, se conserva

$$
\begin{aligned}
Q = \sum_{i=1}^{N} \vec{p}_i \cdot \vec{\xi}_i - F.
\end{aligned}
$$

Si la transformación desplaza también el tiempo, $t \to t + \epsilon \cdot \tau$, con $\tau$ constante, se conserva $Q = \sum_i \vec{p}_i \cdot \vec{\xi}_i - \tau \cdot \bsH - F$ (parte matemática, «Transformaciones que también mueven la variable»).

**Lectura física.** «Para toda trayectoria» significa que la simetría es una propiedad de la ley, es decir, de $\bsL$, y no de un movimiento concreto. El teorema convierte esa propiedad de la ley en una propiedad de todos los movimientos: una magnitud que no cambia con el tiempo.

**Cuatro pasos**, los mismos en todos los casos:

1. describir la transformación y obtener su generador $\vec{\xi}_i$;
2. calcular $\bsdelta_{\vec{\xi}} \bsL$ y decidir si es una derivada total $\dfrac{dF}{dt}$ (con el criterio de la parte matemática para ver que no lo es);
3. escribir $Q = \sum_i \vec{p}_i \cdot \vec{\xi}_i - F$;
4. comprobar que $Q$ es constante sobre los movimientos reales.

## Las transformaciones del espacio y del tiempo

Para una partícula, las diez transformaciones que usaremos y sus generadores son:

| Transformación | Familia | Generador $\vec{\xi}$ | $\dot{\vec{\xi}}$ |
| --- | --- | --- | --- |
| Traslación en la dirección $\vec{a}$ | $\vec{q} \to \vec{q} + \epsilon \cdot \vec{a}$ | $\vec{a}$ | $\vec{0}$ |
| Giro alrededor del eje $\vec{n}$ | $\vec{q} \to R_{\vec{n}}(\epsilon) \cdot \vec{q}$ | $\vec{n} \times \vec{q}$ | $\vec{n} \times \dot{\vec{q}}$ |
| Cambio de velocidad $\vec{u}$ | $\vec{q} \to \vec{q} + \epsilon \cdot \vec{u} \cdot t$ | $\vec{u} \cdot t$ | $\vec{u}$ |
| Traslación en el tiempo | $\vec{q}(t) \to \vec{q}(t + \epsilon)$ | $\dot{\vec{q}}$ | $\ddot{\vec{q}}$ |

Table: Generadores de las transformaciones del espacio y del tiempo.

* $R_{\vec{n}}(\epsilon)$ es la rotación de ángulo $\epsilon$ alrededor de $\vec{n}$. A primer orden, $R_{\vec{n}}(\epsilon) \cdot \vec{q} = \vec{q} + \epsilon \cdot \vec{n} \times \vec{q} + O(\epsilon^2)$ (anexos, «Rotaciones infinitesimales»).
* Son $3 + 3 + 3 + 1 = 10$ transformaciones independientes: tres direcciones $\vec{a}$, tres ejes $\vec{n}$ y tres velocidades $\vec{u}$ (por ejemplo, las de los ejes coordenados), y la traslación en el tiempo.
* El cambio de velocidad es el paso a otro sistema de referencia inercial que se mueve con velocidad $-\epsilon \cdot \vec{u}$ respecto del primero; aquí se aplica de forma activa, sumando $\epsilon \cdot \vec{u} \cdot t$ a cada trayectoria.
* La traslación en el tiempo admite dos descripciones (parte matemática): con el generador $\dot{\vec{q}}$, como en la tabla, o con $\tau = 1$ y $\vec{\xi} = \vec{0}$. Dan la misma cantidad conservada, salvo el signo. En este documento se usa la primera, salvo en el grupo de Galileo.

Con $N$ partículas, cada transformación se aplica a todas a la vez, con el mismo $\vec{a}$, $\vec{n}$ o $\vec{u}$: $\vec{\xi}_i = \vec{a}$, $\vec{\xi}_i = \vec{n} \times \vec{q}_i$, $\vec{\xi}_i = \vec{u} \cdot t$ o $\vec{\xi}_i = \dot{\vec{q}}_i$.

## Primera etapa: una partícula

### La partícula libre

Sin campo exterior, $\bsL = T = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$, $\vec{p} = m \cdot \dot{\vec{q}}$, y $\bsdelta_{\vec{\xi}} \bsL = m \cdot \dot{\vec{q}} \cdot \dot{\vec{\xi}}$, porque $\bsL$ no depende de $\vec{q}$. Con la tabla anterior:

* **Traslaciones:** $\dot{\vec{\xi}} = \vec{0}$, así que $\bsdelta_{\vec{\xi}} \bsL = 0$ y $F = 0$. Se conserva $Q = \vec{p} \cdot \vec{a}$ para todo $\vec{a}$: **la cantidad de movimiento $\vec{p}$**.
* **Giros:** $\bsdelta_{\vec{\xi}} \bsL = m \cdot \dot{\vec{q}} \cdot (\vec{n} \times \dot{\vec{q}}) = 0$, porque un producto mixto con un vector repetido es nulo. Con $F = 0$, se conserva $Q = \vec{p} \cdot (\vec{n} \times \vec{q}) = \vec{n} \cdot (\vec{q} \times \vec{p}) = \vec{n} \cdot \vec{\ell}$, por la propiedad cíclica del producto mixto. Para todo eje $\vec{n}$: **el momento angular $\vec{\ell}$**.
* **Traslación en el tiempo:** $\bsL$ no depende de $t$; por la identidad de Beltrami, se conserva $\bsH = \vec{p} \cdot \dot{\vec{q}} - \bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$: **la energía**.
* **Cambios de velocidad:** $\bsdelta_{\vec{\xi}} \bsL = m \cdot \dot{\vec{q}} \cdot \vec{u} = \dfrac{d}{dt}\big(m \cdot \vec{u} \cdot \vec{q}\big)$, porque $\vec{u}$ es constante. No es nula, pero es una derivada total, con $F = m \cdot \vec{u} \cdot \vec{q}$. Se conserva
  $$
  \begin{aligned}
  Q = \vec{p} \cdot \vec{u} \cdot t - m \cdot \vec{u} \cdot \vec{q} = -\vec{u} \cdot \big(m \cdot \vec{q} - \vec{p} \cdot t\big)
  \end{aligned}
  $$
  para todo $\vec{u}$: **el vector $\vec{g} := m \cdot \vec{q} - \vec{p} \cdot t$**, que es $\vec{G}$ para una partícula.

Son diez cantidades conservadas, una por transformación. Cada simetría expresa una propiedad del espacio y del tiempo vacíos:

| Propiedad | Simetría | Cantidad conservada |
| --- | --- | --- |
| El espacio no tiene puntos privilegiados (homogeneidad) | traslaciones | $\vec{p}$ |
| El espacio no tiene direcciones privilegiadas (isotropía) | giros | $\vec{\ell}$ |
| El tiempo no tiene instantes privilegiados | traslación en el tiempo | $E$ |
| No hay sistemas inerciales privilegiados (relatividad de Galileo) | cambios de velocidad | $\vec{g}$ |

Table: Las simetrías de la partícula libre.

**Qué dicen.** $\vec{p}$ constante es la primera ley de Newton: la partícula libre se mueve con velocidad constante. $\vec{g}$ constante dice además dónde está: en $t = 0$, $\vec{g} = m \cdot \vec{q}(0)$, y $\vec{q}(t) = \dfrac{\vec{g} + \vec{p} \cdot t}{m}$. Las cantidades conservadas determinan la trayectoria entera.

**No son independientes.** Para una partícula libre, $\vec{\ell} = \vec{q} \times \vec{p} = \dfrac{1}{m} \cdot (\vec{g} + \vec{p} \cdot t) \times \vec{p} = \dfrac{1}{m} \cdot \vec{g} \times \vec{p}$ y $E = \dfrac{|\vec{p}|^2}{2 \cdot m}$: los valores de $\vec{\ell}$ y de $E$ se deducen de los de $\vec{p}$ y $\vec{g}$. Diez simetrías dan diez cantidades conservadas, pero no diez datos independientes. Con varias partículas que interaccionan, en cambio, las diez cantidades totales son independientes (tercera etapa).

### Una partícula en un campo exterior

Con un campo exterior estático, $\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 - V(\vec{q})$. El término cinético se comporta como en la partícula libre, y lo nuevo es lo que hace $V$:

$$
\begin{aligned}
\bsdelta_{\vec{\xi}} \bsL = m \cdot \dot{\vec{q}} \cdot \dot{\vec{\xi}} - \nabla V \cdot \vec{\xi}.
\end{aligned}
$$

* **Traslación en la dirección $\vec{a}$:** $\bsdelta_{\vec{\xi}} \bsL = -\nabla V \cdot \vec{a}$, que no depende de $\dot{\vec{q}}$. Por el criterio de la parte matemática, es una simetría si y solo si $\nabla V \cdot \vec{a}$ es constante, digamos $\nabla V \cdot \vec{a} = -c$, y entonces $F = c \cdot t$. El campo tiene que ser uniforme en la dirección $\vec{a}$.
* **Giro alrededor de $\vec{n}$:** $\bsdelta_{\vec{\xi}} \bsL = -\nabla V \cdot (\vec{n} \times \vec{q})$, que es la derivada de $V$ respecto del ángulo de giro alrededor de $\vec{n}$. Por el mismo criterio, tendría que ser constante. Si $V$ es continua en una circunferencia completa alrededor del eje, esa constante es nula: al dar una vuelta, $V$ cambiaría en $2 \cdot \pi$ por la constante, y volvería a su valor inicial. Es una simetría si y solo si $V$ no cambia al girar alrededor de $\vec{n}$, y entonces $F = 0$.
* **Cambio de velocidad $\vec{u}$:** $\bsdelta_{\vec{\xi}} \bsL = \dfrac{d}{dt}\big(m \cdot \vec{u} \cdot \vec{q}\big) - t \cdot \nabla V \cdot \vec{u}$. El último término es una derivada total si y solo si $\nabla V \cdot \vec{u}$ es constante: la misma condición que la traslación en la dirección $\vec{u}$.
* **Traslación en el tiempo:** es una simetría porque $V$ no depende de $t$.

Tres campos de «El formalismo lagrangiano: parte física»:

| | Sin campo, $V = 0$ | Uniforme, $V = -e \cdot \vec{g} \cdot \vec{q}$ | Central, $V = e \cdot U(\lvert\vec{q}\rvert)$ |
| --- | --- | --- | --- |
| Traslaciones | 3 | 3 | 0 |
| Giros | 3 | 1 | 3 |
| Cambios de velocidad | 3 | 3 | 0 |
| Traslación en el tiempo | 1 | 1 | 1 |
| Total | 10 | 8 | 4 |

Table: Simetrías que quedan en cada campo exterior.

* **Campo uniforme.** $\nabla V = -e \cdot \vec{g}$ es constante, así que todas las traslaciones y todos los cambios de velocidad son simetrías, aunque en la dirección de $\vec{g}$ con $F \neq 0$. Los giros solo lo son alrededor de un eje paralelo a $\vec{g}$. El campo uniforme no distingue puntos, pero sí una dirección: rompe la isotropía, no la homogeneidad. La traslación en la dirección $\vec{a}$ da $Q = \vec{a} \cdot (\vec{p} - e \cdot \vec{g} \cdot t)$: lo que se conserva no es $\vec{p}$, sino $\vec{p} - e \cdot \vec{g} \cdot t$, que es la segunda ley de Newton, $\dot{\vec{p}} = e \cdot \vec{g}$, integrada una vez. Con la gravedad y el eje $z$ vertical hacia arriba, $e \cdot \vec{g} = (0, 0, -m \cdot g)$: se conservan $p_x$, $p_y$ y $p_z + m \cdot g \cdot t$, pero no $p_z$.
* **Campo central.** $\nabla V = e \cdot U'(r) \cdot \dfrac{\vec{q}}{r}$ depende de $\vec{q}$ en cualquier dirección: ninguna traslación ni ningún cambio de velocidad es una simetría. El centro es un punto privilegiado. Quedan los giros alrededor de cualquier eje que pase por el centro, porque $V$ solo depende de $|\vec{q}|$, y la traslación en el tiempo. Se conservan $\vec{\ell}$ y $E$, que son las dos leyes que «El formalismo lagrangiano: parte física» («Energía y momento angular») obtenía por cálculo directo y relacionaba con dos simetrías de $\bsL$. Ahora son consecuencia del teorema.

## Segunda etapa: $N$ partículas sin interacción

Sin interacción, $\bsL = \sum_i \bsL_i$, donde $\bsL_i = \dfrac{1}{2} \cdot m_i \cdot |\dot{\vec{q}}_i|^2 - e_i \cdot U(r_i)$ solo depende de las variables de la partícula $i$. Hay más simetrías que con una partícula: las que transforman **una sola** partícula y dejan las demás quietas, es decir, con $\vec{\xi}_j = \vec{0}$ para $j \neq i$. Entonces $\bsdelta_{\vec{\xi}} \bsL = \bsdelta_{\vec{\xi}_i} \bsL_i$, y es una simetría de $\bsL$ si lo es de $\bsL_i$:

* el giro de la partícula $i$ sola da $\vec{\ell}_i$;
* la traslación en el tiempo de la partícula $i$ sola, $\vec{\xi}_i = \dot{\vec{q}}_i$, da $\bsdelta_{\vec{\xi}} \bsL = \dfrac{d\bsL_i}{dt}$, con $F = \bsL_i$, y $Q = \vec{p}_i \cdot \dot{\vec{q}}_i - \bsL_i = E_i$, la energía de la partícula $i$.

Se conservan la energía y el momento angular de cada partícula por separado, como afirmaba «El formalismo lagrangiano: parte física». La causa es que cada partícula puede transformarse sin que las demás lo noten.

## Tercera etapa: interacciones que dependen de las distancias

Con interacción,

$$
\begin{aligned}
\bsL = \sum_{i=1}^{N} \dfrac{1}{2} \cdot m_i \cdot |\dot{\vec{q}}_i|^2 - \sum_{i=1}^{N} e_i \cdot U(r_i) - \sum_{i<j} V_{ij}(r_{ij}).
\end{aligned}
$$

Transformar una sola partícula cambia las distancias $r_{ij}$, y en general deja de ser una simetría. Quedan las transformaciones de todas las partículas a la vez:

* **Traslaciones,** $\vec{\xi}_i = \vec{a}$. Las diferencias $\vec{q}_i - \vec{q}_j$ no cambian, y $V_{ij}(r_{ij})$ tampoco. Sin campo exterior ($U = 0$) es una simetría con $F = 0$, y se conserva $Q = \sum_i \vec{p}_i \cdot \vec{a} = \vec{a} \cdot \vec{P}$: **la cantidad de movimiento total**. No la de cada partícula: lo que no tiene puntos privilegiados es el sistema en su conjunto.
* **Giros,** $\vec{\xi}_i = \vec{n} \times \vec{q}_i$. A primer orden, $|\vec{w}|^2$ cambia en $2 \cdot \epsilon \cdot \vec{w} \cdot (\vec{n} \times \vec{w}) = 0$, tanto para $\vec{w} = \vec{q}_i - \vec{q}_j$ como para $\vec{w} = \vec{q}_i$, así que $V$ no cambia, con campo central o sin él. El término cinético tampoco, como en la primera etapa. Se conserva $Q = \sum_i \vec{p}_i \cdot (\vec{n} \times \vec{q}_i) = \vec{n} \cdot \vec{J}$: **el momento angular total**.
* **Cambios de velocidad,** $\vec{\xi}_i = \vec{u} \cdot t$. Las diferencias no cambian, y sin campo exterior $V$ tampoco. El término cinético da $\sum_i m_i \cdot \dot{\vec{q}}_i \cdot \vec{u} = \dfrac{d}{dt}\big(M \cdot \vec{u} \cdot \vec{X}\big)$, con $F = M \cdot \vec{u} \cdot \vec{X}$, y se conserva $Q = \sum_i \vec{p}_i \cdot \vec{u} \cdot t - M \cdot \vec{u} \cdot \vec{X} = -\vec{u} \cdot \vec{G}$: **el vector $\vec{G} = M \cdot \vec{X} - \vec{P} \cdot t$**.
* **Traslación en el tiempo:** $\bsL$ no depende de $t$, y se conserva $\bsH = T + V = E$.

| Simetría | Condición sobre $V$ | Cantidad conservada |
| --- | --- | --- |
| Traslación en el tiempo | $V$ no depende de $t$ | $E = T + V$ |
| Traslaciones | $V$ solo depende de las diferencias $\vec{q}_i - \vec{q}_j$ | $\vec{P}$ |
| Giros | $V$ no cambia al girar todas las posiciones; por ejemplo, si solo depende de las distancias | $\vec{J}$ |
| Cambios de velocidad | la de las traslaciones | $\vec{G}$ |

Table: Condiciones sobre la energía potencial y cantidades conservadas.

Sin campo exterior se conservan las diez cantidades: $E$, $\vec{P}$, $\vec{J}$ y $\vec{G}$. Con campo central, solo $\vec{J}$ y $E$. Es lo que «El formalismo lagrangiano: parte física» («Tercera etapa › Cantidades conservadas») obtenía con la tercera ley de Newton; aquí la tercera ley no se usa, porque está contenida en que $V$ solo dependa de las diferencias.

**El vector $\vec{G}$ y el centro de masas.** Por la definición de $\vec{X}$, $\dfrac{d}{dt}\big(M \cdot \vec{X}\big) = \vec{P}$, así que $\dfrac{d\vec{G}}{dt} = -\dfrac{d\vec{P}}{dt} \cdot t$, y la conservación de $\vec{G}$ se sigue de la de $\vec{P}$. Lo que añade es su valor: $\vec{G} = M \cdot \vec{X}(0)$, y $\vec{X}(t) = \dfrac{\vec{G} + \vec{P} \cdot t}{M}$. El centro de masas se mueve con velocidad constante, como una partícula libre de masa $M$.

## Cuarta etapa: cargas en un campo magnético uniforme

Con $\vec{B}$ uniforme y constante y el potencial vector $\vec{A}(\vec{q}) = \dfrac{1}{2} \cdot \vec{B} \times \vec{q}$,

$$
\begin{aligned}
\bsL = \sum_{i=1}^{N} \left( \dfrac{1}{2} \cdot m_i \cdot |\dot{\vec{q}}_i|^2 + e_i \cdot \dot{\vec{q}}_i \cdot \vec{A}(\vec{q}_i) \right) - \sum_{i<j} \dfrac{e_i \cdot e_j}{4 \cdot \pi \cdot \varepsilon_0 \cdot r_{ij}}.
\end{aligned}
$$

El momento canónico es $\vec{p}_i = m_i \cdot \dot{\vec{q}}_i + e_i \cdot \vec{A}(\vec{q}_i)$, distinto de la cantidad de movimiento. El término de Coulomb se comporta como en la tercera etapa; lo nuevo es el término magnético.

* **Traslaciones,** $\vec{\xi}_i = \vec{a}$. Como $\vec{A}(\vec{q}_i + \epsilon \cdot \vec{a}) = \vec{A}(\vec{q}_i) + \dfrac{\epsilon}{2} \cdot \vec{B} \times \vec{a}$, el término magnético cambia en
  $$
  \begin{aligned}
  \bsdelta_{\vec{\xi}} \bsL = \sum_{i=1}^{N} \dfrac{e_i}{2} \cdot \dot{\vec{q}}_i \cdot (\vec{B} \times \vec{a}) = \dfrac{d}{dt}\left( \sum_{i=1}^{N} \dfrac{e_i}{2} \cdot \vec{q}_i \cdot (\vec{B} \times \vec{a}) \right),
  \end{aligned}
  $$
  porque $\vec{B} \times \vec{a}$ es constante. Es una simetría para todo $\vec{a}$, con $F = \sum_i \dfrac{e_i}{2} \cdot \vec{q}_i \cdot (\vec{B} \times \vec{a})$. Con $\vec{q}_i \cdot (\vec{B} \times \vec{a}) = -\vec{a} \cdot (\vec{B} \times \vec{q}_i)$, por la propiedad cíclica del producto mixto,
  $$
  \begin{aligned}
  Q = \sum_{i=1}^{N} \left( m_i \cdot \dot{\vec{q}}_i + \dfrac{e_i}{2} \cdot \vec{B} \times \vec{q}_i \right) \cdot \vec{a} + \sum_{i=1}^{N} \dfrac{e_i}{2} \cdot \vec{a} \cdot (\vec{B} \times \vec{q}_i) = \vec{a} \cdot \vec{K},
  \end{aligned}
  $$
  con $\vec{K} := \sum_i \left( m_i \cdot \dot{\vec{q}}_i - e_i \cdot \vec{q}_i \times \vec{B} \right)$. Es la cantidad que «El formalismo lagrangiano: parte física» dejaba para el teorema de Noether. Su componente paralela a $\vec{B}$ es la de la cantidad de movimiento total, porque $(\vec{q}_i \times \vec{B}) \cdot \vec{B} = 0$; la perpendicular no. Para una carga, $\vec{K}$ da el centro de la circunferencia que describe (ejemplos físicos).
* **Por qué aparece $F$.** Trasladar las cargas equivale a cambiar $\vec{A}$ por $\vec{A} + \dfrac{1}{2} \cdot \vec{B} \times \vec{a}$, que es el gradiente de $\dfrac{1}{2} \cdot (\vec{B} \times \vec{a}) \cdot \vec{q}$: un cambio del potencial vector que no cambia $\vec{B}$, y que cambia $\bsL$ en una derivada total («El formalismo lagrangiano: parte física», cuarta etapa).
* **Giros alrededor de un eje paralelo a $\vec{B}$,** $\vec{n} = \dfrac{\vec{B}}{|\vec{B}|}$. Si $R$ es un giro alrededor de $\vec{n}$, $R \cdot \vec{B} = \vec{B}$, y $\vec{A}(R \cdot \vec{q}) = \dfrac{1}{2} \cdot (R \cdot \vec{B}) \times (R \cdot \vec{q}) = R \cdot \vec{A}(\vec{q})$, porque un giro conserva el producto vectorial. El producto escalar $\dot{\vec{q}}_i \cdot \vec{A}(\vec{q}_i)$ no cambia, y $F = 0$. Con la fórmula del doble producto vectorial,
  $$
  \begin{aligned}
  Q = \vec{n} \cdot \sum_{i=1}^{N} \vec{q}_i \times \vec{p}_i = \sum_{i=1}^{N} \left( \vec{n} \cdot \vec{\ell}^{\,\mathrm{cin}}_i + \dfrac{e_i \cdot |\vec{B}|}{2} \cdot \rho_i^2 \right),
  \end{aligned}
  $$
  donde $\vec{\ell}^{\,\mathrm{cin}}_i := \vec{q}_i \times m_i \cdot \dot{\vec{q}}_i$ y $\rho_i$ es la distancia de la partícula $i$ al eje. Se conserva el momento angular canónico, no el cinético.
* **Giros alrededor de otros ejes:** no son simetrías; $\vec{B}$ distingue una dirección.
* **Cambios de velocidad:** solo en la dirección de $\vec{B}$. Para $\vec{u}$ perpendicular a $\vec{B}$ queda un término $-\sum_i e_i \cdot \vec{q}_i \cdot (\vec{B} \times \vec{u})$ que depende de las posiciones y no de las velocidades, y que no es una derivada total. Físicamente, un observador en movimiento perpendicular a $\vec{B}$ mide además un campo eléctrico.
* **Traslación en el tiempo:** el término lineal en las velocidades no contribuye a $\bsH$, porque $\dot{\vec{q}}_i \cdot \partial_{\dot{\vec{q}}_i}\big(e_i \cdot \dot{\vec{q}}_i \cdot \vec{A}\big) = e_i \cdot \dot{\vec{q}}_i \cdot \vec{A}$. Se conserva $\bsH = T + \sum_{i<j} \dfrac{e_i \cdot e_j}{4 \cdot \pi \cdot \varepsilon_0 \cdot r_{ij}}$, la que «El formalismo lagrangiano: parte física» justificaba porque la fuerza magnética no realiza trabajo.

De las diez transformaciones, el campo magnético uniforme conserva seis: las tres traslaciones (con $F \neq 0$), un giro, un cambio de velocidad y la traslación en el tiempo.

## El grupo de Galileo

Las diez transformaciones de la partícula libre se componen entre sí y forman un grupo de diez parámetros, el **grupo de Galileo** (anexos). Un generador general combina los diez, con coeficientes $\vec{\omega}$ (giro), $\vec{u}$ (cambio de velocidad), $\vec{a}$ (traslación) y $\tau$ (tiempo):

$$
\begin{aligned}
\vec{\xi}_i = \vec{\omega} \times \vec{q}_i + \vec{u} \cdot t + \vec{a}, \qquad t \to t + \epsilon \cdot \tau.
\end{aligned}
$$

Para $N$ partículas sin campo exterior, con la fórmula de las transformaciones que mueven el tiempo y $F = M \cdot \vec{u} \cdot \vec{X}$ (solo el cambio de velocidad contribuye a $F$):

$$
\begin{aligned}
Q = \sum_{i=1}^{N} \vec{p}_i \cdot \vec{\xi}_i - \tau \cdot \bsH - F = \vec{\omega} \cdot \vec{J} - \vec{u} \cdot \vec{G} + \vec{a} \cdot \vec{P} - \tau \cdot \bsH.
\end{aligned}
$$

Término a término: $\sum_i \vec{p}_i \cdot (\vec{\omega} \times \vec{q}_i) = \vec{\omega} \cdot \vec{J}$ por la propiedad cíclica del producto mixto; $\sum_i \vec{p}_i \cdot \vec{u} \cdot t - M \cdot \vec{u} \cdot \vec{X} = -\vec{u} \cdot \vec{G}$; y $\sum_i \vec{p}_i \cdot \vec{a} = \vec{a} \cdot \vec{P}$. $Q$ se conserva para cualquier elección de los diez coeficientes y es lineal en ellos. Eligiendo todos nulos salvo uno, se conserva cada una de las diez cantidades por separado: las tres componentes de $\vec{J}$, de $\vec{G}$ y de $\vec{P}$, y $\bsH = E$.

Con SymPy, para tres partículas con una energía potencial cualquiera de las distancias, en `cuadernos/tema1/noether_galileo.py` (apuntes públicos): la invariancia de $\bsL$ bajo cada generador, las cantidades de Noether y su conservación sobre las soluciones.

## Lo que el teorema no dice

* **Las simetrías discretas no dan cantidades conservadas por este camino.** La reflexión $\vec{q} \to -\vec{q}$ puede dejar $\bsL$ igual, pero no depende de un parámetro continuo, no tiene generador y el teorema no se aplica.
* **La simetría es de la ley, no de cada movimiento.** En un campo central, $\bsL$ es invariante bajo todos los giros, pero una órbita elíptica concreta no lo es. Lo que el teorema garantiza es que la cantidad asociada, $\vec{\ell}$, es constante en cada movimiento. Un giro lleva cada movimiento real a otro movimiento real, en general distinto.
* **Una transformación que no es simetría no implica que la cantidad no se conserve en ningún movimiento.** En el campo central, $\vec{p}$ no se conserva en general, pero en un movimiento con $\vec{q}$ en reposo en un punto de equilibrio, si existiera, sería constante. El teorema habla de todos los movimientos a la vez.
