import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests as rq

SPOTIPY_CLIENT_ID='31cff7249b72481688e040188f82b55e'
SPOTIPY_CLIENT_SECRET='b93ffcabe890464f83814a56c221afc6'
#SPOTIPY_REDIRECT_URI="http://127.0.0.1:9090"
SCOPE = "playlist-read-private%20user-read-email"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, scope=SCOPE))


user_playlists = sp.current_user_playlists()

for i in user_playlists["items"]:
    print(i["name"])