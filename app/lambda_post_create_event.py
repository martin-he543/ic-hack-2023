import json
from tuz.deniswork import create_event


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(create_event(event, context)),
    }
