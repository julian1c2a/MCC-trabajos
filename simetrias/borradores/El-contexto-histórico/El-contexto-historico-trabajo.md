# El contexto histórico (versión para el trabajo)

<!--
Versión del contexto histórico que entra en el trabajo, en el capítulo «Contexto y estado de la
cuestión». Es el texto de la versión 2 (comunicaciones/salientes/propuesta_contexto_historico_v2.md),
con las citas pasadas a claves de referencias.bib. La versión completa está en
El-contexto-historico.md. Las líneas «Fuente:» se borran al pasar el texto a simetrias.md.
-->

**Extensión:** unas 850 palabras; con la plantilla de UNIR ocupa unas 1,85 páginas de las 3 previstas, incluido el párrafo opcional de Jacobi. **Pendiente:** decidir si se mantiene el párrafo de Jacobi; añadir las páginas de la biografía de Nivola.

## Contexto histórico

> Fuente: El-contexto-historico.md, «De Newton a Hamilton».

Entre los siglos XVII y XIX, la mecánica cambió dos veces de lenguaje, y esos cambios son los que hicieron posible el teorema de Noether. @newton1687 la formuló a partir de las fuerzas: el movimiento de un cuerpo se deduce de las fuerzas que actúan sobre él. Un siglo después, @lagrange1788 la reformuló por completo a partir de la energía cinética y de una función de las fuerzas (la energía potencial), sin recurrir a construcciones geométricas. Sus ecuaciones valen en cualquier sistema de coordenadas, no solo en las cartesianas. En la década de 1830, Hamilton [-@hamilton1834; -@hamilton1835] dio a esta mecánica la forma de un principio variacional. Entre todas las trayectorias posibles con los mismos extremos, el sistema sigue aquella que hace estacionaria la acción: la integral en el tiempo de la diferencia entre la energía cinética y la potencial, lo que hoy llamamos el lagrangiano. Con este lenguaje, decir que una ley física no cambia bajo una transformación (desplazar el sistema, girarlo o retrasar el reloj) pasa a ser una afirmación precisa: la acción no cambia.

> Fuente: El-contexto-historico.md, «Un precedente: Jacobi». Opcional.

[Opcional. Algunas consecuencias de esa idea se conocían caso a caso antes de Noether. Jacobi, en las lecciones de dinámica que dio en Königsberg en 1842 y 1843, publicadas en 1866, relacionó la conservación del momento lineal y del momento angular con la invariancia del sistema bajo traslaciones y rotaciones [@jacobi1866]. Pero no había un resultado general que dijera qué cantidad se conserva para cada simetría.]

> Fuente: El-contexto-historico.md, «La energía en la relatividad general», resumido sin fórmulas ni el pseudotensor; la última frase resume «El debate de 1918 sobre la energía gravitatoria».

El resultado general llegó a raíz de un problema concreto: la conservación de la energía en la relatividad general. Las leyes de conservación guiaron a Einstein durante toda la búsqueda de las ecuaciones del campo gravitatorio. En 1913, con Marcel Grossmann, descartó unas ecuaciones construidas a partir del tensor de Ricci porque creyó que no las cumplían [@einsteingrossmann1913]. En noviembre de 1915 volvió a unas ecuaciones de ese tipo [@einstein1915] y escribió a Arnold Sommerfeld que el error había sido precisamente creer que las leyes de conservación no se cumplían [@einstein1998, documento 153; @pitts2016]. Pero en la nueva teoría la energía se comportaba de forma extraña: la del campo gravitatorio dependía del sistema de coordenadas y no podía asignarse a cada punto del espacio. En Gotinga, David Hilbert, que en noviembre de 1915 había presentado su propia formulación variacional de la gravitación [@hilbert1915], llegó a la conclusión de que en la teoría no había teoremas de energía «propios» [@klein1918a]. Para estudiar el problema, Hilbert y Felix Klein invitaron a Gotinga ese mismo año a Emmy Noether (1882–1935), la mayor experta de la época en teoría de invariantes, en la que se había doctorado en 1907 [@noether1908]. Einstein, por su parte, mostró en 1918 que la energía total de un sistema aislado sí está bien definida y se conserva, aunque no pueda repartirse punto a punto [@einstein1918].

> Fuente: El-contexto-historico.md, «Emmy Noether y sus dos teoremas», sin la tesis de los 331 covariantes ni la relación con los grupos de Lie.

Noether trabajó en el problema entre 1915 y 1918. El resultado fue el artículo *Invariante Variationsprobleme*, que Klein presentó el 26 de julio de 1918 en la Sociedad de Ciencias de Gotinga [@noether1918]. Contiene dos teoremas. El primero, el que hoy se conoce como teorema de Noether, establece que en todo sistema cuyas ecuaciones se obtienen de un principio variacional, a cada simetría continua de la acción le corresponde una cantidad conservada:

- la invariancia bajo traslaciones en el tiempo da la conservación de la energía;
- bajo traslaciones en el espacio, la del momento lineal;
- y bajo rotaciones, la del momento angular.

Relaciones que antes se conocían caso a caso pasaron a ser consecuencias de una sola regla. El segundo teorema trata las simetrías que dependen de funciones arbitrarias, como los cambios generales de coordenadas de la relatividad general. En ese caso no aparecen cantidades conservadas independientes, y eso explica la forma peculiar que toma la conservación de la energía en esa teoría, la que había señalado Hilbert.

> Fuente: El-contexto-historico.md, «Einstein, Noether y la universidad», sin la carta de mayo de 1918.

Einstein siguió estos trabajos desde Berlín. El 27 de diciembre de 1918, al recibir el artículo, escribió a Klein que volvía a sentir como una gran injusticia que a Noether se le negara la *venia legendi*, el permiso para enseñar en la universidad, y propuso dar un paso enérgico ante el ministerio [@einstein1998, documento 677]. La negativa se debía a que Noether era mujer. Las normas de las universidades prusianas no permitían habilitarse a las mujeres: su solicitud de 1915 fue rechazada, y durante esos años impartió cursos anunciados a nombre de Hilbert. Obtuvo la habilitación en 1919, cuando las normas cambiaron tras la caída del Imperio, pero nunca llegó a tener en Gotinga una plaza de catedrática. En 1933, las leyes del régimen nazi la expulsaron de la universidad por ser judía. Emigró a Estados Unidos, donde enseñó en el Bryn Mawr College, y murió allí en 1935 [@blanco2011]. El primer teorema, en su forma más sencilla, es el que se desarrolla en el capítulo 4 de este trabajo.
