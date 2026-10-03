# El formalismo lagrangiano (versión para el trabajo)

<!--
Versión del formalismo lagrangiano que entra en el trabajo «La importancia de las simetrías en
física»: el apartado «Formalismo lagrangiano» del capítulo de desarrollo y el anexo A. La versión
completa es la serie «El formalismo lagrangiano», privada desde el 03-10-2026
(trabajos/simetrias/borradores/El-formalismo-lagrangiano/).
Cada bloque lleva una línea «Fuente:» con el documento y el apartado de origen, y lo que se ha
cambiado; esas líneas se borran al pasar el texto a simetrias.md.
-->

## Espacio

| Apartado del trabajo | Previsto (propuesta 3) | Medido con la plantilla de UNIR |
| --- | --- | --- |
| Desarrollo › Formalismo lagrangiano | 2 páginas | unas 1,75 |
| Anexo A: deducción de la ecuación de Euler–Lagrange | 1–2 páginas (3 como máximo para todos los anexos) | unas 2,3, con la demostración completa del lema |

Las medidas se han hecho compilando este texto con la plantilla real del trabajo (`trabajos/_plantilla/unir.latex`, 11 puntos, interlineado 1,5). Las 30 páginas y su reparto son una propuesta del grupo que en `NEXT-STEPS-grupo.md` sigue sin marcar como acordada.

## Criterios de la extracción

1. Solo lo que los cuatro podamos explicar y lo que necesitan los dos ejemplos (tiro parabólico y fuerza central). Pensado para lectores que vienen de la ingeniería o la informática: se parte de las leyes de Newton y se apoya cada idea nueva en el cálculo de una variable.
2. Notación del trabajo, no la de la serie: $L$ y $S$ sin negrita; $q_i$ y $t$ en lugar de $f$ y $x$; $\varepsilon$ en lugar de $\epsilon$; $L_z$ para el momento angular, en lugar de $\ell$; una sola $\delta$ para la variación primera.
3. Las demostraciones que exigen argumentos de topología o de convergencia uniforme se resumen en una frase o se quedan fuera.

## Trazabilidad

| Fragmento del trabajo | Documento de origen | Apartado de origen | Cambios |
| --- | --- | --- | --- |
| Coordenadas generalizadas y leyes de Newton | parte física | «Diccionario y notación»; «Primera etapa › Las leyes físicas y las hipótesis» | Una sola partícula; notación del grupo |
| $L = T - V$ deducido de Newton | parte física | «Primera etapa › La determinación de L», condiciones (A) y (B) | Sin el argumento de conexión; la falta de unicidad, en una frase |
| Funcionales y puntos estacionarios; la acción, el principio de Hamilton y $\delta S$ | parte matemática | «Optimizar una función de una variable según un funcional…» | $f \to q$, $x \to t$; sin negrita; analogía con el cálculo de una variable, nueva |
| Una ecuación por coordenada | parte matemática | «Generalización a funciones vectoriales… › La separación de las componentes» y «Casos particulares» | Solo el caso de una variable con $n$ coordenadas |
| La ecuación tiene la misma forma en otras coordenadas | anexos | «Requisito matemático previo › Las ecuaciones mantienen su forma al cambiar de coordenadas» | Solo el enunciado, con una justificación intuitiva |
| Momento conjugado; $p_\theta = m \cdot r^2 \cdot \dot{\theta}$ | parte física y ejemplos físicos | Condición (A); «Coordenadas polares, potencial efectivo y órbitas de Kepler» | $L_z$ en lugar de $\ell$ |
| Ejemplo del tiro parabólico | `BORRADOR_Maria_Julian.md`, sección 2.1 | — | No procede de la serie |
| Anexo A: variación, integración por partes, conclusión | parte matemática | «Optimizar una función de una variable según un funcional…» | Una coordenada; sin el excurso ni la forma desarrollada; la cota del resto, en una frase |
| Anexo A: lema fundamental | anexos | «Lema fundamental del cálculo de variaciones» (una variable) | Completo; $p$ y $q$ de la demostración pasan a $\rho$ y $\sigma$ |
| Anexo A: varias coordenadas | parte matemática | «… › La separación de las componentes» | Un párrafo |

## Texto del apartado «Formalismo lagrangiano»

### Formalismo lagrangiano

> Fuente: «parte física», «Diccionario y notación» y «Primera etapa › Las leyes físicas y las hipótesis». Modificación: una sola partícula y la notación del grupo.

**Coordenadas generalizadas.** La configuración de un sistema mecánico se describe con un conjunto de coordenadas $q_1, \dots, q_n$, que pueden ser posiciones cartesianas, ángulos o distancias: son las coordenadas generalizadas. Sus derivadas respecto del tiempo, $\dot{q}_1, \dots, \dot{q}_n$, son las velocidades generalizadas. Para una partícula de masa $m$ en coordenadas cartesianas, $n = 3$, y las leyes de Newton dicen

$$
\begin{aligned}
p_i = m \cdot \dot{q}_i, \qquad \dfrac{dp_i}{dt} = F_i, \qquad i = 1, 2, 3.
\end{aligned}
$$

> Fuente: «parte física», «Primera etapa › La determinación de L», condiciones (A) y (B). Modificaciones: sin el argumento de conexión; el término que solo depende de $t$ se justifica directamente; la falta de unicidad, en una frase.

**El lagrangiano, a partir de Newton.** Supongamos que la fuerza deriva de una energía potencial, $F_i = -\dfrac{\partial V}{\partial q_i}$. Buscamos una función $L(q, \dot{q}, t)$ de las coordenadas, las velocidades y el tiempo cuyas derivadas sean la cantidad de movimiento y la fuerza:

$$
\begin{aligned}
\dfrac{\partial L}{\partial \dot{q}_i} = m \cdot \dot{q}_i = p_i, \qquad \dfrac{\partial L}{\partial q_i} = -\dfrac{\partial V}{\partial q_i} = F_i.
\end{aligned}
$$

La primera condición obliga a que $L$ sea $\dfrac{1}{2} \cdot m \cdot (\dot{q}_1^2 + \dot{q}_2^2 + \dot{q}_3^2)$ más una función que no depende de las velocidades, y la segunda, a que esa función sea $-V$, salvo un término que solo depende de $t$; ese término no depende de las coordenadas ni de las velocidades, así que no interviene en lo que sigue y lo omitimos. Queda la energía cinética menos la potencial:

$$
\begin{aligned}
L(q, \dot{q}, t) = T - V = \dfrac{1}{2} \cdot m \cdot \left(\dot{q}_1^2 + \dot{q}_2^2 + \dot{q}_3^2\right) - V(q_1, q_2, q_3).
\end{aligned}
$$

Con estas dos derivadas, la segunda ley de Newton, $\dfrac{dp_i}{dt} = F_i$, se escribe

$$
\begin{aligned}
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_i}\right) - \dfrac{\partial L}{\partial q_i} = 0, \qquad i = 1, \dots, n,
\end{aligned}
$$

que es la ecuación de Euler–Lagrange. Otros lagrangianos dan las mismas ecuaciones, por ejemplo $2 \cdot L$; lo que fija este es la primera condición.

> Fuente del ejemplo: `BORRADOR_Maria_Julian.md`, sección 2.1 (no está en los documentos de El formalismo lagrangiano).

**Ejemplo: el tiro parabólico.** Para una partícula en el plano vertical, con $x$ horizontal y $z$ vertical, $L = \dfrac{1}{2} \cdot m \cdot (\dot{x}^2 + \dot{z}^2) - m \cdot g \cdot z$. Las ecuaciones de Euler–Lagrange dan $m \cdot \ddot{x} = 0$ y $m \cdot \ddot{z} = -m \cdot g$: movimiento uniforme en horizontal y uniformemente acelerado en vertical.

> Fuente: «parte matemática», «Optimizar una función de una variable según un funcional…» (el funcional, la variación primera y la estacionariedad). Modificaciones: $f \to q$, $x \to t$, $[a, b] \to [t_1, t_2]$; $S$ y $\delta S$ sin negrita; $\varepsilon$ en lugar de $\epsilon$; se añade la analogía con el cálculo de una variable.

**Funcionales y puntos estacionarios.** Una función ordinaria asigna un número a cada número; un funcional asigna un número a cada función. En el cálculo de una variable, $f'(x_0) = 0$ significa que, al desplazarse una cantidad pequeña $\varepsilon$ desde $x_0$, la función solo cambia a segundo orden en $\varepsilon$; el punto se llama estacionario y no tiene por qué ser un mínimo: puede ser un máximo o un punto de inflexión. El cálculo de variaciones traslada esta idea a los funcionales.

**La acción y el principio de Hamilton.** A cada trayectoria posible $q(t)$ entre los instantes $t_1$ y $t_2$, con las posiciones inicial y final fijadas, se le asocia un número, la acción:

$$
\begin{aligned}
S[q] = \int_{t_1}^{t_2} L(q, \dot{q}, t) \,dt.
\end{aligned}
$$

El principio de Hamilton afirma que la trayectoria real hace **estacionaria** la acción: si se compara con una trayectoria próxima, $q + \varepsilon \cdot h$, con $h(t_1) = h(t_2) = 0$, la acción solo cambia a segundo orden en $\varepsilon$. Dicho de otro modo, su variación primera, el análogo de $f'(x_0)$,

$$
\begin{aligned}
\delta S := \lim_{\varepsilon \to 0} \dfrac{S[q + \varepsilon \cdot h] - S[q]}{\varepsilon},
\end{aligned}
$$

es nula para toda $h$. Esta condición equivale a la ecuación de Euler–Lagrange; la deducción está en el anexo A. Como en el cálculo de una variable, estacionaria no significa mínima.

> Fuente: «parte matemática», «Generalización a funciones vectoriales… › La separación de las componentes» y «Casos particulares» (una variable, $n$ funciones). «Anexos», «Requisito matemático previo › Las ecuaciones mantienen su forma al cambiar de coordenadas». Modificación: del cambio de coordenadas solo se da el enunciado, con una justificación intuitiva en lugar de la demostración.

**Varias coordenadas y cambio de coordenadas.** Con $n$ coordenadas generalizadas hay una ecuación de Euler–Lagrange para cada una. Además, la ecuación tiene la misma forma en cualquier sistema de coordenadas: basta escribir $L$ en las nuevas coordenadas. La razón es que el principio de Hamilton no depende de cómo se describa la trayectoria: su acción es el mismo número en cartesianas que en polares. Por ejemplo, en coordenadas polares del plano, $T = \dfrac{1}{2} \cdot m \cdot (\dot{r}^2 + r^2 \cdot \dot{\theta}^2)$.

> Fuente: «parte física», condición (A); «ejemplos físicos», «Coordenadas polares, potencial efectivo y órbitas de Kepler» ($m \cdot r^2 \cdot \dot{\theta}$). Modificación: notación del grupo, $L_z$ en lugar de $\ell$.

**El momento conjugado.** A cada coordenada generalizada se le asocia su momento conjugado, $p_i := \dfrac{\partial L}{\partial \dot{q}_i}$. En cartesianas es la cantidad de movimiento, $m \cdot \dot{q}_i$; para el ángulo de las coordenadas polares es $p_\theta = m \cdot r^2 \cdot \dot{\theta}$, la componente $L_z$ del momento angular. Con esta notación, la ecuación de Euler–Lagrange se escribe $\dot{p}_i = \dfrac{\partial L}{\partial q_i}$, que es la forma que usa el teorema de Noether.

## Texto del anexo A

### Deducción de la ecuación de Euler–Lagrange

> Fuente: «parte matemática», «Optimizar una función de una variable según un funcional…», desde la variación hasta la ecuación de Euler–Lagrange. Modificaciones: $f \to q$, $x \to t$; una sola coordenada; sin el excurso de la regla de la cadena ni la forma desarrollada; la cota uniforme del resto de Taylor se resume en una frase.

Consideramos una coordenada $q(t)$, dos veces derivable con continuidad en $[t_1, t_2]$ y con $q(t_1)$ y $q(t_2)$ fijados, y un lagrangiano $L(q, \dot{q}, t)$ con derivadas parciales segundas continuas. Para comparar con trayectorias próximas tomamos una función $h$, también dos veces derivable con continuidad, con $h(t_1) = h(t_2) = 0$, de modo que $q + \varepsilon \cdot h$ tiene los mismos extremos.

**1. La variación primera.** Por el desarrollo de Taylor de $L$ en sus dos primeros argumentos, con $t$ fijo,

$$
\begin{aligned}
L(q + \varepsilon \cdot h, \dot{q} + \varepsilon \cdot \dot{h}, t) - L(q, \dot{q}, t) = \varepsilon \cdot \left(\dfrac{\partial L}{\partial q} \cdot h + \dfrac{\partial L}{\partial \dot{q}} \cdot \dot{h}\right) + O(\varepsilon^2),
\end{aligned}
$$

con las derivadas de $L$ evaluadas en $(q(t), \dot{q}(t), t)$. Integramos entre $t_1$ y $t_2$, dividimos por $\varepsilon$ y hacemos $\varepsilon \to 0$. El resto, dividido por $\varepsilon$, tiende a $0$ en todo el intervalo a la vez, porque las derivadas segundas de $L$ son continuas en un conjunto cerrado y acotado. Queda

$$
\begin{aligned}
\delta S = \int_{t_1}^{t_2} \left(\dfrac{\partial L}{\partial q} \cdot h + \dfrac{\partial L}{\partial \dot{q}} \cdot \dot{h}\right) dt.
\end{aligned}
$$

**2. La integración por partes.** El segundo término se integra por partes:

$$
\begin{aligned}
\int_{t_1}^{t_2} \dfrac{\partial L}{\partial \dot{q}} \cdot \dot{h} \,dt = \left[\dfrac{\partial L}{\partial \dot{q}} \cdot h\right]_{t_1}^{t_2} - \int_{t_1}^{t_2} \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}}\right) \cdot h \,dt.
\end{aligned}
$$

El término de contorno es nulo, porque $h(t_1) = h(t_2) = 0$. Queda

$$
\begin{aligned}
\delta S = \int_{t_1}^{t_2} \varphi(t) \cdot h(t) \,dt, \qquad \varphi := \dfrac{\partial L}{\partial q} - \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}}\right).
\end{aligned}
$$

> Fuente: «anexos», «Lema fundamental del cálculo de variaciones» (una variable), completo. Modificaciones: $x \to t$, $[a, b] \to [t_1, t_2]$; las funciones auxiliares $p$ y $q$ de la demostración pasan a llamarse $\rho$ y $\sigma$, porque en el trabajo $p$ y $q$ son el momento y la coordenada.

**3. El lema fundamental del cálculo de variaciones.**

**Lema.** Sea $\varphi: [t_1, t_2] \to \mathbb{R}$ una función continua tal que $\int_{t_1}^{t_2} \varphi(t) \cdot h(t) \,dt = 0$ para toda función $h$ dos veces derivable con continuidad con $h(t_1) = h(t_2) = 0$. Entonces $\varphi(t) = 0$ para todo $t \in [t_1, t_2]$.

**Demostración.** Por reducción al absurdo. Supongamos que existe un punto $t_0 \in (t_1, t_2)$ con $\varphi(t_0) \neq 0$. Podemos suponer que $\varphi(t_0) > 0$: si fuera negativo, el mismo razonamiento se aplica a $-\varphi$, que cumple la misma hipótesis.

1. **Un intervalo donde $\varphi$ es positiva.** Como $\varphi$ es continua en $t_0$, existe $\eta > 0$ tal que $\varphi(t) > \dfrac{\varphi(t_0)}{2} > 0$ siempre que $|t - t_0| < \eta$. Elegimos $\alpha$ y $\beta$ con $\max(t_1, t_0 - \eta) < \alpha < t_0 < \beta < \min(t_2, t_0 + \eta)$. Así, $[\alpha, \beta] \subset (t_1, t_2)$ y $\varphi(t) > 0$ en todo $[\alpha, \beta]$.

2. **Una función $h$ que solo es distinta de cero en $(\alpha, \beta)$.** Definimos

   $$
   \begin{aligned}
   h(t) := \begin{cases} (t - \alpha)^3 \cdot (\beta - t)^3 & \text{si } \alpha \leq t \leq \beta, \\ 0 & \text{en otro caso.} \end{cases}
   \end{aligned}
   $$

3. **$h$ es admisible.** Como $t_1 < \alpha$ y $\beta < t_2$, se cumple $h(t_1) = h(t_2) = 0$. Falta ver que $h$ es dos veces derivable con continuidad. Dentro de $(\alpha, \beta)$, $h$ es un polinomio, y fuera de $[\alpha, \beta]$ es la función nula, así que solo hay que comprobar los puntos $\alpha$ y $\beta$. A la derecha de $\alpha$ escribimos $h(t) = (t - \alpha)^3 \cdot \rho(t)$, con $\rho(t) := (\beta - t)^3$, y derivamos:

   $$
   \begin{aligned}
   h'(t) &= 3 \cdot (t - \alpha)^2 \cdot \rho(t) + (t - \alpha)^3 \cdot \rho'(t), \\
   h''(t) &= 6 \cdot (t - \alpha) \cdot \rho(t) + 6 \cdot (t - \alpha)^2 \cdot \rho'(t) + (t - \alpha)^3 \cdot \rho''(t).
   \end{aligned}
   $$

   A la izquierda de $\alpha$, $h$, $h'$ y $h''$ son nulas. Por la derecha, los cocientes $\dfrac{h(t) - h(\alpha)}{t - \alpha} = (t - \alpha)^2 \cdot \rho(t)$ y $\dfrac{h'(t) - 0}{t - \alpha} = 3 \cdot (t - \alpha) \cdot \rho(t) + (t - \alpha)^2 \cdot \rho'(t)$ tienden a $0$, así que $h'(\alpha) = 0$ y $h''(\alpha) = 0$. Además, $h''(t) \to 0$ cuando $t \to \alpha$ por la derecha, porque cada término contiene el factor $(t - \alpha)$. Por tanto, $h''$ es continua en $\alpha$. En $\beta$ se razona igual, con el factor $(\beta - t)^3$ y $\sigma(t) := (t - \alpha)^3$. Por eso el exponente es $3$: con exponente $2$, $h''$ saltaría en $\alpha$ de $0$ a $2 \cdot (\beta - \alpha)^3$.

4. **La contradicción.** En $(\alpha, \beta)$ son positivas tanto $\varphi$ como $h$, porque $t - \alpha > 0$ y $\beta - t > 0$. Fuera de $[\alpha, \beta]$, $h = 0$. Por tanto,

   $$
   \begin{aligned}
   \int_{t_1}^{t_2} \varphi(t) \cdot h(t) \,dt = \int_\alpha^\beta \varphi(t) \cdot h(t) \,dt > 0,
   \end{aligned}
   $$

   porque es la integral de una función continua y positiva en $(\alpha, \beta)$. Esto contradice la hipótesis, así que $\varphi(t_0) = 0$ para todo $t_0 \in (t_1, t_2)$.

5. **Los extremos.** Por la continuidad de $\varphi$, $\varphi(t_1) = \lim_{t \to t_1^+} \varphi(t) = 0$ y $\varphi(t_2) = \lim_{t \to t_2^-} \varphi(t) = 0$. $\blacksquare$

**4. La conclusión.** Como $\delta S = 0$ para toda $h$, el lema da $\varphi = 0$, que es la ecuación de Euler–Lagrange:

$$
\begin{aligned}
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}}\right) - \dfrac{\partial L}{\partial q} = 0.
\end{aligned}
$$

Recíprocamente, si se cumple la ecuación, $\varphi = 0$ y $\delta S = 0$ para toda $h$.

> Fuente: «parte matemática», «Generalización a funciones vectoriales… › La separación de las componentes».

**Varias coordenadas.** Con $n$ coordenadas se toma una función $h_i$ para cada una. Variando una sola coordenada cada vez, es decir, con todas las $h_j$ nulas salvo $h_i$, el mismo razonamiento da una ecuación de Euler–Lagrange para cada $q_i$.

## Qué se queda fuera y por qué

| Documento | Apartado | Motivo |
| --- | --- | --- |
| parte matemática | «Un excurso» (regla de la cadena) y la forma desarrollada como ecuación de segundo orden | No lo necesitan los ejemplos |
| parte matemática | La cota uniforme del resto de Taylor, con la constante $C$ | Se resume en una frase en el anexo A |
| parte matemática | El caso de dos variables y el de funciones vectoriales de varias variables (jacobiano, campos) | La propuesta 3 deja los campos fuera |
| ejemplos matemáticos | El camino más corto (como gráfica y en forma paramétrica), la membrana casi plana y las ecuaciones con estructura de Newton | No los necesitan los ejemplos del trabajo |
| parte física | Segunda a cuarta etapas ($N$ partículas, interacciones, campo magnético) | Fuera del alcance del trabajo |
| parte física | «Tercera etapa › Cantidades conservadas» | No es formalismo; sirve para «Simetrías y teorema de Noether»: lo que se conserva por la homogeneidad del espacio es la cantidad de movimiento **total** (la imprecisión del tema 1, sección 3.3 del borrador) |
| ejemplos físicos | Coordenadas polares y potencial efectivo | No es formalismo; es la base del ejemplo de la fuerza central (borrador, sección 2.2) |
| ejemplos físicos | Las órbitas de Kepler, el centro de masas, la hélice, la cuerda y la membrana | Fuera del alcance; Kepler, como mucho, en una frase del ejemplo de la fuerza central |
| anexos | Las versiones del lema en dos y en $m$ variables | No hacen falta |
| anexos | La demostración del cambio de coordenadas y la de la derivada total | Basta el enunciado; la derivada total no hace falta (borrador, sección 3.4) |
| anexos | «La forma más general del potencial en $L = T - V$» | Fuera del alcance |

## Pendiente

- **El anexo A ocupa unas 2,3 páginas**, por encima de las 1–2 previstas. Opciones: aceptarlo, si los anexos B y C caben en las 0,7 páginas restantes del máximo de 3; o recortar la deducción de los pasos 1 y 2, que admite resumirse.
- Al pasar el texto a `simetrias.md`, borrar las líneas «Fuente:».
