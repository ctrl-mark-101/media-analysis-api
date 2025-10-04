import pandas as pd
from crud import load_data

def average_rating(media_type: str = None):
    df = load_data()
    if media_type:
        df = df[df['type'] == media_type]
    return df['rating'].mean() if not df.empty else None

def top_genres(n=3):
    df = load_data()
    return df['genre'].value_counts().head(n).to_dict()

def consumption_trend():
    df = load_data()
    df['created_at'] = pd.to_datetime(df['created_at'])
    trend = df.groupby(df['created_at'].dt.to_period("M")).size()
    return trend.to_dict()

def highest_rated(n=5):
    df = load_data()
    top = df.sort_values(by="rating", ascending=False).head(n)
    return top.to_dict(orient="records")
