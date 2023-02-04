import json
from tuz.spotifyapi import search_func


def lambda_handler(event, context):
    body = json.loads(event["body"])

    return {
        "statusCode": 200,
        "body": json.dumps(search_func(body["search_string"])),
    }
