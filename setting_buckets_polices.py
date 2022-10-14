import boto3
import json

s3_resource = boto3.client('s3')


# Create a bucket policy- Set the buckets name on  bucket_name
bucket_name = ['bucketexample1','buckteexample2','bucketexample3','.....']
for nome in bucket_name:

    bucket_policy = {
    "Id": "ExamplePolicy",
    "Version": "2012-10-17",
    "Statement": [
        {
        "Sid": "AllowSSLRequestsOnly",
        "Action": "s3:*",
        "Effect": "Deny",
        "Resource": [
            f"arn:aws:s3:::{nome}",
            f"arn:aws:s3:::{nome}/*"
        ],
        "Condition": {
            "Bool": {
            "aws:SecureTransport": "false"
            }
        },
        "Principal": "*"
        }
    ]
    }
    # Convert the policy from JSON dict to string
    bucket_policy = json.dumps(bucket_policy)

    # Set the new policy
    
    s3_resource.put_bucket_policy(Bucket=nome, Policy=bucket_policy)
