import sys
from pathlib import Path

# Go up one folder (equivalent to the ".." in JS)
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Now Python can see the 'src' folder perfectly
from src.persistence import load_model
from config import MODEL_PATH

pipline = load_model(MODEL_PATH)

print(type(pipline))