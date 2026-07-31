from pathlib import Path


BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA = DATA_DIR / "day.csv"

REPORT_DIR = BASE_DIR / "reports"

FIGURE_DIR = REPORT_DIR / "figures"

JSON_DIR = REPORT_DIR / "json"

TABLE_DIR = REPORT_DIR / "tables"

PROCESSED_DATA = DATA_DIR / "processed" / "bike_sharing_processed.csv"

MODEL_PATH = BASE_DIR / "model" /"bike_pipeline.pkl"
