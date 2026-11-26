"""Smoke tests para validar que el entorno y dependencias clave están operativos."""

import importlib

import pytest


@pytest.mark.parametrize(
    "package_name",
    ["pandas", "duckdb", "pandera", "plotly", "pyarrow"],
)
def test_core_dependencies_importable(package_name: str) -> None:
    module = importlib.import_module(package_name)
    assert module is not None
