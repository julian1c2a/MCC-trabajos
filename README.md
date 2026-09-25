# Trabajos del curso (privado)

Trabajos del Máster en Computación Cuántica. Esta carpeta y `material/` están en el `.gitignore` del repositorio público. Cada una es un repositorio privado propio (`julian1c2a/MCC-trabajos` y `julian1c2a/MCC-material`) del que GUARDA_y_SUBE hace copia de seguridad.

Reglas completas: sección 8 de [REGLAS.md](../REGLAS.md). En resumen, por orden de prioridad:

1. **Modelo UNIR** (`material/Plantilla_LATEX_FCC_MUCC_UNIR/`), obligatorio y sin modificar.
2. **APA 7.ª edición**, con rigor (`_plantilla/apa-es.csl`).
3. **Reglas del proyecto** en todo lo demás (redacción, fórmulas con `\cdot`, `\dfrac`, `aligned`; compilación sin errores ni advertencias).

Contenido:

- `_plantilla/`: `unir.latex` (plantilla de Pandoc que reproduce `plantilla.tex`), `apa.csl` (APA 7 oficial de CSL), `apa-es.csl` (adaptación española que se usa), `trabajo-modelo.md` (esqueleto) y `meta-json.tpl` (auxiliar de las comprobaciones).
- `ejemplo/`: trabajo de ejemplo completo que pasa todas las comprobaciones.
- `<nombre>/`: cada trabajo, con `<nombre>.md`, `referencias.bib` y las salidas `<nombre>.tex` y `<nombre>.pdf`.

Comandos:

- `NUEVO_TRABAJO nombre "título" [profesor]`: `pwsh scripts/nuevo-trabajo.ps1 -Nombre <nombre> -Titulo "<título>"`.
- `SINCRONIZA_TRABAJO [nombre]`: `pwsh scripts/sincroniza-trabajo.ps1 [-Name <nombre>]`.
