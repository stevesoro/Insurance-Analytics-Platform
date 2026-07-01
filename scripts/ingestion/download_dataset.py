from config.datasets import (
    DATASET_ID,
    DATASET_OUTPUT_DIR,
)
from config.project import APPLICATION_NAME

from scripts.ingestion.sources.kaggle_cli import download_kaggle_dataset
from scripts.ingestion.utils.logger import get_logger
from scripts.ingestion.utils.paths import ensure_directory_exists


logger = get_logger(APPLICATION_NAME)


def main() -> None:
    logger.info("Starting dataset ingestion...")

    logger.info("Creating output directory...")
    ensure_directory_exists(DATASET_OUTPUT_DIR)

    logger.info("Downloading dataset from Kaggle...")
    download_kaggle_dataset(
        dataset_id=DATASET_ID,
        output_dir=DATASET_OUTPUT_DIR,
    )

    logger.info("Dataset successfully downloaded.")


if __name__ == "__main__":
    main()