import boto3
import os

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key'),
    region_name=os.getenv('region_name'))



def uploadDoc(uploaded_file):
    try:
        # Upload file to S3
        s3_client.upload_fileobj(uploaded_file, 'aws-bucket-practice-tofik', uploaded_file.name)
        return uploaded_file.name
    except Exception as e:
        return None
    
def generatePresignedURL(file_name):
    presigned_url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': 'aws-bucket-practice-tofik', 'Key': file_name},
        ExpiresIn=60*2)  # URL expires in 2 minute
    return presigned_url


def delete_file(file_name):
    try:
        s3_client.delete_object(Bucket='aws-bucket-practice-tofik', Key=file_name)
        return True
    except Exception as e:
        print('Error occurred:', e)
        return False