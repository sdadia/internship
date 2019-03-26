import json
import boto3
import time
from pprint import pprint
import urllib
import base64

print("loading function")

kinesis_client = boto3.client("kinesis")
dynamodb_clinet = boto3.resource("dynamodb")


def lambda_handler(event, context):
    # record_set = []
    # event
    print("Event is :")
    pprint(event)

    # record
    print("Record is : ")
    record = event["Records"][0]["kinesis"]

    pprint(record)

    # data and partition from record is :
    print("Data and Partitoon Key is : ")
    data = record["data"]
    partition_key = record["partitionKey"]
    # decode them
    data = str(base64.b64decode(data).decode("utf-8"))
    data = json.loads(data)
    partition_key = partition_key
    print(type(data))

    pprint(data)
    pprint(partition_key)

    # write data to dynamo db table
    table = dynamodb_clinet.Table("taxi_fleet_data2")
    # for k in data.keys():
    # 	data[k] = str(data[k])

    response = table.put_item(Item=data)
    pprint(response)
    print("/home/lost+found/)

