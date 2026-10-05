# 4.2 Simetrías y teorema de Noether

Con el lenguaje del apartado anterior se puede formular con precisión matemática qué es una simetría, cómo se distingue de la estacionariedad de la acción, y cómo, a través del teorema de Noether, cada simetría continua lleva asociada inexorablemente una cantidad conservada.

### La coordenada cíclica

El caso más intuitivo de conservación ocurre cuando una coordenada $q_k$ no aparece explícitamente en el lagrangiano $L$, aunque sí lo haga su velocidad $\dot{q}_k$. En este caso, se dice que la coordenada es cíclica. La ecuación de Euler-Lagrange para $q_k$ es:

$$
\begin{aligned}
\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_k}\right) - \dfrac{\partial L}{\partial q_k} = 0
\end{aligned}
$$

Como $q_k$ no aparece, $\dfrac{\partial L}{\partial q_k} = 0$, lo que implica directamente que $\dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_k}\right) = 0$. Por tanto, el momento conjugado $p_k = \dfrac{\partial L}{\partial \dot{q}_k}$ es una constante del movimiento. Desplazar todo el experimento a lo largo de $q_k$ no cambia la física; esa simetría de traslación conduce a una cantidad conservada.

Para ilustrarlo con claridad, veamos algunos ejemplos concretos:
- **Partícula libre:** Si una partícula de masa $m$ no está sometida a ningún campo de potenciales ($V = 0$), su lagrangiano es exclusivamente su energía cinética, $L = T = \dfrac{1}{2} \cdot m \cdot \lVert\dot{\vec{q}}\rVert^2$. Al derivar, $\dfrac{\partial L}{\partial q_i} = 0$ para las tres coordenadas espaciales ($i = 1, 2, 3$). Como las tres son cíclicas, se conserva el vector momento lineal completo, $\vec{p} = m \cdot \dot{\vec{q}}$.
- **Tiro parabólico (gravedad uniforme):** Si la gravedad actúa hacia abajo en el eje $z$, el lagrangiano es $L = \dfrac{1}{2} \cdot m \cdot (\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - m \cdot g \cdot z$. Las coordenadas horizontales $x$ e $y$ son cíclicas, por lo que $p_x$ y $p_y$ se conservan (simetría de traslación horizontal). Sin embargo, $z$ sí aparece en la energía potencial, rompiendo la simetría en la vertical: $\dfrac{\partial L}{\partial z} = -m \cdot g \neq 0$, y por tanto $p_z$ no se conserva.
- **Fuerza central (coordenadas polares):** Ante un potencial que solo depende de la distancia al origen, $V(r)$, el lagrangiano en el plano es $L = \dfrac{1}{2} \cdot m \cdot (\dot{r}^2 + r^2 \cdot \dot{\theta}^2) - V(r)$. La coordenada angular $\theta$ no aparece explícitamente, demostrando que el sistema tiene simetría de rotación. Como $\theta$ es cíclica, se conserva su momento conjugado: el momento angular $p_\theta = m \cdot r^2 \cdot \dot{\theta}$.

### Qué es una simetría y la transformación continua

El teorema de Noether generaliza esta idea. No trabaja con una transformación aislada, sino con familias de transformaciones $\Phi_\varepsilon$ que dependen de forma continua de un parámetro pequeño $\varepsilon$. Cada punto $q_i$ se mueve en una dirección dada por su generador infinitesimal $\xi_i$:

$$
\begin{aligned}
q_i \to q_i + \varepsilon \cdot \xi_i(q, t)
\end{aligned}
$$

Es crucial distinguir dos conceptos que, aunque usan el lagrangiano, responden a preguntas distintas:
- **Estacionariedad (principio de Hamilton, $\delta S = 0$):** se varía una trayectoria de cualquier manera manteniendo sus extremos fijos, buscando aquella cuya acción no cambia a primer orden. Su papel es *seleccionar las soluciones físicas* de entre todos los caminos posibles.
- **Simetría:** se fija una transformación particular $\Phi_\varepsilon$ y se exige que *no cambie la acción de ninguna trayectoria*, sea solución o no, salvo quizá en un término de frontera. La simetría no es una propiedad de una trayectoria particular, sino del lagrangiano, es decir, de la ley física misma. Físicamente, transforma soluciones en otras soluciones válidas.

A nivel infinitesimal, que la transformación sea una simetría equivale a que el lagrangiano quede igual a primer orden, o cambie a lo sumo en una derivada total respecto del tiempo: $\delta L = \varepsilon \cdot \dfrac{dF}{dt}$.

### El teorema de Noether (la cuenta)

El primer teorema de Noether establece que, por cada simetría continua de la acción, existe una cantidad $Q$ que se conserva. Evaluando la variación del lagrangiano mediante la regla de la cadena, tenemos:

$$
\begin{aligned}
\dfrac{\delta L}{\varepsilon} = \sum_i \left( \dfrac{\partial L}{\partial q_i} \cdot \xi_i + \dfrac{\partial L}{\partial \dot{q}_i} \cdot \dot{\xi}_i \right)
\end{aligned}
$$

Sobre una trayectoria que sea solución física, se cumple la ecuación de Euler-Lagrange, $\dfrac{\partial L}{\partial q_i} = \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_i}\right)$. Sustituyendo el primer término, la suma se convierte exactamente en la derivada de un producto:

$$
\begin{aligned}
\dfrac{\delta L}{\varepsilon} = \sum_i \left( \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_i}\right) \cdot \xi_i + \dfrac{\partial L}{\partial \dot{q}_i} \cdot \dot{\xi}_i \right) = \dfrac{d}{dt}\left( \sum_i p_i \cdot \xi_i \right)
\end{aligned}
$$

Como por definición de simetría $\dfrac{\delta L}{\varepsilon} = \dfrac{dF}{dt}$, igualamos ambas derivadas:

$$
\begin{aligned}
\dfrac{d}{dt}\left( \sum_i p_i \cdot \xi_i \right) = \dfrac{dF}{dt} \quad \Longrightarrow \quad Q = \sum_i p_i \cdot \xi_i - F \text{ se conserva.}
\end{aligned}
$$

### La energía y la traslación temporal

Si la transformación afecta también al tiempo, $t \to t + \varepsilon \cdot \tau$, aparece un término adicional con el hamiltoniano, quedando $Q = \sum_i p_i \cdot \xi_i - H \cdot \tau - F$.

En el caso particular de una traslación puramente temporal ($\tau = 1$, $\xi_i = 0$, $F = 0$), la simetría existe si el lagrangiano no depende explícitamente del tiempo ($V$ no depende de $t$). En ese caso, la cantidad conservada es directamente el hamiltoniano $H$:

$$
\begin{aligned}
H = \sum_i p_i \cdot \dot{q}_i - L
\end{aligned}
$$

Para los sistemas habituales de la mecánica clásica (donde $T$ es cuadrática en las velocidades y $V$ no depende de ellas), este hamiltoniano coincide exactamente con la energía mecánica total, $E = T + V$.

### Ejemplo: Partícula bajo un potencial central

Antes de pasar al caso más general, ilustremos la potencia del teorema de Noether con un caso paradigmático. Consideremos una partícula sometida a un potencial central $V(|\vec{q}|)$, cuyo lagrangiano es $L = \frac{1}{2}m |\dot{\vec{q}}|^2 - V(|\vec{q}|)$. 

Dado que el potencial depende exclusivamente de la distancia al origen, el sistema tiene simetría esférica: es totalmente invariante ante cualquier rotación espacial pura ($\tau = 0$). Si tomamos una rotación infinitesimal de ángulo $\varepsilon$ alrededor de un eje arbitrario dictado por un vector unitario $\vec{n}$, las coordenadas de la partícula sufren un desplazamiento cuyo campo generador viene dado por el producto vectorial:

$$
\begin{aligned}
\vec{\xi} = \vec{n} \times \vec{q}
\end{aligned}
$$

Como el lagrangiano completo es un escalar invariante bajo rotaciones, su variación es nula, por lo que $F=0$. Sustituyendo en la expresión general de la carga de Noether $Q = \vec{p} \cdot \vec{\xi}$:

$$
\begin{aligned}
Q = \vec{p} \cdot (\vec{n} \times \vec{q}) = \vec{n} \cdot (\vec{q} \times \vec{p}) = \vec{n} \cdot \vec{L}
\end{aligned}
$$

donde hemos hecho uso de la propiedad cíclica del producto mixto, y donde $\vec{L} = \vec{q} \times \vec{p}$ representa el vector momento angular. Dado que el eje de rotación $\vec{n}$ elegido es completamente arbitrario, la única forma de que la cantidad $\vec{n} \cdot \vec{L}$ sea constante siempre, es que el propio vector $\vec{L}$ sea constante. Así, Noether demuestra matemáticamente de forma irrefutable que **la simetría esférica implica la conservación de las tres componentes del momento angular**.

### Las 10 cantidades conservadas del Grupo de Galileo

Elevando este razonamiento a su forma más general, podemos demostrar que la invariancia fundamental del espacio-tiempo newtoniano encierra en su seno todas las leyes de conservación de la mecánica clásica. Consideremos un sistema de $N$ partículas con un lagrangiano estándar de fuerzas internas $L = \sum_a \frac{1}{2} m_a |\dot{\vec{q}}_a|^2 - V$.

El grupo de Galileo parametriza las transformaciones continuas del espacio y el tiempo mediante **10 parámetros independientes**:
- 3 parámetros para traslaciones espaciales en una dirección $\vec{e}$.
- 3 parámetros para rotaciones espaciales alrededor de un eje $\vec{n}$.
- 3 parámetros para cambios de velocidad relativos (Boosts de Galileo) en una dirección $\vec{u}$.
- 1 parámetro para traslaciones temporales.

Utilizando la fórmula maestra de la carga de Noether $Q = \sum_a \vec{p}_a \cdot \vec{\xi}_a - H \tau - F$, calculemos de un solo plumazo las cantidades conservadas para cada generador:

1. **Traslaciones espaciales (3 parámetros):** El tiempo se congela ($\tau=0$) y las coordenadas de todas las partículas se desplazan de manera uniforme $\vec{\xi}_a = \vec{e}$. Como el lagrangiano de fuerzas internas (donde $V$ depende solo de distancias relativas) es invariante, $F=0$. 
   $$ Q = \sum_a \vec{p}_a \cdot \vec{e} = \vec{e} \cdot \left( \sum_a \vec{p}_a \right) = \vec{e} \cdot \vec{P} $$
   Se conserva el **momento lineal total** $\vec{P}$.

2. **Rotaciones espaciales (3 parámetros):** El tiempo se congela ($\tau=0$) y el espacio gira, $\vec{\xi}_a = \vec{n} \times \vec{q}_a$. El lagrangiano es invariante, luego $F=0$. 
   $$ Q = \sum_a \vec{p}_a \cdot (\vec{n} \times \vec{q}_a) = \vec{n} \cdot \left( \sum_a \vec{q}_a \times \vec{p}_a \right) = \vec{n} \cdot \vec{L} $$
   Se conserva el **momento angular total** $\vec{L}$.

3. **Traslación temporal (1 parámetro):** El espacio no se toca ($\vec{\xi}_a = 0$), pero el reloj avanza un pulso ($\tau=1$). Si las fuerzas no dependen del tiempo, $F=0$.
   $$ Q = - H \cdot 1 = -H $$
   Se conserva la **energía mecánica total** $H$.

4. **Boosts de Galileo (3 parámetros):** El tiempo se congela ($\tau=0$), pero saltamos a un sistema de referencia inercial que se mueve con velocidad relativa $\vec{u}$. El generador de la posición depende ahora explícitamente del tiempo: $\vec{\xi}_a = \vec{u} t$. Bajo esta transformación, las velocidades de las partículas cambian, modificando de facto la energía cinética y, por ende, el lagrangiano. Al calcular su variación infinitesimal, esta resulta ser sorprendentemente una derivada total exacta: $\delta L = \frac{d}{dt} \left( \vec{u} \cdot \sum_a m_a \vec{q}_a \right)$. Esto significa que nuestra función frontera no es nula, sino $F = \vec{u} \cdot \sum_a m_a \vec{q}_a$. Sustituyendo en la carga:
   $$ Q = \sum_a \vec{p}_a \cdot (\vec{u} t) - \left( \vec{u} \cdot \sum_a m_a \vec{q}_a \right) = -\vec{u} \cdot \left( \sum_a m_a \vec{q}_a - \vec{P} t \right) = -\vec{u} \cdot \vec{G} $$
   Se conserva el **vector del movimiento del centro de masas** $\vec{G} = M \vec{q}_{\text{CM}} - \vec{P} t$, lo que matemáticamente garantiza el principio de inercia: el centro de masas del sistema se mueve a velocidad estrictamente constante.

En resumen, exigiendo pura y llanamente que las leyes de la física no cambien ante transformaciones del grupo de Galileo, la maquinaria del teorema de Noether nos ha "regalado" **de forma unificada la conservación de las 10 magnitudes fundamentales del universo clásico**: $\vec{P}$, $\vec{L}$, $\vec{G}$ y $H$.
