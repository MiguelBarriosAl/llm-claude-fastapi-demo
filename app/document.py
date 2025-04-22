from pathlib import Path

FILES_DIR = Path(__file__).parent.parent / "files"


def list_files():
    return [f.name for f in FILES_DIR.glob("*.txt")]


def read_file(filename: str) -> str:
    file_path = FILES_DIR / filename
    if file_path.exists():
        return file_path.read_text()
    return f"The file {filename} does not exists"
