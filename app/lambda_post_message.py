import json
from tuz.webchat_handler import post_message


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    body = json.loads(event["body"])

    return {
        "statusCode": 200,
        "body": json.dumps(post_message(body, context)),
    }
