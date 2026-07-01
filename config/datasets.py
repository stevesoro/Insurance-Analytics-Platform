from config.paths import EXTERNAL_DATA_DIR

DATASET_SOURCE = "kaggle"
DATASET_ID = "kpoviesistphane/insurance-dataset-for-data-engineering-practice"
DATASET_NAME = "insurance_dataset"

DATASET_OUTPUT_DIR = EXTERNAL_DATA_DIR / DATASET_NAME
INSURANCE_DATASET_DIR = DATASET_OUTPUT_DIR / "insurance_simple"