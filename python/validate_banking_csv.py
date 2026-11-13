from pathlib import Path
import pandas as pd

# Get project root from terminal working directory
PROJECT_FOLDER = Path.cwd()

CSV_FOLDER = PROJECT_FOLDER / "csv"

print("Project Folder:", PROJECT_FOLDER)
print("CSV Folder:", CSV_FOLDER)

tables = [
    "branches",
    "merchants",
    "customers",
    "accounts",
    "transactions"
]

for table in tables:

    file_path = CSV_FOLDER / f"{table}.csv"

    if not file_path.exists():
        print(f"File not found: {file_path}")
        continue

    df = pd.read_csv(file_path)

    print(f"\n{'=' * 50}")
    print(f"TABLE: {table.upper()}")
    print(f"{'=' * 50}")

    print("Rows:", f"{len(df):,}")
    print("Columns:", len(df.columns))

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Records:")
    print(df.head().to_string(index=False))