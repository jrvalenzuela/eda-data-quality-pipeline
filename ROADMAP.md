# Roadmap de Aprendizaje (Datos + Desarrollo Agéntico)

Cada fase combina un objetivo técnico de **Ciencia de Datos** con una práctica concreta de **Desarrollo Agéntico**.

## Fase 1 — Definición, Dataset e Ingesta
- **Datos:** Elegir un dataset de **Deportes, Educación o Finanzas**, definir 3–5 preguntas de negocio/análisis y cargarlo en `data/raw/`.
- **Agéntico:** Usar `/grill-me` para refinar las preguntas y `/plan` antes de escribir la primera línea de código. Configurar el entorno virtual (`.venv`).

## Fase 2 — Auditoría de Calidad y Contrato de Datos
- **Datos:** Perfilar tipos, nulos, duplicados, cardinalidad de categorías y valores imposibles. Definir un esquema de validación (`pandera`).
- **Agéntico:** Invocar la skill personalizada `data-audit` (`.agents/skills/data-audit/SKILL.md`) y escribir tests con `pytest` para que el agente verifique automáticamente cada regla.

## Fase 3 — Limpieza Trazable y Análisis Exploratorio (EDA)
- **Datos:** Construir funciones puras de limpieza en `src/`, guardar el dataset limpio en `data/processed/` (formato `Parquet`/`CSV`) y calcular estadísticas clave y correlaciones con `pandas`/`DuckDB`.
- **Agéntico:** Practicar TDD: primero escribir tests sobre casos borde (nulos, negativos, formatos rotos) y luego implementar hasta que `pytest` pase en verde.

## Fase 4 — Reporte Visual Interactivo y Verificación
- **Datos:** Generar un reporte HTML interactivo en `reports/` (con gráficos claros y hallazgos accionables que respondan las preguntas de la Fase 1).
- **Agéntico:** Abrir el reporte con el navegador integrado (`/browser`) o como artefacto interactivo para validar visualmente que los gráficos y textos sean claros y sin errores.

## Fase 5 — Extensión Opcional a ML Tabular (Baseline)
- **Datos:** Plantear un problema supervisado sobre el mismo dataset, entrenar un modelo *baseline* con `scikit-learn`, evaluar con validación cruzada y revisar importancia de variables.
- **Agéntico:** Crear una segunda skill personalizada (`leakage-check`) que audite automáticamente que no haya fugas de datos entre `train` y `test`.
