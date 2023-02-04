PAYMENTS = [
    {"event_id": "eid1", "account_id": "aid1", "reason": "vodka", "money": 1.1},
    {"event_id": "eid2", "account_id": "aid2", "reason": "vodka", "money": 2.2},
    {"event_id": "eid3", "account_id": "aid3", "reason": "vodka", "money": 3.3},
]

ACCOUNTS = [
    
]


def helper():
    return [payment for payment in PAYMENTS]


def event_split(event, payments, include_admins=True):
    payments = helper()
    total_spent = 0
    for element in payments:
        total_spent += element.money

    if include_admins:
        people = event.accounts.extend(event.admin_accounts)
    else:
        people = event.accounts

    per_person = total_spent / len(people)

    money_owed = []

    for person in people:
        person_added = False
        for contributor in payments:
            if person == payments.account_id:
                money_owed.append([person, -per_person + contributor[1]])
                person_added = True
        if not person_added:
            money_owed.append([person, -per_person])

    return money_owed
