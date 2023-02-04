import datetime
import json

import logging
import uuid

from tuz.database import query_equal, put_item

TEST_WEBCHAT_DATA = [
    {
        "account_id": "39b1f6b3-2fba-4d69-bd9b-8406ca9cb058",
        "date_time": "2020-03-20T14:28:23.382748",
        "event_id": "event1",
        "text": "haha wow I love you uwu wow",
    },
    {
        "account_id": "d8ecfb29-3b0b-404d-8c70-3fc75ef49d3a",
        "date_time": "2020-03-21T14:28:23.382748",
        "event_id": "event1",
        "text": "awwww i totally wuv u too how wholesome",
    },
    {
        "account_id": "1e880e54-5ba4-462b-b029-e1839b1dfda8",
        "date_time": "2020-03-22T14:28:23.382748",
        "event_id": "event2",
        "text": "we must plan the destruction of the empire",
    },
    {
        "account_id": "5748b81d-48cf-4d88-a144-88d0d1b8d8f1",
        "date_time": "2020-03-23T14:28:23.382748",
        "event_id": "event2",
        "text": "indeed, long live the rebellion",
    },
    {
        "account_id": "1a28e9be-4323-4392-8e73-73787bf51c1b",
        "date_time": "2020-03-24T14:28:23.382748",
        "event_id": "event2",
        "text": "oh oh, stinkyyyy",
    },
]


def get_messages(event_id):
    return query_equal("messages", "event_id", event_id)


def post_message(message):
    return put_item("messages", message)


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
        "user_id": event["account_id"],
        "date_time": datetime.datetime.now().isoformat(),
        "event_id": event["event_id"],
        "text": event["text"],
    }
    post_message(message)


if __name__ == "__main__":
    lr_event = {"event_id": "event1"}
    print(read_handler(lr_event, None))
    lp_event = {
        "account_id": "d8ecfb29-3b0b-404d-8c70-3fc75ef49d3a",
        "event_id": "event1",
        "text": "haha work go brrrr",
    }
    send_handler(lp_event, None)
