import json
import logging
from hashlib import sha256
from tuz.database import query_equal, put_item, get_item, convert_aws_types
import uuid

PAYMENTS = [
    {"event_id": "eid1", "account_id": "aid1", "reason": "vodka", "money": 300},
    {"event_id": "eid1", "account_id": "aid2", "reason": "vodka", "money": 300},
    {"event_id": "eid1", "account_id": "adminid1", "reason": "vodka", "money": 200},
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
        "money_pool": 0,
        "date": "2023-02-04",
        "arrival_time": "12:00",
        "leaving_time": "12:00",
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
        "money_pool": 0,
        "date": "2023-02-04",
        "arrival_time": "12:00",
        "leaving_time": "12:00",
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


def event_add_user(body, context):
    event = get_item("events", {"event_id": body["event_id"]})
    account = get_item("accounts", {"account_id": body["account_id"]})
    event["accounts"].append(account["account_id"])
    put_item("events", event)


def event_split(body, context):
    payments = query_equal("payments", "event_id", body["event_id"])
    event = get_item("events", {"event_id": body["event_id"]})
    payments = [convert_aws_types(p) for p in payments]

    total_spent = 0
    for element in payments:
        total_spent += element["money"]

    people = event["accounts"]

    people.extend(event["admin_accounts"])

    money_owed = {person: 0 for person in people}

    for contributor in payments:
        if contributor["reason"] != "Pay In" and contributor["reason"] != "Withdrawal":
            money_owed[contributor["account_id"]] += contributor["money"]
            for person in people:
                money_owed[person] -= contributor["money"] / len(money_owed)
        else:
            money_owed[contributor["account_id"]] -= contributor["money"]
    return money_owed


def send_good_contribution(body, context):
    payment = {
        "payment_id": str(uuid.uuid4()),
        "account_id": body["account_id"],
        "event_id": body["event_id"],
        "reason": body["reason"],
        "money": -body["money"],
    }
    put_item("payments", payment)


def send_money_contribution(body, context):
    payment = {
        "payment_id": str(uuid.uuid4()),
        "account_id": body["account_id"],
        "event_id": body["event_id"],
        "reason": "Pay In",
        "money": body["money"],
    }
    put_item("payments", payment)


def send_money_withdrawal(body, context):
    payment = {
        "payment_id": str(uuid.uuid4()),
        "account_id": body["account_id"],
        "event_id": body["event_id"],
        "reason": "Withdrawal",
        "money": -body["money"],
    }
    put_item("payments", payment)


def create_account(body, context):
    account = {
        "account_id": sha256(body["username"].encode("utf-8")).hexdigest(),
        "username": body["username"],
        "password": body["password"],
        "home": {
            "postcode": body["postcode"],
            "house_number": body["house_number"],
            "street": body["street"],
        },
        "dietary_info": body["dietary_info"],
    }
    put_item("accounts", account)


def create_event(body, context):
    event_party = {
        "event_id": sha256(body["event_name"].encode("utf-8")).hexdigest(),
        "event_name": body["event_name"],
        "admin_accounts": [body["account_id"]],  # account that created
        "accounts": [],
        "address": body["address"],
        "date": body["date"],
        "arrival_time": body["arrival_time"],
        "leaving_time": body["leaving_time"],
    }
    put_item("events", event_party)


def get_event(body, context):
    return get_item("events", {"event_id": body["event_id"]})


def get_account(body, context):
    return get_item("accounts", {"account_id": body["account_id"]})


if __name__ == "__main__":
    payment_example = {
        "payment_id": "73474d55-f19d-480b-ace5-2c74be5e6afb",
        "account_id": "aid1",
        "event_id": "eid1",
        "reason": "haha work go brrrr",
        "money": 110,
    }
    event_example = {"event_id": "eid1"}
    account_example = {
        "account_id": "16f78a7d6317f102bbd95fc9a4f3ff2e3249287690b8bdad6b7810f82b34ace3"
    }
    account_example_creation = {
        "username": "username",
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
    print(event_split(EVENT_DICT, None))
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
