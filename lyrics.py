import requests
from urllib.parse import quote
name="Love the way you lie"
artist="eminem"
def getLyrics(name,artist):
    name_encoded = quote(name)
    artist_encoded = quote(artist)
    url = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?q_track="+name_encoded+"&q_artist="+artist_encoded+"&apikey=49d4034fc45ba31e09ce9f02652f4f4f"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()
