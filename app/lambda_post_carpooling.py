# JAMIE CHECK THIS

import json
from tuz.pooling import carpooling_handler


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    body = json.loads(event["body"])

    return {
        "statusCode": 200,
        "body": json.dumps(carpooling_handler(body, context)),
    }
