import sys

import boto
from boto.exception import S3ResponseError
from boto.s3.key import Key
from constants import FILE_NAME, BUCKET_NAME
from file_operations import get_file_path
from secret import AWS_ACCESS_KEY, AWS_SECRET_KEY


def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


def get_or_create_bucket_on_s3(conn, bucket_name):
    try:
        bucket = conn.get_bucket(bucket_name=bucket_name, validate=True)
    except S3ResponseError:
        print("Bucket is not found. Creating bucket with name {}".format(bucket_name))
        bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)
    return bucket


def upload_file_to_aws_s3_bucket():
    bucket_name = BUCKET_NAME
    conn = boto.connect_s3(AWS_ACCESS_KEY,
                           AWS_SECRET_KEY)
    bucket = get_or_create_bucket_on_s3(conn=conn, bucket_name=bucket_name)
    file_to_upload = get_file_path(file_name=FILE_NAME)
    print('Uploading {} to Amazon S3 bucket {}'.format(file_to_upload, bucket_name))

    k = Key(bucket)
    k.key = FILE_NAME
    sent = k.set_contents_from_filename(file_to_upload, replace=True, cb=percent_cb, num_cb=10)
    return sent
