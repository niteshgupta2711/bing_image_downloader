import logging
import boto3
#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIAYC2VJDQCK3NX2GLK',
aws_secret_access_key='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'

)
#Creating S3 Resource From the Session.
s3 = session.resource('s3')
object = s3.Object('project', 'f.zip')
result = object.put(Body=open('ds.zip', 'rb'))
res = result.get('ResponseMetadata')
if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')
else:
    print('File Not Uploaded')

location = boto3.client('s3').get_bucket_location(Bucket='project')['LocationConstraint']
# url = "https://s3-%s.amazonaws.com/%s/%s" % (location, 'project, 'f.zip')