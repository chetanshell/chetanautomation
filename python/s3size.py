import boto3
import os
from datetime import datetime, timedelta

os.environ['AWS_PROFILE'] = "aws"
os.environ['AWS_DEFAULT_REGION'] = "eu-west-1"

cw = boto3.client('cloudwatch',region_name='eu-west-1')
s3client = boto3.client('s3',region_name='eu-west-1')

allbuckets = s3client.list_buckets()

for bucket in allbuckets['Buckets']:
    print bucket['Name']
    response = cw.get_metric_statistics(Namespace='AWS/S3',
                                        MetricName='BucketSizeBytes',
                                        Dimensions=[
                                            {'Name': 'BucketName', 'Value': bucket['Name']},
                                            {'Name': 'StorageType', 'Value': 'StandardStorage'}
                                        ],
                                        StartTime=datetime.now() - timedelta(days=1),
                                        EndTime=datetime.now(),
                                        Period=86400,
                                        Statistics=['Average'],
                                        Unit='Bytes'
                                        )
    # print(bucket)
    bucket_size_bytes = response['Datapoints']
    print(response)
    break
