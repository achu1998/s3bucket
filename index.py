import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Define your file and bucket
file_path = "database.sqlite"  # Local SQLite file path
bucket_name = "your-bucket-name"  # Your S3 bucket
s3_key = "backup/database.sqlite"  # S3 file path

# Upload file
s3.upload_file(file_path, bucket_name, s3_key)

print(f"File uploaded to s3://{bucket_name}/{s3_key}")