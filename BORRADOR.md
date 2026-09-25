Empezaré a dar ideas sueltas sobre este primer trabajo. El trabajo se titulará «Las simetrías en la física».

PLATEANDO EL PROBLEMA

Lo primero es saber que decimos cuando hablamos de leyes de la física.
Tenemos una doble vertiente:

1. Qué es lo que asumimos cuando planteamos una ecuación de la física, que decimos que es verdadera. Un ejemplo es la relatividad de Galileo. El tiempo de cualquier observador es el mismo (que lo distingue de la relatividad especial). Pero el marco espacial depende de forma lineal (como en un álgebra lineal sobre $\mathbb{R}$ de dimensión 3). De aquí vienen las transformaciones de las coordenadas, de las velocidades, etc. afirmando que las leyes son las mismas. Esto lleva implícito que en el espacio tridimensional, las leyes son las mismas bajo traslaciones, bajo rotaciones, antes y después (traslaciones temporales). Con esas aclaraciones ya se ve algo de lo que tenemos que hacer.
2. Pero aún queda un problema. El marco general. Lo que he puesto en el punto 1. nos pone en la ruta, pero el problema es que esas leyes siempre habría que verlas de forma particular. Si hablamos de la ley de Hook del comportamiento de muelles y deformaciones elásticas, $\vec{F} = -k \cdot \vec{r}$, dónde $k$ es una constante propia del medio elástico, y $\vec{r}$ es la elongación producida con dirección, $\vec{F}$ es la fuerza que el elástico produce en dirección contraria a la elongación. Si tenemos dos observadores colocado uno en la posición $0$ de $\mathbb{R}^3$, y otro en otra posición con velocidad constante respecto al $0$, deben poder medirse con la mediación de una matriz $A_{3\times 3}(t)$ que indique el movimiento del segundo observador contra el observador que está en $0$. A lo medido por el obsevador central, debemos poder multiplicar su fuerza y su elongación por esta matriz, y el resultado debe ser conforme a la ley de Hook. ¿¿?? Pero todo esto nos obliga siempre a mirar problemas particulares. ¿Podemos dar este tipo de resultados con mayor generalidad? Aquí es dónde entra el Principio de Mínima Acción de Hamilton. El formalismo langrangiano da una forma muy general y muy precisa ala vez de la idea de teoría física. Toda la mecánica clásica parece caber en esta formulación. Damos un funcional para un sistema de $N$ partículas discretas, para cada función $f : \mathbb{R}^{3 \cdot N + 1} \to \mathbb{R}$ tal que tenga determinadas propiedades, como tener segundas derivadas parciales continuas en todas las variables, esto formará un espacio vectorial de funciones que llamaremos $\mathcal{C}^2 = \{f : \mathbb{R}^{3 \cdot N + 1} \to \mathbb{R} | \forall i < 3\cdot N+1, \forall j < 3>, \exists \dfrac {\partial^j f} {\partial x_i^j}, f(\infty)=f(-\infty)=0\}$ y definimos $\mathcal{L}: \mathcal{C}^2 \to \mathbb{R}$, terminamos obteniendo la acción $S[f] = \int_{t_0}^{t_1} \mathcal{L}(f) \dt$, si $f$ es tal que $\vardelta S[f] = 0$, entonces la ley dada por $f$ es físicamente correcta.

IDEAS PARA EL DESARROLLO (conversación con la IA, 25-09-2026)

Material de trabajo para el capítulo «Desarrollo del trabajo» de simetrias.md. El planteamiento ya recoge la definición de simetría y el camino; aquí van los detalles.

1. Transformaciones continuas, campos vectoriales y flujos

El teorema de Noether no trabaja con una transformación suelta, sino con familias de un parámetro $\Phi_\varepsilon$ que dependen de forma continua de $\varepsilon$ y cumplen

$$
\begin{aligned}
\Phi_0 = \text{identidad}, \qquad \Phi_{\varepsilon} \circ \Phi_{\delta} = \Phi_{\varepsilon + \delta}.
\end{aligned}
$$

Por ejemplo, las rotaciones de ángulo $\varepsilon$ alrededor de un eje fijo, o las traslaciones de longitud $\varepsilon$ en una dirección fija. Cada una es un subgrupo uniparamétrico del grupo de Galileo.

Derivando respecto de $\varepsilon$ en $\varepsilon = 0$ se obtiene en cada punto un vector, la dirección en que la transformación empieza a moverlo. Es el campo vectorial generador (generador infinitesimal):

$$
\begin{aligned}
\xi(q) = \left.\dfrac{d}{d\varepsilon}\Phi_\varepsilon(q)\right|_{\varepsilon = 0}.
\end{aligned}
$$

A la inversa, dado el campo $\xi$, la familia se recupera resolviendo $\dfrac{d}{d\varepsilon}\Phi_\varepsilon(q) = \xi(\Phi_\varepsilon(q))$: es el flujo del campo. «Transformación continua» y «campo vectorial» son dos caras de lo mismo, y Noether solo necesita el campo, que es lo lineal.

Generadores del grupo de Galileo, para partículas en posiciones $\vec{x}_a$:

| Transformación | Flujo $\Phi_\varepsilon$ | Generador |
| --- | --- | --- |
| Traslación temporal | $t \to t + \varepsilon$ | $\tau = 1$ (mueve el tiempo, no las posiciones) |
| Traslación espacial en la dirección $\vec{e}$ | $\vec{x}_a \to \vec{x}_a + \varepsilon \cdot \vec{e}$ | $\vec{\xi}_a = \vec{e}$ |
| Rotación alrededor del eje $\vec{n}$ | $\vec{x}_a \to R_{\vec{n}}(\varepsilon) \cdot \vec{x}_a$ | $\vec{\xi}_a = \vec{n} \times \vec{x}_a$ |
| Cambio de velocidad $\vec{u}$ | $\vec{x}_a \to \vec{x}_a + \varepsilon \cdot \vec{u} \cdot t$ | $\vec{\xi}_a = \vec{u} \cdot t$ (depende del tiempo) |

Son 1 + 3 + 3 + 3 = 10 generadores independientes, tantos como parámetros del grupo.

2. Qué es una simetría y en qué se distingue de la estacionariedad

- Estacionariedad ($\delta S = 0$): se varía la trayectoria de cualquier manera sin mover sus extremos y se busca la trayectoria cuya acción no cambia en primer orden. Selecciona las soluciones.
- Simetría: se fija una transformación $\Phi_\varepsilon$ y se exige que no cambie la acción de ninguna trayectoria, física o no, $S[\Phi_\varepsilon \circ q] = S[q]$ para toda $q$, salvo un término de frontera. Equivale a $\delta L = \varepsilon \cdot \dfrac{dF}{dt}$.
- La simetría la tiene la transformación (su campo $\xi$), no una trayectoria, y es una propiedad del lagrangiano, es decir, de la ley. Transforma soluciones en soluciones.

3. Primer teorema de Noether en mecánica: la cuenta

Sea $q_i \to q_i + \varepsilon \cdot \xi_i(q, t)$ con $\delta L = \varepsilon \cdot \dfrac{dF}{dt}$. Por la regla de la cadena,

$$
\begin{aligned}
\dfrac{\delta L}{\varepsilon} = \sum_i \left( \dfrac{\partial L}{\partial q_i} \cdot \xi_i + \dfrac{\partial L}{\partial \dot{q}_i} \cdot \dot{\xi}_i \right).
\end{aligned}
$$

Sobre una solución vale la ecuación de Euler-Lagrange, $\dfrac{\partial L}{\partial q_i} = \dfrac{d}{dt}\left(\dfrac{\partial L}{\partial \dot{q}_i}\right) = \dot{p}_i$, y los dos términos forman la derivada de un producto:

$$
\begin{aligned}
\dfrac{\delta L}{\varepsilon} = \dfrac{d}{dt}\left( \sum_i p_i \cdot \xi_i \right) = \dfrac{dF}{dt}
\quad \Longrightarrow \quad
Q = \sum_i p_i \cdot \xi_i - F \ \text{ se conserva.}
\end{aligned}
$$

Si la transformación mueve también el tiempo ($t \to t + \varepsilon \cdot \tau$), aparece un término más: $Q = \sum_i p_i \cdot \xi_i - H \cdot \tau - F$, con $H$ el hamiltoniano. De ahí sale que $H$ se conserva cuando $L$ no depende explícitamente del tiempo (Tema 1, sección 7).

4. Aplicación al grupo de Galileo

Para $N$ partículas con $L = \sum_a \dfrac{1}{2} \cdot m_a \cdot |\dot{\vec{x}}_a|^2 - V$, cada simetría impone una condición sobre $V$ (la física del problema):

| Simetría | Condición sobre $V$ | Cantidad conservada |
| --- | --- | --- |
| Traslación temporal | $V$ no depende de $t$ | Energía $E = T + V$ |
| Traslaciones espaciales | $V$ solo depende de las diferencias $\vec{x}_a - \vec{x}_b$ | Momento total $\vec{P} = \sum_a m_a \cdot \dot{\vec{x}}_a$ |
| Rotaciones | además, solo de las distancias $\lvert \vec{x}_a - \vec{x}_b \rvert$ | Momento angular $\vec{J} = \sum_a \vec{x}_a \times \vec{p}_a$ |
| Cambios de velocidad | se cumple si se cumple la de las traslaciones; $L$ cambia en $\dfrac{d}{dt}\left(\sum_a m_a \cdot \vec{u} \cdot \vec{x}_a\right)$ | $\vec{G} = M \cdot \vec{X}_{\mathrm{cm}} - \vec{P} \cdot t$ |

En total, 1 + 3 + 3 + 3 = 10 cantidades conservadas. Comprobado con SymPy para tres partículas en cuadernos/tema1/noether_galileo.py (16 comprobaciones: invariancia de L bajo cada generador, cantidades de Noether y su conservación sobre las soluciones).

5. Posibles extensiones (opcionales)

- Campos y relatividad especial: grupo de Poincaré (también 10 parámetros) y tensor de energía-momento; segundo teorema de Noether y relatividad general, enlazando con el contexto histórico.
- Mecánica cuántica (la asignatura es Fundamentos de Mecánica Cuántica): una simetría es un operador unitario; su generador es un observable $\hat{Q}$; se conserva si y solo si $[\hat{H}, \hat{Q}] = 0$. Ejemplos: momento lineal y traslaciones, momento angular y rotaciones.
