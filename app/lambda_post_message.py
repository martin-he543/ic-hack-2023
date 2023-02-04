import json
from tuz.test import test_function


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(test_function(event, context)),
    }
