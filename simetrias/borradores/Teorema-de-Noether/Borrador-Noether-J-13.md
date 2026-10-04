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
