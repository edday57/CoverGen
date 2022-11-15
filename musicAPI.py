from flask import Flask
from flask_restful import reqparse, Resource, Api, abort
import random
import json
from csv import DictReader

parser = reqparse.RequestParser()
parser.add_argument('track_name')
parser.add_argument('artists')
parser.add_argument('album_name')
parser.add_argument('image_url')

with open("playlist.csv", 'r') as f:
    dict_reader = DictReader(f)
    list_of_tracks = list(dict_reader)
   

def randSong():
    count=len(list_of_tracks)
    randId=random.randint(0, count-1)
    return list_of_tracks[randId]

def findSong(name):
    for track in list_of_tracks:
        if track['track_name'].lower() == name.lower():
            return(track)
    abort(404, message="Song {} is not added.".format(name))

def delSong(name):
    i = 0
    for track in list_of_tracks:
        if track['track_name'].lower() == name.lower():
            list_of_tracks.pop(i)
            return(track)
        i+=1
    abort(404, message="Song {} is not added.".format(name))

app = Flask(__name__)
api = Api(app)

class AllSongs(Resource):
    #random song
    def get(self):
        return list_of_tracks
class RandomSong(Resource):
    #random song
    def get(self):
        song = randSong()
        return song
class Song(Resource):
    #selected song
    def get(self,name):
        song=findSong(name)
        return song
    def delete(self, name):
        delSong(name)
        return '',204
class AddSong(Resource):
    def post(self):
        args = parser.parse_args()
        song = {'track_name': args['track_name'], 'artists': args['artists'], 'album_name': args['album_name'], 'image_url': args['image_url']}
        list_of_tracks.append(song)
        return list_of_tracks[-1], 201
    
api.add_resource(AllSongs, '/all')
api.add_resource(RandomSong, '/random')
api.add_resource(Song, '/song/<name>')
api.add_resource(AddSong, '/song')

if __name__ == '__main__':
    app.run(debug=True)
