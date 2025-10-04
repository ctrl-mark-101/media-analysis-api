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

def add_media(media: Media):
    df = load_data()
    
    # Auto-generate ID
    new_id = int(df['id'].max() + 1) if not df.empty else 1
    
    media_dict = media.dict()
    media_dict['id'] = new_id
    
    df = pd.concat([df, pd.DataFrame([media_dict])], ignore_index=True)
    save_data(df)
    return media_dict

def get_all_media():
    return load_data().to_dict(orient="records")

def delete_media(media_id: int):
    df = load_data()
    df = df[df["id"] != media_id]
    save_data(df)
    return {"message": f"Media {media_id} deleted"}
