import json
import logging
from hashlib import sha256

PAYMENTS = [
    {"event_id": "eid1", "account_id": "aid1", "reason": "vodka", "money": -3},
    {"event_id": "eid1", "account_id": "aid2", "reason": "vodka", "money": -3},
    {"event_id": "eid1", "account_id": "adminid1", "reason": "vodka", "money": -2},
]

EVENTS = [
    {
        "event_id": "eid1",
        "event_name": "name",
        "admin_accounts": ["adminid1"],
        "accounts": ["aid1", "aid2", "aid3"],
        "address": {
            "postcode": "postcode",
            "house_number": "number",
            "street": "street",
        },
        "money_pool": 0.0,
        "date": "2023-02-04",
        "arrival_ time": "12:00",
        "leavin_time": "12:00",
    },
    {
        "event_id": "eid2",
        "event_name": "name",
        "admin_accounts": ["adminid1"],
        "accounts": ["aid1", "aid2"],
        "address": {
            "postcode": "postcode",
            "house_number": "number",
            "street": "street",
        },
        "money_pool": 0.0,
        "date": "2023-02-04",
        "arrival_ time": "12:00",
        "leavin_time": "12:00",
    },
]

ACCOUNTS = [
    {
        "account_id": "aid1",
        "username": "username",
        "password": "password",
        "home": {"postcode": "postcode", "house_number": "number", "street": "street"},
        "dietary_info": "nut allergy",
    }
]

EVENT_DICT = {"event_id": "eid1"}


def helper_payments(event_id):
    return [payment for payment in PAYMENTS if payment["event_id"] == event_id]


def helper_events(event_id):
    for event in EVENTS:
        if event["event_id"] == event_id:
            return event


def helper_accounts(account_id):
    for account in ACCOUNTS:
        if account["account_id"] == account_id:
            return account


def event_split(event_dict, context):
    payments = helper_payments(event_dict["event_id"])
    event = helper_events(event_dict["event_id"])
    total_spent = 0
    for element in payments:
        total_spent += element["money"]

    people = event["accounts"]

    people.extend(event["admin_accounts"])

    per_person = total_spent / len(people)

    money_owed = {}

    for person in people:
        person_added = False
        for contributor in payments:
            if person == contributor["account_id"]:
                money_owed[person] = -per_person + contributor["money"]
                person_added = True
        if not person_added:
            money_owed[person] = -per_person

    return money_owed


def send_good_contribution(event, context):
    payment = {
        "account_id": event["account_id"],
        "event_id": event["event_id"],
        "reason": event["reason"],
        "money": -event["money"],
    }
    post_good_contribution(payment)


def post_good_contribution(payment):
    """Place holder"""
    logging.warning(json.dumps(payment))


def create_account(event, context):
    account = {
        "account_id": sha256(event["username"].encode("utf-8")).hexdigest(),
        "username": event["username"],
        "password": event["password"],
        "home": {
            "postcode": event["postcode"],
            "house_number": event["house_number"],
            "street": event["street"],
        },
        "dietary_info": event["dietary_info"],
    }
    post_create_account(account)


def post_create_account(account):
    """Place holder"""
    logging.warning(json.dumps(account))


def create_event(event, context):
    event_party = {
        "event_id": sha256(event["event_name"].encode("utf-8")).hexdigest(),
        "event_name": event["event_name"],
        "admin_accounts": event["account_id"],  # account that created
        "accounts": [],
        "address": {
            "postcode": event["postcode"],
            "house_number": event["house_number"],
            "street": event["street"],
        },
        "date": event["date"],
        "arrival_ time": event["arrival_time"],
        "leaving_time": event["leaving_time"],
    }
    post_create_event(event_party)


def post_create_event(event):
    """Place holder"""
    logging.warning(json.dumps(event))


def send_money_contribution(event, context):
    payment = {
        "account_id": event["account_id"],
        "event_id": event["event_id"],
        "reason": "Pay In",
        "money": event["money"],
    }
    post_money_contribution(payment)


def post_money_contribution(payment):
    """Place holder"""
    logging.warning(json.dumps(payment))


def get_event(event, context):
    event_id = event["event_id"]
    event = helper_events(event_id)
    return event


def get_account(event, context):
    account_id = event["account_id"]
    account = helper_accounts(account_id)
    return account


if __name__ == "__main__":
    payment_example = {
        "account_id": "aid1",
        "event_id": "eid1",
        "reason": "haha work go brrrr",
        "money": 1.1,
    }
    event_example = {"event_id": "eid1"}
    account_example = {"account_id": "aid1"}
    account_example_creation = {
        "account_id": "account_id",
        "username": "username",
        "password": "password",
        "postcode": "postcode",
        "house_number": "house_number",
        "street": "street",
        "dietary_info": "dietary_info",
    }
    money_example = {
        "account_id": "account_id",
        "event_id": "event_id",
        "money": "money",
    }
    print(event_split(EVENT_DICT))
    print("\n")
    send_good_contribution(payment_example, None)
    print("\n")
    print(get_event(event_example, None))
    print("\n")
    print(get_account(account_example, None))
    print("\n")
    create_account(account_example_creation, None)
    print("\n")
    send_money_contribution(money_example, None)
