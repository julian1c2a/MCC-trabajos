# Matrices de Rotación

Supongamos que existe un vector unitario $\hat{u}$ cualquiera en $\mathbb{R}^3$. Entonces podemos pensar en una transformación $R(\hat{u},\theta)$ como una rotación de ángulo $\theta$ de cualquier punto alrededor de la recta definida por $\hat{u}$ (tomándola como base de un subespacio vectorial unidimensional). Llamaremos matriz asociada a la transformación (tomando $B_C$ como la base canónica) $\mathcal{R}_{\theta} := {\mathcal{M}_{B_C}}(R(\hat{u},\theta))$, donde, a partir de ahora, dejamos fijo el vector $\hat{u}$, de forma que la matriz depende exclusivamente del parámetro real $\theta \in \mathbb{R}$, con $\mathcal{R}_{\theta + 2\cdot\pi} = \mathcal{R}_{\theta}$: un ángulo y ese ángulo más una vuelta completa dan la misma rotación. (Si se toma $\theta \in [0, 2\cdot\pi)$, los ángulos se suman módulo $2\cdot\pi$.)

**En $\mathbb{R}^n$.** Girar alrededor de una recta solo tiene sentido en $\mathbb{R}^3$. Con $n = 2$, el complemento ortogonal de una recta es otra recta, y una transformación ortogonal que deja fija la recta es la identidad o una reflexión: en el plano se gira alrededor de un punto. Con $n \ge 4$, el complemento ortogonal de la recta tiene dimensión $n - 1 \ge 3$, y «girar un ángulo $\theta$» no determina una única transformación. En general, una rotación gira un plano $\Pi$ (un subespacio de dimensión $2$) y deja fijo su complemento ortogonal $\Pi^\perp$; en $\mathbb{R}^3$, $\Pi$ es el plano perpendicular a $\hat{u}$. Las propiedades siguientes que no usan el eje $\hat{u}$ valen en $\mathbb{R}^n$ para cualquier $n \ge 2$.

¿Qué sabemos hasta ahora?

- $\mathcal{R}_{\theta_1}\cdot\mathcal{R}_{\theta_2} = \mathcal{R}_{\theta_1+\theta_2}$.
- $\mathcal{R}_{0} = {(\delta_{i,j})}_{i\,j} = \mathcal{I}$, la matriz identidad, donde $\delta_{i,i}=1$ y si $i\neq j$ entonces $\delta_{i,j}=0$, esto es, la delta de Kronecker.
- Al ser rotaciones, la distancia al centro y al eje de rotación $\hat{u}$ no cambia en el punto transformado. Sea el vector a transformar $\vec{p}$. El vector transformado será $\vec{p}' = \mathcal{R}_{\theta}\vec{p}$. El cuadrado del módulo de $\vec{p}$ será $\vec{p}^T\cdot\vec{p}$, y el de $\vec{p}'$ será ${\vec{p}'}^T \cdot {\vec{p}'}$. Vamos a poner ahora el último en función de $\vec{p}$, ${\vec{p}'}^T \cdot {\vec{p}'} = {(\mathcal{R}_{\theta}\vec{p})}^T \cdot {(\mathcal{R}_{\theta}\vec{p})} = {\vec{p}^T\mathcal{R}_{\theta}^T} \cdot {(\mathcal{R}_{\theta}\vec{p})} = \vec{p}^T{(\mathcal{R}_{\theta}^T \cdot \mathcal{R}_{\theta})}\vec{p}$. Pero por la invariancia de los módulos tendremos:

$$
\begin{aligned}
\forall \vec{p} \in \mathbb{R}^n \quad &\phantom{\iff} \vec{p}^T \cdot \vec{p}=\vec{p}^T{(\mathcal{R}_{\theta}^T \cdot \mathcal{R}_{\theta})}\vec{p} \\
&\iff \mathcal{R}_{\theta}^T \cdot \mathcal{R}_{\theta} = \mathcal{I} \\
&\iff {{\mathcal{R}}_{\theta}}^{-1} = {{\mathcal{R}}_{\theta}}^T,
\end{aligned}
$$

$\qquad$ por lo que sabemos ahora que la condición de no variar el módulo de los vectores es equivalente a $\mathcal{R}_{\theta}^{-1}=\mathcal{R}_{\theta}^T$. La primera equivalencia usa que $S := \mathcal{R}_{\theta}^T \cdot \mathcal{R}_{\theta}$ es simétrica, $S^T = S$. Para una matriz simétrica vale la identidad de polarización, $\vec{p}^T \cdot S \cdot \vec{q} = \dfrac{1}{4} \cdot \big((\vec{p}+\vec{q})^T \cdot S \cdot (\vec{p}+\vec{q}) - (\vec{p}-\vec{q})^T \cdot S \cdot (\vec{p}-\vec{q})\big)$: los valores de la forma cuadrática $\vec{p}^T \cdot S \cdot \vec{p}$ determinan todos los $\vec{p}^T \cdot S \cdot \vec{q}$, y con ellos la matriz $S$. Si coinciden con los de $\mathcal{I}$, $S = \mathcal{I}$. Para una matriz no simétrica no valdría, porque su parte antisimétrica no aparece en la forma cuadrática.

- Si $\varepsilon \to 0$ podremos aproximar $\mathcal{R}_{\varepsilon \cdot \theta} = \mathcal{I} + \varepsilon \cdot \mathcal{G}_{\theta} + O(\varepsilon^2)$.
- Con la aproximación anterior, vamos a componer dos rotaciones distintas de ángulos $\alpha$ y $\beta$ pequeñas y aproximarlas a primer orden:
  $$
  \begin{aligned}
  &\mathcal{R}_{\varepsilon \cdot \alpha} \cdot \mathcal{R}_{\varepsilon \cdot \beta} &&= (\mathcal{I} + \mathcal{G}_{\varepsilon \cdot \alpha})\cdot(\mathcal{I} + \mathcal{G}_{\varepsilon \cdot \beta}) + O(\varepsilon^2)\\
  &{} &&= (\mathcal{I} + \mathcal{G}_{\varepsilon \cdot \beta})+(\mathcal{G}_{\varepsilon \cdot \alpha} + \mathcal{G}_{\varepsilon \cdot \alpha} \cdot \mathcal{G}_{\varepsilon \cdot \beta}) + O(\varepsilon^2) \\
  &{} &&= \mathcal{I} + (\mathcal{G}_{\varepsilon \cdot \beta}+\mathcal{G}_{\varepsilon \cdot \alpha}) + O(\varepsilon^2) \\
  &\mathcal{R}_{\varepsilon \cdot \alpha} \cdot \mathcal{R}_{\varepsilon \cdot \beta} &&= \mathcal {I} + \mathcal{G}_{\varepsilon \cdot \beta}+\mathcal{G}_{\varepsilon \cdot \alpha} \mod (\varepsilon^2 = 0)
  \end{aligned}
  $$

$\qquad$ a primer orden es una igualdad. `¿Cómo hacer este razonamiento más formal?` No es lo mismo (en principio) $\varepsilon \cdot \mathcal{R}_\theta$ que $\mathcal{R}_{\varepsilon \cdot \theta}$.

<!-- AI: Atiende a la última pregutna hecha -->

- Las rotaciones alrededor del mismo vector-eje $\hat{u}$ conmutan para cualquier ángulo, no solo para giros pequeños. No hace falta el cálculo anterior: basta la primera propiedad, $\mathcal{R}_{\theta_1}\cdot\mathcal{R}_{\theta_2} = \mathcal{R}_{\theta_1+\theta_2} = \mathcal{R}_{\theta_2+\theta_1} = \mathcal{R}_{\theta_2}\cdot\mathcal{R}_{\theta_1}$, y la composición forma un grupo conmutativo. Lo que dice el cálculo anterior, la conmutatividad a primer orden, vale para cualquier par de ejes: dos rotaciones pequeñas alrededor de ejes distintos también conmutan a primer orden, y la diferencia entre los dos órdenes aparece a segundo orden.
- Como $\mathcal{R}_{\theta}^T\cdot\mathcal{R}_{\theta} = \mathcal{I}$, tomando determinantes, $\det \mathcal{R}_{\theta}^T\cdot \det\mathcal{R}_{\theta} = 1$, pero el determinante de la matriz transpuesta es igual al determinante de la matriz sin transponer, por lo que $(\det \mathcal{R}_{\theta})^2 = 1$ y $\det \mathcal{R}_{\theta} = \pm 1$. No hay que elegir el signo: $\theta \mapsto \det \mathcal{R}_{\theta}$ es continua, porque lo es $\mathcal{R}_{\theta}$ y el determinante es un polinomio en las entradas; solo toma los valores $\pm 1$ y vale $1$ en $\theta = 0$, porque $\mathcal{R}_0 = \mathcal{I}$. Como no puede saltar de $1$ a $-1$, $\det \mathcal{R}_{\theta} = 1$ para todo $\theta$. Las matrices ortogonales de determinante $-1$ incluyen una reflexión, y no forman en sí mismas un grupo: no contienen la identidad, y el producto de dos de ellas tiene determinante $(-1)\cdot(-1) = 1$, así que no es una de ellas.
- Si $\mathcal{R}_\theta$ es una matriz de rotación sobre $\hat{u}$, podemos obtener que $\mathcal{R}_\theta^T = \mathcal{R}_{-\theta}$. Al menos si $\theta$ es pequeña. Esto es porque $\mathcal{R}_\theta \cdot \mathcal{R}_{-\theta} \approx \mathcal{I} + \mathcal{G}_\theta + \mathcal{G}_{-\theta}$. Como son dos rotaciones opuestas, $\mathcal{G}_\theta + \mathcal{G}_{-\theta} = 0$, y de ahí $\mathcal{R}_\theta \cdot \mathcal{R}_{-\theta} \approx \mathcal{I}$, esto es, ${\mathcal{R}}_{\theta}^{T} = {\mathcal{R}}_{\theta}^{-1} = {\mathcal{R}}_{-\theta}$.
- `¿Cómo obtener que las matrices $\mathcal{G}_\theta$ son antisimétricas y que $tr \mathcal{G}_\theta = 0$?`
  <!-- AI: Atiende a la última pregutna hecha -->
- `¿Cómo expandir la propiedad de que $\mathcal{G}_{-\theta}=\mathcal{G}_{\theta}^T$ alejándonos de los casos infinitesimales?`
  <!-- AI: Atiende a la última pregutna hecha -->

## Respuestas a las preguntas

Las referencias a los anexos son a «El teorema de Noether: anexos (versión 2)», en este mismo directorio.

### 1. Cómo hacer más formal el razonamiento de primer orden

La clave es que $\mathcal{G}_\theta$ no es una matriz distinta para cada $\theta$: es $\theta$ por una sola matriz.

- **El generador.** Supongamos que $\theta \mapsto \mathcal{R}_\theta$ es derivable. Con la ley de grupo basta que sea continua: es el teorema de los subgrupos de un parámetro (Hall, 2015, cap. 2), que da además $\mathcal{R}_\theta = e^{\theta \cdot \mathcal{G}}$. Se define

  $$
  \begin{aligned}
  \mathcal{G} := \left.\dfrac{d\mathcal{R}_\theta}{d\theta}\right|_{\theta = 0}.
  \end{aligned}
  $$

- **Lo que se multiplica por $\varepsilon$ es la derivada.** El desarrollo de Taylor de la función matricial $\varepsilon \mapsto \mathcal{R}_{\varepsilon \cdot \theta}$ en $\varepsilon = 0$ es $\mathcal{R}_{\varepsilon \cdot \theta} = \mathcal{I} + \varepsilon \cdot \theta \cdot \mathcal{G} + r(\varepsilon)$, con $\lVert r(\varepsilon) \rVert \leq C \cdot \varepsilon^2$ para una constante $C$. Es decir, $\mathcal{G}_\theta = \theta \cdot \mathcal{G}$ y $\mathcal{G}_{\varepsilon \cdot \theta} = \varepsilon \cdot \mathcal{G}_\theta$. $\varepsilon \cdot \mathcal{R}_\theta$ y $\mathcal{R}_{\varepsilon \cdot \theta}$ son, efectivamente, matrices distintas, pero $\varepsilon \cdot \mathcal{R}_\theta$ no aparece en ningún momento.
- **El producto, con cotas.** Para dos rotaciones pequeñas, $\mathcal{R}_{\varepsilon \cdot \alpha} = \mathcal{I} + \varepsilon \cdot A + r_1$ y $\mathcal{R}_{\varepsilon \cdot \beta} = \mathcal{I} + \varepsilon \cdot B + r_2$, con $A = \mathcal{G}_\alpha$, $B = \mathcal{G}_\beta$ y $\lVert r_1 \rVert, \lVert r_2 \rVert \leq C \cdot \varepsilon^2$. Multiplicando:

  $$
  \begin{aligned}
  (\mathcal{I} + \varepsilon \cdot A + r_1) \cdot (\mathcal{I} + \varepsilon \cdot B + r_2) &= \mathcal{I} + \varepsilon \cdot (A + B) + E, \\
  E &:= \varepsilon^2 \cdot A \cdot B + (\mathcal{I} + \varepsilon \cdot A) \cdot r_2 + r_1 \cdot (\mathcal{I} + \varepsilon \cdot B) + r_1 \cdot r_2.
  \end{aligned}
  $$

  Por la desigualdad $\lVert X \cdot Y \rVert \leq \lVert X \rVert \cdot \lVert Y \rVert$ (anexos, apartado 2.1), $\lVert E \rVert \leq C' \cdot \varepsilon^2$ para otra constante $C'$. Eso es exactamente lo que significa «mód $\varepsilon^2$».
- **La versión algebraica.** Se trabaja con matrices cuyas entradas son **números duales**: polinomios en $\varepsilon$ en los que se descartan las potencias $\varepsilon^2$ y superiores, es decir, los elementos del anillo $\mathbb{R}[\varepsilon]/(\varepsilon^2)$, en el que $\varepsilon^2 = 0$ literalmente. Ahí el cálculo de primer orden es exacto.
- **Con el mismo eje no hace falta aproximar.** La ley de grupo da exactamente $\mathcal{R}_{\varepsilon \cdot \alpha} \cdot \mathcal{R}_{\varepsilon \cdot \beta} = \mathcal{R}_{\varepsilon \cdot (\alpha + \beta)}$. A primer orden, esto dice $\mathcal{G}_{\alpha+\beta} = \mathcal{G}_\alpha + \mathcal{G}_\beta$, y con la derivabilidad se obtiene $\mathcal{G}_\theta = \theta \cdot \mathcal{G}$. El primer orden solo dice algo nuevo con ejes distintos: allí suma los dos generadores, y la diferencia entre los dos órdenes aparece a segundo orden, con el conmutador (anexos, apartados 1.5 y 2.7).

### 2. Por qué $\mathcal{G}$ es antisimétrica y tiene traza nula

- **Antisimetría.** Derivando $\mathcal{R}_\theta^T \cdot \mathcal{R}_\theta = \mathcal{I}$ respecto de $\theta$ en $\theta = 0$, con la regla del producto y $\mathcal{R}_0 = \mathcal{I}$, queda $\mathcal{G}^T + \mathcal{G} = 0$. Con el desarrollo se llega a lo mismo: $\mathcal{I} + \varepsilon \cdot \theta \cdot (\mathcal{G}^T + \mathcal{G}) + O(\varepsilon^2) = \mathcal{I}$ para todo $\varepsilon$ pequeño, y dividiendo por $\varepsilon$ y haciendo $\varepsilon \to 0$, $\mathcal{G}^T + \mathcal{G} = 0$. También son antisimétricas, por tanto, las $\mathcal{G}_\theta = \theta \cdot \mathcal{G}$.
- **Traza nula.** Si $g_{ij}$ son los elementos de $\mathcal{G}$, la antisimetría da $g_{ii} = -g_{ii}$ en la diagonal, así que $g_{ii} = 0$ y $\operatorname{tr} \mathcal{G} = 0$. Otra vía, con el determinante: $\det(\mathcal{I} + \varepsilon \cdot \mathcal{G} + O(\varepsilon^2)) = 1 + \varepsilon \cdot \operatorname{tr} \mathcal{G} + O(\varepsilon^2)$, y como $\det \mathcal{R}_\varepsilon = 1$, $\operatorname{tr} \mathcal{G} = 0$. Es la fórmula $\det e^M = e^{\operatorname{tr} M}$ (anexos, apartado 2.2).
- **En $\mathbb{R}^3$, la forma del generador.** Como $\mathcal{R}_\theta \cdot \hat{u} = \hat{u}$ para todo $\theta$, derivando sale $\mathcal{G} \cdot \hat{u} = \vec{0}$. Toda matriz antisimétrica $3 \times 3$ actúa como $\vec{v} \mapsto \vec{\omega} \times \vec{v}$ para algún vector $\vec{\omega}$, y $\vec{\omega} \times \hat{u} = \vec{0}$ obliga a que $\vec{\omega}$ sea paralelo a $\hat{u}$. Con $\theta$ como ángulo de giro, $\mathcal{G} \cdot \vec{v} = \hat{u} \times \vec{v}$.

### 3. $\mathcal{R}_{-\theta} = \mathcal{R}_\theta^T$ lejos de lo infinitesimal

No hace falta ningún argumento infinitesimal: la igualdad es exacta para todo $\theta$.

- **Con la ley de grupo y la ortogonalidad.** $\mathcal{R}_\theta \cdot \mathcal{R}_{-\theta} = \mathcal{R}_0 = \mathcal{I}$, así que $\mathcal{R}_{-\theta} = \mathcal{R}_\theta^{-1}$, y por la ortogonalidad, $\mathcal{R}_\theta^{-1} = \mathcal{R}_\theta^T$.
- **Con la exponencial.** $(e^{\theta \cdot \mathcal{G}})^T = e^{\theta \cdot \mathcal{G}^T} = e^{-\theta \cdot \mathcal{G}} = \mathcal{R}_{-\theta}$ (anexos, apartados 2.2 y 2.4).
- **La relación entre las dos versiones.** $\mathcal{G}_{-\theta} = \mathcal{G}_\theta^T$ es la versión infinitesimal de la anterior: $-\theta \cdot \mathcal{G} = \theta \cdot \mathcal{G}^T$, que es la antisimetría de la respuesta 2.

### Referencia

* Hall, B. C. (2015). *Lie groups, Lie algebras, and representations: An elementary introduction* (2.ª ed.). Springer.
