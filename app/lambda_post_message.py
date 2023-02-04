import json
from tuz.webchat_handler import post_message


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(post_message(event, context)),
    }
