from pprint import pprint
import boto3
import json
import time
## aws creds are stored in ~/.boto
kinesis = boto3.client("kinesis")
shard_id = "shardId-000000000000" #only one shard!
# shard_id = kinesis.describe_stream(StreamName='taxi_fleet_stream')['StreamDescription']['Shards'][0]['ShardId']
# print(shard_id)
pre_shard_it = kinesis.get_shard_iterator(StreamName="taxi_fleet_stream", 
                                          ShardId=shard_id, 
                                          ShardIteratorType="LATEST")
shard_it = pre_shard_it["ShardIterator"]
while 1==1:
    out = kinesis.get_records(ShardIterator=shard_it)
    record_set = out["Records"]

    pprint(record_set)

    shard_it = out["NextShardIterator"]
    
    print("=================")
    time.sleep(3)
    time.sleep
    
