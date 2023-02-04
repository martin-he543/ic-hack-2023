from functools import cache
from decimal import Decimal
from boto3.dynamodb.conditions import Key
import boto3


@cache
def db():
    return boto3.resource("dynamodb")


def get_item(table, key, normal=False):
    table = f"ichack_{table}" if not normal else table
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


def is_int(string):
    try:
        return float(string).is_integer()
    except:
        return False


def convert_aws_type(v):
    if isinstance(v, Decimal):
        return int(v) if is_int(v) else float(v)
    if isinstance(v, dict):
        return convert_aws_types(v)
    return v


def convert_aws_types(obj):
    return {k: convert_aws_type(v) for k, v in obj.items()}


def get_parameter(param):
    return get_item("parameters", {"parameter": param}, normal=True)["value"]
