import pandas as pd
from models import Media
from pathlib import Path

DATA_FILE = Path("database.csv")

def load_data():
    if not DATA_FILE.exists():
        df = pd.DataFrame(columns=["id", "title", "type", "genre", "rating", "created_at"])
        df.to_csv(DATA_FILE, index=False)
    return pd.read_csv(DATA_FILE)

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def add_media(media: Media):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([media.dict()])], ignore_index=True)
    save_data(df)
    return media

def get_all_media():
    return load_data().to_dict(orient="records")

def delete_media(media_id: int):
    df = load_data()
    df = df[df["id"] != media_id]
    save_data(df)
    return {"message": f"Media {media_id} deleted"}
