import requests
from urllib.parse import quote
from lyrics import getLyrics
import json
import time
name="Love the way you lie"
artist="eminem"

def getRandomSong():
    url="http://localhost:5000/random"
    payload = ""
    headers = {}
    t1 = time.perf_counter()
    song = requests.request("GET", url, headers=headers, data=payload)
    t2 = time.perf_counter()
    print(f"get request completed in {t2 - t1:0.6f} seconds")
    return song.json()

song={"track_name": "name 3",
    "artists": "ben",
    "album_name": "demo",
    "image_url": "abc.com"}

def addSong(song):
    songJson=json.dumps(song)
    url = "http://localhost:5000/song"
    headers = {'Content-Type': 'application/json'}
    t1 = time.perf_counter()
    response = requests.request("POST", url, headers=headers, data=songJson)
    t2 = time.perf_counter()
    print(f"post request completed in {t2 - t1:0.6f} seconds")
    return response.text

def delSong(name):
    name = quote(name)
    url="http://localhost:5000/song/"+name
    t1 = time.perf_counter()
    response = requests.delete(url)
    t2 = time.perf_counter()
    print(f"del request completed in {t2 - t1:0.6f} seconds")
    return response.text

def getSong(name):
    name = quote(name)
    url="http://localhost:5000/song/"+name
    payload = ""
    headers = {}
    t1 = time.perf_counter()
    song = requests.request("GET", url, headers=headers, data=payload)
    t2 = time.perf_counter()
    print(f"get request completed in {t2 - t1:0.6f} seconds")
    return song.json()

getRandomSong()
#song = getRandomSong()
#lyrics = getLyrics(song['track_name'], song['artists'])
#print(lyrics['message']['body']['lyrics']['lyrics_body'])
