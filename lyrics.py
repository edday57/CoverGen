import requests
from urllib.parse import quote
import time
name="Love the way you lie"
artist="eminem"
def getLyrics(name,artist):
    name_encoded = quote(name)
    artist_encoded = quote(artist)
    t1 = time.perf_counter()
    url = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?q_track="+name_encoded+"&q_artist="+artist_encoded+"&apikey=49d4034fc45ba31e09ce9f02652f4f4f"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    t2 = time.perf_counter()
    print(f"external API get request completed in {t2 - t1:0.6f} seconds")
    return response.json()
