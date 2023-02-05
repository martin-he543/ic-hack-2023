import json
from tuz.spotifyapi import search_add


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    body = json.loads(event['body'])

    return {
        "statusCode": 200,
        "body": json.dumps(
            search_add(
                body["results"],
                body["choice"],
                body["playlist_id"],
                body["spotify_name"],
            )
        ),
    }
