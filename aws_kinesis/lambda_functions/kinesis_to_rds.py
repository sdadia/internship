import psycopg2
# from sqlalchemy import create_engine
import json
import boto3
import time
from pprint import pprint
import urllib
import base64

print("psycopyg version is ")
# print(psycopg2.__version__)
# import sys
# sys.exit()


print("loading function")

kinesis_client = boto3.client("kinesis")
POSTGRES_USERNAME = "sahil"
POSTGRES_PASSWORD = "3Bbx46T3Q6tnTqS"
POSTGRES_DBNAME = "postgres"
POSTGRES_HOST = "postgrestestdb2.cznthudneeub.eu-west-1.rds.amazonaws.com"

url = "postgresql://{}:{}@{}:{}/{}".format(
    POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_HOST, 5432, POSTGRES_DBNAME
)
print(url)
# engine = create_engine(url)


try:
    conn = psycopg2.connect("dbname='postgres' user='sahil' host='postgrestestdb2.cznthudneeub.eu-west-1.rds.amazonaws.com' password='3Bbx46T3Q6tnTqS'")
    cur = conn.cursor()
    print("Connection Successful")
except:
    print("I am unable to connect to the database")


def lambda_handler(event, context):
    print("Event is :")
    pprint(event)

    print("Number of records is : ")
    records = event["Records"]
    print(len(records))

    if len(records) == 1:
        # get data and decode it
        data = records[0]["kinesis"]["data"]
        data = str(base64.b64decode(data).decode("utf-8"))
        print("Data is ")
        print(data)

    else:
        for rec in records:
            data = rec["kinesis"]["data"]
            data = str(base64.b64decode(data).decode("utf-8"))
            print("Overall data is ")
            print(data)

            print("mmmmmmmmmmm")

    print("\n\n==============\n\n")
