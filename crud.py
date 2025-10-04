import pandas as pd
from models import Media
from pathlib import Path
import os

# CSV path
DATA_FILE = Path(os.path.join(os.path.dirname(__file__), "data", "media.csv"))

# Ensure CSV exists at startup
if not DATA_FILE.exists():
    df = pd.DataFrame(columns=["id", "title", "type", "genre", "rating", "created_at"])
    df.to_csv(DATA_FILE, index=False)

def load_data():
    return pd.read_csv(DATA_FILE)

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def add_media_
