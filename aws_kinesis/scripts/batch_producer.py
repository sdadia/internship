from datetime import datetime
from pprint import pprint
import boto3
import json
import random
import time


# initialize client
kinesis_client = boto3.client('kinesis', region_name='eu-west-1')


## send data when we have 10 records,
RECORD_LIMIT = 2
record_set = [] # holds all 10 records
record = {}
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
    record

    ## send the data as a batch, send them togather
    if(len(record_set) == RECORD_LIMIT):
        response = kinesis_client.put_records(StreamName='taxi_fleet_stream', 
                                              Records = record_set
                                              )    
        pprint(record_set)
        print("\n\n")
        pprint(response)
        print("\n====================\n")
        record_set = [] #clear payload_set


    record_set.append(record)
    record = {} # clear record

    ## sleep for 1 second - then generate next record
    time.sleep(2)

