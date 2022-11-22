from flask import Flask, render_template, request, redirect
from getSong import *
from forms import SearchForm
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search= SearchForm(request.form)
    if request.method == 'POST':
        search_string=search.data['search']
        if search.data['search']=='':
            song=getRandomSong()
            lyrics= getLyrics(song['track_name'], song['artists'])
            return render_template('index.html', title=song['track_name'],song=song, lyrics=lyrics, form=search)
        return Song(search_string)
    song=getRandomSong()
    lyrics= getLyrics(song['track_name'], song['artists'])
    return render_template('index.html', title=song['track_name'],song=song, lyrics=lyrics, form=search)

@app.route('/song/<trackname>')
def Song(trackname):
    search= SearchForm(request.form)
    song = getSong(trackname)
    if 'track_name'in song:
        lyrics= getLyrics(song['track_name'], song['artists'])
        return render_template('index.html', title=song['track_name'],song=song, lyrics=lyrics, form=search)
    else:
        song=getRandomSong()
        lyrics= getLyrics(song['track_name'], song['artists'])
        return render_template('index.html', title=song['track_name'],song=song, lyrics=lyrics, form=search)
