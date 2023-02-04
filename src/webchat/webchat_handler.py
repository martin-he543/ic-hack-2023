import datetime
import json

import logging


TEST_WEBCHAT_DATA = [
    {
        "account_id": 1,
        "date_time": "2020-03-20T14:28:23.382748",
        "event_id": 1,
        "text": "haha wow I love you uwu wow",
    },
    {
        "account_id": 2,
        "date_time": "2020-03-21T14:28:23.382748",
        "event_id": 1,
        "text": "awwww i totally wuv u too how wholesome",
    },
    {
        "account_id": 3,
        "date_time": "2020-03-22T14:28:23.382748",
        "event_id": 2,
        "text": "we must plan the destruction of the empire",
    },
    {
        "account_id": 4,
        "date_time": "2020-03-23T14:28:23.382748",
        "event_id": 2,
        "text": "indeed, long live the rebellion",
    },
    {
        "account_id": 5,
        "date_time": "2020-03-23T14:28:23.382748",
        "event_id": 2,
        "text": "oh oh, stinkyyyy",
    },
]


def get_messages(event_id):
    """Place holder"""
    return [m for m in TEST_WEBCHAT_DATA if m["event_id"] == event_id]


def post_message(message):
    """Place holder"""
    logging.warning(json.dumps(message))


def read_all_event_msgs(event_id):
    messages = get_messages(event_id)
    messages.sort(key=lambda x: x["date_time"])
    return messages


def read_handler(event, context):
    event_id = event["event_id"]
    data = read_all_event_msgs(event_id)
    return data


def send_handler(event, context):
    message = {
        "user_id": event["account_idvccf"],
        "date_time": datetime.datetime.now().isoformat(),
        "event_id": event["event_id"],
        "text": event["text"],
    }
    post_message(message)


if __name__ == '__main__':
    lr_event = {"event_id": 2}
    print(read_handler(lr_event, None))
    lp_event = {"account_id": 6, "event_id": 2, "text": "haha work go brrrr"}
    send_handler(lp_event, None)
