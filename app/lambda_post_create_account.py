import json
from tuz.deniswork import create_account


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(create_account(event, context)),
    }
