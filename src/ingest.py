"""Descarga reproducible de los CSVs crudos de International Football Results."""

from __future__ import annotations

import argparse
from collections.abc import Callable
from pathlib import Path
from urllib.request import urlopen

BASE_URL = "https://raw.githubusercontent.com/martj42/international_results/master"
DATASET_FILES: tuple[str, ...] = (
    "results.csv",
    "shootouts.csv",
    "goalscorers.csv",
)
DEFAULT_RAW_DIR = Path("data/raw")


def _fetch_bytes(url: str, timeout: int = 30) -> bytes:
    """Descarga el contenido binario desde una URL HTTP/HTTPS."""
    with urlopen(url, timeout=timeout) as response:
        return response.read()


def download_dataset(
    output_dir: Path = DEFAULT_RAW_DIR,
    *,
    force: bool = False,
    fetcher: Callable[[str], bytes] = _fetch_bytes,
) -> dict[str, Path]:
    """Descarga los 3 CSVs en output_dir sin sobreescribir salvo force=True."""
    output_dir.mkdir(parents=True, exist_ok=True)
    downloaded: dict[str, Path] = {}

    for filename in DATASET_FILES:
        target = output_dir / filename
        if target.exists() and not force:
            downloaded[filename] = target
            continue

        url = f"{BASE_URL}/{filename}"
        content = fetcher(url)
        if not content:
            raise ValueError(f"Respuesta vacía al descargar {url}")

        target.write_bytes(content)
        downloaded[filename] = target

    return downloaded


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Descarga los CSVs crudos en data/raw/."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_RAW_DIR,
        help="Carpeta destino (por defecto: data/raw).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Sobreescribe archivos existentes si ya fueron descargados.",
    )
    args = parser.parse_args()

    files = download_dataset(args.output_dir, force=args.force)
    for name, path in files.items():
        size_kb = path.stat().st_size / 1024
        print(f"[OK] {name} -> {path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
