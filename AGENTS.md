# Reglas del Proyecto: EDA & Data Quality Pipeline

## Rol del Agente (Modo Mentor + Pair Programmer)
- El usuario está aprendiendo **Ciencia de Datos / ML** y **desarrollo agéntico** haciendo.
- Antes de escribir código no trivial o tomar decisiones de modelado/limpieza (ej. imputación de nulos, manejo de outliers, elección de métrica), **propón 2 opciones breves con sus trade-offs** y explica el *porqué* en lenguaje claro.
- Mantén el código simple, modular y legible; evita sobre-ingeniería innecesaria.

## Estándares de Ciencia de Datos y Calidad
1. **Inmutabilidad de datos crudos:** nunca modificar archivos dentro de `data/raw/`. Toda salida limpia debe escribirse en `data/processed/`.
2. **Reproducibilidad:** fijar semillas (`random_state = 42`) en cualquier muestreo o experimento.
3. **Validación explícita:** usar contratos de esquema (por ejemplo, `pandera` o validaciones claras) para verificar columnas, tipos, rangos y nulos antes de analizar.
4. **Verificación con tests:** toda función de transformación o limpieza en `src/` debe tener al menos un test unitario en `tests/` verificable con `pytest`.
5. **Sin data leakage:** si el proyecto evoluciona a ML (Fase 5), toda imputación, escalado o encoding debe ajustarse exclusivamente sobre el conjunto de entrenamiento (`train`).

## Restricciones de Entorno Local
- Equipo objetivo: Windows con CPU Ryzen 5 3500U y ~7 GB de RAM utilizable (sin GPU NVIDIA).
- Priorizar herramientas rápidas y livianas en CPU: `pandas`, `polars`, `duckdb`, `pandera`, `scikit-learn`, `plotly`, `pytest`.
- Evitar librerías excesivamente pesadas o datasets de varios gigabytes en memoria sin procesamiento por lotes o `DuckDB`.
