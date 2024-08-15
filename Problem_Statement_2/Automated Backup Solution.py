import os
import logging
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from datetime import datetime


BUCKET_NAME = 'diiviij'
LOCAL_DIR = '/docs/namelist'
LOG_FILE = 'backup_report.log'

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def upload_file_to_s3(s3_client, local_file, bucket_name, s3_file):
    try:
        s3_client.upload_file(local_file, bucket_name, s3_file)
        logging.info(f"Successfully uploaded {local_file} to s3://diiviij/")
    except FileNotFoundError:
        logging.error(f"File not found: backup_report.log")
    except NoCredentialsError:
        logging.error("Credentials not available for AWS S3")
    except PartialCredentialsError:
        logging.error("Incomplete credentials for AWS S3")
    except Exception as e:
        logging.error(f"Failed to upload {local_file} to s3://diiviij/: {e}")

def backup_directory(local_dir, bucket_name):
    s3_client = boto3.client('s3')
    
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_file = os.path.join(root, file)
            s3_file = os.path.relpath(local_file, local_dir)
            upload_file_to_s3(s3_client, local_file, bucket_name, s3_file)

def main():
    logging.info("Backup process started.")
    try:
        backup_directory(LOCAL_DIR, BUCKET_NAME)
        logging.info("Backup process completed successfully.")
    except Exception as e:
        logging.error(f"Backup process failed: {e}")

if __name__ == "__main__":
    main()
