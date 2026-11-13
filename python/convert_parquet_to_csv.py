
from pathlib import Path
import duckdb

# =====================================
# 1. PROJECT CONFIGURATION
# =====================================

PROJECT_FOLDER = Path(__file__).resolve().parents[1]

DATA_FOLDER = PROJECT_FOLDER / "data"
CSV_FOLDER = PROJECT_FOLDER / "csv"

CSV_FOLDER.mkdir(exist_ok=True)

TABLES = [
    "branches",
    "merchants",
    "customers",
    "accounts",
    "transactions"
]

# =====================================
# 2. PARQUET TO CSV CONVERSION
# =====================================

con = duckdb.connect()

try:
    for table in TABLES:

        input_file = DATA_FOLDER / f"{table}.parquet"
        output_file = CSV_FOLDER / f"{table}.csv"

        if not input_file.exists():
            raise FileNotFoundError(
                f"Missing source file: {input_file}"
            )

        # Escape paths for SQL strings
        source = str(input_file).replace("'", "''")
        target = str(output_file).replace("'", "''")

        # Source record count
        count = con.execute(
            f"SELECT COUNT(*) FROM read_parquet('{source}')"
        ).fetchone()[0]

        # Convert Parquet into CSV
        con.execute(f"""
            COPY (
                SELECT *
                FROM read_parquet('{source}')
            )
            TO '{target}'
            (HEADER, DELIMITER ',');
        """)

        print(f"{table.upper()}")
        print(f"Records : {count:,}")
        print(f"Output  : {output_file}")
        print("-" * 40)

    print("All conversions completed successfully!")

finally:
    con.close()
