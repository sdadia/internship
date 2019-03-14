from datetime import datetime
from pprint import pprint
import boto3
import json
import random
import time


# initialize client
kinesis_client = boto3.client('kinesis', region_name='eu-west-1')

record = {}
## send data every 1 second
while True:
    ## create the data we want to send

    data = {
        "fuel_level" : random.randint(1,100),
        "car_id" : random.randint(1,5),
        "warning" : random.randint(0, 10)
    }
    
    # convert it to record
    record['Data'] = json.dumps(data)
    record['PartitionKey'] = str(data['car_id'])
    
    ## send the record
    response = kinesis_client.put_record(**record,StreamName='taxi_fleet_stream')
    pprint(record)
    # print("\n\n")
    # pprint(response)
    # print("\n====================\n")
    record = {}
    
    ## sleep for 1 second - then send next record
    time.sleep(2)
    # time.send

    # time.send()
