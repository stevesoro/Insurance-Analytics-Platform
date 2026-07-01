import subprocess
from pathlib import Path


def download_kaggle_dataset(dataset_id: str, output_dir: Path) -> None:
    """
    Download and unzip a Kaggle dataset using the Kaggle CLI.
    """
    command = [
        "kaggle",
        "datasets",
        "download",
        dataset_id,
        "--path",
        str(output_dir),
        "--unzip",
    ]

    result = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )

    return result