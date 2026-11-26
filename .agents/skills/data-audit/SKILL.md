---
name: data-audit
description: Ejecuta una auditoría estructurada de calidad de datos y perfilado inicial (EDA) sobre un dataset tabular antes de limpiarlo o modelarlo.
---

# Skill: Auditoría Inicial de Calidad de Datos

Cuando el usuario pida auditar un dataset nuevo o evaluar su calidad, sigue exactamente estos pasos:

1. **Inspección estructural:** reporta número de filas, columnas, uso aproximado de memoria, nombres de columnas y tipos inferidos.
2. **Completitud y duplicados:** calcula el porcentaje de valores nulos por columna y detecta filas duplicadas exactas o claves duplicadas.
3. **Validez y anomalías:**
   - En columnas numéricas: mínimo, máximo, mediana, percentiles (P1, P99) y detección de valores imposibles (ej. edades negativas, fechas futuras, ceros sospechosos).
   - En columnas categóricas: cardinalidad, valores más frecuentes, espacios ocultos o inconsistencias de mayúsculas/minúsculas.
4. **Riesgos analíticos:** señala posibles sesgos, desbalance de clases o columnas con posible fuga de información (*target leakage*) si hubiera una variable objetivo.
5. **Propuesta accionable:** entrega una lista priorizada de reglas de validación recomendadas para codificar en `pandera` y `pytest`, explicando cada decisión al usuario antes de modificar nada.
