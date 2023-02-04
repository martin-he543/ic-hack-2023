import json
from tuz.test import test_function
from tuz.webchat_handler import read_handler


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(read_handler(event, context)),
    }
