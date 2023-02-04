import spotipy
import requests
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials

# get token from spotify api (removed here)

def get_auth_keys():
    return '', ''

def initial_setup():
    cid, cs = get_auth_keys()
    c_spotify=spotipy.oauth2.SpotifyClientCredentials(client_id=cid, client_secret=cs)
    get_token = c_spotify.get_access_token(check_cache=False)
    token=get_token['access_token']
    spotify = spotipy.Spotify(token)
    return spotify, token

def playlist_gen(spotify, token, limit=20, market='US', seed_genres='indie', target_danceability=0.9):
    endpoint_url = "https://api.spotify.com/v1/recommendations?"
    query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'

    response =requests.get(query, 
                headers={"Content-Type":"application/json", 
                            "Authorization":'Bearer '+token})

    json_response = response.json()
    for i in json_response['tracks']:
            print(f"\"{i['name']}\" by {i['artists'][0]['name']}")


def print_albums(spotify, uri):
    results = spotify.artist_albums(uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])

def find_artist_uri(spotify, artist_name):
    artist = spotify.search(q=artist_name, type="artist", limit=10)['artists']['items']
    return artist[0]['uri']

def search_func(spotify, search_string):
    song = spotify.search(q=search_string, type='track', limit=5)['tracks']['items']
    results_dict = dict()
    text_options=np.array([])
    uri_options=np.array([])
    for i in range(len(song)):
        option_text = (song[i]['name'] + ' by ' + song[i]['artists'][0]['name'])
        option_uri=(song[i]['uri'])
        text_options = np.append(text_options, option_text)
        uri_options = np.append(uri_options, option_uri)
    
    results_dict['text'] = text_options
    results_dict['uris'] = uri_options
    return results_dict

#get authentication token
spotify, token = initial_setup()

search_string='ruin amazing devil'

search_results = search_func(search_string)
print(search_results)

