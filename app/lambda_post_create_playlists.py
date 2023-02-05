import json
from tuz.spotifyapi import create_playlist


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    body = json.loads(event["body"])

    spotify_name = body["spotify_username"]
    playlist_name = body["playlist_name"]

    return {
        "statusCode": 200,
        "body": json.dumps(create_playlist(playlist_name, spotify_name)),
    }
