from pathlib import Path


def ensure_directory_exists(path: Path) -> None:
    """
    Create a directory if it does not already exist.
    """
    path.mkdir(parents=True, exist_ok=True)