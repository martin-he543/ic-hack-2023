import json
import boto3

def update_dietary_info(account_id: str, dietary_info: str)
    dynamodb = boto3.client("dynamodb", region_name="eu-west-2")
    response = dynamodb.get_item(
        TableName="Accounts",
        Key=account_id,
    )
    account = json.loads(response)  
    account.dietary_info = dietary_info
    return account  