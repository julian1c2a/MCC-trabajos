---
title: "Ejemplo de trabajo con el modelo UNIR"
author: "Julián Calderón Almendros"
date: "25 de septiembre de 2026"
profesor: "Rodrigo Gil-Merino y Rubio"
lang: es-ES
bibliography: referencias.bib
resumen: |
  Documento de ejemplo que muestra cómo se escribe un trabajo del máster en Markdown con el
  modelo LaTeX de UNIR y referencias en formato APA 7. Incluye citas narrativas y entre
  paréntesis, una fórmula display y un apéndice. Sirve de referencia para los trabajos reales.
palabras-clave: [modelo UNIR, formato APA, Markdown, LaTeX]
abstract: |
  Sample document showing how a master's assignment is written in Markdown with the UNIR
  LaTeX template and APA 7 references. It includes narrative and parenthetical citations,
  a display formula and an appendix. It serves as a reference for real assignments.
keywords: [UNIR template, APA style, Markdown, LaTeX]
---

# Introducción

## Motivación y justificación

La mecánica ondulatoria de @schrodinger1926 describe el estado de un sistema mediante una función de onda que obedece una ecuación de autovalores. El debate sobre la completitud de esa descripción [@epr1935] está en el origen de la información cuántica moderna [@nielsen2010].

## Planteamiento del trabajo

La ecuación de Schrödinger independiente del tiempo para una partícula de masa $m$ en un potencial $V(x)$ es

$$
\begin{aligned}
-\dfrac{\hbar^2}{2 \cdot m} \cdot \dfrac{d^2 \psi}{dx^2} + V(x) \cdot \psi(x) = E \cdot \psi(x).
\end{aligned}
$$

## Estructura del trabajo

El capítulo siguiente resume el contexto; después se fijan los objetivos, se desarrolla el trabajo y se exponen las conclusiones.

# Contexto y estado de la cuestión

El documento se compone con \LaTeX{} [@lamport1994].

# Objetivos

1. Mostrar la estructura del modelo.
2. Comprobar que las citas y la bibliografía siguen APA 7.

# Desarrollo del trabajo

Cuando se cita varias veces la misma obra con tres o más autores, APA abrevia con «et al.» desde la primera cita [@epr1935, p. 778].

# Conclusiones

La estructura del modelo y el formato APA se generan desde una única fuente en Markdown.

# Bibliografía {-}

::: {#refs}
:::

\appendix

# Apéndices

Desarrollos auxiliares que no encajan en el cuerpo del trabajo.
