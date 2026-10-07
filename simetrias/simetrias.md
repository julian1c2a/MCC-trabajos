---
title: "La importancia de las\\newline simetrías en física"
author:
  - "Jose Miguel Alcaraz Ramiro"
  - "Julián Calderón Almendros"
  - "Gonzalo Garcia Lasurtegui"
  - "Maria Pérez I Pullès"
autor-cabecera: "Alcaraz, Calderón, Garcia y Pérez"
date: "DD de MES de AAAA"
profesor: "Rodrigo Gil-Merino y Rubio"
lang: es-ES
bibliography: referencias.bib
resumen: |
  Resumen en español del trabajo (máximo 150 palabras): objetivo o propósito, metodología,
  resultados y conclusiones.
palabras-clave: [palabra clave 1, palabra clave 2, palabra clave 3]
abstract: |
  English version of the Resumen (maximum 150 words).
keywords: [keyword 1, keyword 2, keyword 3]
indice-figuras: false
indice-tablas: true
---

<!--
Estructura obligatoria del modelo UNIR (material/Plantilla_LATEX_FCC_MUCC_UNIR/plantilla.tex).
Los capítulos no se numeran a mano: LaTeX los numera. Las citas se escriben [@clave] o @clave
y las referencias van en referencias.bib (APA 7). REGLAS.md, sección 8.
-->

# Introducción

## Motivación y justificación

Un experimento de laboratorio da el mismo resultado si se repite en otra ciudad, si se gira la mesa sobre la que está montado o si se repite al día siguiente. Esta regularidad es tan habitual que apenas se nota, pero expresa una propiedad profunda de las leyes físicas: no cambian al desplazar el sistema, al girarlo ni al retrasar el reloj. Se dice que esas transformaciones son **simetrías** de las leyes.

Por otra parte, la mecánica conoce desde hace siglos tres magnitudes que se conservan en un sistema aislado: la energía, el momento lineal y el momento angular. La pregunta que guía este trabajo es por qué se conservan precisamente esas tres. La respuesta que construiremos es que cada una corresponde a una de las simetrías anteriores: la energía, a la traslación en el tiempo; el momento lineal, a la traslación en el espacio; y el momento angular, a los giros. Es el contenido del teorema que Emmy Noether publicó en 1918 [@noether1918].

La relación entre simetría y conservación no es una curiosidad de la mecánica clásica. En mecánica cuántica se mantiene, y además la simetría determina la estructura de los estados posibles: por ejemplo, los números cuánticos $\ell$ y $m_\ell$, que clasifican los estados de un electrón en un átomo según su momento angular, proceden de la simetría de giro. Por eso es un tema central en la formación de quien estudia computación cuántica.

## Planteamiento del trabajo

Conviene fijar desde el principio el significado de las palabras que usaremos:

* **Transformación:** un cambio en la descripción del sistema, como trasladarlo una distancia $a$ (cada posición $x$ pasa a ser $x + a$), girarlo un ángulo o retrasar el reloj un tiempo.
* **Simetría:** una transformación que no cambia la ley que describe el sistema.
* **Cantidad conservada:** una magnitud cuyo valor no cambia con el tiempo mientras el sistema evoluciona.

Las simetrías pueden ser **continuas**, cuando se pueden aplicar en pasos tan pequeños como se quiera (una traslación de cualquier distancia, un giro de cualquier ángulo), o **discretas**, cuando no admiten pasos intermedios (una reflexión en un espejo). El teorema de Noether trata las continuas, y son las que estudia este trabajo.

Tres ejemplos intuitivos muestran la idea. Si en el espacio vacío no hay ningún punto privilegiado, desplazar todo el sistema no cambia nada, y el momento lineal se conserva. Si tampoco hay ninguna dirección privilegiada, girarlo no cambia nada, y se conserva el momento angular. Y si las leyes son las mismas hoy que mañana, retrasar el reloj no cambia nada, y se conserva la energía. Una simetría también puede romperse: cerca de la superficie de la Tierra, la gravedad distingue la dirección vertical, y el momento lineal vertical de un objeto que cae no se conserva, aunque el horizontal sí. Veremos este ejemplo con detalle.

Para pasar de estas ideas a un resultado demostrable hace falta un lenguaje en el que «la ley no cambia» tenga un significado matemático preciso. Ese lenguaje es el formalismo lagrangiano: el sistema se describe con una función, el lagrangiano, y la ley no cambia bajo una transformación si el lagrangiano no cambia.

## Estructura del trabajo

El capítulo 2 sitúa el problema en la historia: cómo la mecánica pasó de formularse con fuerzas (Newton) a formularse con una función y un principio variacional (Lagrange y Hamilton), y cómo Emmy Noether llegó a su teorema a partir del problema de la energía en la relatividad general. El capítulo 3 enumera los objetivos. El capítulo 4 desarrolla el trabajo:

* el apartado 4.1 presenta el formalismo lagrangiano mínimo necesario, cuya deducción completa está en el anexo A;
* el 4.2 define con precisión qué es una simetría, demuestra el teorema de Noether en su forma más sencilla y obtiene las tres conservaciones en tres ejemplos resueltos: la partícula libre, el tiro parabólico y la fuerza central; el anexo B lo completa con los cambios de velocidad y el grupo de Galileo;
* los apartados 4.3 y 4.4 trasladan la misma idea a la mecánica cuántica, donde la simetría de giro de un potencial central da los números cuánticos del momento angular.

<!-- Revisar la descripción de los apartados 4.3 y 4.4 cuando se integren los textos de la pareja 2. -->

El capítulo 5 recoge las conclusiones y la reflexión personal del grupo.

Los desarrollos completos en que se apoyan el capítulo 2, los apartados 4.1 y 4.2 y los anexos están en apuntes de uno de los autores [@calderon2026contexto; @calderon2026matematicas; @calderon2026fisica; @calderon2026fisicaejemplos; @calderon2026anexos; @calderon2026noethermat; @calderon2026noetherfis; @calderon2026noetherfisej; @calderon2026noetheranexos]. Otros apuntes y cuadernos de cálculo simbólico sobre los mismos temas están en su repositorio [@calderon2026mcc].

# Contexto y estado de la cuestión

<!-- Qué se ha hecho en el ámbito del trabajo, con la bibliografía que lo respalda. Versión para el
trabajo; la completa está en borradores/El-contexto-historico.md. -->

## Contexto histórico

Entre los siglos XVII y XIX, la mecánica cambió dos veces de lenguaje, y esos cambios son los que hicieron posible el teorema de Noether. @newton1687 la formuló a partir de las fuerzas: el movimiento de un cuerpo se deduce de las fuerzas que actúan sobre él. Un siglo después, @lagrange1788 la reformuló por completo a partir de la energía cinética y de una función de las fuerzas (la energía potencial), sin recurrir a construcciones geométricas. Sus ecuaciones valen en cualquier sistema de coordenadas, no solo en las cartesianas. En la década de 1830, Hamilton [-@hamilton1834; -@hamilton1835] dio a esta mecánica la forma de un principio variacional. Entre todas las trayectorias posibles con los mismos extremos, el sistema sigue aquella que hace estacionaria la acción: la integral en el tiempo de la diferencia entre la energía cinética y la potencial, lo que hoy llamamos el lagrangiano. Con este lenguaje, decir que una ley física no cambia bajo una transformación (desplazar el sistema, girarlo o retrasar el reloj) pasa a ser una afirmación precisa: la acción no cambia.

El resultado general llegó a raíz de un problema concreto: la conservación de la energía en la relatividad general. Las leyes de conservación guiaron a Einstein durante toda la búsqueda de las ecuaciones del campo gravitatorio. En 1913, con Marcel Grossmann, descartó unas ecuaciones construidas a partir del tensor de Ricci porque creyó que no las cumplían [@einsteingrossmann1913]. En noviembre de 1915 volvió a unas ecuaciones de ese tipo [@einstein1915] y escribió a Arnold Sommerfeld que el error había sido precisamente creer que las leyes de conservación no se cumplían [@einstein1998, documento 153; @pitts2016]. Pero en la nueva teoría la energía se comportaba de forma extraña: la del campo gravitatorio dependía del sistema de coordenadas y no podía asignarse a cada punto del espacio. En Gotinga, David Hilbert, que en noviembre de 1915 había presentado su propia formulación variacional de la gravitación [@hilbert1915], llegó a la conclusión de que en la teoría no había teoremas de energía «propios» [@klein1918a]. Para estudiar el problema, Hilbert y Felix Klein invitaron a Gotinga ese mismo año a Emmy Noether (1882–1935), la mayor experta de la época en teoría de invariantes, en la que se había doctorado en 1907 [@noether1908]. Einstein, por su parte, mostró en 1918 que la energía total de un sistema aislado sí está bien definida y se conserva, aunque no pueda repartirse punto a punto [@einstein1918].

Noether trabajó en el problema entre 1915 y 1918. El resultado fue el artículo *Invariante Variationsprobleme*, que Klein presentó el 26 de julio de 1918 en la Sociedad de Ciencias de Gotinga [@noether1918]. Contiene dos teoremas. El primero, el que hoy se conoce como teorema de Noether, establece que en todo sistema cuyas ecuaciones se obtienen de un principio variacional, a cada simetría continua de la acción le corresponde una cantidad conservada:

* la invariancia bajo traslaciones en el tiempo da la conservación de la energía;
* bajo traslaciones en el espacio, la del momento lineal;
* y bajo rotaciones, la del momento angular.

Relaciones que antes se conocían caso a caso pasaron a ser consecuencias de una sola regla. El segundo teorema trata las simetrías que dependen de funciones arbitrarias, como los cambios generales de coordenadas de la relatividad general. En ese caso no aparecen cantidades conservadas independientes, y eso explica la forma peculiar que toma la conservación de la energía en esa teoría, la que había señalado Hilbert.

Einstein siguió estos trabajos desde Berlín. El 27 de diciembre de 1918, al recibir el artículo, escribió a Klein que volvía a sentir como una gran injusticia que a Noether se le negara la *venia legendi*, el permiso para enseñar en la universidad, y propuso dar un paso enérgico ante el ministerio [@einstein1998, documento 677]. La negativa se debía a que Noether era mujer. Las normas de las universidades prusianas no permitían habilitarse a las mujeres: su solicitud de 1915 fue rechazada, y durante esos años impartió cursos anunciados a nombre de Hilbert. Obtuvo la habilitación en 1919, cuando las normas cambiaron tras la caída del Imperio, pero nunca llegó a tener en Gotinga una plaza de catedrática. En 1933, las leyes del régimen nazi la expulsaron de la universidad por ser judía. Emigró a Estados Unidos, donde enseñó en el Bryn Mawr College, y murió allí en 1935 [@blanco2011]. El primer teorema, en su forma más sencilla, es el que se desarrolla en el capítulo 4 de este trabajo.

Este capítulo resume una versión más extensa, que incluye además la teoría de invariantes del siglo XIX y el debate de 1918 sobre la energía del campo gravitatorio [@calderon2026contexto].

# Objetivos

**Objetivo general:** mostrar cómo las simetrías de un sistema físico están relacionadas con sus leyes de conservación, y cómo esa relación sigue siendo fundamental en mecánica cuántica.

**Objetivos específicos:**

1. Presentar el formalismo lagrangiano mínimo necesario para formular con precisión qué es una simetría (apartado 4.1 y anexo A).
2. Enunciar y demostrar el teorema de Noether en su forma más sencilla, y obtener de él la conservación del momento lineal, del momento angular y de la energía (apartado 4.2).
3. Comprobar las tres conservaciones en tres ejemplos resueltos, la partícula libre, el tiro parabólico y la fuerza central, y mostrar que una simetría no solo dice qué se conserva, sino que también ayuda a resolver el problema (apartado 4.2).
4. Mostrar cómo se expresa la misma idea en mecánica cuántica, donde una transformación es una simetría si conmuta con el hamiltoniano (apartado 4.3).
5. Relacionar la simetría de giro de un potencial central con los números cuánticos $\ell$ y $m_\ell$ del momento angular (apartado 4.4).

# Desarrollo del trabajo

<!-- Desarrollo, contrastando las ideas de varios autores y, si es posible, con las propias. -->

## Formalismo lagrangiano

Este apartado resume el desarrollo de @calderon2026fisica, para el lagrangiano, y de @calderon2026matematicas, para la acción y la ecuación de Euler–Lagrange.

**Coordenadas generalizadas.** La configuración de un sistema mecánico se describe con un conjunto de coordenadas $q_1, \dots, q_n$, que pueden ser posiciones cartesianas, ángulos o distancias: son las coordenadas generalizadas. Sus derivadas respecto del tiempo, $\dot{q}_1, \dots, \dot{q}_n$, son las velocidades generalizadas. Para una partícula de masa $m$ en coordenadas cartesianas, $n = 3$, y las leyes de Newton dicen

$$
\begin{aligned}
p_i = m \cdot \dot{q}_i, \qquad \dfrac{dp_i}{dt} = F_i, \qquad i = 1, 2, 3.
\end{aligned}
$$

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

**Ejemplo: el tiro parabólico.** Para una partícula en el plano vertical, con $x$ horizontal y $z$ vertical, $L = \dfrac{1}{2} \cdot m \cdot (\dot{x}^2 + \dot{z}^2) - m \cdot g \cdot z$. Las ecuaciones de Euler–Lagrange dan $m \cdot \ddot{x} = 0$ y $m \cdot \ddot{z} = -m \cdot g$: movimiento uniforme en horizontal y uniformemente acelerado en vertical.

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

**Varias coordenadas y cambio de coordenadas.** Con $n$ coordenadas generalizadas hay una ecuación de Euler–Lagrange para cada una. Además, la ecuación tiene la misma forma en cualquier sistema de coordenadas: basta escribir $L$ en las nuevas coordenadas. La razón es que el principio de Hamilton no depende de cómo se describa la trayectoria: su acción es el mismo número en cartesianas que en polares. Por ejemplo, en coordenadas polares del plano, $T = \dfrac{1}{2} \cdot m \cdot (\dot{r}^2 + r^2 \cdot \dot{\theta}^2)$.

**El momento conjugado.** A cada coordenada generalizada se le asocia su momento conjugado, $p_i := \dfrac{\partial L}{\partial \dot{q}_i}$. En cartesianas es la cantidad de movimiento, $m \cdot \dot{q}_i$; para el ángulo de las coordenadas polares es $p_\theta = m \cdot r^2 \cdot \dot{\theta}$, la componente $L_z$ del momento angular. Con esta notación, la ecuación de Euler–Lagrange se escribe $\dot{p}_i = \dfrac{\partial L}{\partial q_i}$, que es la forma que usa el teorema de Noether.

## Simetrías y teorema de Noether

Este apartado resume @calderon2026noethermat, para la definición de simetría y el teorema, y @calderon2026noetherfis y @calderon2026noetherfisej, para los ejemplos. Con el lenguaje del apartado anterior se puede precisar qué es una simetría y demostrar que cada simetría continua lleva asociada una cantidad conservada. Después, tres ejemplos aplican el teorema paso a paso, de más a menos simétricos: la partícula libre, el tiro parabólico y la fuerza central.

### La coordenada cíclica

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

### Transformaciones continuas y simetrías

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

### El teorema de Noether

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

### La energía y la traslación en el tiempo

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

### Primer ejemplo: la partícula libre

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

### Segundo ejemplo: el tiro parabólico

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

### Tercer ejemplo: la fuerza central

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

### Lo que muestran los ejemplos

Cada campo exterior conserva unas simetrías de la partícula libre y rompe otras, y las cantidades conservadas siguen a las simetrías:

| Simetría | Partícula libre | Tiro parabólico | Fuerza central |
| --- | --- | --- | --- |
| Traslaciones | $\vec{p}$ | $p_x$, $p_y$ y $p_z + m \cdot g \cdot t$ | ninguna |
| Giros | $\vec{L}$ | $L_z$ | $\vec{L}$ |
| Traslación en el tiempo | $E$ | $E$ | $E$ |

Table: Cantidades conservadas según las simetrías que deja cada campo.

La gravedad uniforme distingue una dirección; la fuerza central, un punto. Y la elección de coordenadas importa: en cartesianas, ninguna coordenada de la fuerza central es cíclica; en polares, la simetría aparece como una coordenada cíclica.

### Lo que hereda la parte cuántica

Los ejemplos preparan la parte cuántica del trabajo, para que las dos no queden como explicaciones separadas:

| De la parte clásica | Lo que reaparece en cuántica |
| --- | --- |
| La idea «simetría, cantidad conservada» | La misma idea, con operadores |
| El momento $p_x$, conservado cuando $x$ es cíclica | El operador $\hat{p} = -i \cdot \hbar \cdot \dfrac{d}{dx}$ y la partícula libre |
| La energía $H$ | El hamiltoniano $\hat{H}$ y la ecuación de Schrödinger |
| La fuerza central: $L_z$ conservado y reducción a una dimensión | El potencial central: $\hat{L}^2$, $\hat{L}_z$ y los números cuánticos $\ell$ y $m_\ell$ |

Table: Correspondencia entre la parte clásica y la parte cuántica.

# Conclusiones

<!-- Los cuatro (2 páginas). Recuperar la pregunta inicial y responderla: las leyes de conservación son
consecuencias de las simetrías. Reflexión personal obligatoria. Guion: documento_general_trabajo.md,
apartado 5. -->

# Bibliografía {-}

::: {#refs}
:::

\appendix

# Deducción de la ecuación de Euler–Lagrange

La deducción sigue @calderon2026matematicas, y la demostración del lema fundamental, @calderon2026anexos.

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

**Varias coordenadas.** Con $n$ coordenadas se toma una función $h_i$ para cada una. Variando una sola coordenada cada vez, es decir, con todas las $h_j$ nulas salvo $h_i$, el mismo razonamiento da una ecuación de Euler–Lagrange para cada $q_i$.

# Las simetrías de Galileo

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

**Varias partículas.** Con $N$ partículas que interaccionan con fuerzas que solo dependen de las distancias entre ellas, y sin campo exterior, las diez transformaciones aplicadas a todas las partículas a la vez siguen siendo simetrías, y se conservan las cantidades **totales**:

| Simetría | Condición sobre $V$ | Cantidad conservada |
| --- | --- | --- |
| Traslación en el tiempo | $V$ no depende de $t$ | $E = T + V$ |
| Traslaciones | $V$ solo depende de las diferencias $\vec{r}_a - \vec{r}_b$ | $\vec{P} = \sum_a \vec{p}_a$ |
| Giros | $V$ no cambia al girar todas las posiciones | $\vec{L} = \sum_a \vec{r}_a \times \vec{p}_a$ |
| Cambios de velocidad | la de las traslaciones | $\vec{G} = M \cdot \vec{R}_{\mathrm{cm}} - \vec{P} \cdot t$ |

Table: Simetrías de un sistema de partículas y cantidades conservadas.

Aquí $M$ es la masa total y $\vec{R}_{\mathrm{cm}}$, el centro de masas. Cada partícula conserva su propia cantidad de movimiento solo si no interacciona con las demás: lo que no tiene puntos privilegiados es el sistema en su conjunto. La conservación de $\vec{G}$ dice que el centro de masas se mueve con velocidad constante, $\vec{R}_{\mathrm{cm}}(t) = \dfrac{\vec{G} + \vec{P} \cdot t}{M}$. Las diez transformaciones se componen entre sí y forman un grupo de diez parámetros, el **grupo de Galileo** [@calderon2026noetheranexos]. El cálculo de las diez cantidades está comprobado con cálculo simbólico en el repositorio de uno de los autores [@calderon2026mcc].
