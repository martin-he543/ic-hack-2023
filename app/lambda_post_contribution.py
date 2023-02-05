import json
from tuz.deniswork import (
    send_good_contribution,
    send_money_contribution,
    send_money_withdrawal,
)


def lambda_handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    body = json.loads(event["body"])

    funcMap = {"Pay In": send_money_contribution, "Withdrawal": send_money_withdrawal}
    func = funcMap.get(body["reason"], send_good_contribution)

    return {
        "statusCode": 200,
        "body": json.dumps(func(body, context)),
    }
