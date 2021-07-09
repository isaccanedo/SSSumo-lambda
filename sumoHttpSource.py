from __future__ import print_function

import json
import urllib
import boto3
import requests

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type and contents of object
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:

        #get object from S3
        response = s3.get_object(Bucket=bucket, Key=key)

        # get object data and push to Sumologic
        key1_data = response['Body']._raw_stream.data
        sumo_url = '<insert sumologic http source URL here>'
        header = {'content-type': 'text/plain', 'Content-Encoding': 'gzip'}
        
        r = requests.post(sumo_url, data=key1_data, headers=header)
        if r.status_code == 200:
            print('Post to Sumologic successful')
            return r.status_code
        else:
            return r.status_code
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

def main():
    lambda_handler(event)

if __name__ == "__main__":
    main()
