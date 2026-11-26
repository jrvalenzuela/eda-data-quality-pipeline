"""Tests unitarios para la ingesta de datos crudos (sin depender de internet)."""

from pathlib import Path

import pytest

from ingest import BASE_URL, DATASET_FILES, download_dataset


def test_download_dataset_writes_all_expected_files(tmp_path: Path) -> None:
    requested_urls: list[str] = []

    def fake_fetcher(url: str) -> bytes:
        requested_urls.append(url)
        return f"col1,col2\n1,{url.rsplit('/', maxsplit=1)[-1]}\n".encode()

    result = download_dataset(tmp_path, fetcher=fake_fetcher)

    assert set(result.keys()) == set(DATASET_FILES)
    assert requested_urls == [f"{BASE_URL}/{name}" for name in DATASET_FILES]
    for name, path in result.items():
        assert path == tmp_path / name
        assert path.exists()
        assert name in path.read_text(encoding="utf-8")


def test_download_dataset_skips_existing_files_by_default(tmp_path: Path) -> None:
    existing = tmp_path / "results.csv"
    existing.write_text("original_data\n", encoding="utf-8")
    requested_urls: list[str] = []

    def fake_fetcher(url: str) -> bytes:
        requested_urls.append(url)
        return b"new_data\n"

    download_dataset(tmp_path, force=False, fetcher=fake_fetcher)

    assert existing.read_text(encoding="utf-8") == "original_data\n"
    assert f"{BASE_URL}/results.csv" not in requested_urls
    assert len(requested_urls) == len(DATASET_FILES) - 1


def test_download_dataset_overwrites_when_force_is_true(tmp_path: Path) -> None:
    existing = tmp_path / "results.csv"
    existing.write_text("original_data\n", encoding="utf-8")

    download_dataset(tmp_path, force=True, fetcher=lambda _url: b"updated_data\n")

    assert existing.read_text(encoding="utf-8") == "updated_data\n"


def test_download_dataset_raises_on_empty_response(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="Respuesta vacía"):
        download_dataset(tmp_path, fetcher=lambda _url: b"")

    assert not (tmp_path / "results.csv").exists()
