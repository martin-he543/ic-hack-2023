import json
from tuz.deniswork import create_event


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    body = json.loads(event["body"])

    return {
        "statusCode": 200,
        "body": json.dumps(create_event(body, context)),
    }
