import os
import boto3

s3client = boto3.client('s3')
bucket = open("/Users/cheta/Desktop/buckets.txt", "r")
#def get_bucket_size(bucket):
for i in bucket.readlines():
	print(i.rstrip("\n"))
