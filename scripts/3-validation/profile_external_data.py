from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

EXTERNAL_DATA_DIR = (
    PROJECT_ROOT
    / "data"
    / "1-external"
    / "insurance_dataset"
    / "insurance_simple"
)

PROFILING_OUTPUT_DIR = PROJECT_ROOT / "docs" / "profiling"


def profile_csv(file_path: Path) -> str:
    df = pd.read_csv(file_path)

    report = []
    report.append(f"# Data Profile: {file_path.name}")
    report.append("")
    report.append(f"Rows: {df.shape[0]}")
    report.append(f"Columns: {df.shape[1]}")
    report.append("")
    report.append("## Columns")
    report.append("")
    for column in df.columns:
        report.append(f"- {column}: {df[column].dtype}")

    report.append("")
    report.append("## Missing Values")
    report.append("")
    missing_values = df.isna().sum()
    for column, count in missing_values.items():
        report.append(f"- {column}: {count}")

    report.append("")
    report.append("## Duplicate Rows")
    report.append("")
    report.append(f"Duplicate rows: {df.duplicated().sum()}")

    return "\n".join(report)


def main() -> None:
    PROFILING_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    csv_files = EXTERNAL_DATA_DIR.glob("*.csv")

    for csv_file in csv_files:
        report = profile_csv(csv_file)
        output_file = PROFILING_OUTPUT_DIR / f"{csv_file.stem}_profile.md"
        output_file.write_text(report, encoding="utf-8")

    print("Profiling reports generated successfully.")


if __name__ == "__main__":
    main()