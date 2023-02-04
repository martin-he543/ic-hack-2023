import json
import boto3


def event_split(event_id, include_admins=True):
    dynamodb = boto3.client("dynamodb", region_name="eu-west-2")
    response = dynamodb.get_item(
        TableName="Events",
        Key=event_id,
    )
    event = json.loads(response)

    total_spent = 0
    for element in event.money:
        total_spent += element[1]

    if include_admins:
        people = event.accounts.extend(event.admin_accounts)
    else:
        people = event.accounts

    per_person = total_spent / len(people)

    money_owed = []

    for person in people:
        person_added = False
        for contributor in event.money:
            if person == contributor[0]:
                money_owed.append([person, -per_person + contributor[1]])
                person_added = True
        if not person_added:
            money_owed.append([person, -per_person])

    return money_owed
