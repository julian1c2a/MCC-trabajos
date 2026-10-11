---
author: "Julián Calderón Almendros"
---

# El teorema de Noether: parte física (versión 2)

* **Asignatura:** Complementos de Mecánica Cuántica (Máster en Computación Cuántica)
* **Propósito:** apuntes de autoestudio elaborados para preparar la asignatura.
* **Última edición:** 2026-10-11
* **Autor:** Julián Calderón Almendros
* **Correo electrónico:** julian.calderon.almendros at gmail.com
* **GitHub:** [\@julian1c2a](https://github.com/julian1c2a)
* **Proyecto:** <https://github.com/julian1c2a/MCC>
* **Licencia:** [Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Se permite copiar, redistribuir, modificar y reutilizar este material con cualquier finalidad, incluso comercial, siempre que se reconozca la autoría original, se enlace la licencia y se indique si se han hecho cambios.

Este documento aplica «El teorema de Noether: parte matemática (versión 2)» a los sistemas de partículas de «El formalismo lagrangiano: parte física», en sus mismas cuatro etapas:

1. una partícula, libre o en un campo exterior;
2. $N$ partículas sin interacción;
3. partículas con interacciones que dependen de las distancias;
4. cargas en un campo magnético uniforme.

En cada etapa se pregunta qué transformaciones del espacio y del tiempo son simetrías y qué cantidades conservadas dan. Las diez transformaciones de la partícula libre se reúnen después en el grupo de Galileo (apartado 8). Los dos últimos apartados salen de la mecánica de Newton: el grupo de Lorentz y el de Poincaré, con la partícula libre relativista y su límite de Galileo (apartado 9), y la mecánica cuántica no relativista, explicada desde el principio, con la forma que toma el teorema para un hamiltoniano cuántico (apartado 10).

La versión 2 de la serie consta de cinco documentos:

* «El teorema de Noether: parte matemática (versión 2)»: la teoría, con una función, varias funciones y varias variables, los flujos, las derivadas de Fréchet y de Lie, y una guía de dimensión infinita.
* «El teorema de Noether: ejemplos matemáticos (versión 2)»: el camino más corto, como gráfica y en forma paramétrica, las ecuaciones con la estructura de las de Newton y la ecuación de Laplace.
* «El teorema de Noether: parte física (versión 2)», este documento.
* «El teorema de Noether: ejemplos físicos (versión 2)»: los casos de la parte física con la comprobación sobre la solución explícita, la cuerda con el cambio de velocidad de Lorentz, la partícula relativista y la partícula cuántica en un potencial central.
* «El teorema de Noether: anexos (versión 2)»: las rotaciones, la exponencial de una matriz y los grupos de Galileo, de Lorentz y de Poincaré en forma de matrices, con la contracción de Poincaré a Galileo y la carga central.

Las citas «parte matemática, apartado X» se refieren a la versión 2. Las rotaciones y los grupos de Galileo, de Lorentz y de Poincaré se desarrollan en «El teorema de Noether: anexos (versión 2)», que se cita como «anexos».

**Diferencias con la versión 1**, cuyos documentos se conservan:

* la versión 1 escribe la familia de transformaciones $\bsT_\epsilon$, con el parámetro $\epsilon$; la versión 2 usa $\Phi_\varepsilon$ y $\varepsilon$, como el trabajo «La importancia de las simetrías en física»;
* las transformaciones actúan sobre los puntos $(t, \vec{q}_1, \dots, \vec{q}_N)$, con un generador $(\tau, \vec{\xi})$, y la condición de simetría se escribe con el término $D$ de la parte matemática;
* la traslación en el tiempo se describe con $\tau = 1$ y $\vec{\xi} = \vec{0}$, y su cantidad conservada es $-\bsH$;
* la intensidad del campo uniforme se sigue llamando $\vec{g}$, y la cantidad asociada a los cambios de velocidad de una partícula es $\vec{G}$ (la versión 1 usaba $\vec{g}$ para las dos);
* los apartados 9 y 10 son nuevos.

## 1. Diccionario y notación

### 1.1. Diccionario

| Parte matemática | Sistema de partículas |
| ------------------------------------ | ---------------------------------------------------- |
| variable $x$, en $[a, b]$ | tiempo $t$, en $[t_1, t_2]$ |
| $\vec{f} = (f_1, \dots, f_n)$ | posiciones $(\vec{q}_1, \dots, \vec{q}_N)$, con $n = 3 \cdot N$ |
| punto $(x, \vec{y})$ de $\mathbb{R}^{1+n}$ | instante y posiciones, $(t, \vec{q}_1, \dots, \vec{q}_N)$ |
| prima, $f'_i$ | punto, $\dot{\vec{q}}_i$ |
| $p_i = \partial_{f'_i} \bsL$ | momento canónico $\vec{p}_i := \nabla_{\dot{\vec{q}}_i} \bsL$ |
| $\varphi_i = \partial_{f_i} \bsL - p'_i$ | $\vec{\varphi}_i := \nabla_{\vec{q}_i} \bsL - \dot{\vec{p}}_i$ |
| $\bsH = \sum_i p_i \cdot f'_i - \bsL$ | hamiltoniano $\bsH = \sum_i \vec{p}_i \cdot \dot{\vec{q}}_i - \bsL$ |
| generador $(\tau, \vec{\xi})$ | desplazamiento infinitesimal del tiempo, $\tau$, y de cada partícula, $\vec{\xi}_i$ |
| $F(x, \vec{y})$ | $F(t, \vec{q}_1, \dots, \vec{q}_N)$ |
| solución | movimiento real del sistema |
| cantidad conservada $Q$ | ley de conservación |

Table: Diccionario entre la parte matemática y la física.

$\nabla_{\vec{q}_i} \bsL$ es el vector de las derivadas parciales de $\bsL$ respecto de las tres componentes de $\vec{q}_i$, y $\nabla_{\dot{\vec{q}}_i} \bsL$, el de las derivadas respecto de las tres componentes de $\dot{\vec{q}}_i$. Las ecuaciones de Euler–Lagrange son $\vec{\varphi}_i = \vec{0}$, $i = 1, \dots, N$.

### 1.2. Notación

La de «El formalismo lagrangiano: parte física», y además:

* $i, j = 1, \dots, N$ numeran las partículas; $m_i$ es la masa y $e_i$ la carga de la partícula $i$ respecto del campo exterior ($e_i = m_i$ si el campo es gravitatorio).
* $\vec{\ell}_i := \vec{q}_i \times \vec{p}_i$ es el momento angular de la partícula $i$ respecto del origen.
* Totales: $M := \sum_i m_i$, $\vec{P} := \sum_i \vec{p}_i$, $\vec{J} := \sum_i \vec{\ell}_i$, el centro de masas $\vec{X} := \dfrac{1}{M} \cdot \sum_i m_i \cdot \vec{q}_i$, y la energía $E := T + V$, con $T$ la energía cinética y $V$ la potencial.
* $\vec{G} := M \cdot \vec{X} - \vec{P} \cdot t$ es la cantidad asociada a los cambios de velocidad; para una partícula, $\vec{G} = m \cdot \vec{q} - \vec{p} \cdot t$. No tiene relación con la constante de la gravitación, que en este documento no aparece.
* Para las transformaciones: $\vec{a}$ es un vector constante (dirección de una traslación), $\vec{n}$ un vector unitario constante (eje de un giro que pasa por el origen) y $\vec{u}$ un vector constante (cambio de velocidad).
* $F$ es la función de la definición de simetría. No es una fuerza: las fuerzas llevan siempre flecha, $\vec{F}$.
* El punto indica la derivada respecto del tiempo **a lo largo de la trayectoria**. Para una función $G(t, \vec{q}_1, \dots, \vec{q}_N)$, por la regla de la cadena, $\dot{G} = \partial_t G + \sum_i \nabla_{\vec{q}_i} G \cdot \dot{\vec{q}}_i$.

### 1.3. Avisos de notación

* $i$: el índice de las partículas; en el apartado 10, la unidad imaginaria, y allí las partículas se numeran con $j$.
* $c$: la velocidad de la luz en el apartado 9; en la cuerda vibrante (apartado 9.5 y parte matemática, apartado 8.8), la velocidad de propagación de las ondas.
* $\vec{g}$, con minúscula, es la intensidad de un campo uniforme; $\vec{G}$, con mayúscula, la cantidad de los cambios de velocidad.
* $H$: $\bsH$, en negrita, es el hamiltoniano clásico; $\hat{H}$, con gorro, el operador hamiltoniano (apartado 10).
* $\vec{A}$: el potencial vector (apartado 7); $\hat{A}$, con gorro, un operador (apartado 10).
* $E$: la energía. En la parte matemática, $E$ es también un espacio de Banach, que aquí no aparece.
* $T$: la energía cinética; $T_{\mu\nu}$, con dos índices, el tensor de energía-momento de la parte matemática, apartado 8.7.
* $m$: una masa. En la parte matemática, apartado 8, es el número de variables.
* $\gamma$: el factor de Lorentz (apartado 9).
* $\tau$: la componente temporal del generador. El tiempo propio del apartado 9 no lleva símbolo.

## 2. El teorema en mecánica

**Las transformaciones.** Una familia de transformaciones de los puntos $(t, \vec{q}_1, \dots, \vec{q}_N)$, que depende de un parámetro real $\varepsilon$ y es la identidad para $\varepsilon = 0$, desplaza a primer orden el instante y cada posición:

$$
\begin{aligned}
t \mapsto t + \varepsilon \cdot \tau(t, \vec{q}_1, \dots, \vec{q}_N) + O(\varepsilon^2), \qquad \vec{q}_i \mapsto \vec{q}_i + \varepsilon \cdot \vec{\xi}_i(t, \vec{q}_1, \dots, \vec{q}_N) + O(\varepsilon^2).
\end{aligned}
$$

Es el caso de $n = 3 \cdot N$ funciones de la parte matemática, apartado 7. El generador puede depender del tiempo y de todas las posiciones, pero no de las velocidades (las que dependen de ellas son las del apartado 9.6 de la parte matemática).

**El término $D$.** Con la forma de cuatro términos de la parte matemática (apartado 5), componente a componente,

$$
\begin{aligned}
D = \sum_{i=1}^{N} \Big( \nabla_{\vec{q}_i} \bsL \cdot \vec{\xi}_i + \vec{p}_i \cdot \big(\dot{\vec{\xi}}_i - \dot{\tau} \cdot \dot{\vec{q}}_i\big) \Big) + \partial_t \bsL \cdot \tau + \bsL \cdot \dot{\tau}.
\end{aligned}
$$

**La definición.** La familia es una **simetría** si existe una función $F(t, \vec{q}_1, \dots, \vec{q}_N)$ tal que, para **toda** trayectoria de clase $C^2$, real o no,

$$
\begin{aligned}
D = \dot{F} = \partial_t F + \sum_{i=1}^{N} \nabla_{\vec{q}_i} F \cdot \dot{\vec{q}}_i.
\end{aligned}
$$

**El teorema** (parte matemática, apartado 7.4). Para toda trayectoria se cumple la identidad

$$
\begin{aligned}
\dfrac{d}{dt}\Big(\sum_{i=1}^{N} \vec{p}_i \cdot \vec{\xi}_i - \tau \cdot \bsH - F\Big) = -\sum_{i=1}^{N} \vec{\varphi}_i \cdot \big(\vec{\xi}_i - \tau \cdot \dot{\vec{q}}_i\big),
\end{aligned}
$$

y, por tanto, a lo largo de todo **movimiento real**, en el que las $\vec{\varphi}_i$ son nulas, se conserva

$$
\begin{aligned}
Q := \sum_{i=1}^{N} \vec{p}_i \cdot \vec{\xi}_i - \tau \cdot \bsH - F.
\end{aligned}
$$

**Cuándo existe $F$** (parte matemática, apartado 7.3). $D$ tiene que ser una función afín de las velocidades, $D = \alpha + \sum_i \vec{\beta}_i \cdot \dot{\vec{q}}_i$, con $\partial_t F = \alpha$ y $\nabla_{\vec{q}_i} F = \vec{\beta}_i$, y se tienen que cumplir las condiciones de integrabilidad. Un caso que se usa a menudo: si $D$ no depende de las velocidades, las $\vec{\beta}_i$ son nulas, $F$ solo depende de $t$ y $D$ tampoco puede depender de las posiciones.

**Lectura física.** «Para toda trayectoria» significa que la simetría es una propiedad de la ley, es decir, de $\bsL$, y no de un movimiento concreto. El teorema convierte esa propiedad de la ley en una propiedad de todos los movimientos: una magnitud que no cambia con el tiempo.

**Cuatro pasos**, los mismos en todos los casos:

1. describir la transformación y obtener su generador $(\tau, \vec{\xi}_i)$;
2. calcular $D$ con la forma de cuatro términos y decidir si es una derivada total $\dot{F}$;
3. escribir $Q = \sum_i \vec{p}_i \cdot \vec{\xi}_i - \tau \cdot \bsH - F$;
4. comprobar que $Q$ es constante sobre los movimientos reales.

**Transformaciones activas y pasivas.** Las transformaciones de este documento son **activas**: mueven el sistema y dejan quieto al observador. Cambiar de observador equivale a la transformación inversa, la de $-\varepsilon$: el generador, $F$ y $Q$ cambian de signo, y la cantidad conservada es la misma salvo el signo.

## 3. Las transformaciones del espacio y del tiempo

Para una partícula, las diez transformaciones que usaremos y sus generadores son:

| Transformación | Familia | $\tau$ | $\vec{\xi}$ |
| ---------------------------------- | ------------------------------------------------ | --------- | ------------------------ |
| Traslación en la dirección $\vec{a}$ | $\vec{q} \mapsto \vec{q} + \varepsilon \cdot \vec{a}$ | $0$ | $\vec{a}$ |
| Giro alrededor del eje $\vec{n}$ | $\vec{q} \mapsto R_{\vec{n}}(\varepsilon) \cdot \vec{q}$ | $0$ | $\vec{n} \times \vec{q}$ |
| Cambio de velocidad $\vec{u}$ | $\vec{q} \mapsto \vec{q} + \varepsilon \cdot \vec{u} \cdot t$ | $0$ | $\vec{u} \cdot t$ |
| Traslación en el tiempo | $t \mapsto t + \varepsilon$ | $1$ | $\vec{0}$ |

Table: Generadores de las transformaciones del espacio y del tiempo.

* $R_{\vec{n}}(\varepsilon)$ es la rotación de ángulo $\varepsilon$ alrededor de $\vec{n}$. A primer orden, $R_{\vec{n}}(\varepsilon) \cdot \vec{q} = \vec{q} + \varepsilon \cdot \vec{n} \times \vec{q} + O(\varepsilon^2)$ (anexos, apartado 1.5).
* Son $3 + 3 + 3 + 1 = 10$ transformaciones independientes: tres direcciones $\vec{a}$, tres ejes $\vec{n}$ y tres velocidades $\vec{u}$ (por ejemplo, las de los ejes coordenados), y la traslación en el tiempo.
* El cambio de velocidad suma $\varepsilon \cdot \vec{u} \cdot t$ a cada trayectoria. Es la forma activa del paso a otro sistema de referencia inercial, que se mueve con velocidad $-\varepsilon \cdot \vec{u}$ respecto del primero.
* La traslación en el tiempo lleva el punto $(t, \vec{q})$ a $(t + \varepsilon, \vec{q})$: la trayectoria transformada cumple $\tilde{\vec{q}}(t + \varepsilon) = \vec{q}(t)$, y es el mismo movimiento con un retraso $\varepsilon$. La versión 1 la describía con el generador $\dot{\vec{q}}$, que depende de la velocidad; es la forma del apartado 9.6 de la parte matemática, $\bar{\vec{\xi}} = \vec{\xi} - \tau \cdot \dot{\vec{q}} = -\dot{\vec{q}}$, con el signo de $\varepsilon$ cambiado.

Con $N$ partículas, cada transformación se aplica a todas a la vez, con el mismo $\vec{a}$, $\vec{n}$ o $\vec{u}$: $\vec{\xi}_i = \vec{a}$, $\vec{\xi}_i = \vec{n} \times \vec{q}_i$ o $\vec{\xi}_i = \vec{u} \cdot t$. El tiempo es común a todas las partículas, y la traslación en el tiempo tiene un solo $\tau = 1$.

## 4. Primera etapa: una partícula

### 4.1. La partícula libre

Sin campo exterior, $\bsL = T = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$ y $\vec{p} = m \cdot \dot{\vec{q}}$. $\bsL$ no depende de $\vec{q}$ ni de $t$, así que en la forma de cuatro términos solo quedan $D = \vec{p} \cdot \big(\dot{\vec{\xi}} - \dot{\tau} \cdot \dot{\vec{q}}\big) + \bsL \cdot \dot{\tau}$. Con la tabla anterior:

* **Traslaciones:** $\tau = 0$ y $\dot{\vec{\xi}} = \vec{0}$, así que $D = 0$ y $F = 0$. Se conserva $Q = \vec{p} \cdot \vec{a}$ para todo $\vec{a}$: **la cantidad de movimiento $\vec{p}$**.
* **Giros:** $D = m \cdot \dot{\vec{q}} \cdot (\vec{n} \times \dot{\vec{q}}) = 0$, porque un producto mixto con un vector repetido es nulo. Con $F = 0$, se conserva $Q = \vec{p} \cdot (\vec{n} \times \vec{q}) = \vec{n} \cdot (\vec{q} \times \vec{p}) = \vec{n} \cdot \vec{\ell}$, por la propiedad cíclica del producto mixto. Para todo eje $\vec{n}$: **el momento angular $\vec{\ell}$**.
* **Traslación en el tiempo:** $\tau = 1$, $\vec{\xi} = \vec{0}$ y $\dot{\tau} = 0$, así que $D = 0$ y $F = 0$. Se conserva $Q = -\bsH$, con $\bsH = \vec{p} \cdot \dot{\vec{q}} - \bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2$: **la energía**.
* **Cambios de velocidad:** $\tau = 0$ y $\dot{\vec{\xi}} = \vec{u}$, así que $D = m \cdot \dot{\vec{q}} \cdot \vec{u} = \dfrac{d}{dt}\big(m \cdot \vec{u} \cdot \vec{q}\big)$, porque $\vec{u}$ es constante. No es nula, pero es una derivada total, con $F = m \cdot \vec{u} \cdot \vec{q}$. Se conserva
  $$
  \begin{aligned}
  Q = \vec{p} \cdot \vec{u} \cdot t - m \cdot \vec{u} \cdot \vec{q} = -\vec{u} \cdot \big(m \cdot \vec{q} - \vec{p} \cdot t\big)
  \end{aligned}
  $$
  para todo $\vec{u}$: **el vector $\vec{G} = m \cdot \vec{q} - \vec{p} \cdot t$**.

Son diez cantidades conservadas, una por transformación. Cada simetría expresa una propiedad del espacio y del tiempo vacíos:

| Propiedad | Simetría | Cantidad conservada |
| ---------------------------------------------------------- | ------------------------ | ------------------- |
| El espacio no tiene puntos privilegiados (homogeneidad) | traslaciones | $\vec{p}$ |
| El espacio no tiene direcciones privilegiadas (isotropía) | giros | $\vec{\ell}$ |
| El tiempo no tiene instantes privilegiados | traslación en el tiempo | $E$ |
| No hay sistemas inerciales privilegiados (relatividad de Galileo) | cambios de velocidad | $\vec{G}$ |

Table: Las simetrías de la partícula libre.

**Qué dicen.** $\vec{p}$ constante es la primera ley de Newton: la partícula libre se mueve con velocidad constante. $\vec{G}$ constante dice además dónde está: en $t = 0$, $\vec{G} = m \cdot \vec{q}(0)$, y $\vec{q}(t) = \dfrac{\vec{G} + \vec{p} \cdot t}{m}$. Las cantidades conservadas determinan la trayectoria entera.

**No son independientes.** Para una partícula libre, $\vec{\ell} = \vec{q} \times \vec{p} = \dfrac{1}{m} \cdot (\vec{G} + \vec{p} \cdot t) \times \vec{p} = \dfrac{1}{m} \cdot \vec{G} \times \vec{p}$ y $E = \dfrac{|\vec{p}|^2}{2 \cdot m}$: los valores de $\vec{\ell}$ y de $E$ se deducen de los de $\vec{p}$ y $\vec{G}$. Diez simetrías dan diez cantidades conservadas, pero no diez datos independientes. Con varias partículas que interaccionan, en cambio, las diez cantidades totales son independientes (apartado 6).

### 4.2. Una partícula en un campo exterior

Con un campo exterior estático, $\bsL = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 - V(\vec{q})$. El término cinético se comporta como en la partícula libre, y lo nuevo es lo que hace $V$. Con $\tau = 0$,

$$
\begin{aligned}
D = m \cdot \dot{\vec{q}} \cdot \dot{\vec{\xi}} - \nabla V \cdot \vec{\xi}.
\end{aligned}
$$

* **Traslación en la dirección $\vec{a}$:** $D = -\nabla V \cdot \vec{a}$, que no depende de $\dot{\vec{q}}$. Por el criterio del apartado 2, es una simetría si y solo si $\nabla V \cdot \vec{a}$ solo depende de $t$; como $V$ no depende de $t$, tiene que ser constante. Si $\nabla V \cdot \vec{a} = -\kappa$, con $\kappa$ constante, $F = \kappa \cdot t$. El campo tiene que ser uniforme en la dirección $\vec{a}$.
* **Giro alrededor de $\vec{n}$:** $D = -\nabla V \cdot (\vec{n} \times \vec{q})$, que es, cambiada de signo, la derivada de $V$ respecto del ángulo de giro alrededor de $\vec{n}$. Por el mismo criterio, tendría que ser constante. Si $V$ es continua en una circunferencia completa alrededor del eje, esa constante es nula: al dar una vuelta, $V$ cambiaría en $2 \cdot \pi$ por la constante, y volvería a su valor inicial. Es una simetría si y solo si $V$ no cambia al girar alrededor de $\vec{n}$, y entonces $F = 0$.
* **Cambio de velocidad $\vec{u}$:** $D = \dfrac{d}{dt}\big(m \cdot \vec{u} \cdot \vec{q}\big) - t \cdot \nabla V \cdot \vec{u}$. El último término es una derivada total si y solo si $\nabla V \cdot \vec{u}$ es constante: la misma condición que la traslación en la dirección $\vec{u}$.
* **Traslación en el tiempo:** $D = \partial_t \bsL = 0$, porque $V$ no depende de $t$. Se conserva $Q = -\bsH$, con $\bsH = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 + V$, la energía.

Tres campos de «El formalismo lagrangiano: parte física»:

| | Sin campo, $V = 0$ | Uniforme, $V = -e \cdot \vec{g} \cdot \vec{q}$ | Central, $V = e \cdot U(\lvert\vec{q}\rvert)$ |
| ------------------------ | ------------------ | ------------------------------------- | ------------------------------------- |
| Traslaciones | 3 | 3 | 0 |
| Giros | 3 | 1 | 3 |
| Cambios de velocidad | 3 | 3 | 0 |
| Traslación en el tiempo | 1 | 1 | 1 |
| Total | 10 | 8 | 4 |

Table: Simetrías que quedan en cada campo exterior.

* **Campo uniforme.** $\nabla V = -e \cdot \vec{g}$ es constante, así que todas las traslaciones y todos los cambios de velocidad son simetrías, aunque en la dirección de $\vec{g}$ con un término más en $F$. Los giros solo lo son alrededor de un eje paralelo a $\vec{g}$. El campo uniforme no distingue puntos, pero sí una dirección: rompe la isotropía, no la homogeneidad. La traslación en la dirección $\vec{a}$ tiene $\kappa = e \cdot \vec{g} \cdot \vec{a}$ y da $Q = \vec{a} \cdot (\vec{p} - e \cdot \vec{g} \cdot t)$: lo que se conserva no es $\vec{p}$, sino $\vec{p} - e \cdot \vec{g} \cdot t$, que es la segunda ley de Newton, $\dot{\vec{p}} = e \cdot \vec{g}$, integrada una vez. Con la gravedad y el eje $q_3$ vertical hacia arriba, $e \cdot \vec{g} = (0, 0, -m \cdot g)$, con $g > 0$ la aceleración de la gravedad: se conservan $p_1$, $p_2$ y $p_3 + m \cdot g \cdot t$, pero no $p_3$.
* **Campo central.** $\nabla V = e \cdot U'(r) \cdot \dfrac{\vec{q}}{r}$, con $r := |\vec{q}|$, depende de $\vec{q}$ en cualquier dirección: ninguna traslación ni ningún cambio de velocidad es una simetría. El centro es un punto privilegiado. Quedan los giros alrededor de cualquier eje que pase por el centro, porque $V$ solo depende de $|\vec{q}|$, y la traslación en el tiempo. Se conservan $\vec{\ell}$ y $E$, que son las dos leyes que «El formalismo lagrangiano: parte física» («Energía y momento angular») obtenía por cálculo directo y relacionaba con dos simetrías de $\bsL$. Ahora son consecuencia del teorema.

## 5. Segunda etapa: $N$ partículas sin interacción

Sin interacción, $\bsL = \sum_i \bsL_i$, donde $\bsL_i = \dfrac{1}{2} \cdot m_i \cdot |\dot{\vec{q}}_i|^2 - e_i \cdot U(r_i)$, con $r_i := |\vec{q}_i|$, solo depende de las variables de la partícula $i$. Hay más simetrías que con una partícula: las que transforman **una sola** partícula y dejan las demás quietas, con $\vec{\xi}_j = \vec{0}$ para $j \neq i$. Entonces $D$ solo contiene los términos de $\bsL_i$, y es una simetría de $\bsL$ si lo es de $\bsL_i$. El giro de la partícula $i$ sola da su momento angular $\vec{\ell}_i$.

**La energía de cada partícula.** El tiempo es común a todas las partículas, y no hay una transformación de los puntos $(t, \vec{q}_1, \dots, \vec{q}_N)$ que traslade el tiempo de una sola. Hay dos formas de obtener la energía $E_i$ de la partícula $i$:

* **Cada partícula es un sistema.** Las ecuaciones de Euler–Lagrange de $\vec{q}_i$ solo contienen $\bsL_i$, así que la partícula $i$ se mueve como un sistema con lagrangiano $\bsL_i$, y la traslación en el tiempo de ese sistema da $E_i$.
* **Con un generador que depende de la velocidad** (parte matemática, apartado 9.6). El generador $\bar{\vec{\xi}}_i = -\dot{\vec{q}}_i$, con $\bar{\vec{\xi}}_j = \vec{0}$ para $j \neq i$, desplaza en el tiempo la trayectoria de la partícula $i$ sola. Como $\bsL_i$ no depende explícitamente de $t$, por la regla de la cadena,
  $$
  \begin{aligned}
  \nabla_{\vec{q}_i} \bsL_i \cdot \big(-\dot{\vec{q}}_i\big) + \vec{p}_i \cdot \big(-\ddot{\vec{q}}_i\big) = -\dfrac{d\bsL_i}{dt},
  \end{aligned}
  $$
  y es una simetría generalizada con $\bar{F} = -\bsL_i$. Se conserva $\bar{Q} = \vec{p}_i \cdot \big(-\dot{\vec{q}}_i\big) + \bsL_i = -E_i$.

Se conservan la energía y el momento angular de cada partícula por separado, como afirmaba «El formalismo lagrangiano: parte física». La causa es que cada partícula puede transformarse sin que las demás lo noten.

## 6. Tercera etapa: interacciones que dependen de las distancias

Con interacción,

$$
\begin{aligned}
\bsL = \sum_{i=1}^{N} \dfrac{1}{2} \cdot m_i \cdot |\dot{\vec{q}}_i|^2 - \sum_{i=1}^{N} e_i \cdot U(r_i) - \sum_{i<j} V_{ij}(r_{ij}),
\end{aligned}
$$

con $r_{ij} := |\vec{q}_i - \vec{q}_j|$. Transformar una sola partícula cambia las distancias $r_{ij}$, y en general deja de ser una simetría. Quedan las transformaciones de todas las partículas a la vez:

* **Traslaciones,** $\vec{\xi}_i = \vec{a}$. Las diferencias $\vec{q}_i - \vec{q}_j$ no cambian, y $V_{ij}(r_{ij})$ tampoco. Sin campo exterior ($U = 0$) es una simetría con $F = 0$, y se conserva $Q = \sum_i \vec{p}_i \cdot \vec{a} = \vec{a} \cdot \vec{P}$: **la cantidad de movimiento total**. No la de cada partícula: lo que no tiene puntos privilegiados es el sistema en su conjunto.
* **Giros,** $\vec{\xi}_i = \vec{n} \times \vec{q}_i$. A primer orden, $|\vec{w}|^2$ cambia en $2 \cdot \varepsilon \cdot \vec{w} \cdot (\vec{n} \times \vec{w}) = 0$, tanto para $\vec{w} = \vec{q}_i - \vec{q}_j$ como para $\vec{w} = \vec{q}_i$, así que la energía potencial no cambia, con campo central o sin él. El término cinético tampoco, como en la primera etapa. Se conserva $Q = \sum_i \vec{p}_i \cdot (\vec{n} \times \vec{q}_i) = \vec{n} \cdot \vec{J}$: **el momento angular total**.
* **Cambios de velocidad,** $\vec{\xi}_i = \vec{u} \cdot t$. Las diferencias no cambian, y sin campo exterior la energía potencial tampoco. El término cinético da $D = \sum_i m_i \cdot \dot{\vec{q}}_i \cdot \vec{u} = \dfrac{d}{dt}\big(M \cdot \vec{u} \cdot \vec{X}\big)$, con $F = M \cdot \vec{u} \cdot \vec{X}$, y se conserva $Q = \sum_i \vec{p}_i \cdot \vec{u} \cdot t - M \cdot \vec{u} \cdot \vec{X} = -\vec{u} \cdot \vec{G}$: **el vector $\vec{G} = M \cdot \vec{X} - \vec{P} \cdot t$**.
* **Traslación en el tiempo:** $\tau = 1$, $D = \partial_t \bsL = 0$, y se conserva $Q = -\bsH$, con $\bsH = T + V = E$.

| Simetría | Condición sobre la energía potencial | Cantidad conservada |
| ------------------------ | ---------------------------------------------------------- | ------------------- |
| Traslación en el tiempo | no depende de $t$ | $E = T + V$ |
| Traslaciones | solo depende de las diferencias $\vec{q}_i - \vec{q}_j$ | $\vec{P}$ |
| Giros | no cambia al girar todas las posiciones; por ejemplo, si solo depende de las distancias | $\vec{J}$ |
| Cambios de velocidad | la de las traslaciones | $\vec{G}$ |

Table: Condiciones sobre la energía potencial y cantidades conservadas.

Sin campo exterior se conservan las diez cantidades: $E$, $\vec{P}$, $\vec{J}$ y $\vec{G}$. Con campo central, solo $\vec{J}$ y $E$. Es lo que «El formalismo lagrangiano: parte física» («Tercera etapa › Cantidades conservadas») obtenía con la tercera ley de Newton; aquí la tercera ley no se usa, porque está contenida en que la energía potencial solo dependa de las diferencias.

**El vector $\vec{G}$ y el centro de masas.** Por la definición de $\vec{X}$, $\dfrac{d}{dt}\big(M \cdot \vec{X}\big) = \vec{P}$, así que $\dot{\vec{G}} = -\dot{\vec{P}} \cdot t$, y la conservación de $\vec{G}$ se sigue de la de $\vec{P}$. Lo que añade es su valor: $\vec{G} = M \cdot \vec{X}(0)$, y $\vec{X}(t) = \dfrac{\vec{G} + \vec{P} \cdot t}{M}$. El centro de masas se mueve con velocidad constante, como una partícula libre de masa $M$.

## 7. Cuarta etapa: cargas en un campo magnético uniforme

Con $\vec{B}$ uniforme y constante y el potencial vector $\vec{A}(\vec{q}) = \dfrac{1}{2} \cdot \vec{B} \times \vec{q}$,

$$
\begin{aligned}
\bsL = \sum_{i=1}^{N} \left( \dfrac{1}{2} \cdot m_i \cdot |\dot{\vec{q}}_i|^2 + e_i \cdot \dot{\vec{q}}_i \cdot \vec{A}(\vec{q}_i) \right) - \sum_{i<j} \dfrac{e_i \cdot e_j}{4 \cdot \pi \cdot \varepsilon_0 \cdot r_{ij}},
\end{aligned}
$$

con $\varepsilon_0$ la permitividad del vacío (no el parámetro $\varepsilon$ de la familia). El momento canónico es $\vec{p}_i = m_i \cdot \dot{\vec{q}}_i + e_i \cdot \vec{A}(\vec{q}_i)$, distinto de la cantidad de movimiento. El término de Coulomb se comporta como en la tercera etapa; lo nuevo es el término magnético.

* **Traslaciones,** $\vec{\xi}_i = \vec{a}$ y $\tau = 0$. Como $\vec{A}(\vec{q}_i + \varepsilon \cdot \vec{a}) = \vec{A}(\vec{q}_i) + \dfrac{\varepsilon}{2} \cdot \vec{B} \times \vec{a}$, el término magnético aporta
  $$
  \begin{aligned}
  D = \sum_{i=1}^{N} \dfrac{e_i}{2} \cdot \dot{\vec{q}}_i \cdot (\vec{B} \times \vec{a}) = \dfrac{d}{dt}\left( \sum_{i=1}^{N} \dfrac{e_i}{2} \cdot \vec{q}_i \cdot (\vec{B} \times \vec{a}) \right),
  \end{aligned}
  $$
  porque $\vec{B} \times \vec{a}$ es constante. Es una simetría para todo $\vec{a}$, con $F = \sum_i \dfrac{e_i}{2} \cdot \vec{q}_i \cdot (\vec{B} \times \vec{a})$. Con $\vec{q}_i \cdot (\vec{B} \times \vec{a}) = -\vec{a} \cdot (\vec{B} \times \vec{q}_i)$, por la propiedad cíclica del producto mixto,
  $$
  \begin{aligned}
  Q = \sum_{i=1}^{N} \left( m_i \cdot \dot{\vec{q}}_i + \dfrac{e_i}{2} \cdot \vec{B} \times \vec{q}_i \right) \cdot \vec{a} + \sum_{i=1}^{N} \dfrac{e_i}{2} \cdot \vec{a} \cdot (\vec{B} \times \vec{q}_i) = \vec{a} \cdot \vec{K},
  \end{aligned}
  $$
  con $\vec{K} := \sum_i \left( m_i \cdot \dot{\vec{q}}_i - e_i \cdot \vec{q}_i \times \vec{B} \right)$. Es la cantidad que «El formalismo lagrangiano: parte física» dejaba para el teorema de Noether, y la de la parte matemática, apartado 7.5, en tres dimensiones. Su componente paralela a $\vec{B}$ es la de la cantidad de movimiento total, porque $(\vec{q}_i \times \vec{B}) \cdot \vec{B} = 0$; la perpendicular no. Para una carga, $\vec{K}$ da el centro de la circunferencia que describe (ejemplos físicos).
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
* **Traslación en el tiempo:** $\tau = 1$, $D = \partial_t \bsL = 0$, y se conserva $Q = -\bsH$. El término lineal en las velocidades no contribuye a $\bsH$, porque $\dot{\vec{q}}_i \cdot \nabla_{\dot{\vec{q}}_i}\big(e_i \cdot \dot{\vec{q}}_i \cdot \vec{A}\big) = e_i \cdot \dot{\vec{q}}_i \cdot \vec{A}$. Así, $\bsH = T + \sum_{i<j} \dfrac{e_i \cdot e_j}{4 \cdot \pi \cdot \varepsilon_0 \cdot r_{ij}}$, la energía que «El formalismo lagrangiano: parte física» justificaba porque la fuerza magnética no realiza trabajo.

De las diez transformaciones, el campo magnético uniforme conserva seis: las tres traslaciones (con $F \neq 0$), un giro, un cambio de velocidad y la traslación en el tiempo.

## 8. El grupo de Galileo

Las diez transformaciones de la partícula libre se componen entre sí y forman un grupo de diez parámetros, el **grupo de Galileo** (anexos, apartado 3): la composición de dos de ellas es otra del grupo, y cada una tiene inversa. Un generador general combina los diez, con coeficientes constantes $\vec{\omega}$ (giro), $\vec{u}$ (cambio de velocidad), $\vec{a}$ (traslación) y $\tau$ (tiempo):

$$
\begin{aligned}
\tau, \qquad \vec{\xi}_i = \vec{\omega} \times \vec{q}_i + \vec{u} \cdot t + \vec{a}.
\end{aligned}
$$

Aquí la letra $\tau$ designa a la vez la componente temporal del generador y su valor, que es constante. Para $N$ partículas sin campo exterior, $D$ es lineal en el generador (parte matemática, apartado 6.6), y solo el cambio de velocidad contribuye a $F$, con $F = M \cdot \vec{u} \cdot \vec{X}$:

$$
\begin{aligned}
Q = \sum_{i=1}^{N} \vec{p}_i \cdot \vec{\xi}_i - \tau \cdot \bsH - F = \vec{\omega} \cdot \vec{J} - \vec{u} \cdot \vec{G} + \vec{a} \cdot \vec{P} - \tau \cdot \bsH.
\end{aligned}
$$

Término a término: $\sum_i \vec{p}_i \cdot (\vec{\omega} \times \vec{q}_i) = \vec{\omega} \cdot \vec{J}$ por la propiedad cíclica del producto mixto; $\sum_i \vec{p}_i \cdot \vec{u} \cdot t - M \cdot \vec{u} \cdot \vec{X} = -\vec{u} \cdot \vec{G}$; y $\sum_i \vec{p}_i \cdot \vec{a} = \vec{a} \cdot \vec{P}$. $Q$ se conserva para cualquier elección de los diez coeficientes y es lineal en ellos. Eligiendo todos nulos salvo uno, se conserva cada una de las diez cantidades por separado: las tres componentes de $\vec{J}$, de $\vec{G}$ y de $\vec{P}$, y $\bsH = E$.

Con SymPy, para tres partículas con una energía potencial cualquiera de las distancias, en `cuadernos/tema1/noether_galileo.py` (apuntes públicos): la invariancia de $\bsL$ bajo cada generador, las cantidades de Noether y su conservación sobre las soluciones.

## 9. El grupo de Lorentz y el de Poincaré

La mecánica de Newton es una aproximación: vale cuando las velocidades son pequeñas frente a la de la luz. Este apartado sustituye el grupo de Galileo por el de Lorentz, que es el que corresponde a la relatividad especial, y aplica el teorema a la partícula libre relativista.

### 9.1. Lo necesario de la relatividad especial

* **Sucesos.** Un **suceso** es un punto $(t, \vec{q})$: un lugar en un instante. El conjunto de los sucesos es el **espacio-tiempo**, $\mathbb{R}^4$.
* **Los dos postulados** (Einstein, 1905): las leyes de la física son las mismas en todos los sistemas de referencia inerciales, y la velocidad de la luz en el vacío, $c \approx 2{,}998 \cdot 10^8\ \mathrm{m/s}$, es la misma en todos ellos. El segundo es incompatible con la relatividad de Galileo, en la que las velocidades se suman.
* **La transformación de Lorentz.** Si un observador se mueve respecto de otro con velocidad $v$ en la dirección del eje $q_1$, con $|v| < c$, y los dos coinciden en $t = 0$, las coordenadas que mide para el suceso $(t, \vec{q})$ son
  $$
  \begin{aligned}
  t' &= \gamma \cdot \left(t - \dfrac{v \cdot q_1}{c^2}\right), \qquad q_1' = \gamma \cdot (q_1 - v \cdot t), \qquad q_2' = q_2, \qquad q_3' = q_3, \\
  \gamma &:= \dfrac{1}{\sqrt{1 - v^2/c^2}}.
  \end{aligned}
  $$
  $\gamma$ es el **factor de Lorentz**: $\gamma \geq 1$, y $\gamma \to 1$ cuando $\dfrac{v}{c} \to 0$. En ese límite, $t' = t$ y $q_1' = q_1 - v \cdot t$: la transformación de Galileo.
* **La simultaneidad es relativa.** Dos sucesos con el mismo $t$ y distintos valores de $q_1$ tienen distintos $t'$: lo que es simultáneo para un observador no lo es para otro.
* **El intervalo.** La cantidad $c^2 \cdot t^2 - |\vec{q}|^2$ toma el mismo valor para los dos observadores. Como $q_2$ y $q_3$ no cambian, basta con ver que $c^2 \cdot t'^2 - q_1'^2 = c^2 \cdot t^2 - q_1^2$:
  $$
  \begin{aligned}
  c^2 \cdot t'^2 - q_1'^2 &\overset{(1)}{=} \gamma^2 \cdot \Big(c^2 \cdot t^2 - 2 \cdot v \cdot t \cdot q_1 + \dfrac{v^2 \cdot q_1^2}{c^2} \\
  &\qquad - q_1^2 + 2 \cdot v \cdot t \cdot q_1 - v^2 \cdot t^2\Big) \\
  &\overset{(2)}{=} \gamma^2 \cdot \left(1 - \dfrac{v^2}{c^2}\right) \cdot \big(c^2 \cdot t^2 - q_1^2\big) \overset{(3)}{=} c^2 \cdot t^2 - q_1^2.
  \end{aligned}
  $$
  **(1)** Sustituimos $t'$ y $q_1'$ y desarrollamos los cuadrados. **(2)** Se cancelan los términos con $t \cdot q_1$, y agrupamos $c^2 \cdot t^2 - v^2 \cdot t^2 = c^2 \cdot t^2 \cdot \left(1 - \dfrac{v^2}{c^2}\right)$ y $\dfrac{v^2 \cdot q_1^2}{c^2} - q_1^2 = -q_1^2 \cdot \left(1 - \dfrac{v^2}{c^2}\right)$. **(3)** Definición de $\gamma$.
* **El grupo de Lorentz** es el conjunto de las transformaciones lineales de $(t, \vec{q})$ que conservan el intervalo, no invierten el sentido del tiempo ni la orientación del espacio (no contienen reflexiones). Contiene los giros del espacio (tres parámetros) y los cambios de velocidad en cualquier dirección (tres parámetros); el de una dirección cualquiera se obtiene del anterior girando los ejes. Tiene seis parámetros. Su forma de matrices está en los anexos, apartado 4.
* **El grupo de Poincaré** añade las traslaciones en el tiempo y en el espacio, que no cambian las diferencias entre sucesos (cuatro parámetros). Tiene diez parámetros, como el de Galileo (anexos, apartado 5).
* **A primer orden.** Con $v = -\varepsilon \cdot \vec{u}$, la forma activa del cambio de velocidad, como en el apartado 3, $\gamma = 1 + O(\varepsilon^2)$, y la transformación de Lorentz en la dirección de $\vec{u}$ es
  $$
  \begin{aligned}
  t \mapsto t + \varepsilon \cdot \dfrac{\vec{u} \cdot \vec{q}}{c^2} + O(\varepsilon^2), \qquad \vec{q} \mapsto \vec{q} + \varepsilon \cdot \vec{u} \cdot t + O(\varepsilon^2).
  \end{aligned}
  $$
  Su generador es $\tau = \dfrac{\vec{u} \cdot \vec{q}}{c^2}$ y $\vec{\xi} = \vec{u} \cdot t$. Cuando $c \to \infty$, $\tau \to 0$, y queda el cambio de velocidad de Galileo. Los giros y las traslaciones tienen los mismos generadores que en la tabla del apartado 3.
* **La novedad** es que $\tau$ depende de la posición: el cambio de velocidad mezcla el tiempo y el espacio. Es el caso de la parte matemática, apartado 7.1, en el que la nueva variable depende de los valores.

### 9.2. La partícula libre relativista

El lagrangiano es

$$
\begin{aligned}
\bsL = -m \cdot c^2 \cdot \sqrt{1 - \dfrac{|\dot{\vec{q}}|^2}{c^2}},
\end{aligned}
$$

definido y de clase $C^2$ en el abierto $|\dot{\vec{q}}| < c$: la partícula, de masa $m > 0$, se mueve más despacio que la luz.

* **Por qué este lagrangiano.** $\displaystyle\int_{t_1}^{t_2} \sqrt{1 - \dfrac{|\dot{\vec{q}}|^2}{c^2}} \,dt$ es el **tiempo propio**: el tiempo que marca un reloj que viaja con la partícula. A lo largo de la trayectoria, $c^2 \cdot dt^2 - |d\vec{q}|^2 = c^2 \cdot dt^2 \cdot \left(1 - \dfrac{|\dot{\vec{q}}|^2}{c^2}\right)$, y por la invariancia del intervalo todos los observadores inerciales le asignan el mismo valor. La acción, $-m \cdot c^2$ por el tiempo propio, es la misma para todos ellos, como pide el primer postulado. El factor $-m \cdot c^2$ se elige para que el límite de velocidades pequeñas sea el lagrangiano de Newton (apartado 9.4; Landau y Lifshitz, 1975, § 8).
* **Momento y energía.** Con el factor de Lorentz de la partícula, $\gamma := \dfrac{1}{\sqrt{1 - |\dot{\vec{q}}|^2/c^2}}$ (aquí la velocidad es la de la partícula), la regla de la cadena da $\vec{p} = \nabla_{\dot{\vec{q}}} \bsL = \gamma \cdot m \cdot \dot{\vec{q}}$, y

  $$
  \begin{aligned}
  \bsH = \vec{p} \cdot \dot{\vec{q}} - \bsL &\overset{(1)}{=} \gamma \cdot m \cdot |\dot{\vec{q}}|^2 + \dfrac{m \cdot c^2}{\gamma} \\
  &\overset{(2)}{=} \gamma \cdot m \cdot \left(|\dot{\vec{q}}|^2 + c^2 - |\dot{\vec{q}}|^2\right) = \gamma \cdot m \cdot c^2.
  \end{aligned}
  $$

  **(1)** $\vec{p} = \gamma \cdot m \cdot \dot{\vec{q}}$, y $\sqrt{1 - |\dot{\vec{q}}|^2/c^2} = \dfrac{1}{\gamma}$. **(2)** $\dfrac{1}{\gamma} = \gamma \cdot \left(1 - \dfrac{|\dot{\vec{q}}|^2}{c^2}\right)$, y sacamos factor común $\gamma \cdot m$.

  La energía es $E := \bsH = \gamma \cdot m \cdot c^2$. En reposo, $E = m \cdot c^2$, la **energía en reposo**. Además, $E^2 - |\vec{p}|^2 \cdot c^2 = \gamma^2 \cdot m^2 \cdot c^4 \cdot \left(1 - \dfrac{|\dot{\vec{q}}|^2}{c^2}\right) = m^2 \cdot c^4$.
* **El movimiento.** $\bsL$ no depende de $\vec{q}$, así que las ecuaciones de Euler–Lagrange son $\dot{\vec{p}} = \vec{0}$: $\vec{p}$ es constante, y también $E = \sqrt{|\vec{p}|^2 \cdot c^2 + m^2 \cdot c^4}$ y la velocidad, $\dot{\vec{q}} = \dfrac{\vec{p}}{\gamma \cdot m} = \dfrac{c^2 \cdot \vec{p}}{E}$. El movimiento es rectilíneo y uniforme.

### 9.3. Las diez cantidades conservadas

$\bsL$ no depende de $\vec{q}$ ni de $t$, y en la forma de cuatro términos quedan $D = \vec{p} \cdot \big(\dot{\vec{\xi}} - \dot{\tau} \cdot \dot{\vec{q}}\big) + \bsL \cdot \dot{\tau}$.

* **Traslaciones:** como en el apartado 4.1, $D = 0$ y se conserva $\vec{a} \cdot \vec{p}$.
* **Giros:** $D = \gamma \cdot m \cdot \dot{\vec{q}} \cdot (\vec{n} \times \dot{\vec{q}}) = 0$, y se conserva $\vec{n} \cdot \vec{\ell}$, con $\vec{\ell} = \vec{q} \times \vec{p}$.
* **Traslación en el tiempo:** $D = 0$ y se conserva $-\bsH = -E$.
* **Cambios de velocidad:** $\tau = \dfrac{\vec{u} \cdot \vec{q}}{c^2}$ y $\vec{\xi} = \vec{u} \cdot t$. Entonces

  $$
  \begin{aligned}
  D &\overset{(1)}{=} \vec{p} \cdot \left(\vec{u} - \dfrac{\vec{u} \cdot \dot{\vec{q}}}{c^2} \cdot \dot{\vec{q}}\right) + \bsL \cdot \dfrac{\vec{u} \cdot \dot{\vec{q}}}{c^2} \\
  &\overset{(2)}{=} \vec{p} \cdot \vec{u} - \dfrac{\vec{u} \cdot \dot{\vec{q}}}{c^2} \cdot \big(\vec{p} \cdot \dot{\vec{q}} - \bsL\big) \\
  &\overset{(3)}{=} \gamma \cdot m \cdot \vec{u} \cdot \dot{\vec{q}} - \dfrac{\vec{u} \cdot \dot{\vec{q}}}{c^2} \cdot \gamma \cdot m \cdot c^2 \overset{(4)}{=} 0.
  \end{aligned}
  $$

  **(1)** $\dot{\vec{\xi}} = \vec{u}$ y $\dot{\tau} = \dfrac{\vec{u} \cdot \dot{\vec{q}}}{c^2}$, porque $\vec{u}$ es constante. **(2)** Repartimos el producto escalar y agrupamos los términos con el factor $\dfrac{\vec{u} \cdot \dot{\vec{q}}}{c^2}$. **(3)** $\vec{p} = \gamma \cdot m \cdot \dot{\vec{q}}$ y $\vec{p} \cdot \dot{\vec{q}} - \bsL = \bsH = \gamma \cdot m \cdot c^2$ (apartado 9.2). **(4)** Los dos términos son iguales.

  Es una simetría con $F = 0$, y se conserva

  $$
  \begin{aligned}
  Q = \vec{p} \cdot \vec{u} \cdot t - \dfrac{\vec{u} \cdot \vec{q}}{c^2} \cdot E = -\vec{u} \cdot \vec{G}_{\mathrm{rel}}, \qquad \vec{G}_{\mathrm{rel}} := \dfrac{E \cdot \vec{q}}{c^2} - \vec{p} \cdot t.
  \end{aligned}
  $$

| Simetría | $(\tau, \vec{\xi})$ | $F$ | Cantidad conservada |
| ------------------------ | ------------------------------------------------ | ----- | ------------------------------------- |
| Traslaciones | $(0, \vec{a})$ | $0$ | $\vec{p} = \gamma \cdot m \cdot \dot{\vec{q}}$ |
| Giros | $(0, \vec{n} \times \vec{q})$ | $0$ | $\vec{\ell} = \vec{q} \times \vec{p}$ |
| Traslación en el tiempo | $(1, \vec{0})$ | $0$ | $E = \gamma \cdot m \cdot c^2$ |
| Cambios de velocidad | $\left(\dfrac{\vec{u} \cdot \vec{q}}{c^2}, \vec{u} \cdot t\right)$ | $0$ | $\vec{G}_{\mathrm{rel}} = \dfrac{E \cdot \vec{q}}{c^2} - \vec{p} \cdot t$ |

Table: Las simetrías de la partícula libre relativista.

**Qué dice $\vec{G}_{\mathrm{rel}}$.** Como $E$ y $\vec{p}$ son constantes, $\vec{q}(t) = \dfrac{c^2}{E} \cdot \big(\vec{G}_{\mathrm{rel}} + \vec{p} \cdot t\big)$: la partícula está en $\dfrac{c^2}{E} \cdot \vec{G}_{\mathrm{rel}}$ en $t = 0$ y se mueve con la velocidad $\dfrac{c^2 \cdot \vec{p}}{E}$ del apartado 9.2. Es el papel de $\vec{G}$ en el apartado 4.1.

**La diferencia con Galileo.** Ninguna de las diez simetrías necesita $F$. El cambio de velocidad de Galileo sí la necesitaba, $F = m \cdot \vec{u} \cdot \vec{q}$; en el de Lorentz su papel lo hace el término $-\tau \cdot \bsH$, que aparece porque la transformación mueve el tiempo.

### 9.4. El límite de Galileo

* **El lagrangiano.** Con $\sqrt{1 - z} = 1 - \dfrac{z}{2} + O(z^2)$ y $z = \dfrac{|\dot{\vec{q}}|^2}{c^2}$,
  $$
  \begin{aligned}
  \bsL = -m \cdot c^2 + \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 + O\!\left(\dfrac{|\dot{\vec{q}}|^4}{c^2}\right).
  \end{aligned}
  $$
  La constante $-m \cdot c^2$ es la derivada total de $-m \cdot c^2 \cdot t$, y no cambia las ecuaciones (parte matemática, apartado 4). Del mismo modo, $\vec{p} = m \cdot \dot{\vec{q}} + O(1/c^2)$ y $E = m \cdot c^2 + \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 + O(1/c^2)$: la energía relativista es la energía en reposo más la cinética de Newton.
* **El generador.** $\tau = \dfrac{\vec{u} \cdot \vec{q}}{c^2} \to 0$ y $\vec{\xi} = \vec{u} \cdot t$: el cambio de velocidad de Lorentz tiende al de Galileo.
* **La cantidad conservada.** $\dfrac{E}{c^2} \to m$, así que $-\vec{u} \cdot \vec{G}_{\mathrm{rel}} = \vec{p} \cdot \vec{u} \cdot t - \dfrac{E}{c^2} \cdot \vec{u} \cdot \vec{q}$ tiende a $\vec{p} \cdot \vec{u} \cdot t - m \cdot \vec{u} \cdot \vec{q} = -\vec{u} \cdot \vec{G}$, la del apartado 4.1.
* **De dónde sale la $F$ de Galileo.** En la $Q$ de Lorentz, el término que se convierte en $-F = -m \cdot \vec{u} \cdot \vec{q}$ es $-\tau \cdot \bsH = -\dfrac{\vec{u} \cdot \vec{q}}{c^2} \cdot E$. El retraso $\tau$ es pequeño, de orden $\dfrac{1}{c^2}$, pero multiplica a la energía en reposo, que es de orden $c^2$, y el producto tiende a $m \cdot \vec{u} \cdot \vec{q}$. En $D$ ocurre lo mismo: la constante $-m \cdot c^2$ de $\bsL$ aporta $\bsL \cdot \dot{\tau} = -m \cdot c^2 \cdot \dfrac{\vec{u} \cdot \dot{\vec{q}}}{c^2} = -m \cdot \vec{u} \cdot \dot{\vec{q}}$, que cancela el término $m \cdot \vec{u} \cdot \dot{\vec{q}}$ de la energía cinética. La mecánica de Newton prescinde de la constante y de $\tau$; el término $m \cdot \vec{u} \cdot \dot{\vec{q}}$ queda sin compensar, y es la derivada de $F = m \cdot \vec{u} \cdot \vec{q}$.
* **Los grupos.** El grupo de Galileo es el límite del de Poincaré cuando $c \to \infty$, en un sentido que se precisa con la **contracción** de grupos (Inönü y Wigner, 1953; anexos, apartado 6).

### 9.5. Varias partículas y campos

* **Partículas libres.** Con $\bsL = \sum_i \bsL_i$, cada partícula es un sistema y conserva sus diez cantidades, con su energía $E_i = \gamma_i \cdot m_i \cdot c^2$. Las totales son $\vec{P}$, $\vec{J}$, $E := \sum_i E_i$ y
  $$
  \begin{aligned}
  \vec{G}_{\mathrm{rel}} := \sum_{i=1}^{N} \dfrac{E_i \cdot \vec{q}_i}{c^2} - \vec{P} \cdot t = \dfrac{E}{c^2} \cdot \vec{X}_E - \vec{P} \cdot t, \qquad \vec{X}_E := \dfrac{1}{E} \cdot \sum_{i=1}^{N} E_i \cdot \vec{q}_i.
  \end{aligned}
  $$
  $\vec{X}_E$ es el **centro de energía**, que se mueve con la velocidad constante $\dfrac{c^2 \cdot \vec{P}}{E}$. Cuando $c \to \infty$, $\dfrac{E_i}{c^2} \to m_i$, $\vec{X}_E \to \vec{X}$ y $\vec{G}_{\mathrm{rel}} \to \vec{G}$.
* **Un solo tiempo.** El cambio de velocidad retrasa el tiempo de cada partícula en una cantidad distinta, $\tau_i = \dfrac{\vec{u} \cdot \vec{q}_i}{c^2}$, y no es una transformación de los puntos $(t, \vec{q}_1, \dots, \vec{q}_N)$, que solo tienen un tiempo. En el lenguaje de la parte matemática, apartado 9.6, es una simetría generalizada, con $\bar{\vec{\xi}}_i = \vec{u} \cdot t - \tau_i \cdot \dot{\vec{q}}_i$ y $\bar{F} = -\sum_i \tau_i \cdot \bsL_i$, y su cantidad conservada es $\bar{Q} = -\vec{u} \cdot \vec{G}_{\mathrm{rel}}$.
* **Interacciones.** Una energía potencial $V(r_{ij})$ que depende de las distancias en un mismo instante no es invariante bajo el grupo de Lorentz, porque la simultaneidad es relativa. En relatividad, las interacciones se transmiten mediante campos, a velocidad finita, no mayor que $c$. Hay además un resultado negativo: con las posiciones de las partículas como coordenadas canónicas, y con las transformaciones de Lorentz actuando sobre ellas como sobre sucesos, un sistema hamiltoniano de partículas invariante bajo el grupo de Poincaré no puede tener interacción (teorema de no interacción; Currie et al., 1963).
* **Campos.** Por eso el teorema de Noether relativista se formula para campos, con la parte matemática, apartado 8, y $x_0 = t$. Si el lagrangiano de un campo es invariante bajo el grupo de Poincaré, las traslaciones dan el tensor de energía-momento, y los giros y los cambios de velocidad, las corrientes del momento angular y del movimiento del centro de energía. Las ecuaciones de Maxwell del electromagnetismo son invariantes bajo el grupo de Lorentz, y fueron su origen histórico (Einstein, 1905). Un ejemplo sencillo es la cuerda vibrante de la parte matemática, apartado 8.8: la ecuación de ondas, $\partial_t^2 f = c^2 \cdot \partial_x^2 f$, es invariante bajo las transformaciones de Lorentz de $(t, x)$ con $c$ la velocidad de las ondas, y no la de la luz. Se desarrolla en «El teorema de Noether: ejemplos físicos (versión 2)».

## 10. Mecánica cuántica no relativista

Este apartado explica desde el principio lo necesario de la mecánica cuántica no relativista para aplicar el teorema a un hamiltoniano cuántico. Usa la guía de dimensión infinita de la parte matemática (apartado 10), en particular el lagrangiano de Schrödinger del apartado 10.3, y el teorema con varias variables (apartado 8). Las referencias generales son Sakurai y Napolitano (2017) y Ballentine (1998).

**Avisos.** En este apartado, $i$ es la unidad imaginaria, y las partículas, si hay varias, se numeran con $j$. $\hbar$ es la constante de Planck reducida (parte matemática, apartado 10.3). Los operadores llevan gorro. La barra indica el conjugado de un número complejo: $\bar{z}$.

### 10.1. Estados, observables y valores esperados

* **El estado.** El estado de una partícula de masa $m$ en cada instante se describe con una función compleja $\psi(t, \vec{q})$, la **función de onda**. Según la **regla de Born**, $|\psi(t, \vec{q})|^2$ es la densidad de probabilidad de encontrar la partícula en $\vec{q}$ si se mide su posición en el instante $t$: la probabilidad de encontrarla en una región $B$ es $\int_B |\psi|^2 \,d^3q$, con $d^3q := dq_1 \, dq_2 \, dq_3$. Por eso se pide la normalización $\int_{\mathbb{R}^3} |\psi|^2 \,d^3q = 1$.
* **El espacio de los estados** es $L^2(\mathbb{R}^3)$, el de las funciones complejas de cuadrado integrable, con el producto escalar
  $$
  \begin{aligned}
  \langle \phi, \psi \rangle := \int_{\mathbb{R}^3} \bar{\phi} \cdot \psi \,d^3q.
  \end{aligned}
  $$
  Es un espacio de Hilbert complejo (parte matemática, apartados 10.1 y 10.4), y el producto escalar es antilineal en el primer argumento. $\psi$ y $e^{i \cdot \alpha} \cdot \psi$, con $\alpha$ real y constante, dan las mismas probabilidades y describen el mismo estado.
* **Observables.** Cada magnitud que se puede medir se representa con un operador autoadjunto (parte matemática, apartado 10.2). Si $\hat{A}\phi = \lambda \cdot \phi$ con $\phi \neq 0$, $\lambda$ es un **valor propio** de $\hat{A}$ y $\phi$ una **función propia** (o vector propio). Los resultados posibles de una medida son los valores propios (en general, los elementos del espectro, que en dimensión infinita puede contener más que valores propios; Reed y Simon, 1980), y si el estado es una función propia con valor propio $\lambda$, la medida da $\lambda$ con certeza. Los valores propios de un operador autoadjunto son reales: $\lambda \cdot \langle \phi, \phi \rangle = \langle \phi, \hat{A}\phi \rangle = \langle \hat{A}\phi, \phi \rangle = \bar{\lambda} \cdot \langle \phi, \phi \rangle$.
* **Posición y momento.** El operador posición multiplica por la coordenada, $(\hat{q}_k\psi)(\vec{q}) := q_k \cdot \psi(\vec{q})$. El operador momento es $\hat{p}_k := -i \cdot \hbar \cdot \partial_k$, con $\partial_k := \dfrac{\partial}{\partial q_k}$, definido sobre las funciones derivables. El motivo: la onda plana $e^{i \cdot \vec{p} \cdot \vec{q}/\hbar}$, la de una partícula con momento $\vec{p}$ según de Broglie, es función propia de $\hat{p}_k$ con valor propio $p_k$, porque $-i \cdot \hbar \cdot \partial_k e^{i \cdot \vec{p} \cdot \vec{q}/\hbar} = p_k \cdot e^{i \cdot \vec{p} \cdot \vec{q}/\hbar}$. (No es de cuadrado integrable: es la idealización de un estado con el momento exactamente definido.) $\hat{p}_k$ es autoadjunto en un dominio adecuado; formalmente, integrando por partes con términos de borde nulos, $\langle \phi, \hat{p}_k\psi \rangle = \int \bar{\phi} \cdot (-i \cdot \hbar \cdot \partial_k \psi) \,d^3q = \int \overline{(-i \cdot \hbar \cdot \partial_k \phi)} \cdot \psi \,d^3q = \langle \hat{p}_k\phi, \psi \rangle$. Escribimos $\hat{\vec{q}}$, $\hat{\vec{p}}$ y $\hat{\vec{\ell}} := \hat{\vec{q}} \times \hat{\vec{p}}$, el momento angular, con componentes como $\hat{\ell}_3 = \hat{q}_1\hat{p}_2 - \hat{q}_2\hat{p}_1$.
* **Valor esperado.** Para $\psi$ normalizada, $\langle \hat{A} \rangle := \langle \psi, \hat{A}\psi \rangle$ es la media de los resultados al medir $\hat{A}$ en muchos sistemas preparados en el mismo estado. Es real si $\hat{A}$ es autoadjunto: $\langle \psi, \hat{A}\psi \rangle = \langle \hat{A}\psi, \psi \rangle = \overline{\langle \psi, \hat{A}\psi \rangle}$. Por ejemplo, $\langle \hat{q}_k \rangle = \int q_k \cdot |\psi|^2 \,d^3q$ es la posición media.
* **Conmutador.** $[\hat{A}, \hat{B}] := \hat{A}\hat{B} - \hat{B}\hat{A}$. Dos observables tienen una base común de funciones propias, y pueden tener a la vez valores definidos, cuando conmutan (para matrices hermíticas, es el teorema de diagonalización simultánea; en dimensión infinita, con precisiones sobre los dominios). Dos reglas:
  * **Relación canónica:** $[\hat{q}_j, \hat{p}_k] = i \cdot \hbar \cdot \delta_{jk}$, con $\delta_{jk}$ igual a $1$ si $j = k$ y a $0$ si no. Para cada $\psi$, por la regla del producto,
    $$
    \begin{aligned}
    {[\hat{q}_j, \hat{p}_k]}\psi = q_j \cdot (-i \cdot \hbar \cdot \partial_k \psi) + i \cdot \hbar \cdot \partial_k(q_j \cdot \psi) = i \cdot \hbar \cdot \delta_{jk} \cdot \psi.
    \end{aligned}
    $$
    La posición y el momento en la misma dirección no conmutan y no pueden tener a la vez valores definidos: es el origen del principio de indeterminación de Heisenberg (Sakurai y Napolitano, 2017, cap. 1).
  * **Regla de Leibniz:** $[\hat{A}\hat{B}, \hat{C}] = \hat{A}[\hat{B}, \hat{C}] + [\hat{A}, \hat{C}]\hat{B}$, que se ve sumando y restando $\hat{A}\hat{C}\hat{B}$ en $\hat{A}\hat{B}\hat{C} - \hat{C}\hat{A}\hat{B}$.

### 10.2. El hamiltoniano y la ecuación de Schrödinger

* **De la mecánica clásica a la cuántica.** Para una partícula en un campo $V(\vec{q})$, el hamiltoniano clásico es $\bsH = \dfrac{|\vec{p}|^2}{2 \cdot m} + V(\vec{q})$ (apartado 4.2). El cuántico se obtiene sustituyendo $\vec{q}$ y $\vec{p}$ por los operadores:
  $$
  \begin{aligned}
  \hat{H} := \dfrac{1}{2 \cdot m} \cdot \sum_{k=1}^{3} \hat{p}_k^2 + V(\hat{\vec{q}}) = -\dfrac{\hbar^2}{2 \cdot m} \cdot \nabla^2 + V,
  \end{aligned}
  $$
  donde $\nabla^2 := \sum_k \partial_k^2$ es el **laplaciano** y $V$ actúa multiplicando: $(V\psi)(\vec{q}) = V(\vec{q}) \cdot \psi(\vec{q})$. Aquí no aparecen productos de $\hat{q}_k$ por $\hat{p}_k$, y no hay que decidir en qué orden se escriben, que importa, porque no conmutan. En otros hamiltonianos, como el de una carga en un campo magnético, el orden se elige para que el operador sea autoadjunto.
* **Varias partículas.** Con $N$ partículas, la función de onda es $\psi(t, \vec{q}_1, \dots, \vec{q}_N)$ y $\hat{H} = \sum_j \left(-\dfrac{\hbar^2}{2 \cdot m_j} \cdot \nabla_j^2\right) + V(\vec{q}_1, \dots, \vec{q}_N)$, con $\nabla_j^2$ el laplaciano en las coordenadas de la partícula $j$. Lo que sigue se escribe para una partícula; con varias es igual, con sumas sobre $j$.
* **La ecuación de Schrödinger** es la ley de evolución del estado, un postulado, como las leyes de Newton en la mecánica clásica:
  $$
  \begin{aligned}
  i \cdot \hbar \cdot \partial_t \psi = \hat{H}\psi = -\dfrac{\hbar^2}{2 \cdot m} \cdot \nabla^2\psi + V \cdot \psi.
  \end{aligned}
  $$
  Es de primer orden en $t$: la función de onda en un instante determina la de los instantes siguientes.
* **Estados estacionarios.** Si $\hat{H}\phi = E \cdot \phi$, con $\phi(\vec{q})$ independiente de $t$, entonces $\psi(t, \vec{q}) = e^{-i \cdot E \cdot t/\hbar} \cdot \phi(\vec{q})$ es solución: $i \cdot \hbar \cdot \partial_t \psi = E \cdot \psi = \hat{H}\psi$. $|\psi|^2 = |\phi|^2$ no depende de $t$, y $E$ es una de las energías posibles del sistema; por ejemplo, los niveles de energía del átomo de hidrógeno.

### 10.3. La ecuación de Schrödinger como ecuación de Euler–Lagrange

**El campo.** Escribimos $\psi = \psi_{\mathrm{R}} + i \cdot \psi_{\mathrm{I}}$, con $\psi_{\mathrm{R}}$ y $\psi_{\mathrm{I}}$ reales. Son dos funciones reales de cuatro variables, $(t, q_1, q_2, q_3)$: el caso $n = 2$ de la parte matemática, apartado 8, con $x_0 = t$ y tres coordenadas espaciales. La densidad lagrangiana es

$$
\begin{aligned}
\bsL &= \operatorname{Re}\big(\bar{\psi} \cdot i \cdot \hbar \cdot \partial_t \psi\big) - \dfrac{\hbar^2}{2 \cdot m} \cdot |\nabla\psi|^2 - V \cdot |\psi|^2 \\
&= \hbar \cdot \big(\psi_{\mathrm{I}} \cdot \partial_t \psi_{\mathrm{R}} - \psi_{\mathrm{R}} \cdot \partial_t \psi_{\mathrm{I}}\big) - \dfrac{\hbar^2}{2 \cdot m} \cdot \sum_{k=1}^{3} \Big( (\partial_k \psi_{\mathrm{R}})^2 + (\partial_k \psi_{\mathrm{I}})^2 \Big) \\
&\qquad - V \cdot \big(\psi_{\mathrm{R}}^2 + \psi_{\mathrm{I}}^2\big),
\end{aligned}
$$

con $|\nabla\psi|^2 := \sum_k |\partial_k \psi|^2$. La segunda línea sale de $\bar{\psi} \cdot i \cdot \partial_t \psi = i \cdot \big(\psi_{\mathrm{R}} \cdot \partial_t \psi_{\mathrm{R}} + \psi_{\mathrm{I}} \cdot \partial_t \psi_{\mathrm{I}}\big) + \psi_{\mathrm{I}} \cdot \partial_t \psi_{\mathrm{R}} - \psi_{\mathrm{R}} \cdot \partial_t \psi_{\mathrm{I}}$, cuya parte real es la de los dos últimos términos.

* **Los momentos** (parte matemática, apartado 8.1): $u_{\mathrm{R}0} = \hbar \cdot \psi_{\mathrm{I}}$, $u_{\mathrm{I}0} = -\hbar \cdot \psi_{\mathrm{R}}$, $u_{\mathrm{R}k} = -\dfrac{\hbar^2}{m} \cdot \partial_k \psi_{\mathrm{R}}$ y $u_{\mathrm{I}k} = -\dfrac{\hbar^2}{m} \cdot \partial_k \psi_{\mathrm{I}}$, para $k = 1, 2, 3$.
* **Las ecuaciones de Euler–Lagrange.** Para $\psi_{\mathrm{R}}$,
  $$
  \begin{aligned}
  \varphi_{\mathrm{R}} &= \big(-\hbar \cdot \partial_t \psi_{\mathrm{I}} - 2 \cdot V \cdot \psi_{\mathrm{R}}\big) - \hbar \cdot \partial_t \psi_{\mathrm{I}} + \dfrac{\hbar^2}{m} \cdot \nabla^2\psi_{\mathrm{R}} \\
  &= 2 \cdot \left(-\hbar \cdot \partial_t \psi_{\mathrm{I}} + \dfrac{\hbar^2}{2 \cdot m} \cdot \nabla^2\psi_{\mathrm{R}} - V \cdot \psi_{\mathrm{R}}\right) = 2 \cdot \operatorname{Re}\big(i \cdot \hbar \cdot \partial_t \psi - \hat{H}\psi\big),
  \end{aligned}
  $$
  y del mismo modo $\varphi_{\mathrm{I}} = 2 \cdot \operatorname{Im}\big(i \cdot \hbar \cdot \partial_t \psi - \hat{H}\psi\big)$. Las dos ecuaciones de Euler–Lagrange son las partes real e imaginaria de la ecuación de Schrödinger.
* **La relación con la parte matemática, apartado 10.3.** Integrando en el espacio, y con $\psi$ y sus derivadas tendiendo a cero en el infinito, la integración por partes da $\int \dfrac{\hbar^2}{2 \cdot m} \cdot |\nabla\psi|^2 \,d^3q = \left\langle \psi, -\dfrac{\hbar^2}{2 \cdot m} \cdot \nabla^2\psi \right\rangle$, y la integral de $\bsL$ es el lagrangiano $\operatorname{Re}\langle \psi, i \cdot \hbar \cdot \dot{\psi} \rangle - \langle \psi, \hat{H}\psi \rangle$ de aquel apartado. Hay, por tanto, dos formas de verlo: como un campo de dimensión finita, con el apartado 8, que es riguroso sin más; y como una curva en el espacio de Hilbert, con el apartado 10, que es más directo para los operadores (apartado 10.4).
* **La simetría de fase.** $\psi \mapsto e^{i \cdot \varepsilon} \cdot \psi$ gira el par $(\psi_{\mathrm{R}}, \psi_{\mathrm{I}})$ un ángulo $\varepsilon$, con $\vec{\tau} = \vec{0}$ y generador $\xi_{\mathrm{R}} = -\psi_{\mathrm{I}}$, $\xi_{\mathrm{I}} = \psi_{\mathrm{R}}$. $\bsL$ solo depende de $\psi$ a través de $\bar{\psi} \cdot \partial_t \psi$, $|\nabla\psi|^2$ y $|\psi|^2$, que no cambian, así que $D = 0$ y $\vec{F} = \vec{0}$. La corriente de la parte matemática, apartado 8.6, $Q_\mu = \sum_i u_{i\mu} \cdot \xi_i$, es
  $$
  \begin{aligned}
  Q_0 &= -\hbar \cdot |\psi|^2, \qquad Q_k = -\hbar \cdot j_k, \\
  j_k &:= \dfrac{\hbar}{m} \cdot \big(\psi_{\mathrm{R}} \cdot \partial_k \psi_{\mathrm{I}} - \psi_{\mathrm{I}} \cdot \partial_k \psi_{\mathrm{R}}\big) = \dfrac{\hbar}{m} \cdot \operatorname{Im}\big(\bar{\psi} \cdot \partial_k \psi\big).
  \end{aligned}
  $$
  Dividida por $-\hbar$, la ley local (parte matemática, apartado 8.7) es la **ecuación de continuidad de la probabilidad**, $\partial_t |\psi|^2 + \sum_k \partial_k j_k = 0$: $\vec{\jmath}$ es la **densidad de corriente de probabilidad**. Si el flujo de $\vec{\jmath}$ por la frontera se anula (en una caja con $\psi = 0$ en las paredes, o en todo el espacio con $\psi$ y sus derivadas decreciendo lo bastante deprisa en el infinito, como límite de cajas cada vez mayores), la probabilidad total, $\int |\psi|^2 \,d^3q$, es constante. Por eso la normalización se impone una vez y se mantiene.
* **Otras simetrías en esta forma.** Las traslaciones de las variables dan el tensor de energía-momento (parte matemática, apartado 8.7). Con los momentos anteriores:

| Simetría | Condición | Densidad $Q_0$ | Total |
| ------------------------ | ------------------ | -------------------------------------------------------- | ------------------------- |
| Fase | ninguna | $-\hbar \cdot \lvert\psi\rvert^2$ | $-\hbar \cdot \langle \psi, \psi \rangle$ |
| Traslación en el tiempo | $V$ no depende de $t$ | $-\Big(\dfrac{\hbar^2}{2 \cdot m} \cdot \lvert\nabla\psi\rvert^2 + V \cdot \lvert\psi\rvert^2\Big)$ | $-\langle \hat{H} \rangle$ |
| Traslación en $q_k$ | $V$ no depende de $q_k$ | $\operatorname{Re}\big(\bar{\psi} \cdot \hat{p}_k\psi\big)$ | $\langle \hat{p}_k \rangle$ |

Table: Simetrías de la densidad lagrangiana de Schrödinger, con $\psi$ normalizada en la última columna.

La densidad de la traslación en el tiempo es $-T_{00}$, y la de la traslación en $q_k$, $-T_{0k} = \hbar \cdot \big(\psi_{\mathrm{R}} \cdot \partial_k \psi_{\mathrm{I}} - \psi_{\mathrm{I}} \cdot \partial_k \psi_{\mathrm{R}}\big)$, que es $\operatorname{Re}\big(\bar{\psi} \cdot \hat{p}_k\psi\big)$. Los totales de la última columna se obtienen integrando por partes, con las mismas condiciones en el infinito. Si $V$ depende de $q_k$, $D = \partial_{q_k} \bsL = -\partial_k V \cdot |\psi|^2$ no es nula y la traslación no es una simetría.

### 10.4. «Si conmuta con $\hat{H}$, se conserva»

**Las transformaciones.** Por el teorema de Stone (parte matemática, apartado 10.2), una familia de transformaciones unitarias con la ley de grupo es de la forma $\hat{U}(\varepsilon) = e^{-i \cdot \varepsilon \cdot \hat{A}/\hbar}$, con $\hat{A}$ autoadjunto. Actúa sobre cada $\psi(t)$, sin mover el tiempo: $\tau = 0$ y $\xi = -\dfrac{i}{\hbar} \cdot \hat{A}\psi$. Permitimos que $\hat{A}$ dependa explícitamente de $t$, y escribimos $\partial_t \hat{A}$ para su derivada. Es la tabla de la parte matemática, apartado 10.3, con $\dfrac{\hat{A}}{\hbar}$ en lugar de $\hat{A}$. Ejemplos, con $R_{\vec{n}}(-\varepsilon)$ el giro de ángulo $-\varepsilon$ alrededor de $\vec{n}$:

| Familia $\hat{U}(\varepsilon)\psi$ | $\hat{A}$ | Qué hace |
| -------------------------------------------- | ------------------ | ---------------------------------------- |
| $\psi(\vec{q} - \varepsilon \cdot \vec{a})$ | $\vec{a} \cdot \hat{\vec{p}}$ | traslada la función de onda en $\varepsilon \cdot \vec{a}$ |
| $\psi\big(R_{\vec{n}}(-\varepsilon) \cdot \vec{q}\big)$ | $\vec{n} \cdot \hat{\vec{\ell}}$ | la gira un ángulo $\varepsilon$ alrededor de $\vec{n}$ |
| $e^{i \cdot \varepsilon} \cdot \psi$ | $-\hbar$ (constante) | cambia la fase |
| apartado 10.5 | $-\vec{u} \cdot \hat{\vec{G}}$ | cambia la velocidad |

Table: Familias unitarias y sus generadores.

Para la primera fila, la derivada en $\varepsilon = 0$ es $\xi = -\vec{a} \cdot \nabla\psi = -\dfrac{i}{\hbar} \cdot \vec{a} \cdot \hat{\vec{p}}\psi$, porque $\hat{\vec{p}} = -i \cdot \hbar \cdot \nabla$. Para la segunda, $\xi = -(\vec{n} \times \vec{q}) \cdot \nabla\psi$, y por la propiedad cíclica del producto mixto, $\vec{n} \cdot \hat{\vec{\ell}}\psi = -i \cdot \hbar \cdot \vec{n} \cdot (\vec{q} \times \nabla\psi) = -i \cdot \hbar \cdot (\vec{n} \times \vec{q}) \cdot \nabla\psi$.

**El término $D$.** Con el lagrangiano $\bsL = \operatorname{Re}\langle \psi, i \cdot \hbar \cdot \dot{\psi} \rangle - \langle \psi, \hat{H}\psi \rangle$ y $\tau = 0$, $D$ es el coeficiente de $\varepsilon$ en $\bsL\big(\psi + \varepsilon \cdot \xi, \dot{\psi} + \varepsilon \cdot \dot{\xi}\big)$:

$$
\begin{aligned}
D &\overset{(1)}{=} \operatorname{Re}\langle \xi, i \cdot \hbar \cdot \dot{\psi} \rangle + \operatorname{Re}\langle \psi, i \cdot \hbar \cdot \dot{\xi} \rangle - 2 \cdot \operatorname{Re}\langle \xi, \hat{H}\psi \rangle \\
&\overset{(2)}{=} -\operatorname{Re}\langle \hat{A}\psi, \dot{\psi} \rangle + \langle \psi, \partial_t \hat{A}\psi \rangle + \operatorname{Re}\langle \psi, \hat{A}\dot{\psi} \rangle - 2 \cdot \operatorname{Re}\left(\dfrac{i}{\hbar} \cdot \langle \hat{A}\psi, \hat{H}\psi \rangle\right) \\
&\overset{(3)}{=} \langle \psi, \partial_t \hat{A}\psi \rangle + \dfrac{2}{\hbar} \cdot \operatorname{Im}\langle \psi, \hat{A}\hat{H}\psi \rangle \\
&\overset{(4)}{=} \left\langle \psi, \left(\partial_t \hat{A} + \dfrac{i}{\hbar} \cdot [\hat{H}, \hat{A}]\right)\psi \right\rangle.
\end{aligned}
$$

* **(1)** $\operatorname{Re}\langle \cdot, \cdot \rangle$ es bilineal con coeficientes reales, lo que da los dos primeros términos. En el segundo término de $\bsL$, $\langle \psi + \varepsilon \cdot \xi, \hat{H}(\psi + \varepsilon \cdot \xi) \rangle = \langle \psi, \hat{H}\psi \rangle + \varepsilon \cdot \big(\langle \xi, \hat{H}\psi \rangle + \langle \psi, \hat{H}\xi \rangle\big) + O(\varepsilon^2)$, y $\langle \psi, \hat{H}\xi \rangle = \langle \hat{H}\psi, \xi \rangle = \overline{\langle \xi, \hat{H}\psi \rangle}$, porque $\hat{H}$ es autoadjunto: la suma es $2 \cdot \operatorname{Re}\langle \xi, \hat{H}\psi \rangle$.
* **(2)** Sustituimos $\xi = -\dfrac{i}{\hbar} \cdot \hat{A}\psi$ y, por la regla del producto, $\dot{\xi} = -\dfrac{i}{\hbar} \cdot \big(\partial_t \hat{A}\psi + \hat{A}\dot{\psi}\big)$. En el primer argumento, el factor sale conjugado:

  $$
  \begin{aligned}
  \left\langle -\dfrac{i}{\hbar} \cdot \hat{A}\psi, i \cdot \hbar \cdot \dot{\psi} \right\rangle = \dfrac{i}{\hbar} \cdot i \cdot \hbar \cdot \langle \hat{A}\psi, \dot{\psi} \rangle = -\langle \hat{A}\psi, \dot{\psi} \rangle.
  \end{aligned}
  $$

  En el segundo, $i \cdot \hbar \cdot \left(-\dfrac{i}{\hbar}\right) = 1$, y $\langle \psi, \partial_t \hat{A}\psi \rangle$ es real porque $\partial_t \hat{A}$ es autoadjunto.
* **(3)** $\langle \hat{A}\psi, \dot{\psi} \rangle = \langle \psi, \hat{A}\dot{\psi} \rangle$, porque $\hat{A}$ es autoadjunto: el primer término y el tercero se cancelan. Además, $\langle \hat{A}\psi, \hat{H}\psi \rangle = \langle \psi, \hat{A}\hat{H}\psi \rangle$, y $\operatorname{Re}(i \cdot z) = -\operatorname{Im} z$ para todo complejo $z$.
* **(4)** Con $z := \langle \psi, \hat{A}\hat{H}\psi \rangle$, $\langle \psi, \hat{H}\hat{A}\psi \rangle = \langle \hat{A}\hat{H}\psi, \psi \rangle = \bar{z}$, porque $\hat{H}$ y $\hat{A}$ son autoadjuntos. Entonces $\langle \psi, [\hat{H}, \hat{A}]\psi \rangle = \bar{z} - z = -2 \cdot i \cdot \operatorname{Im} z$, es decir, $\dfrac{2}{\hbar} \cdot \operatorname{Im} z = \dfrac{i}{\hbar} \cdot \langle \psi, [\hat{H}, \hat{A}]\psi \rangle$.

**La condición de simetría.** $D$ no contiene $\dot{\psi}$, así que $F$ no puede depender de $\psi$ (como en la parte matemática, apartado 5, punto (3): si dependiera, $\dot{F}$ contendría $\dot{\psi}$). Entonces $F$ solo depende de $t$, y $D = \dot{F}$ no puede depender de $\psi$; como $D$ es nulo para $\psi = 0$, es nulo siempre. Por tanto, la familia es una simetría si y solo si $\langle \psi, \hat{K}\psi \rangle = 0$ para todo $\psi$, con $\hat{K} := \partial_t \hat{A} + \dfrac{i}{\hbar} \cdot [\hat{H}, \hat{A}]$. $\hat{K}$ es autoadjunto, y un operador autoadjunto con todos sus valores esperados nulos es nulo (por la identidad de polarización, sus valores esperados determinan todos los $\langle \phi, \hat{K}\psi \rangle$). La condición es

$$
\begin{aligned}
\partial_t \hat{A} + \dfrac{i}{\hbar} \cdot [\hat{H}, \hat{A}] = 0, \qquad \text{y, si } \hat{A} \text{ no depende de } t, \qquad [\hat{H}, \hat{A}] = 0.
\end{aligned}
$$

**La cantidad conservada.** Con $\tau = 0$ y $F = 0$, $Q$ es el momento aplicado al generador: $Q = \operatorname{Re}\left\langle \psi, i \cdot \hbar \cdot \left(-\dfrac{i}{\hbar}\right) \cdot \hat{A}\psi \right\rangle = \langle \psi, \hat{A}\psi \rangle$, el valor esperado de $\hat{A}$. Es la regla «si conmuta con $\hat{H}$, se conserva».

**La identidad sobre las soluciones.** La identidad de Noether (parte matemática, apartados 7.4 y 10.1), antes de usar la hipótesis de simetría, dice que la derivada de $\langle \psi, \hat{A}\psi \rangle$ es $D$ menos un término que se anula sobre las soluciones. Por tanto, sobre las soluciones,

$$
\begin{aligned}
\dfrac{d}{dt}\langle \hat{A} \rangle = \left\langle \partial_t \hat{A} + \dfrac{i}{\hbar} \cdot [\hat{H}, \hat{A}] \right\rangle,
\end{aligned}
$$

la **ecuación de Heisenberg** para los valores esperados. Se comprueba también directamente con la ecuación de Schrödinger, $\dot{\psi} = -\dfrac{i}{\hbar} \cdot \hat{H}\psi$:

$$
\begin{aligned}
\dfrac{d}{dt}\langle \psi, \hat{A}\psi \rangle &\overset{(1)}{=} \langle \dot{\psi}, \hat{A}\psi \rangle + \langle \psi, \partial_t \hat{A}\psi \rangle + \langle \psi, \hat{A}\dot{\psi} \rangle \\
&\overset{(2)}{=} \dfrac{i}{\hbar} \cdot \langle \hat{H}\psi, \hat{A}\psi \rangle + \langle \psi, \partial_t \hat{A}\psi \rangle - \dfrac{i}{\hbar} \cdot \langle \psi, \hat{A}\hat{H}\psi \rangle \\
&\overset{(3)}{=} \left\langle \psi, \left(\partial_t \hat{A} + \dfrac{i}{\hbar} \cdot [\hat{H}, \hat{A}]\right)\psi \right\rangle.
\end{aligned}
$$

**(1)** Regla del producto. **(2)** Ecuación de Schrödinger; en el primer argumento, el factor $-\dfrac{i}{\hbar}$ sale conjugado. **(3)** $\langle \hat{H}\psi, \hat{A}\psi \rangle = \langle \psi, \hat{H}\hat{A}\psi \rangle$, porque $\hat{H}$ es autoadjunto, y agrupamos. En dimensión infinita estas cuentas son formales: requieren que $\psi(t)$ esté en los dominios de los operadores (parte matemática, apartado 10.2, punto 3).

**Ejemplos**, con $\hat{H} = -\dfrac{\hbar^2}{2 \cdot m} \cdot \nabla^2 + V$:

* **Traslaciones.** $[\hat{H}, \hat{p}_k] = i \cdot \hbar \cdot \partial_k V$: el laplaciano conmuta con $\partial_k$ por el teorema de Schwarz, y $[V, \hat{p}_k]\psi = V \cdot (-i \cdot \hbar \cdot \partial_k \psi) + i \cdot \hbar \cdot \partial_k(V \cdot \psi) = i \cdot \hbar \cdot \partial_k V \cdot \psi$. $\langle \hat{p}_k \rangle$ se conserva si $V$ no depende de $q_k$.
* **Giros con potencial central**, $V = V(r)$ con $r := |\vec{q}|$. $[\hat{H}, \hat{\ell}_3] = 0$, con $\hat{\ell}_3 = -i \cdot \hbar \cdot (q_1 \cdot \partial_2 - q_2 \cdot \partial_1)$:
  * por la regla del producto, $\nabla^2(q_1 \cdot \partial_2 \psi) = q_1 \cdot \partial_2 \nabla^2\psi + 2 \cdot \partial_1 \partial_2 \psi$ y $\nabla^2(q_2 \cdot \partial_1 \psi) = q_2 \cdot \partial_1 \nabla^2\psi + 2 \cdot \partial_2 \partial_1 \psi$; al restar, los últimos términos se cancelan por el teorema de Schwarz, y el laplaciano conmuta con $\hat{\ell}_3$;
  * $[V, \hat{\ell}_3]\psi = i \cdot \hbar \cdot \big(q_1 \cdot \partial_2 V - q_2 \cdot \partial_1 V\big) \cdot \psi$, y con $\partial_k V = V'(r) \cdot \dfrac{q_k}{r}$, el paréntesis es $\dfrac{V'(r)}{r} \cdot (q_1 \cdot q_2 - q_2 \cdot q_1) = 0$.

  Lo mismo vale para $\hat{\ell}_1$ y $\hat{\ell}_2$, y se conserva $\langle \hat{\vec{\ell}} \rangle$.
* **Energía.** $[\hat{H}, \hat{H}] = 0$, y $\langle \hat{H} \rangle$ se conserva si $V$ no depende de $t$. Es lo mismo que da la traslación en el tiempo, $\tau = 1$, con $Q = -\langle \hat{H} \rangle$ (parte matemática, apartado 10.3).
* **Teorema de Ehrenfest.** Por la regla de Leibniz y la relación canónica, $[\hat{p}_k^2, \hat{q}_k] = \hat{p}_k[\hat{p}_k, \hat{q}_k] + [\hat{p}_k, \hat{q}_k]\hat{p}_k = -2 \cdot i \cdot \hbar \cdot \hat{p}_k$, así que $[\hat{H}, \hat{q}_k] = -\dfrac{i \cdot \hbar}{m} \cdot \hat{p}_k$. La ecuación de Heisenberg da
  $$
  \begin{aligned}
  \dfrac{d}{dt}\langle \hat{q}_k \rangle = \dfrac{\langle \hat{p}_k \rangle}{m}, \qquad \dfrac{d}{dt}\langle \hat{p}_k \rangle = -\langle \partial_k V \rangle:
  \end{aligned}
  $$
  las leyes de Newton para los valores esperados.

**Lo que añade la mecánica cuántica.**

* **Se conserva toda la distribución.** Si $[\hat{H}, \hat{A}] = 0$, por la regla de Leibniz $\hat{H}$ conmuta también con $\hat{A}^2$, $\hat{A}^3$, ..., y se conservan todos los $\langle \hat{A}^k \rangle$: los momentos de la distribución de los resultados de medir $\hat{A}$, no solo su media (con las precisiones sobre los dominios).
* **Números cuánticos.** Como $\hat{H}$ y $\hat{A}$ conmutan, los estados estacionarios se pueden elegir funciones propias de $\hat{A}$, y se etiquetan con sus valores propios. Un estado con un valor definido de $\hat{A}$ lo conserva.
* **Cantidades conservadas que no conmutan entre sí.** Las componentes de $\hat{\vec{\ell}}$ cumplen $[\hat{\ell}_1, \hat{\ell}_2] = i \cdot \hbar \cdot \hat{\ell}_3$ (y las que resultan de permutar cíclicamente los índices), y no pueden tener a la vez valores definidos. Con un potencial central, los estados estacionarios se etiquetan con la energía, con $\hat{\vec{\ell}}^{\,2} := \sum_k \hat{\ell}_k^2$, que conmuta con las tres componentes, y con una sola componente, $\hat{\ell}_3$. Sus valores propios son $\hbar^2 \cdot \ell \cdot (\ell + 1)$, con $\ell = 0, 1, 2, \dots$, y $\hbar \cdot m_\ell$, con $m_\ell = -\ell, \dots, \ell$ (Sakurai y Napolitano, 2017, cap. 3). El desarrollo está en «El teorema de Noether: ejemplos físicos (versión 2)».

### 10.5. El cambio de velocidad: la fase

En la mecánica clásica, el cambio de velocidad necesita $F = m \cdot \vec{u} \cdot \vec{q}$ (apartado 4.1). En la cuántica, trasladar la función de onda con velocidad $\varepsilon \cdot \vec{u}$, $\psi(t, \vec{q} - \varepsilon \cdot \vec{u} \cdot t)$, no lleva soluciones de la ecuación de Schrödinger libre en soluciones. Hace falta una fase:

$$
\begin{aligned}
\big(\hat{U}(\varepsilon)\psi\big)(t, \vec{q}) := e^{i \cdot \left(\varepsilon \cdot m \cdot \vec{u} \cdot \vec{q} - \varepsilon^2 \cdot m \cdot |\vec{u}|^2 \cdot t/2\right)/\hbar} \cdot \psi(t, \vec{q} - \varepsilon \cdot \vec{u} \cdot t).
\end{aligned}
$$

* **Lleva soluciones en soluciones**: si $\psi$ cumple la ecuación de Schrödinger libre, también la cumple $\hat{U}(\varepsilon)\psi$ (comprobado con SymPy). La fase cambia el momento en $\varepsilon \cdot m \cdot \vec{u}$, que es lo que debe hacer un cambio de velocidad: $e^{i \cdot \varepsilon \cdot m \cdot \vec{u} \cdot \vec{q}/\hbar} \cdot e^{i \cdot \vec{p} \cdot \vec{q}/\hbar} = e^{i \cdot (\vec{p} + \varepsilon \cdot m \cdot \vec{u}) \cdot \vec{q}/\hbar}$.
* **El generador.** Derivando en $\varepsilon = 0$, $\xi = \dfrac{i}{\hbar} \cdot m \cdot (\vec{u} \cdot \vec{q}) \cdot \psi - t \cdot \vec{u} \cdot \nabla\psi = -\dfrac{i}{\hbar} \cdot \big(t \cdot \vec{u} \cdot \hat{\vec{p}} - m \cdot \vec{u} \cdot \hat{\vec{q}}\big)\psi$. Es la familia del apartado 10.4 con $\hat{A} = -\vec{u} \cdot \hat{\vec{G}}$, donde
  $$
  \begin{aligned}
  \hat{\vec{G}} := m \cdot \hat{\vec{q}} - \hat{\vec{p}} \cdot t
  \end{aligned}
  $$
  es el operador del vector $\vec{G}$ del apartado 4.1. Depende explícitamente de $t$.
* **La condición.** $\partial_t \hat{G}_k = -\hat{p}_k$, y con el apartado 10.4, $\dfrac{i}{\hbar} \cdot [\hat{H}, m \cdot \hat{q}_k] = \hat{p}_k$ y $\dfrac{i}{\hbar} \cdot [\hat{H}, -\hat{p}_k \cdot t] = t \cdot \partial_k V$. Por tanto,
  $$
  \begin{aligned}
  \partial_t \hat{G}_k + \dfrac{i}{\hbar} \cdot [\hat{H}, \hat{G}_k] = -\hat{p}_k + \hat{p}_k + t \cdot \partial_k V = t \cdot \partial_k V,
  \end{aligned}
  $$
  que es nulo para la partícula libre. Se conserva $\langle \hat{\vec{G}} \rangle = m \cdot \langle \hat{\vec{q}} \rangle - \langle \hat{\vec{p}} \rangle \cdot t$: la posición media se mueve con velocidad constante, $\dfrac{\langle \hat{\vec{p}} \rangle}{m}$. En un campo uniforme, $\nabla V$ es constante, y el término $-t \cdot \vec{u} \cdot \nabla V$ que queda en la condición de $\hat{A} = -\vec{u} \cdot \hat{\vec{G}}$ se compensa sumando a $\hat{A}$ el múltiplo de la identidad $\dfrac{t^2}{2} \cdot \vec{u} \cdot \nabla V$: una fase más, que solo depende de $t$.
* **Otro ejemplo: la traslación en un campo uniforme.** Con $\nabla V \cdot \vec{a} = -\kappa$ constante, como en el apartado 4.2, $\hat{A} = \vec{a} \cdot \hat{\vec{p}} - \kappa \cdot t$ cumple $\partial_t \hat{A} + \dfrac{i}{\hbar} \cdot [\hat{H}, \hat{A}] = -\kappa - \vec{a} \cdot \nabla V = 0$. La familia es la traslación multiplicada por la fase $e^{i \cdot \varepsilon \cdot \kappa \cdot t/\hbar}$, y se conserva $\langle \vec{a} \cdot \hat{\vec{p}} \rangle - \kappa \cdot t$, como en la mecánica clásica.
* **La fase y $F$.** En los dos ejemplos, la familia lleva, a primer orden, el factor $e^{i \cdot \varepsilon \cdot F/\hbar}$, con la $F$ de la simetría clásica: $F = m \cdot \vec{u} \cdot \vec{q}$ en el cambio de velocidad y $F = \kappa \cdot t$ en la traslación. Es un hecho general en la formulación de Feynman (Feynman y Hibbs, 1965), en la que cada camino contribuye con el factor $e^{i \cdot \bsS/\hbar}$: sumar $\dot{F}$ al lagrangiano cambia $\bsS$ en los valores de $F$ en los extremos, y eso se compensa multiplicando la función de onda por $e^{i \cdot F/\hbar}$. La fase exacta del cambio de velocidad también lo es: escrita en el punto de partida, $\vec{q} - \varepsilon \cdot \vec{u} \cdot t$, su exponente es $\dfrac{1}{\hbar} \cdot \big(\varepsilon \cdot m \cdot \vec{u} \cdot (\vec{q} - \varepsilon \cdot \vec{u} \cdot t) + \varepsilon^2 \cdot m \cdot |\vec{u}|^2 \cdot t/2\big)$, y $\dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}} + \varepsilon \cdot \vec{u}|^2 - \dfrac{1}{2} \cdot m \cdot |\dot{\vec{q}}|^2 = \dfrac{d}{dt}\big(\varepsilon \cdot m \cdot \vec{u} \cdot \vec{q} + \varepsilon^2 \cdot m \cdot |\vec{u}|^2 \cdot t/2\big)$, la fórmula exacta de la parte matemática, apartado 9.5.
* **Una consecuencia: la masa.** Con $\varepsilon = 1$ y $t$ fijo, sean $\hat{B}$ el cambio de velocidad $\vec{u}$ y $\hat{T}$ la traslación $\vec{a}$, $(\hat{T}\psi)(\vec{q}) = \psi(\vec{q} - \vec{a})$. Entonces $\hat{B}\hat{T} = e^{i \cdot m \cdot \vec{u} \cdot \vec{a}/\hbar} \cdot \hat{T}\hat{B}$ (comprobado con SymPy): las transformaciones de Galileo se componen como en el grupo solo salvo fases, que dependen de la masa. Una fase global no cambia el estado, pero una superposición de estados con masas distintas no se transformaría de forma coherente. Es la **regla de superselección de la masa**: esas superposiciones no se admiten (Bargmann, 1954; Lévy-Leblond, 1963; anexos, apartado 6.3).

### 10.6. Por qué no se aplica el grupo de Lorentz

* **La ecuación de Schrödinger es de Galileo.** $\hat{H}$ procede de $\bsH = \dfrac{|\vec{p}|^2}{2 \cdot m} + V$, la energía de la mecánica de Newton. La ecuación es de primer orden en $t$ y de segundo en $\vec{q}$. Un cambio de velocidad de Lorentz mezcla $t$ y $q_1$ (apartado 9.1), y con ellos las derivadas $\partial_t$ y $\partial_1$: una ecuación con órdenes distintos en $t$ y en $q_1$ no puede conservar su forma. Sus simetrías son las de Galileo, con la fase del apartado 10.5. Es válida cuando las energías, sin contar la energía en reposo, son pequeñas frente a $m \cdot c^2$.
* **La ecuación relativista.** Partiendo de $E^2 = |\vec{p}|^2 \cdot c^2 + m^2 \cdot c^4$ (apartado 9.2) y sustituyendo $E$ por $i \cdot \hbar \cdot \partial_t$ y $\vec{p}$ por $-i \cdot \hbar \cdot \nabla$, que es lo que hacen sobre $e^{-i \cdot (E \cdot t - \vec{p} \cdot \vec{q})/\hbar}$, se obtiene la **ecuación de Klein–Gordon**:
  $$
  \begin{aligned}
  \dfrac{1}{c^2} \cdot \partial_t^2 \phi - \nabla^2\phi + \left(\dfrac{m \cdot c}{\hbar}\right)^2 \cdot \phi = 0.
  \end{aligned}
  $$
  Es invariante bajo el grupo de Lorentz, como la ecuación de ondas de la cuerda (apartado 9.5), y es la ecuación de Euler–Lagrange de una densidad lagrangiana invariante bajo el grupo de Poincaré. Sus diez simetrías dan, con la parte matemática, apartado 8, la energía, la cantidad de movimiento, el momento angular y el movimiento del centro de energía. Como ecuación de una partícula tiene dificultades: es de segundo orden en $t$, y la densidad que da la simetría de fase puede ser negativa, así que no es una densidad de probabilidad. Su interpretación coherente necesita la teoría cuántica de campos. Para las partículas de espín $\dfrac{1}{2}$, como el electrón, la ecuación relativista es la de Dirac (1928), de primer orden en $t$ y en $\vec{q}$ (Weinberg, 1995, caps. 1 y 2; Peskin y Schroeder, 1995, caps. 2 y 3). Las representaciones del grupo de Poincaré en un espacio de Hilbert clasifican las partículas por su masa y su espín (Wigner, 1939).
* **El límite no relativista.** Con $\phi = e^{-i \cdot m \cdot c^2 \cdot t/\hbar} \cdot \psi$, la regla del producto da
  $$
  \begin{aligned}
  \dfrac{1}{c^2} \cdot \partial_t^2 \phi = e^{-i \cdot m \cdot c^2 \cdot t/\hbar} \cdot \left(\dfrac{1}{c^2} \cdot \partial_t^2 \psi - \dfrac{2 \cdot i \cdot m}{\hbar} \cdot \partial_t \psi - \dfrac{m^2 \cdot c^2}{\hbar^2} \cdot \psi\right).
  \end{aligned}
  $$
  En la ecuación de Klein–Gordon, el último término cancela el de la masa, y queda $\dfrac{1}{c^2} \cdot \partial_t^2 \psi - \dfrac{2 \cdot i \cdot m}{\hbar} \cdot \partial_t \psi - \nabla^2\psi = 0$. Si $\psi$ varía despacio comparada con $e^{-i \cdot m \cdot c^2 \cdot t/\hbar}$ (energías pequeñas frente a $m \cdot c^2$), el primer término es despreciable frente al segundo. Sin él, y multiplicando por $-\dfrac{\hbar^2}{2 \cdot m}$, queda $i \cdot \hbar \cdot \partial_t \psi = -\dfrac{\hbar^2}{2 \cdot m} \cdot \nabla^2\psi$: la ecuación de Schrödinger libre.
* **La fase de la energía en reposo.** $e^{-i \cdot m \cdot c^2 \cdot t/\hbar}$ es la fase de un estado estacionario con energía $m \cdot c^2$ (apartado 10.2). Al aplicar a $\phi$ el cambio de velocidad de Lorentz, a primer orden $\phi\big(t - \varepsilon \cdot \vec{u} \cdot \vec{q}/c^2, \vec{q} - \varepsilon \cdot \vec{u} \cdot t\big)$, esa fase se convierte en $e^{-i \cdot m \cdot c^2 \cdot t/\hbar} \cdot e^{i \cdot \varepsilon \cdot m \cdot \vec{u} \cdot \vec{q}/\hbar}$. La fase del cambio de velocidad de Galileo es lo que queda de la de la energía en reposo al mover el tiempo en $\varepsilon \cdot \dfrac{\vec{u} \cdot \vec{q}}{c^2}$, como la $F$ de Galileo es lo que queda de $-\tau \cdot \bsH$ (apartado 9.4).

## 11. Lo que el teorema no dice

* **Las simetrías discretas no dan cantidades conservadas por este camino.** La reflexión $\vec{q} \mapsto -\vec{q}$ puede dejar $\bsL$ igual, pero no depende de un parámetro continuo, no tiene generador y el teorema no se aplica.
* **En mecánica cuántica, la regla es más amplia.** «Si conmuta con $\hat{H}$, se conserva» (apartado 10.4) solo usa la ecuación de Schrödinger y que los operadores sean autoadjuntos, y vale para cualquier operador autoadjunto, genere o no una familia continua. La **paridad**, $(\hat{P}\psi)(\vec{q}) := \psi(-\vec{q})$, es autoadjunta, cumple $\hat{P}^2 = 1$ y tiene los valores propios $\pm 1$. Si $V(-\vec{q}) = V(\vec{q})$, conmuta con $\hat{H}$, y la paridad de un estado se conserva: es un número cuántico que no procede del teorema de Noether.
* **La simetría es de la ley, no de cada movimiento.** En un campo central, $\bsL$ es invariante bajo todos los giros, pero una órbita elíptica concreta no lo es. Lo que el teorema garantiza es que la cantidad asociada, $\vec{\ell}$, es constante en cada movimiento. Un giro lleva cada movimiento real a otro movimiento real, en general distinto.
* **Una transformación que no es simetría no implica que la cantidad no se conserve en ningún movimiento.** En el campo central, $\vec{p}$ no se conserva en general, pero en un movimiento con $\vec{q}$ en reposo en un punto de equilibrio, si existiera, sería constante. El teorema habla de todos los movimientos a la vez.
* **Una simetría del lagrangiano no basta para conservar el total de un campo.** Da la ley local, pero el total se conserva solo si las condiciones de contorno anulan el flujo (parte matemática, apartados 8.7 y 8.8; apartado 10.3).

## 12. Referencias

* Ballentine, L. E. (1998). *Quantum mechanics: A modern development*. World Scientific.
* Bargmann, V. (1954). On unitary ray representations of continuous groups. *Annals of Mathematics*, *59*(1), 1–46.
* Currie, D. G., Jordan, T. F. y Sudarshan, E. C. G. (1963). Relativistic invariance and Hamiltonian theories of interacting particles. *Reviews of Modern Physics*, *35*(2), 350–375.
* Dirac, P. A. M. (1928). The quantum theory of the electron. *Proceedings of the Royal Society of London. Series A*, *117*(778), 610–624.
* Einstein, A. (1905). Zur Elektrodynamik bewegter Körper. *Annalen der Physik*, *322*(10), 891–921.
* Feynman, R. P. y Hibbs, A. R. (1965). *Quantum mechanics and path integrals*. McGraw-Hill.
* Inönü, E. y Wigner, E. P. (1953). On the contraction of groups and their representations. *Proceedings of the National Academy of Sciences*, *39*(6), 510–524.
* Landau, L. D. y Lifshitz, E. M. (1975). *The classical theory of fields* (4.ª ed.). Pergamon Press.
* Lévy-Leblond, J.-M. (1963). Galilei group and nonrelativistic quantum mechanics. *Journal of Mathematical Physics*, *4*(6), 776–788.
* Peskin, M. E. y Schroeder, D. V. (1995). *An introduction to quantum field theory*. Addison-Wesley.
* Reed, M. y Simon, B. (1980). *Methods of modern mathematical physics: Vol. 1. Functional analysis* (ed. rev.). Academic Press.
* Sakurai, J. J. y Napolitano, J. (2017). *Modern quantum mechanics* (2.ª ed.). Cambridge University Press.
* Weinberg, S. (1995). *The quantum theory of fields: Vol. 1. Foundations*. Cambridge University Press.
* Wigner, E. (1939). On unitary representations of the inhomogeneous Lorentz group. *Annals of Mathematics*, *40*(1), 149–204.

Las cuentas nuevas de este documento (la partícula relativista: momento, energía, las simetrías, el cambio de velocidad con $F = 0$ y su límite de Galileo, y el de dos partículas como simetría generalizada; la densidad lagrangiana de Schrödinger, sus ecuaciones de Euler–Lagrange, la corriente de probabilidad y las densidades de energía y de momento; el término $D$ de una familia unitaria con generador dependiente del tiempo; los conmutadores; la fase del cambio de velocidad y su composición con las traslaciones; y el límite no relativista de Klein–Gordon) están comprobadas con SymPy en Teorema-de-Noether-v2-comprobaciones.py, en el mismo directorio que este documento.
