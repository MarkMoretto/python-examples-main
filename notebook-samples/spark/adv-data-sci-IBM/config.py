__all__ = [
    "NOTEBOOKS_DIR",
    "PARQUET_FILE",
    ]

import os

NOTEBOOKS_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd())))
PARQUET_FILE = rf"{NOTEBOOKS_DIR}\washing.parquet"
