# El teorema de Noether (versión para el trabajo)

<!--
Versión del teorema de Noether que entra en el trabajo «La importancia de las simetrías en física»:
el apartado «Simetrías y teorema de Noether» (4.2) del capítulo de desarrollo, con sus tres ejemplos,
y el anexo B. La versión completa es la serie «El teorema de Noether», en este mismo directorio.
Sustituye a borrador-Noether-J-13-trabajo.md (versión J-13, 05-10-2026).
Cada bloque lleva una línea «Fuente:» con el documento y el apartado de origen, y lo que se ha
cambiado; esas líneas se borran al pasar el texto a simetrias.md.
-->

## Espacio

| Parte del trabajo | Previsto (propuesta 3) | Medido con la plantilla de UNIR |
| --- | --- | --- |
| Desarrollo › Simetrías y teorema de Noether (4.2), con los tres ejemplos | 6 páginas (los antiguos 4.2 y 4.3 de la pareja 1) | unas 8,3 (antes, 4.2 y 4.3 por separado: 5,35 + 4,0) |
| Anexo B: las simetrías de Galileo (cambios de velocidad, sistemas de partículas, grupo de Galileo) | — (3 páginas como máximo para todos los anexos) | unas 1,8 |
| Anexo A, para comparar | 1–2 páginas | unas 2,4 |

Las medidas se han hecho compilando `simetrias.md` con la plantilla real del trabajo (`trabajos/_plantilla/unir.latex`, 11 puntos, interlineado 1,5), como diferencia entre la posición del título y el final del texto en el PDF. El PDF completo tiene 31 páginas, con los apartados de la pareja 2 todavía sin integrar y las conclusiones sin escribir. Los dos anexos suman unas 4,2 páginas, por encima de las 3 previstas para todos los anexos.

## Estructura del desarrollo (desde el 07-10-2026)

* 4.1. Formalismo lagrangiano (pareja 1).
* 4.2. Simetrías y teorema de Noether, con los ejemplos que antes formaban el 4.3: la partícula libre, el tiro parabólico y la fuerza central (pareja 1).
* 4.3. La parte cuántica de la pareja 2, a partir del texto de Gonzalo (pendiente de integrar).
* 4.4. El siguiente apartado de la pareja 2 (pendiente de recibir).

`simetrias.md` contiene solo lo hecho: introducción, contexto histórico, objetivos, 4.1 y 4.2, el capítulo de conclusiones sin texto (es obligatorio en el modelo), la bibliografía y los anexos A y B. Los cambios de velocidad y el grupo de Galileo pasan al anexo B, porque son la ampliación propuesta por la pareja 1 que el grupo aún no ha acordado (`documento_general_trabajo.md`, sección 6: «ampliación de +1 página o anexo»).

## Cambios respecto de la versión J-13

La versión J-13 (`borrador-Noether-J-13-trabajo.md`, integrada en `simetrias.md` el 05-10-2026) tenía estos problemas, que esta versión corrige:

1. **Inconsistencia en la traslación vertical.** La definición de simetría admitía una derivada total, $\delta L = \varepsilon \cdot \dfrac{dF}{dt}$, pero el tiro parabólico decía que la traslación vertical no es una simetría. Con esa definición sí lo es: $\delta L = -m \cdot g \cdot \varepsilon$ es la derivada de $-m \cdot g \cdot \varepsilon \cdot t$, y el teorema da que se conserva $p_z + m \cdot g \cdot t$. Lo que la gravedad rompe es la conservación de $p_z$ y la isotropía: los giros alrededor de ejes horizontales no son simetrías.
2. **La energía, sin demostrar.** La fórmula $Q = \sum_i p_i \cdot \xi_i - H \cdot \tau - F$ se enunciaba sin demostración («aparece un término adicional»). Ahora la energía sale del mismo teorema demostrado, con el generador $\xi_i = \dot{q}_i$ y $F = L$. La fórmula general, con su demostración, está en la parte matemática de la serie.
3. **Los ejemplos no se conectaban con el teorema.** Los de la coordenada cíclica no pasaban por el teorema, y los del teorema (potencial central, grupo de Galileo) no se comprobaban. Ahora hay una receta de cuatro pasos, y cada ejemplo la sigue y termina comprobando la cantidad conservada sobre la solución explícita.
4. **Faltaba el ejemplo más sencillo.** La partícula libre tiene todas las simetrías del espacio y del tiempo, y en ella cada cantidad conservada se comprueba con $\vec{r}(t) = \vec{r}_0 + \vec{v}_0 \cdot t$. El campo uniforme es el tiro parabólico, ahora tratado paso a paso.
5. **Duplicación.** El potencial central se desarrollaba dos veces; ahora, una.
6. **Notación.** $\vec{q}$ y $\vec{r}$ para la posición; ahora solo $\vec{r}$, y $q_i$ para las coordenadas generalizadas.
7. **Reglas de estilo.** `\frac`, multiplicaciones implícitas (`\frac{1}{2}m |\dot{\vec{q}}|^2`, `\vec{u} t`, `m_a \vec{q}_a`, `H \tau`), fórmulas display en una sola línea sin `aligned` dentro de las listas, mayúsculas en los títulos («Grupo de Galileo», «Partícula bajo...») y el anglicismo «boosts».
8. **Tono.** Adjetivos valorativos y coloquialismos: «inexorablemente», «es crucial», «de forma irrefutable», «de un solo plumazo», «regalado», «sorprendentemente», «encierra en su seno», «las 10 magnitudes fundamentales del universo clásico», «la potencia del teorema», «caso paradigmático».

## Criterios de la extracción

1. Lo que piden los guiones de los antiguos 4.2 y 4.3 (`documento_general_trabajo.md`: coordenada cíclica, simetría, teorema con demostración de tres líneas, energía; tiro parabólico y fuerza central), más la partícula libre como primer ejemplo.
2. Notación del trabajo, no la de la serie: $L$, $S$ y $H$ sin negrita; $q_i$ y $t$ en lugar de $f$ y $x$; $\vec{r}$ para la posición; $\varepsilon$ en lugar de $\epsilon$; $\Phi_\varepsilon$ para la familia de transformaciones; $\vec{L}$ y $L_z$ para el momento angular (la notación de la parte cuántica).
3. Solo transformaciones que no mueven el tiempo: la traslación en el tiempo se trata con el generador $\xi_i = \dot{q}_i$, que el teorema demostrado cubre. La fórmula con $\tau$ queda en la serie.
4. En el texto principal, las tres conservaciones (cantidad de movimiento, momento angular y energía), que son la pregunta del trabajo. Los cambios de velocidad, el vector $\vec{G}$, los sistemas de partículas y el grupo de Galileo, en el anexo B.

## Trazabilidad

| Fragmento del trabajo | Documento de origen | Apartado de origen | Cambios |
| --- | --- | --- | --- |
| La coordenada cíclica | parte matemática | «Dos casos particulares › Una componente que no aparece en $\bsL$» | Con la partícula libre y el campo uniforme como ejemplos |
| Transformaciones continuas, generador, definición de simetría | parte matemática | «Transformaciones de las funciones»; «Simetría de un funcional › Definición» y «Lo que significa para el funcional» | Una variable; sin la equivalencia con la forma integral |
| Simetría y estacionariedad | parte matemática | «Simetría de un funcional › Simetría y estacionariedad» | En dos frases, sin la tabla |
| Teorema y demostración | parte matemática | «El teorema de Noether» | Sin la identidad de Noether ni las observaciones |
| Cómo se aplica | parte física | «El teorema en mecánica» (los cuatro pasos) | — |
| La energía | parte matemática | «Dos casos particulares › Cuando $\bsL$ no depende de la variable» | $x \to t$; $H = T + V$, de la versión anterior del trabajo |
| Primer ejemplo: la partícula libre | parte física y ejemplos físicos | «Primera etapa › La partícula libre»; «Ejemplo: la partícula libre» | Sin los cambios de velocidad; generador del giro deducido en el texto |
| Segundo ejemplo: el tiro parabólico | ejemplos físicos | «Ejemplo: una partícula en un campo uniforme» | Sin los cambios de velocidad |
| Tercer ejemplo: la fuerza central | ejemplos físicos | «Ejemplo: una partícula en un campo central» | Potencial efectivo y Kepler, de la versión anterior del trabajo |
| Lo que muestran los ejemplos | parte física | «Primera etapa › Una partícula en un campo exterior» (tabla) | Sin los cambios de velocidad |
| Anexo B: cambio de velocidad y las diez simetrías | parte física y ejemplos físicos | «Primera etapa › La partícula libre»; «Ejemplo: la partícula libre» | La parte de los cambios de velocidad |
| Anexo B: varias partículas y grupo de Galileo | parte física; anexos | «Tercera etapa»; «El grupo de Galileo»; «El grupo de Galileo» (anexos) | Solo la tabla de condiciones y la conclusión; $\vec{J} \to \vec{L}$ |

## Texto del apartado «Simetrías y teorema de Noether»

### Simetrías y teorema de Noether

Este apartado resume @calderon2026noethermat, para la definición de simetría y el teorema, y @calderon2026noetherfis y @calderon2026noetherfisej, para los ejemplos. Con el lenguaje del apartado anterior se puede precisar qué es una simetría y demostrar que cada simetría continua lleva asociada una cantidad conservada. Después, tres ejemplos aplican el teorema paso a paso, de más a menos simétricos: la partícula libre, el tiro parabólico y la fuerza central.

> Fuente: «parte matemática», «Dos casos particulares › Una componente que no aparece en $\bsL$». Modificaciones: $f \to q$, $x \to t$; los dos ejemplos son nuevos en este lugar.

#### La coordenada cíclica

Una coordenada $q_k$ que no aparece en el lagrangiano, aunque sí aparezca su velocidad $\dot{q}_k$, se llama **cíclica**. Para ella, $\dfrac{\partial L}{\partial q_k} = 0$, y la ecuación de Euler–Lagrange queda

$$
\begin{aligned}
\dfrac{dp_k}{dt} = \dfrac{\partial L}{\partial q_k} = 0:
\end{aligned}
$$

su momento conjugado se conserva. Que $q_k$ no aparezca en $L$ significa que desplazar el sistema en esa coordenada no cambia el lagrangiano. Dos ejemplos:

* **Partícula libre.** Sin fuerzas, $L = \dfrac{1}{2} \cdot m \cdot (\dot{x}^2 + \dot{y}^2 + \dot{z}^2)$ no contiene ninguna coordenada. Las tres son cíclicas, y se conserva $\vec{p} = m \cdot \dot{\vec{r}}$: la partícula se mueve con velocidad constante. La primera ley de Newton aparece como consecuencia de que en el espacio vacío ningún punto es privilegiado.
* **Partícula en un campo uniforme.** Con la gravedad y el eje $z$ vertical hacia arriba, $L = \dfrac{1}{2} \cdot m \cdot (\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - m \cdot g \cdot z$. Las coordenadas $x$ e $y$ son cíclicas, y se conservan $p_x$ y $p_y$. La coordenada $z$ no lo es, y $p_z$ no se conserva.

Pero que una coordenada sea cíclica depende de las coordenadas elegidas. En la fuerza central, con una energía potencial $V(r)$ que solo depende de la distancia al centro, ninguna coordenada cartesiana es cíclica; en coordenadas polares, el ángulo sí lo es (tercer ejemplo de este apartado). Hace falta una formulación que no dependa de esa elección, y es la que da el teorema de Noether.

> Fuente: «parte matemática», «Transformaciones de las funciones» y «Simetría de un funcional» (definición, significado para el funcional, simetría y estacionariedad). Modificaciones: una variable; la equivalencia con la forma integral, en una frase; la comparación, sin tabla. Ejemplo: «parte física», «Primera etapa › La partícula libre».

#### Transformaciones continuas y simetrías

Una **transformación continua** es una familia $\Phi_\varepsilon$ de transformaciones que depende de un parámetro real $\varepsilon$, como una distancia o un ángulo, y que para $\varepsilon = 0$ es la identidad. Por ejemplo, las traslaciones de longitud $\varepsilon$ en una dirección fija, o los giros de ángulo $\varepsilon$ alrededor de un eje fijo. A primer orden en $\varepsilon$, cada coordenada cambia en

$$
\begin{aligned}
q_i \to q_i + \varepsilon \cdot \xi_i,
\end{aligned}
$$

donde $\xi_i$, el **generador**, indica en qué dirección empieza a moverse la coordenada $q_i$; puede depender de las coordenadas, de las velocidades y del tiempo. Las velocidades cambian entonces en $\varepsilon \cdot \dot{\xi}_i$, donde $\dot{\xi}_i$ es la derivada de $\xi_i$ respecto del tiempo a lo largo de la trayectoria. Por el desarrollo de Taylor, el lagrangiano cambia en

$$
\begin{aligned}
\delta L &:= L(q + \varepsilon \cdot \xi, \dot{q} + \varepsilon \cdot \dot{\xi}, t) - L(q, \dot{q}, t) \\
&= \varepsilon \cdot \sum_i \left( \dfrac{\partial L}{\partial q_i} \cdot \xi_i + \dfrac{\partial L}{\partial \dot{q}_i} \cdot \dot{\xi}_i \right) + O(\varepsilon^2).
\end{aligned}
$$

**Definición.** La transformación es una **simetría** si el término de primer orden es la derivada respecto del tiempo de alguna función $F(q, \dot{q}, t)$,

$$
\begin{aligned}
\sum_i \left( \dfrac{\partial L}{\partial q_i} \cdot \xi_i + \dfrac{\partial L}{\partial \dot{q}_i} \cdot \dot{\xi}_i \right) = \dfrac{dF}{dt},
\end{aligned}
$$

para **cualquier** trayectoria $q(t)$, sea o no la real. En la mayoría de los casos, $F = 0$: el lagrangiano no cambia a primer orden. Se admite una derivada total porque la acción cambia entonces, a primer orden, en $\varepsilon \cdot \big(F(t_2) - F(t_1)\big)$, que solo depende de lo que ocurre en los extremos; y cuando $F$ solo depende de las coordenadas y del tiempo, sumar $\dfrac{dF}{dt}$ al lagrangiano no cambia las ecuaciones de Euler–Lagrange [@calderon2026anexos].

**Simetría y estacionariedad.** Las dos ideas usan la variación del lagrangiano, pero responden a preguntas distintas. La estacionariedad (el principio de Hamilton) fija los extremos, varía la trayectoria de cualquier manera y selecciona las trayectorias reales. La simetría fija una transformación y exige una propiedad para todas las trayectorias: es una propiedad del lagrangiano, es decir, de la ley, y no de una solución particular.

**Un ejemplo, en la partícula libre.** Con $L = \dfrac{1}{2} \cdot m \cdot |\dot{\vec{r}}|^2$, $L$ no depende de las coordenadas y $\dfrac{\partial L}{\partial \dot{q}_i} = m \cdot \dot{q}_i$, así que el término de primer orden es $m \cdot \dot{\vec{r}} \cdot \dot{\vec{\xi}}$. Para la traslación en la dirección de un vector fijo $\vec{a}$, $\vec{r} \to \vec{r} + \varepsilon \cdot \vec{a}$, con $\vec{\xi} = \vec{a}$ y $\dot{\vec{\xi}} = \vec{0}$, el término es nulo: es una simetría con $F = 0$. Los casos con $F \neq 0$ aparecen más adelante, en la energía y en el tiro parabólico, y en los cambios de velocidad del anexo B.

> Fuente: «parte matemática», «El teorema de Noether» (enunciado y demostración). Modificaciones: $f \to q$, $x \to t$; la demostración, en la forma corta, sin la identidad de Noether. Los cuatro pasos: «parte física», «El teorema en mecánica».

#### El teorema de Noether

**Teorema.** Si la transformación de generador $\xi_i$ es una simetría, con la función $F$, la cantidad

$$
\begin{aligned}
Q = \sum_i p_i \cdot \xi_i - F, \qquad p_i = \dfrac{\partial L}{\partial \dot{q}_i},
\end{aligned}
$$

se conserva a lo largo de las trayectorias reales.

**Demostración.** Por la definición de simetría y, en las trayectorias reales, por la ecuación de Euler–Lagrange, $\dfrac{\partial L}{\partial q_i} = \dot{p}_i$:

$$
\begin{aligned}
\dfrac{dF}{dt} = \sum_i \left( \dfrac{\partial L}{\partial q_i} \cdot \xi_i + \dfrac{\partial L}{\partial \dot{q}_i} \cdot \dot{\xi}_i \right) = \sum_i \left( \dot{p}_i \cdot \xi_i + p_i \cdot \dot{\xi}_i \right) = \dfrac{d}{dt}\left( \sum_i p_i \cdot \xi_i \right).
\end{aligned}
$$

La última igualdad es la regla de derivación del producto. Por tanto,

$$
\begin{aligned}
\dfrac{d}{dt}\left(\sum_i p_i \cdot \xi_i - F\right) = 0. \qquad \blacksquare
\end{aligned}
$$

La demostración solo usa que $\xi_i$ es una función derivable del tiempo a lo largo de cada trayectoria, así que vale igual si el generador depende de las velocidades o del tiempo.

**Cómo se aplica.** En todos los ejemplos se siguen cuatro pasos: obtener el generador $\xi_i$; calcular el término de primer orden de $\delta L$ y ver si es una derivada total $\dfrac{dF}{dt}$; escribir $Q$; y comprobar que $Q$ es constante sobre la solución. La coordenada cíclica es el caso más sencillo: $\xi_k = 1$, las demás $\xi_i$ nulas y $F = 0$ dan $Q = p_k$.

> Fuente: «parte matemática», «Dos casos particulares › Cuando $\bsL$ no depende de la variable: la identidad de Beltrami». Modificaciones: $x \to t$, $\bsH \to H$; $H = T + V$ y $\dfrac{dH}{dt} = -\dfrac{\partial L}{\partial t}$, de la versión anterior del trabajo.

#### La energía y la traslación en el tiempo

Desplazar una trayectoria en el tiempo, $q(t) \to q(t + \varepsilon) = q(t) + \varepsilon \cdot \dot{q}(t) + O(\varepsilon^2)$, es una transformación de generador $\xi_i = \dot{q}_i$, con $\dot{\xi}_i = \ddot{q}_i$. Por la regla de la cadena, el término de primer orden de $\delta L$ es

$$
\begin{aligned}
\sum_i \left( \dfrac{\partial L}{\partial q_i} \cdot \dot{q}_i + \dfrac{\partial L}{\partial \dot{q}_i} \cdot \ddot{q}_i \right) = \dfrac{dL}{dt} - \dfrac{\partial L}{\partial t}.
\end{aligned}
$$

Si $L$ no depende explícitamente del tiempo, es decir, si las leyes son las mismas hoy que mañana, el término es $\dfrac{dL}{dt}$: es una simetría con $F = L$, y el teorema da que se conserva el **hamiltoniano**

$$
\begin{aligned}
H := \sum_i p_i \cdot \dot{q}_i - L.
\end{aligned}
$$

La misma cuenta que en la demostración del teorema, sin suponer nada sobre $L$, da sobre las trayectorias reales

$$
\begin{aligned}
\dfrac{d}{dt}\left(\sum_i p_i \cdot \dot{q}_i\right) = \dfrac{dL}{dt} - \dfrac{\partial L}{\partial t}, \qquad \text{es decir,} \qquad \dfrac{dH}{dt} = -\dfrac{\partial L}{\partial t}.
\end{aligned}
$$

En los ejemplos del trabajo, $H$ es la energía. Cada término de la energía cinética es cuadrático en una velocidad, como $\dfrac{1}{2} \cdot m \cdot \dot{x}^2$ o $\dfrac{1}{2} \cdot m \cdot r^2 \cdot \dot{\theta}^2$, y al multiplicar su derivada por la velocidad se obtiene el doble del término: $\dot{x} \cdot (m \cdot \dot{x}) = 2 \cdot \dfrac{1}{2} \cdot m \cdot \dot{x}^2$. Como $V$ no depende de las velocidades, $\sum_i p_i \cdot \dot{q}_i = 2 \cdot T$, y

$$
\begin{aligned}
H = 2 \cdot T - (T - V) = T + V = E.
\end{aligned}
$$

> Fuente: «parte física», «Primera etapa › La partícula libre»; «ejemplos físicos», «Ejemplo: la partícula libre». Modificaciones: $\vec{q} \to \vec{r}$, $\vec{\ell} \to \vec{L}$; sin los cambios de velocidad, que pasan al anexo B; el generador del giro se deduce aquí, en lugar de remitir a los anexos de la serie.

#### Primer ejemplo: la partícula libre

Sin fuerzas, además de las traslaciones, ya vistas, son simetrías los giros y la traslación en el tiempo:

* **Giros.** Un giro de ángulo $\varepsilon$ alrededor del eje $z$ lleva $(x, y)$ a $(x \cdot \cos\varepsilon - y \cdot \sin\varepsilon,\ x \cdot \sin\varepsilon + y \cdot \cos\varepsilon)$. Con $\cos\varepsilon = 1 + O(\varepsilon^2)$ y $\sin\varepsilon = \varepsilon + O(\varepsilon^2)$, el generador es $(-y, x, 0) = \vec{e}_z \times \vec{r}$, y alrededor de un eje unitario cualquiera $\vec{n}$, $\vec{\xi} = \vec{n} \times \vec{r}$. El término de primer orden es $m \cdot \dot{\vec{r}} \cdot (\vec{n} \times \dot{\vec{r}}) = 0$, porque un producto mixto con un vector repetido es nulo: simetría con $F = 0$.
* **Traslación en el tiempo.** $L$ no depende de $t$.

Con el teorema:

| Transformación | Generador $\vec{\xi}$ | $F$ | Cantidad conservada |
| --- | --- | --- | --- |
| Traslaciones (3) | $\vec{a}$ | $0$ | $\vec{a} \cdot \vec{p}$: la cantidad de movimiento $\vec{p}$ |
| Giros (3) | $\vec{n} \times \vec{r}$ | $0$ | $\vec{p} \cdot (\vec{n} \times \vec{r}) = \vec{n} \cdot \vec{L}$: el momento angular $\vec{L} = \vec{r} \times \vec{p}$ |
| Traslación en el tiempo (1) | $\dot{\vec{r}}$ | $L$ | $H = E = \dfrac{1}{2} \cdot m \cdot \lvert\dot{\vec{r}}\rvert^2$ |

Table: Simetrías de la partícula libre y sus cantidades conservadas.

En la fila de los giros se usa la propiedad cíclica del producto mixto, $\vec{p} \cdot (\vec{n} \times \vec{r}) = \vec{n} \cdot (\vec{r} \times \vec{p})$. Cada cantidad se conserva para cualquier $\vec{a}$ o $\vec{n}$, así que se conservan los vectores $\vec{p}$ y $\vec{L}$ completos.

**Comprobación sobre la solución.** La solución es el movimiento uniforme $\vec{r}(t) = \vec{r}_0 + \vec{v}_0 \cdot t$. Sobre ella, $\vec{p} = m \cdot \vec{v}_0$; $\vec{L} = (\vec{r}_0 + \vec{v}_0 \cdot t) \times m \cdot \vec{v}_0 = m \cdot \vec{r}_0 \times \vec{v}_0$, porque $\vec{v}_0 \times \vec{v}_0 = \vec{0}$; y $E = \dfrac{1}{2} \cdot m \cdot |\vec{v}_0|^2$. Las tres son constantes.

Las tres conservaciones aparecen juntas porque el espacio vacío no tiene puntos ni direcciones privilegiados, y el tiempo no tiene instantes privilegiados. La partícula libre tiene además una cuarta familia de simetrías, los cambios de velocidad, que completan las diez simetrías de la mecánica de Newton (anexo B). Con varias partículas que interaccionan con fuerzas que solo dependen de las distancias entre ellas, las mismas transformaciones, aplicadas a todas las partículas a la vez, siguen siendo simetrías, y lo que se conserva son las cantidades **totales**: cada partícula conserva su propia cantidad de movimiento solo si no interacciona con las demás (anexo B).

> Fuente: «ejemplos físicos», «Ejemplo: una partícula en un campo uniforme (el tiro parabólico)», e introducción. Modificaciones: sin los cambios de velocidad; el origen en el tema 1 y la comprobación de la energía, de la versión anterior del trabajo; el argumento de que no hay $F$ para los giros horizontales, en una frase.

#### Segundo ejemplo: el tiro parabólico

Este ejemplo y el siguiente muestran qué simetrías de la partícula libre rompe un campo exterior, y qué cantidades conservadas se pierden con ellas. Proceden del tema 1 de la asignatura: el tiro parabólico es el lagrangiano de su ejercicio 1 antes de imponer la ligadura del plano inclinado, y la fuerza central es su ejercicio 2.

Una partícula de masa $m$ está sometida a la gravedad $g$, con el eje $z$ vertical hacia arriba:

$$
\begin{aligned}
L = T - V = \dfrac{1}{2} \cdot m \cdot (\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - m \cdot g \cdot z.
\end{aligned}
$$

Las ecuaciones de Euler–Lagrange dan $\ddot{x} = \ddot{y} = 0$ y $\ddot{z} = -g$, con solución $x = x_0 + v_x \cdot t$, $y = y_0 + v_y \cdot t$ y $z = z_0 + v_z \cdot t - \dfrac{1}{2} \cdot g \cdot t^2$.

**Traslaciones horizontales.** $x$ e $y$ no aparecen en $L$: el desplazamiento horizontal es una simetría con $F = 0$, y se conservan $p_x = m \cdot \dot{x} = m \cdot v_x$ y $p_y = m \cdot v_y$.

**Traslación vertical: una simetría con $F \neq 0$.** Para $z \to z + \varepsilon$, con generador $(0, 0, 1)$, el término de primer orden de $\delta L$ es $\dfrac{\partial L}{\partial z} = -m \cdot g$. No es nulo, pero es constante, y una constante es la derivada de una función del tiempo: $-m \cdot g = \dfrac{d}{dt}(-m \cdot g \cdot t)$. Es una simetría con $F = -m \cdot g \cdot t$, y el teorema da que se conserva

$$
\begin{aligned}
Q = p_z - F = p_z + m \cdot g \cdot t.
\end{aligned}
$$

En efecto, sobre la solución, $p_z = m \cdot (v_z - g \cdot t)$, y $Q = m \cdot v_z$. La cantidad de movimiento vertical $p_z$ no se conserva: la gravedad la cambia a ritmo constante. Pero desplazar la trayectoria en vertical sigue siendo una simetría: una parábola desplazada hacia arriba es otra solución, porque la gravedad es la misma a todas las alturas. $Q$ no dice nada que no diga ya la ecuación $\dot{p}_z = -m \cdot g$, integrada una vez, pero muestra que la energía potencial distingue unas alturas de otras solo en una constante aditiva, que no afecta al movimiento.

**Giros: la gravedad distingue la vertical.** El giro alrededor del eje $z$ tiene generador $\vec{e}_z \times \vec{r} = (-y, x, 0)$, que no cambia $z$: $V$ no cambia, la energía cinética tampoco (primer ejemplo), y es una simetría con $F = 0$. Se conserva $L_z = m \cdot (x \cdot \dot{y} - y \cdot \dot{x})$, y sobre la solución, $L_z = m \cdot \big((x_0 + v_x \cdot t) \cdot v_y - (y_0 + v_y \cdot t) \cdot v_x\big) = m \cdot (x_0 \cdot v_y - y_0 \cdot v_x)$. El giro alrededor del eje $x$, en cambio, tiene generador $\vec{e}_x \times \vec{r} = (0, -z, y)$ y cambia la altura: el término de primer orden de $\delta L$ es $-m \cdot g \cdot y$. Ninguna $F$ lo produce, porque $\dfrac{dF}{dt}$ contiene las velocidades o las aceleraciones, salvo que $F$ solo dependa de $t$, y entonces es una función del tiempo, no de $y$. No es una simetría, y $L_x$ no se conserva: $\dfrac{dL_x}{dt} = -m \cdot g \cdot y$, el momento de la fuerza de la gravedad respecto del eje $x$.

**Energía.** $L$ no depende explícitamente del tiempo, así que se conserva $H = T + V = E$. Con la solución, usando $\dot{z} = v_z - g \cdot t$:

$$
\begin{aligned}
E &= \dfrac{1}{2} \cdot m \cdot \left(v_x^2 + v_y^2 + (v_z - g \cdot t)^2\right) + m \cdot g \cdot \left(z_0 + v_z \cdot t - \dfrac{1}{2} \cdot g \cdot t^2\right) \\
&= \dfrac{1}{2} \cdot m \cdot (v_x^2 + v_y^2 + v_z^2) + m \cdot g \cdot z_0.
\end{aligned}
$$

Los términos $-m \cdot g \cdot v_z \cdot t$ y $\dfrac{1}{2} \cdot m \cdot g^2 \cdot t^2$ de la energía cinética se cancelan con los de la potencial.

**Qué muestra el ejemplo:** la gravedad uniforme no distingue unos puntos de otros, sino una dirección, la vertical. Rompe los giros alrededor de ejes horizontales, y con ellos la conservación de $L_x$ y $L_y$. La expresión «la gravedad rompe la simetría vertical» hay que precisarla: lo que se pierde es la conservación de $p_z$, no la posibilidad de desplazar la trayectoria en vertical.

> Fuente: «ejemplos físicos», «Ejemplo: una partícula en un campo central» (giros, coordenadas polares, traslaciones). La reducción con el potencial efectivo, de la versión anterior del trabajo, que procede de «El formalismo lagrangiano: ejemplos físicos». Modificaciones: $\vec{q} \to \vec{r}$, $\ell \to L_z$, $e \cdot U \to V$.

#### Tercer ejemplo: la fuerza central

Una partícula de masa $m$ está sometida a una fuerza dirigida hacia un centro fijo, con una energía potencial $V(r)$ que solo depende de la distancia $r = |\vec{r}|$ al centro, como la gravitatoria o la eléctrica.

**Giros: el momento angular.** Para el giro alrededor de un eje $\vec{n}$ que pasa por el centro, $\vec{\xi} = \vec{n} \times \vec{r}$, y a primer orden $|\vec{r}|^2$ cambia en $2 \cdot \varepsilon \cdot \vec{r} \cdot (\vec{n} \times \vec{r}) = 0$: la distancia al centro no cambia, y $V(r)$ tampoco. La energía cinética tampoco cambia (primer ejemplo). Es una simetría con $F = 0$ para todo eje $\vec{n}$, y se conserva el vector $\vec{L} = \vec{r} \times \vec{p}$. Se comprueba directamente:

$$
\begin{aligned}
\dfrac{d\vec{L}}{dt} = \dot{\vec{r}} \times \vec{p} + \vec{r} \times \dot{\vec{p}} = \vec{0} + \vec{r} \times \vec{F} = \vec{0}.
\end{aligned}
$$

El primer término es nulo porque $\vec{p} = m \cdot \dot{\vec{r}}$ es paralelo a $\dot{\vec{r}}$, y el segundo, porque la fuerza central es paralela a $\vec{r}$. Como $\vec{L}$ es constante, la posición $\vec{r}$ es siempre perpendicular a ese vector fijo, y el movimiento ocurre en un plano.

**El mismo giro en coordenadas polares.** En ese plano usamos coordenadas polares $(r, \theta)$, en las que $\dot{x}^2 + \dot{y}^2 = \dot{r}^2 + r^2 \cdot \dot{\theta}^2$:

$$
\begin{aligned}
L = \dfrac{1}{2} \cdot m \cdot (\dot{r}^2 + r^2 \cdot \dot{\theta}^2) - V(r).
\end{aligned}
$$

El giro es ahora $\theta \to \theta + \varepsilon$: $\theta$ es cíclica, y se conserva $p_\theta = m \cdot r^2 \cdot \dot{\theta}$. Es la misma cantidad que da el teorema en cartesianas, $L_z = m \cdot (x \cdot \dot{y} - y \cdot \dot{x}) = m \cdot r^2 \cdot \dot{\theta}$: la coordenada cíclica aparece cuando las coordenadas se adaptan a la simetría. Tiene un significado geométrico: en un tiempo $dt$, el radio barre un triángulo de área $dA = \dfrac{1}{2} \cdot r^2 \cdot d\theta$, así que el área barrida por unidad de tiempo, $\dfrac{dA}{dt} = \dfrac{L_z}{2 \cdot m}$, es constante. Es la segunda ley de Kepler.

**Traslaciones: no hay simetría.** Para $\vec{\xi} = \vec{a}$, el término de primer orden de $\delta L$ es $-V'(r) \cdot \dfrac{\vec{r} \cdot \vec{a}}{r}$, que depende de la posición y no de las velocidades. Por el mismo argumento que en los giros horizontales del tiro parabólico, no es una derivada total, salvo que $V' = 0$. El centro es un punto privilegiado, y $\vec{p}$ no se conserva: $\dot{\vec{p}} = \vec{F} \neq \vec{0}$.

**La simetría ayuda a resolver.** La ecuación de Euler–Lagrange para $r$ es

$$
\begin{aligned}
m \cdot \ddot{r} - m \cdot r \cdot \dot{\theta}^2 + \dfrac{dV}{dr} = 0.
\end{aligned}
$$

Sustituyendo $\dot{\theta} = \dfrac{L_z}{m \cdot r^2}$, el término $m \cdot r \cdot \dot{\theta}^2 = \dfrac{L_z^2}{m \cdot r^3}$ es la derivada de $-\dfrac{L_z^2}{2 \cdot m \cdot r^2}$ respecto de $r$, y desaparece $\theta$:

$$
\begin{aligned}
m \cdot \ddot{r} = -\dfrac{dV_{\mathrm{ef}}}{dr}, \qquad V_{\mathrm{ef}}(r) := V(r) + \dfrac{L_z^2}{2 \cdot m \cdot r^2}.
\end{aligned}
$$

Es el movimiento de una partícula en una sola dimensión, con un potencial efectivo. El segundo término, la barrera centrífuga, impide que la partícula llegue al centro si $L_z \neq 0$. La energía también se conserva, porque $L$ no depende de $t$, y queda $E = \dfrac{1}{2} \cdot m \cdot \dot{r}^2 + V_{\mathrm{ef}}(r)$: un problema de dos coordenadas se ha reducido a uno de una. La distancia $r$ solo puede tomar los valores en los que $V_{\mathrm{ef}}(r) \leq E$.

> Fuente: «parte física», «Primera etapa › Una partícula en un campo exterior» (tabla). Modificaciones: con las cantidades conservadas en lugar del número de simetrías, y sin los cambios de velocidad.

#### Lo que muestran los ejemplos

Cada campo exterior conserva unas simetrías de la partícula libre y rompe otras, y las cantidades conservadas siguen a las simetrías:

| Simetría | Partícula libre | Tiro parabólico | Fuerza central |
| --- | --- | --- | --- |
| Traslaciones | $\vec{p}$ | $p_x$, $p_y$ y $p_z + m \cdot g \cdot t$ | ninguna |
| Giros | $\vec{L}$ | $L_z$ | $\vec{L}$ |
| Traslación en el tiempo | $E$ | $E$ | $E$ |

Table: Cantidades conservadas según las simetrías que deja cada campo.

La gravedad uniforme distingue una dirección; la fuerza central, un punto. Y la elección de coordenadas importa: en cartesianas, ninguna coordenada de la fuerza central es cíclica; en polares, la simetría aparece como una coordenada cíclica.

#### Lo que hereda la parte cuántica

Los ejemplos preparan la parte cuántica del trabajo, para que las dos no queden como explicaciones separadas:

| De la parte clásica | Lo que reaparece en cuántica |
| --- | --- |
| La idea «simetría, cantidad conservada» | La misma idea, con operadores |
| El momento $p_x$, conservado cuando $x$ es cíclica | El operador $\hat{p} = -i \cdot \hbar \cdot \dfrac{d}{dx}$ y la partícula libre |
| La energía $H$ | El hamiltoniano $\hat{H}$ y la ecuación de Schrödinger |
| La fuerza central: $L_z$ conservado y reducción a una dimensión | El potencial central: $\hat{L}^2$, $\hat{L}_z$ y los números cuánticos $\ell$ y $m_\ell$ |

Table: Correspondencia entre la parte clásica y la parte cuántica.

## Texto del anexo B

### Las simetrías de Galileo

> Fuente: «parte física», «Primera etapa › La partícula libre»; «ejemplos físicos», «Ejemplo: la partícula libre». Modificaciones: $\vec{q} \to \vec{r}$, $\vec{g} \to \vec{G}$; solo los cambios de velocidad y la tabla de las diez simetrías.

Este anexo completa el primer ejemplo del apartado 4.2 con la cuarta familia de transformaciones del espacio y del tiempo, los cambios de velocidad, y extiende las simetrías de la partícula libre a un sistema de partículas. Resume @calderon2026noetherfis y @calderon2026noetheranexos.

**El cambio de velocidad.** Un observador que se mueve con velocidad constante $-\varepsilon \cdot \vec{u}$ respecto de otro ve cada trayectoria desplazada en $\varepsilon \cdot \vec{u} \cdot t$: $\vec{r} \to \vec{r} + \varepsilon \cdot \vec{u} \cdot t$. Es una transformación continua, de generador $\vec{\xi} = \vec{u} \cdot t$, que depende del tiempo, con $\dot{\vec{\xi}} = \vec{u}$. Para la partícula libre, el término de primer orden de $\delta L$ es

$$
\begin{aligned}
m \cdot \dot{\vec{r}} \cdot \vec{u} = \dfrac{d}{dt}\left(m \cdot \vec{u} \cdot \vec{r}\right),
\end{aligned}
$$

porque $\vec{u}$ es constante. No es nulo, pero es una derivada total: es una simetría con $F = m \cdot \vec{u} \cdot \vec{r}$. El teorema de Noether da que se conserva

$$
\begin{aligned}
Q = \vec{p} \cdot \vec{u} \cdot t - m \cdot \vec{u} \cdot \vec{r} = -\vec{u} \cdot \vec{G}, \qquad \vec{G} := m \cdot \vec{r} - \vec{p} \cdot t,
\end{aligned}
$$

para todo $\vec{u}$, es decir, el vector $\vec{G}$. Sobre la solución $\vec{r} = \vec{r}_0 + \vec{v}_0 \cdot t$, $\vec{G} = m \cdot (\vec{r}_0 + \vec{v}_0 \cdot t) - m \cdot \vec{v}_0 \cdot t = m \cdot \vec{r}_0$: es la masa por la posición inicial. Con $\vec{p}$, determina la trayectoria entera, $\vec{r}(t) = \dfrac{\vec{G} + \vec{p} \cdot t}{m}$.

**Las diez simetrías de la partícula libre.** Con los cambios de velocidad, la partícula libre tiene diez simetrías independientes:

| Transformación | Generador $\vec{\xi}$ | $F$ | Cantidad conservada |
| --- | --- | --- | --- |
| Traslaciones (3) | $\vec{a}$ | $0$ | $\vec{p}$ |
| Giros (3) | $\vec{n} \times \vec{r}$ | $0$ | $\vec{L} = \vec{r} \times \vec{p}$ |
| Cambios de velocidad (3) | $\vec{u} \cdot t$ | $m \cdot \vec{u} \cdot \vec{r}$ | $\vec{G} = m \cdot \vec{r} - \vec{p} \cdot t$ |
| Traslación en el tiempo (1) | $\dot{\vec{r}}$ | $L$ | $E$ |

Table: Las diez simetrías de la partícula libre.

Cada familia expresa una propiedad del espacio y del tiempo vacíos: no hay puntos, direcciones, instantes ni observadores inerciales privilegiados. La última es la relatividad de Galileo. Las diez cantidades no son independientes como datos del movimiento: $\vec{L} = \dfrac{1}{m} \cdot \vec{G} \times \vec{p}$ y $E = \dfrac{|\vec{p}|^2}{2 \cdot m}$ se deducen de $\vec{p}$ y de $\vec{G}$.

> Fuente: «parte física», «Tercera etapa: interacciones que dependen de las distancias» (tabla de condiciones) y «El grupo de Galileo»; «anexos», «El grupo de Galileo». Modificaciones: solo la tabla y la conclusión; $\vec{J} \to \vec{L}$, $\vec{X} \to \vec{R}_{\mathrm{cm}}$; la composición del grupo, en una frase con la cita.

**Varias partículas.** Con $N$ partículas que interaccionan con fuerzas que solo dependen de las distancias entre ellas, y sin campo exterior, las diez transformaciones aplicadas a todas las partículas a la vez siguen siendo simetrías, y se conservan las cantidades **totales**:

| Simetría | Condición sobre $V$ | Cantidad conservada |
| --- | --- | --- |
| Traslación en el tiempo | $V$ no depende de $t$ | $E = T + V$ |
| Traslaciones | $V$ solo depende de las diferencias $\vec{r}_a - \vec{r}_b$ | $\vec{P} = \sum_a \vec{p}_a$ |
| Giros | $V$ no cambia al girar todas las posiciones | $\vec{L} = \sum_a \vec{r}_a \times \vec{p}_a$ |
| Cambios de velocidad | la de las traslaciones | $\vec{G} = M \cdot \vec{R}_{\mathrm{cm}} - \vec{P} \cdot t$ |

Table: Simetrías de un sistema de partículas y cantidades conservadas.

Aquí $M$ es la masa total y $\vec{R}_{\mathrm{cm}}$, el centro de masas. Cada partícula conserva su propia cantidad de movimiento solo si no interacciona con las demás: lo que no tiene puntos privilegiados es el sistema en su conjunto. La conservación de $\vec{G}$ dice que el centro de masas se mueve con velocidad constante, $\vec{R}_{\mathrm{cm}}(t) = \dfrac{\vec{G} + \vec{P} \cdot t}{M}$. Las diez transformaciones se componen entre sí y forman un grupo de diez parámetros, el **grupo de Galileo** [@calderon2026noetheranexos]. El cálculo de las diez cantidades está comprobado con cálculo simbólico en el repositorio de uno de los autores [@calderon2026mcc].

## Qué se queda fuera y por qué

| Documento | Apartado | Motivo |
| --- | --- | --- |
| parte matemática | La identidad de Noether, la linealidad y las cantidades triviales | No las necesitan los ejemplos |
| parte matemática | «Transformaciones que también mueven la variable» (la fórmula con $\tau$) | La energía sale con $\xi_i = \dot{q}_i$; la fórmula general solo hace falta para escribir el grupo de Galileo con una sola cantidad |
| parte matemática | Varias variables y corrientes conservadas | La propuesta 3 deja los campos fuera |
| ejemplos matemáticos | Todos (camino más corto, Newton, Laplace) | El trabajo es de física; quedan como respaldo |
| parte física | Segunda y cuarta etapas ($N$ partículas sin interacción, campo magnético) | Fuera del alcance |
| parte física | «Lo que el teorema no dice» (simetrías discretas, simetría de la ley y de la solución) | Útil para la defensa oral; puede pasar a las conclusiones |
| ejemplos físicos | Cambios de velocidad en el campo uniforme; dos partículas; carga en un campo magnético; cuerda vibrante | Fuera del alcance |
| anexos | Rotaciones, composición del grupo de Galileo, exponencial de una matriz | Se citan en el anexo B |

## Pendiente

* El anexo B es la ampliación de la pareja 1 (cambio de observador inercial) que el grupo aún no ha acordado. Si no se acepta, se quita el anexo B y las dos referencias del apartado 4.2 («Un ejemplo, en la partícula libre» y el último párrafo del primer ejemplo).
* `NEXT-STEPS-grupo.md` tiene sin decidir la numeración del desarrollo: con esta estructura, la parte cuántica de la pareja 2 es el 4.3.
* Al pasar el texto a `simetrias.md`, borrar las líneas «Fuente:».
