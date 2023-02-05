import json
from tuz.deniswork import get_event


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    return {
        "statusCode": 200,
        "body": json.dumps(get_event(event["queryStringParameters"], context)),
    }
