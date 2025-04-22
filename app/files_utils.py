from pathlib import Path

FILES_DIR = Path(__file__).parent.parent / "files"

def get_file_content(filename: str) -> str:
    file_path = FILES_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Archivo '{filename}' no encontrado.")
    return file_path.read_text()
