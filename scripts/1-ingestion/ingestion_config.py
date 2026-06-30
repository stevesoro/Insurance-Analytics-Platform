from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET_SOURCE = "kaggle"
DATASET_ID = "kpoviesistphane/insurance-dataset-for-data-engineering-practice"
DATASET_NAME = "insurance_dataset"
APPLICATION_NAME = "Insurance Analytics Platform"

EXTERNAL_DATA_DIR = PROJECT_ROOT / "data" / "1-external"
DATASET_OUTPUT_DIR = EXTERNAL_DATA_DIR / DATASET_NAME