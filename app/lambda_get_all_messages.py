import json
from tuz.webchat_handler import read_handler


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    return {
        "statusCode": 200,
        "body": json.dumps(
            read_handler(event["queryStringParameters"]["event_id"], context)
        ),
    }
