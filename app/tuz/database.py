from functools import cache

from boto3.dynamodb.conditions import Key
import boto3


@cache
def db():
    return boto3.resource("dynamodb")


def get_item(table, key):
    table = f"ichack_{table}"
    print(f"Internal GET to ic{table} for {key}")
    return db().Table(table).get_item(Key=key).get("Item")


def put_item(table, item):
    table = f"ichack_{table}"
    print(f"Putting {item} in table {table}")
    db().Table(table).put_item(Item=item)


def query(table, q):
    table = f"ichack_{table}"
    print(f"Internal QUERY to {table}")
    return db().Table(table).query(**q)["Items"]


def query_equal(table, index, val, primary=False, **kwargs):
    q = {"KeyConditionExpression": Key(index).eq(val)}
    q |= kwargs
    if not primary:
        q["IndexName"] = f"{index}-index"

    return query(table, q)
