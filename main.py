from fastapi import FastAPI
from models import Media
import crud, analytics

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Media Consumption Analysis API!"}

@app.post("/media")
def add_media(media: Media):
    return crud.add_media(media)

@app.get("/media")
def get_media():
    return crud.get_all_media()

@app.delete("/media/{media_id}")
def delete_media(media_id: int):
    return crud.delete_media(media_id)

# ---------- Analytics ----------
@app.get("/analytics/average-rating")
def avg_rating(media_type: str = None):
    return {"average_rating": analytics.average_rating(media_type)}

@app.get("/analytics/top-genres")
def top_genres():
    return analytics.top_genres()

@app.get("/analytics/consumption-trend")
def trend():
    return analytics.consumption_trend()

@app.get("/analytics/highest-rated")
def top_rated():
    return analytics.highest_rated()

@app.get("/analytics/filter")
def filter_media(media_type: str = None, platform: str = None):
    return analytics.filter_media(media_type, platform)
