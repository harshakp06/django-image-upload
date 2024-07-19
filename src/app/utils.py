import os
import boto3
from django.conf import settings
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def generate_presigned_url(object_name, expiration=600):
    """Generate a pre-signed URL to share an S3 object

    :param object_name: S3 object name
    :param expiration: Time in seconds for the URL to remain valid
    :return: Pre-signed URL as string. If error, returns None.
    """
    # Create a session using your AWS credentials
    s3_client = boto3.client(
        's3',
        aws_access_key_id= os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key= os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name= os.getenv("AWS_S3_REGION_NAME")
    )

    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': os.getenv("AWS_STORAGE_BUCKET_NAME"),
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except NoCredentialsError:
        print("Credentials not available")
        return None
    except PartialCredentialsError:
        print("Incomplete credentials provided")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return response
