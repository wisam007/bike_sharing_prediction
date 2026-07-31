import json
from pathlib import Path
import pandas as pd


def save_json(data:dict,output_path: Path)->None:
    output_path.parent.mkdir(parents=True,exist_ok=True)
    with output_path.open("w") as f:
        json.dump(data,f,indent=4)
def save_csv(df: pd.DataFrame,output_path:Path) -> None:
    output_path.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(output_path,index=True)
def save_dataframe(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)