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

def check_bucket_contents(bucket_name, expected_file):
    try:
        # List objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' not in response:
            print(f"The bucket '{bucket_name}' is empty.")
            return False

        # Print the files in the bucket
        print(f"Files in '{bucket_name}':")
        file_found = False
        for obj in response['Contents']:
            print(f" - {obj['Key']}")
            if obj['Key'] == expected_file:
                file_found = True

        if file_found:
            print(f"The file '{expected_file}' was found in the bucket.")
        else:
            print(f"The file '{expected_file}' was not found in the bucket.")

        return file_found

    except Exception as e:
        print(f"Error: {e}")
        return False

# Run the function
if __name__ == "__main__":
    bucket_name = "mlops-dvc-leticiacb1"
    expected_file = "data/data.csv"

    check_bucket_contents(bucket_name, expected_file)
