import pytest
from unittest.mock import patch, mock_open
from botocore.exceptions import ClientError
from utils.s3_utils import upload_to_s3

@patch("boto3.client")
def test_upload_to_s3_success(mock_boto_client):
    """Test successful upload to S3."""
    mock_s3_client = mock_boto_client.return_value
    mock_s3_client.put_object.return_value = {"ResponseMetadata": {"HTTPStatusCode": 200}}

    # Call the function
    upload_to_s3("test_file.csv", "test_file_in_s3.csv")

    # Assert that put_object was called with the correct parameters
    mock_s3_client.put_object.assert_called_once_with(
        Bucket="reddit-project-data-01",
        Key="bucket/raw/test_file_in_s3.csv",
        Body=mock_open().read(),
        ContentType="text/csv"
    )

@patch("boto3.client")
def test_upload_to_s3_bucket_not_found(mock_boto_client):
    """Test upload to S3 when the bucket does not exist."""
    mock_s3_client = mock_boto_client.return_value
    mock_s3_client.head_bucket.side_effect = ClientError(
        {"Error": {"Code": "404", "Message": "Not Found"}}, "HeadBucket"
    )
    mock_s3_client.create_bucket.return_value = {"ResponseMetadata": {"HTTPStatusCode": 200}}

    # Call the function
    upload_to_s3("test_file.csv", "test_file_in_s3.csv")

    # Assert that create_bucket was called
    mock_s3_client.create_bucket.assert_called_once()

@patch("boto3.client")
def test_upload_to_s3_failure(mock_boto_client):
    """Test upload to S3 when an error occurs."""
    mock_s3_client = mock_boto_client.return_value
    mock_s3_client.put_object.side_effect = ClientError(
        {"Error": {"Code": "500", "Message": "Internal Server Error"}}, "PutObject"
    )

    # Call the function and assert it handles the exception
    with pytest.raises(ClientError):
        upload_to_s3("test_file.csv", "test_file_in_s3.csv")
