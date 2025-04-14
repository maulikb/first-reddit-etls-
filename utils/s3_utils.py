import boto3
import json
from botocore.exceptions import ClientError
import os
import sys

# Add the parent directory to the Python path to locate constants
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, AWS_BUCKET_NAME, RAW_DATA_PATH

def upload_to_s3(file_path, file_name):
    """
    Uploads a file to an S3 bucket.

    :param file_path: The local file path to upload.
    :param file_name: The name of the file to save in the bucket.
    """
    # Initialize the S3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

    # Ensure the bucket exists or create it
    try:
        s3_client.head_bucket(Bucket=AWS_BUCKET_NAME)
    except ClientError:
        try:
            s3_client.create_bucket(
                Bucket=AWS_BUCKET_NAME,
                CreateBucketConfiguration={'LocationConstraint': AWS_REGION}
            )
            print(f"Bucket '{AWS_BUCKET_NAME}' created successfully.")
        except ClientError as e:
            print(f"Error creating bucket: {e}")
            return

    # Generate the file path
    file_path_in_s3 = RAW_DATA_PATH.format(file_name=file_name)

    # Upload the CSV file to S3
    try:
        with open(file_path, "rb") as file_data:
            s3_client.put_object(
                Bucket=AWS_BUCKET_NAME,
                Key=file_path_in_s3,
                Body=file_data,
                ContentType='text/csv'
            )
        print(f"File successfully uploaded to S3 bucket '{AWS_BUCKET_NAME}' with key '{file_path_in_s3}'.")
    except ClientError as e:
        print(f"Error uploading file to S3: {e}")
