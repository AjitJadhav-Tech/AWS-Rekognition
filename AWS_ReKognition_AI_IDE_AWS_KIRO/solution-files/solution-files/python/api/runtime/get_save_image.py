import os
import json
import logging
import boto3
import requests
import botocore.exceptions

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

s3_client = boto3.client("s3")
S3_BUCKET = os.getenv('BUCKET_NAME')

# TODO: Implement get_file_from_url function
# KIRO PROMPT: "Create a Python function called get_file_from_url that downloads content from a URL using the requests library and handles exceptions"
# Expected: Function should take a URL parameter, return response.content as bytes, and print any RequestException errors

def get_file_from_url(url):
    """
    Downloads file content from a given URL.
    
    Args:
        url (str): The URL to download from
        
    Returns:
        bytes: The file content
        
    Raises:
        requests.exceptions.RequestException: If the download fails
    """
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (compatible; CloudageBot/1.0)"}, timeout=10)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        logger.error("Failed to download file from URL %s: %s", url, e)
        raise


# TODO: Implement upload_to_s3 function
# KIRO PROMPT: "Create a Python function called upload_to_s3 that uploads an object to S3 using boto3 and handles exceptions"
# Expected: Function should take file_content and file_name parameters, upload to S3_BUCKET, and print any exceptions

def upload_to_s3(file_content, file_name):
    """
    Uploads file content to an S3 bucket.
    
    Args:
        file_content (bytes): The file content to upload
        file_name (str): The name for the file in S3
        
    Raises:
        botocore.exceptions.ClientError: If the S3 upload fails
    """
    try:
        s3_client.put_object(Bucket=S3_BUCKET, Key=file_name, Body=file_content)
    except botocore.exceptions.ClientError as e:
        logger.error("Failed to upload file %s to S3: %s", file_name, e)
        raise
    

def handler(event, context):
    params = event.get("queryStringParameters") or {}

    if "url" not in params or "name" not in params:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing required query parameters: url and name')
        }

    url = params["url"]
    name = params["name"]

    if not url.startswith("http://") and not url.startswith("https://"):
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid URL: must start with http:// or https://')
        }

    # Call get_file_from_url function
    try:
        image = get_file_from_url(url)
    except requests.exceptions.RequestException as e:
        logger.error("Download failed: %s", e)
        return {
            'statusCode': 502,
            'body': json.dumps(f'Failed to download image: {str(e)}')
        }

    # Call upload_to_s3 function
    try:
        upload_to_s3(image, name)
    except botocore.exceptions.ClientError as e:
        logger.error("Upload failed: %s", e)
        return {
            'statusCode': 502,
            'body': json.dumps(f'Failed to upload image to S3: {str(e)}')
        }

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully Uploaded Img!')
    }
