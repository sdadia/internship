"""
This code is used to transfer data from source s3 bucket to target s3 bucket.

"""

import json
import boto3
import time
from pprint import pprint
import urllib

print("loading function")
s3 = boto3.client("s3")


def lambda_handler(event, context):

    source_bucket = "bucket1-sahil"
    target_bucket = "bucket2-sahil"
    key = event["Records"][0]["s3"]["object"]["key"]
    print("File to be copied is : {}".format(key))

    copy_source = {"Bucket": source_bucket, "Key": key}

    try:
        print("waiting for file persist in source bucket")
        # waiter = s3.get_waiter('object_exists')
        # waiter.wait(**copy_source)
        # print("Copying now")
        response = s3.copy_object(
            Bucket=target_bucket, Key=key, CopySource=copy_source)
        pprint(response)
        # return response
    except Exception as e:
        print(e)
        # return e
