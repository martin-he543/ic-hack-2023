import spotipy
import requests
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials

def get_auth_keys():
    return '', ''

def get_object():
    cid, cs = get_auth_keys()
    c_spotify=spotipy.oauth2.SpotifyClientCredentials(client_id=cid, client_secret=cs)
    get_token = c_spotify.get_access_token(check_cache=False)
    token=get_token['access_token']
    spotify = spotipy.Spotify(token)
    return spotify, token

def playlist_gen(playlist_id, limit=20, market='US', seed_genres='indie', target_danceability=0.9):
    spotify, token = get_object()
    endpoint_url = "https://api.spotify.com/v1/recommendations?"
    query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'

    response =requests.get(query, 
                headers={"Content-Type":"application/json", 
                            "Authorization":'Bearer '+token})

    json_response = response.json()
    uri_array=np.array([])
    for info in json_response['tracks']:
        uri_array= np.append(uri_array, info['uri'])
    add_song(user_id, playlist_id, uri_array)


def search_func(search_string):
    spotify, token = get_object()
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

def search_add(results_dict, choice, playlist_id, user_id):
    song_uri = results_dict['uris'][choice]
    add_song(user_id, playlist_id, [song_uri])


def add_song(user_id, playlist_id, uri_array):
    token,spotify = user_authentication(user_id)
    spotify.playlist_add_items(playlist_id, uri_array)
    

def user_authentication(user_id):
    scope_set = 'playlist-modify-private'
    cid, cs = get_auth_keys()
    user_auth = spotipy.oauth2.SpotifyOAuth(client_id=cid, client_secret=cs, redirect_uri='http://localhost:666', scope=scope_set, username=user_id)
    token = user_auth.get_access_token()['access_token']
    spotify = spotipy.Spotify(token)
    return token, spotify


def create_playlist(playlist_name, user_id):
    token, spotify = user_authentication(user_id)
    event_playlist = spotify.user_playlist_create(user_id, playlist_name, public=False, collaborative=False, description='testingabc')
    playlist_id = event_playlist['uri']
    return playlist_id


def find_playlists(user_id):
    token, spotify = user_authentication(user_id)
    playlists = spotify.current_user_playlists()
    print(playlists['items'][0]['name'])
