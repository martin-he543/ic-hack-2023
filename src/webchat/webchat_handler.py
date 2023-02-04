import datetime
import json
import logging

from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
import boto3


def read_all_event_msgs(event_id):
    dynamodb = boto3.resource('dynamodb', region_name="eu-west-2")
    table = dynamodb.Table("Messages")
    try:
        response = table.query(KeyConditionExpression=Key('event_id').eq(event_id))
    except ClientError as err:
        logging.error(
            "Couldn't query for messages in event %s. Here's why: %s: %s", event_id,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    else:
        messages = [json.loads(message) for message in response['Items']]
        messages.sort(key=lambda x: x["date_time"])
    return messages


def post_event_msg(message_dict):
    dynamodb = boto3.resource('dynamodb', region_name="eu-west-2")
    table = dynamodb.Table("Messages")
    try:
        table.put_item(Item=message_dict)
    except ClientError as err:
        logging.error(
            "Couldn't post message. Here's why: %s: %s",
            err.response['Error']['Code'], err.response['Error']['Message'])


def read_handler(event, context):
    event_id = event["event_id"]
    data = read_all_event_msgs(event_id)
    return data


def send_handler(event, context):
    message = {
        "user_id": event["user_id"],
        "date_time": datetime.datetime.now().isoformat(),
        "event_id": event["event_id"],
        "text": event["text"],
    }
    post_event_msg(message)
    return True
