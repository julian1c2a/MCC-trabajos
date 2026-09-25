---
title: "Las simetrías en la física"
author: "Julián Calderón Almendros"
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
indice-tablas: false
---

<!--
Estructura obligatoria del modelo UNIR (material/Plantilla_LATEX_FCC_MUCC_UNIR/plantilla.tex).
Los capítulos no se numeran a mano: LaTeX los numera. Las citas se escriben [@clave] o @clave
y las referencias van en referencias.bib (APA 7). REGLAS.md, sección 8.
-->

# Introducción

<!--
Resumen esquemático de cada parte del trabajo, con abundantes referencias a los trabajos
originales (no a libros de texto que los mencionan). Tres apartados, a modo de guía:
motivación y justificación del tema, planteamiento del trabajo y estructura del trabajo.
-->

## Motivación y justificación

## Planteamiento del trabajo

## Estructura del trabajo

# Contexto y estado de la cuestión

<!-- Qué se ha hecho en el ámbito del trabajo, con la bibliografía que lo respalda. -->

## Contexto histórico

Entre finales de la década de 1860 y comienzos de la de 1870, se desarrolló un movimiento matemático trascendental protagonizado por **Felix Klein** (1849–1925) y **Sophus Lie** (1842–1899). Ambos coincidieron en Berlín en el invierno de 1869 a 1870 y en París en la primavera de 1870, y de esa colaboración salió un trabajo conjunto sobre las curvas planas que quedan invariantes bajo un sistema de transformaciones lineales [@kleinlie1871]. De ahí procede la idea de que la geometría debía definirse a través de las propiedades y magnitudes que permanecen invariantes bajo un determinado grupo de transformaciones. Esta visión la formuló Klein en solitario en 1872, en el escrito programático (*Programmschrift*) que, según la costumbre de las universidades alemanas, presentó a la facultad al incorporarse como catedrático a la Universidad de Erlangen, y que se conoce como el Programa de Erlangen [@klein1893]. No debe confundirse con la lección inaugural que Klein pronunció en esa misma ocasión, con la que a menudo se identifica [@rowe2025]. El programa ordenó las distintas geometrías de la época (euclídea, afín, proyectiva...) mediante sus grupos de transformaciones: cada geometría estudia lo que deja invariante su grupo, y cuanto mayor es el grupo, menos propiedades se conservan. Su influencia inmediata fue escasa; se difundió a partir de 1890, con sus reediciones y traducciones: al italiano en 1890, por Gino Fano, y al inglés en 1893, por Mellen W. Haskell [@kleinhaskell1893]. Rowe [-@rowe2025] ha publicado una nueva traducción inglesa, con comentario y análisis histórico. Hay que decir que Klein y Lie, a pesar de tener temperamentos muy diferentes, colaboraron estrechamente durante su juventud, desarrollando ideas conjuntas sobre curvas y transformaciones geométricas. Sin embargo, con los años sus caminos se bifurcaron: mientras Klein se orientó hacia una visión global, institucional y unificadora de las matemáticas, Lie se concentró en la profunda especialización analítica que dio origen a la teoría de los grupos continuos de transformaciones (hoy llamados grupos de Lie), con la que buscaba hacer para las ecuaciones diferenciales lo que la teoría de Galois había hecho para las ecuaciones algebraicas. La expuso con Friedrich Engel en *Theorie der Transformationsgruppen*, publicada en tres volúmenes entre 1888 y 1893 [@lieengel1893]. La relación entre ambos se rompió en 1892–1893 por disputas de prioridad: en el prólogo del tercer volumen, Lie afirmó públicamente que no era discípulo de Klein, lo que terminó por distanciar profesional y personalmente a ambos genios [@guijarro2007].

Esta idea de invariancia llenaba el ambiente matemático, y en paralelo se desarrolló la teoría algebraica de invariantes: el estudio de las expresiones formadas con los coeficientes de una forma (un polinomio homogéneo) que no cambian, o que solo quedan multiplicadas por una potencia del determinante, al hacer un cambio lineal de variables. En Gran Bretaña la iniciaron Arthur Cayley [-@cayley1845] y James Joseph Sylvester en la década de 1840, y el irlandés George Salmon [-@salmon1859] la sistematizó en sus libros de texto. La llamada «trinidad invariante» no incluye a Salmon: Sylvester dio ese nombre al grupo que formaba con Cayley y el francés Charles Hermite [@parshall2024]. En Alemania, la escuela principal, paralela y coetánea a la británica, fue la de **Alfred Clebsch** (1833–1872) y **Paul Gordan** (1837–1912), que desarrollaron el método simbólico para calcular invariantes [@clebsch1872]. Gordan y **Max Noether** (1844–1921) enseñaron en Erlangen, por lo que a veces se habla de una escuela de invariantes de Erlangen, que no debe confundirse con el Programa de Erlangen de Klein (Clebsch, por su parte, nunca estuvo en Erlangen: trabajó en Karlsruhe, Giessen y Gotinga). El problema central de la teoría era de finitud: demostrar que todos los invariantes de una forma se obtienen como polinomios de un número finito de ellos. El enfoque tradicional era un trabajo minucioso y descomunal de cálculo, en el que cada caso concreto (formas de un grado y un número de variables dados) debía estudiarse por separado, calculando explícitamente sus invariantes; así demostró Gordan [-@gordan1868] la finitud para las formas binarias (de dos variables) de cualquier grado. Con un enfoque mucho más novedoso, **David Hilbert** (1862–1943) resolvió el problema para cualquier número de variables con su **Teorema de la Base** (1888, publicado en 1890): todo ideal de un anillo de polinomios en un número finito de variables sobre un cuerpo es finitamente generado [@hilbert1890]. Pero su demostración era de existencia: probaba que hay una base finita de invariantes sin dar un método para construirla, y por eso Gordan llegó a calificarla de teología. Tras estudiarla, según Almira Picazo y Sabina de Lis [-@almira2007, pp. 44–45], exclamó: «¡Esto no son matemáticas: es teología!» [véanse también @derksen2002, p. 49; @weyl1944]. En 1893 Hilbert publicó una demostración más constructiva [@hilbert1893]. Gordan acabó cambiando de opinión: afirmó haberse convencido de que «incluso la teología tiene sus méritos» [@klein1979, p. 311] y en 1899 publicó una versión simplificada de la demostración de Hilbert [@gordan1899]. El resultado no hizo innecesario el cálculo explícito de invariantes, pero, al resolver con carácter general el problema de la finitud, prácticamente cerró la teoría de invariantes y le quitó durante un tiempo su interés a este campo matemático.

<!-- Pendiente: Almira y Sabina (2007) narran el episodio en las pp. 40–52; como la frase de Gordan es una cita textual en español, APA exige la página exacta en que aparece: [@almira2007, p. N]. Las frases que traducimos del inglés (Derksen y Kemper; Klein) cuentan en APA como paráfrasis, y ya llevan su página. Estado: hecho (la cita empieza al final de la p. 44 y termina al comienzo de la p. 45; se cita literalmente). -->

<!-- Pendiente: (para la IA) Falta describir el contexto en que Einstein se dio cuenta que en el marco de la teoría de la relatividad general parecía no conservarse la energía en un entorno local y aislado (cerrado). Estado: hecho. -->

La fusión definitiva entre esta potente álgebra de invariantes y la geometría de las transformaciones no tardaría en revolucionar la física. A principios del siglo XX, la física teórica se encontraba en plena ebullición con el desarrollo de la Teoría de la Relatividad General de Albert Einstein. Fue en ese escenario donde las simetrías continuas —aquellas transformaciones suaves y fluidas descritas originalmente por los grupos de Lie, como las rotaciones en el espacio o el avance del tiempo— revelaron su verdadero poder.

La conservación de la energía y del momento acompañó a Einstein durante toda la búsqueda de las ecuaciones del campo gravitatorio. En 1912 y 1913, en Zúrich, Einstein y Marcel Grossmann estudiaron ecuaciones construidas a partir del tensor de Ricci, pero las descartaron porque creyeron que no eran compatibles con esas leyes de conservación ni con el límite newtoniano. Publicaron en su lugar la teoría del *Entwurf* («borrador»), cuyas ecuaciones no eran generalmente covariantes, es decir, no conservaban su forma bajo cualquier cambio de coordenadas [@einsteingrossmann1913]. En noviembre de 1915 Einstein volvió a unas ecuaciones generalmente covariantes [@einstein1915], y el 28 de noviembre escribió a Arnold Sommerfeld que el error había sido precisamente creer que las leyes de conservación no se cumplían [@einstein1998, documento 153; @pitts2016].

En la nueva teoría, la conservación toma una forma distinta de la habitual. Si $T^{\mu\nu}$ es el tensor de energía-momento de la materia, las ecuaciones de campo implican que su divergencia covariante es nula:

$$
\begin{aligned}
\nabla_\mu T^{\mu\nu} = \partial_\mu T^{\mu\nu} + \Gamma^{\mu}_{\mu\lambda} \cdot T^{\lambda\nu} + \Gamma^{\nu}_{\mu\lambda} \cdot T^{\mu\lambda} = 0.
\end{aligned}
$$

Aquí $\partial_\mu$ es la derivada parcial respecto de la coordenada $x^\mu$, se suma sobre los índices repetidos y los símbolos de Christoffel $\Gamma^{\alpha}_{\beta\gamma}$ describen el campo gravitatorio. Los términos con $\Gamma$ representan el intercambio de energía y momento entre la materia y el campo, de modo que la energía de la materia sola no se conserva. En su exposición de 1916, Einstein introdujo unas cantidades $t_\mu^{\ \sigma}$ para la energía y el momento del propio campo gravitatorio, con las que la suma cumple una ley de conservación ordinaria, en coordenadas con $\sqrt{-g} = 1$ [@einstein1916]:

$$
\begin{aligned}
\partial_\sigma \left( T_\mu^{\ \sigma} + t_\mu^{\ \sigma} \right) = 0.
\end{aligned}
$$

Pero $t_\mu^{\ \sigma}$ no es un tensor, sino un pseudotensor: sus valores dependen del sistema de coordenadas y, de acuerdo con el principio de equivalencia, pueden anularse en cualquier punto eligiendo las coordenadas adecuadas. Por eso la energía del campo gravitatorio no puede localizarse, es decir, asignarse a cada punto del espacio.

En Gotinga, David Hilbert, que en noviembre de 1915 había presentado una formulación variacional de la gravitación, contemporánea de las ecuaciones de campo de Einstein [@hilbert1915], llegó a la conclusión de que en la nueva teoría no había teoremas de energía «propios»: la energía no parecía conservarse de la manera local y matemática tradicional [@klein1918a]. Para estudiar este problema, David Hilbert y Felix Klein invitaron a Gotinga en 1915 a la mayor experta en álgebra de invariantes de la época: Emmy Noether (1882–1935), hija de Max Noether y discípula directa de Paul Gordan. Noether había hecho en 1907 su tesis doctoral sobre invariantes calculados a mano, un trabajo ingente: un sistema completo de 331 covariantes de la forma ternaria de cuarto grado [@noether1908]. Trabajó en el problema de la energía entre 1915 y 1918, y el resultado fue el artículo *Invariante Variationsprobleme*, que Klein presentó el 26 de julio de 1918 en la Sociedad de Ciencias de Gotinga [@noether1918]. El artículo contiene dos teoremas. El primero es el que hoy se conoce como Teorema de Noether, una de las piedras angulares de la física moderna: en todo sistema cuyas ecuaciones se obtienen de un principio variacional, a cada simetría continua de la acción (un grupo de Lie de transformaciones) le corresponde una ley de conservación. Así, la invariancia bajo traslaciones en el tiempo implica la conservación de la energía; bajo traslaciones en el espacio, la del momento lineal, y bajo rotaciones, la del momento angular. El segundo teorema trata las simetrías que dependen de funciones arbitrarias, como los cambios generales de coordenadas de la relatividad general: en ese caso no aparecen cantidades conservadas independientes, sino identidades entre las ecuaciones del movimiento. Es este segundo teorema el que explica la forma peculiar que toma la conservación de la energía en la relatividad general, la que había señalado Hilbert. El trabajo de Noether reunió así las dos líneas anteriores: los grupos continuos de Lie y los métodos de la teoría de invariantes.

Mientras tanto, la naturaleza de la energía gravitatoria se discutía abiertamente. Schrödinger [-@schrodinger1918] mostró que, en coordenadas adecuadas, todas las componentes del pseudotensor de Einstein se anulan fuera de una masa con simetría esférica, y Bauer [-@bauer1918] mostró que no se anulan en el espacio-tiempo plano si se usan coordenadas no cartesianas. Einstein respondió en mayo de 1918 con *Der Energiesatz in der allgemeinen Relativitätstheorie* [@einstein1918]. Para un sistema cerrado, con la materia en una región finita y el espacio-tiempo plano lejos de ella, las integrales en todo el espacio de las componentes temporales de $T + t$ no varían con el tiempo ni dependen del sistema de coordenadas, siempre que este se reduzca lejos del sistema al de la relatividad especial. La energía total de un sistema aislado está, por tanto, bien definida y se conserva, aunque no pueda asignarse a cada punto. En Gotinga, Klein analizó la forma diferencial y la forma integral de estas leyes de conservación, con la ayuda de Noether [@klein1918b; @klein1918c; @rowe2019].

Einstein, que seguía estos trabajos desde Berlín, dejó constancia de su aprecio por ellos en dos cartas [@einstein1998; @tollmien2018]. El 24 de mayo de 1918, al recibir un artículo anterior de Noether sobre la construcción de invariantes [@noether1918a], escribió a Hilbert: «me impresiona que se puedan abarcar estas cosas desde un punto de vista tan general» [@einstein1998, documento 548]. El 27 de diciembre de 1918, al recibir *Invariante Variationsprobleme*, escribió a Klein que volvía a sentir como una gran injusticia que a Noether se le negara la *venia legendi*, el permiso para enseñar en la universidad, y propuso dar un paso enérgico ante el ministerio [@einstein1998, documento 677]. Noether obtuvo la habilitación en 1919.

# Objetivos

<!-- Objetivos del trabajo, esquematizados y ordenados. -->

# Desarrollo del trabajo

<!-- Desarrollo, contrastando las ideas de varios autores y, si es posible, con las propias. -->

# Conclusiones

<!-- Claras; si es posible, un párrafo por idea con un pequeño título ilustrativo. -->

# Bibliografía {-}

::: {#refs}
:::

\appendix

# Apéndices

<!-- Desarrollos largos que no encajan en el cuerpo. Si no hay apéndices, se borran esta sección y la línea \appendix. -->
