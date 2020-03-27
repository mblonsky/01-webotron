# coding: utf-8
import boto3
from pathlib import Path

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='robinvideolyzervideos-mblonsky')
from pathlib import Path
get_ipython().run_line_magic('ls', '/users/mblonsky/Downloads/*.mp4')
pathname = '~/Downloads/Pexel Videos 1851768.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
result['ResponseMetadata']
result['Labels']
len(result['Labels'])
