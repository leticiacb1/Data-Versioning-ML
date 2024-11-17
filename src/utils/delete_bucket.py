import boto3
from dotenv import load_dotenv
import os

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

s3_resource = boto3.resource(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

def delete_bucket(bucket_name):
    try:
        # Get the bucket resource
        bucket = s3_resource.Bucket(bucket_name)

        # Delete all objects in the bucket
        print(f"Deleting all objects in bucket '{bucket_name}'...")
        bucket.objects.all().delete()

        # Delete the bucket itself
        print(f"Deleting bucket '{bucket_name}'...")
        s3_client.delete_bucket(Bucket=bucket_name)

        print(f"Bucket '{bucket_name}' has been deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Run the function
if __name__ == "__main__":

    bucket_name = "mlops-dvc-leticiacb1"
    delete_bucket(BUCKET_NAME)
