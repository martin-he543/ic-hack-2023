import json
from tuz.deniswork import event_split


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    return {
        "statusCode": 200,
        "body": json.dumps(event_split(event["queryStringParameters"], context)),
    }
