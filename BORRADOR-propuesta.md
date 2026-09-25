# Propuesta de redacción: contexto histórico de «Las simetrías en la física»

Revisión de `BORRADOR.md` (25-09-2026). El borrador original no se ha modificado. Esta es una propuesta para el capítulo «Contexto y estado de la cuestión» del modelo UNIR (REGLAS.md, sección 8.3). Las citas usan la sintaxis de Pandoc, y sus referencias están al final, en formato BibTeX, listas para `referencias.bib`. Los datos bibliográficos se han comprobado en Crossref y EUDML.

---

## Contexto histórico: de la geometría de las transformaciones al teorema de Noether

### Klein, Lie y el programa de Erlangen

Felix Klein (1849–1925) y Sophus Lie (1842–1899) se conocieron en Berlín en el invierno de 1869 a 1870 y pasaron juntos en París la primavera de 1870. De esa colaboración salió un trabajo conjunto sobre las curvas planas que se transforman en sí mismas bajo un sistema de transformaciones lineales que conmutan entre sí [@kleinlie1871]. En él aparece la idea que ambos desarrollarían después por separado: estudiar un objeto geométrico a través de las transformaciones que lo dejan invariante.

En 1872, al incorporarse como catedrático a la Universidad de Erlangen, Klein publicó el folleto *Vergleichende Betrachtungen über neuere geometrische Forschungen* («Consideraciones comparativas sobre las investigaciones geométricas recientes»), conocido después como programa de Erlangen [@klein1893]. Su tesis es que cada geometría queda caracterizada por un grupo de transformaciones y consiste en el estudio de las propiedades que ese grupo deja invariantes. Las geometrías euclídea, afín y proyectiva corresponden a grupos cada vez mayores, y cuanto mayor es el grupo, menos propiedades se conservan. De este modo, las geometrías conocidas quedaban ordenadas, dentro de la geometría proyectiva, mediante la teoría de grupos. Su influencia inmediata fue limitada: el texto circuló poco hasta que se reeditó y tradujo a partir de 1890 [@hawkins1984].

Lie, por su parte, se dedicó a los grupos continuos de transformaciones, con el propósito de hacer para las ecuaciones diferenciales lo que la teoría de Galois había hecho para las ecuaciones algebraicas. Su exposición sistemática, escrita con Friedrich Engel, se publicó en tres volúmenes entre 1888 y 1893 [@lieengel1893; @hawkins2000]. Estos grupos se llaman hoy grupos de Lie. La relación entre ambos matemáticos se deterioró a partir de 1892 por disputas de prioridad, y en el prólogo del tercer volumen Lie afirmó que no era discípulo de Klein, ni Klein discípulo suyo.

### La teoría de invariantes

En paralelo se desarrolló la teoría algebraica de invariantes. Estudia las expresiones formadas con los coeficientes de una forma (un polinomio homogéneo) que no cambian, o que solo quedan multiplicadas por una potencia del determinante, cuando se efectúa un cambio lineal de variables. En Gran Bretaña la iniciaron Arthur Cayley y James Joseph Sylvester en la década de 1840, y el irlandés George Salmon la sistematizó en sus libros de texto [@parshall2006]. Sylvester llamó «trinidad invariante» al grupo formado por Cayley, el francés Charles Hermite y él mismo [@parshall2024].

En Alemania, la escuela principal fue la de Alfred Clebsch (1833–1872) y Paul Gordan (1837–1912), que desarrollaron el método simbólico para el cálculo de invariantes. Gordan y Max Noether (1844–1921) enseñaron en Erlangen, por lo que a veces se habla de una escuela de invariantes de Erlangen, que no debe confundirse con el programa de Erlangen de Klein. El problema central de la teoría era de finitud: demostrar que todos los invariantes de una forma se obtienen como polinomios de un número finito de ellos. Gordan lo demostró en 1868 para las formas binarias (de dos variables) de cualquier grado, con un método constructivo que exigía calcular explícitamente cada caso [@gordan1868].

David Hilbert (1862–1943) resolvió el problema para cualquier número de variables en 1888, con un argumento de otra naturaleza que publicó en 1890 [@hilbert1890]. Su teorema de la base establece que todo ideal de un anillo de polinomios en un número finito de variables sobre un cuerpo está generado por un número finito de elementos. De él se deduce que existe un sistema finito de invariantes, pero no se obtiene un método para construirlo. A esta demostración de existencia se atribuye la frase de Gordan «esto no es matemática, es teología». En 1893 Hilbert publicó una demostración más constructiva [@hilbert1893]. Resuelta la cuestión de la finitud con carácter general, el interés por los cálculos explícitos de invariantes decayó durante décadas.

### Emmy Noether y las leyes de conservación

Emmy Noether (1882–1935), hija de Max Noether, se doctoró en Erlangen en 1907 bajo la dirección de Gordan. Su tesis calcula, por el método constructivo, un sistema completo de 331 covariantes de la forma ternaria de cuarto grado [@noether1908]. Más adelante adoptó los métodos abstractos de Hilbert.

En 1915, Hilbert y Klein la invitaron a Gotinga. Ese mismo año Hilbert presentó una formulación variacional de la teoría de la gravitación [@hilbert1915], contemporánea de las ecuaciones de campo de la relatividad general de Albert Einstein. En esa teoría, la conservación de la energía no toma la forma habitual de una ley de conservación, y Hilbert sostenía que en ella no hay teoremas de energía «propios». El conocimiento de Noether de la teoría de invariantes era el adecuado para estudiar esta cuestión.

El resultado fue el artículo *Invariante Variationsprobleme*, que Klein presentó en la sesión del 26 de julio de 1918 de la Sociedad de Ciencias de Gotinga [@noether1918; traducción al inglés en @tavel1971]. Contiene dos teoremas sobre los sistemas cuyas ecuaciones se obtienen de un principio variacional:

* El primero establece que, si la acción es invariante bajo un grupo continuo de transformaciones que depende de un número finito $\rho$ de parámetros (un grupo de Lie), existen $\rho$ cantidades conservadas. Así, la invariancia bajo traslaciones en el tiempo implica la conservación de la energía; bajo traslaciones en el espacio, la del momento lineal, y bajo rotaciones, la del momento angular.
* El segundo trata los grupos que dependen de funciones arbitrarias, como las transformaciones generales de coordenadas de la relatividad general. En ese caso la invariancia no produce cantidades conservadas independientes, sino identidades entre las ecuaciones del movimiento. Esto explica la forma «impropia» de la conservación de la energía que había señalado Hilbert [@kosmann2011].

El trabajo de Noether reunió así las dos líneas anteriores: los grupos continuos de Lie y los métodos de la teoría de invariantes.

---

## Referencias propuestas (BibTeX)

```bibtex
@article{kleinlie1871,
  author  = {Klein, Felix and Lie, Sophus},
  title   = {Ueber diejenigen ebenen {Curven}, welche durch ein geschlossenes {System} von einfach unendlich vielen vertauschbaren linearen {Transformationen} in sich übergehen},
  journal = {Mathematische Annalen},
  volume  = {4},
  number  = {1},
  pages   = {50--84},
  year    = {1871},
  doi     = {10.1007/BF01443297}
}

@article{klein1893,
  author   = {Klein, Felix},
  title    = {Vergleichende {Betrachtungen} über neuere geometrische {Forschungen}},
  journal  = {Mathematische Annalen},
  volume   = {43},
  number   = {1},
  pages    = {63--100},
  year     = {1893},
  origdate = {1872},
  doi      = {10.1007/BF01446615}
}

@book{lieengel1893,
  author    = {Lie, Sophus and Engel, Friedrich},
  title     = {Theorie der {Transformationsgruppen}},
  volumes   = {3},
  publisher = {B. G. Teubner},
  date      = {1888/1893}
}

@article{gordan1868,
  author  = {Gordan, Paul},
  title   = {Beweis, dass jede {Covariante} und {Invariante} einer binären {Form} eine ganze {Function} mit numerischen {Coefficienten} einer endlichen {Anzahl} solcher {Formen} ist},
  journal = {Journal für die reine und angewandte Mathematik},
  volume  = {69},
  pages   = {323--354},
  year    = {1868},
  doi     = {10.1515/crll.1868.69.323}
}

@article{hilbert1890,
  author  = {Hilbert, David},
  title   = {Ueber die {Theorie} der algebraischen {Formen}},
  journal = {Mathematische Annalen},
  volume  = {36},
  number  = {4},
  pages   = {473--534},
  year    = {1890},
  doi     = {10.1007/BF01208503}
}

@article{hilbert1893,
  author  = {Hilbert, David},
  title   = {Ueber die vollen {Invariantensysteme}},
  journal = {Mathematische Annalen},
  volume  = {42},
  number  = {3},
  pages   = {313--373},
  year    = {1893},
  doi     = {10.1007/BF01444162}
}

@article{noether1908,
  author  = {Noether, Emmy},
  title   = {Über die {Bildung} des {Formensystems} der ternären biquadratischen {Form}},
  journal = {Journal für die reine und angewandte Mathematik},
  volume  = {134},
  pages   = {23--90},
  year    = {1908},
  doi     = {10.1515/crll.1908.134.23}
}

@article{hilbert1915,
  author  = {Hilbert, David},
  title   = {Die {Grundlagen} der {Physik} ({Erste} {Mitteilung})},
  journal = {Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse},
  volume  = {1915},
  pages   = {395--408},
  year    = {1915},
  url     = {http://eudml.org/doc/58946}
}

@article{noether1918,
  author  = {Noether, Emmy},
  title   = {Invariante {Variationsprobleme}},
  journal = {Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse},
  volume  = {1918},
  pages   = {235--257},
  year    = {1918},
  url     = {http://eudml.org/doc/59024}
}

@article{tavel1971,
  author     = {Noether, Emmy},
  translator = {Tavel, M. A.},
  title      = {Invariant variation problems},
  journal    = {Transport Theory and Statistical Physics},
  volume     = {1},
  number     = {3},
  pages      = {186--207},
  year       = {1971},
  doi        = {10.1080/00411457108231446}
}

@article{hawkins1984,
  author  = {Hawkins, Thomas},
  title   = {The {Erlanger Programm} of {Felix Klein}: Reflections on its place in the history of mathematics},
  journal = {Historia Mathematica},
  volume  = {11},
  number  = {4},
  pages   = {442--470},
  year    = {1984},
  doi     = {10.1016/0315-0860(84)90028-4}
}

@book{hawkins2000,
  author    = {Hawkins, Thomas},
  title     = {Emergence of the theory of {Lie} groups: An essay in the history of mathematics 1869--1926},
  publisher = {Springer},
  year      = {2000},
  doi       = {10.1007/978-1-4612-1202-7}
}

@article{parshall2006,
  author  = {Parshall, Karen Hunger},
  title   = {The {British} development of the theory of invariants (1841--1895)},
  journal = {BSHM Bulletin: Journal of the British Society for the History of Mathematics},
  volume  = {21},
  number  = {3},
  pages   = {186--199},
  year    = {2006},
  doi     = {10.1080/17498430600964417}
}

@article{parshall2024,
  author  = {Parshall, Karen Hunger},
  title   = {A convergence of paths: {Cayley}, {Hermite}, {Sylvester}, and early invariant theory},
  journal = {Revue d'histoire des mathématiques},
  volume  = {30},
  pages   = {233--260},
  year    = {2024},
  doi     = {10.24033/rhm.316}
}

@book{kosmann2011,
  author    = {Kosmann-Schwarzbach, Yvette},
  title     = {The {Noether} theorems: Invariance and conservation laws in the twentieth century},
  publisher = {Springer},
  year      = {2011},
  doi       = {10.1007/978-0-387-87868-3}
}
```
