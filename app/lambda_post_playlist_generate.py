import json
from tuz.spotifyapi import playlist_gen


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    body = json.loads(event["body"])

    return {
        "statusCode": 200,
        "body": json.dumps(
            playlist_gen(
                body["playlist_id"],
                body["spotify_name"],
                limit=body.get("song_count"),
                target_danceability=body.get("danceability"),
            )
        ),
    }
