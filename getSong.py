import requests
from urllib.parse import quote
from lyrics import getLyrics
import json
name="Love the way you lie"
artist="eminem"

def getRandomSong():
    url="http://localhost:5000/random"
    payload = ""
    headers = {}
    song = requests.request("GET", url, headers=headers, data=payload)
    return song.json()

song={"track_name": "name 3",
    "artists": "ben",
    "album_name": "demo",
    "image_url": "abc.com"}

def addSong(song):
    songJson=json.dumps(song)
    url = "http://localhost:5000/song"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=songJson)
    return response.text

def getSong(name):
    name = quote(name)
    url="http://localhost:5000/song/"+name
    payload = ""
    headers = {}
    song = requests.request("GET", url, headers=headers, data=payload)
    return song.json()


song = getRandomSong()
lyrics = getLyrics(song['track_name'], song['artists'])
#print(lyrics['message']['body']['lyrics']['lyrics_body'])
