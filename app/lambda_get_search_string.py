import json
from tuz.spotifyapi import search_func


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    return {
        "statusCode": 200,
        "body": json.dumps(
            search_func(event["queryStringParameters"]["search_string"])
        ),
    }
