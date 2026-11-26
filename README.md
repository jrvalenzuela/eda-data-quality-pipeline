# EDA & Data Quality Pipeline (Laboratorio Agéntico)

Proyecto práctico para aprender **Ciencia de Datos / Análisis de Datos** y **desarrollo agéntico** en paralelo usando Antigravity (o Claude Code).

## Objetivo
Construir un pipeline reproducible en Python que tome un dataset real (de **Deportes**, **Educación** o **Finanzas**), valide su calidad de datos automáticamente, realice limpieza trazable y genere un reporte visual interactivo — todo respaldado por tests automatizados (`pytest`) y reglas de agente (`AGENTS.md` + Skills).

## Estructura del proyecto

```text
eda-data-quality-pipeline/
├── AGENTS.md                        # Reglas del proyecto (cargadas automáticamente por el agente)
├── ROADMAP.md                       # Ruta de aprendizaje paso a paso (Fases 1 a 5)
├── pyproject.toml                   # Dependencias y configuración de Python / pytest
├── .agents/
│   └── skills/
│       └── data-audit/SKILL.md      # Primera Skill personalizada de auditoría de datos
├── data/
│   ├── raw/                         # Datos originales (inmutables, nunca se sobreescriben)
│   └── processed/                   # Datos limpios generados por el pipeline
├── src/                             # Código modular del pipeline (ingesta, validación, limpieza, reporte)
├── tests/                           # Tests unitarios y de calidad de datos (pytest)
└── reports/                         # Reportes HTML interactivos generados
```

## Ideas de datasets iniciales (elige uno en tu nueva conversación)

1. **Finanzas:** *Credit Risk Dataset* o *Personal Loan / Bank Marketing* (Kaggle) — excelente para aprender valores faltantes, outliers en ingresos/montos y luego extender a ML de clasificación.
2. **Educación:** *Student Performance / Dropout & Academic Success* (UCI / Kaggle) — gran mezcla de variables categóricas y numéricas, ideal para análisis de factores y sesgos.
3. **Deportes:** *FIFA / European Football / NBA Player Stats* (Kaggle) — muy entretenido para explorar rankings, correlaciones, limpieza de unidades (altura, peso, salarios) y visualizaciones.

## Cómo arrancar en una nueva conversación

1. Abre esta carpeta (`D:\Proyectos\eda-data-quality-pipeline`) como proyecto en Antigravity (**Projects → Add Project**).
2. Inicia una conversación nueva dentro de ese proyecto.
3. Prueba empezar con `/plan` o pidiéndole al agente: *"Leamos `ROADMAP.md` y elijamos el dataset para arrancar la Fase 1"*.
