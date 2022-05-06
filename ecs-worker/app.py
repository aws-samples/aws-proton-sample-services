import logging
import boto3
import os
from botocore.exceptions import ClientError
import json

QUEUE_URI = os.getenv("QUEUE_URI")
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

sqs_client = boto3.client("sqs", region_name = os.getenv("QUEUE_REGION"))


def receive_queue_message():
    try:
        response = sqs_client.receive_message(QueueUrl=QUEUE_URI, WaitTimeSeconds=5, MaxNumberOfMessages=1)
    except ClientError:
        logger.exception('Could not receive the message from the - {}.'.format(
            QUEUE_URI))
        raise
    else:
        return response


def delete_queue_message(receipt_handle):
    try:
        response = sqs_client.delete_message(QueueUrl=QUEUE_URI,
                                             ReceiptHandle=receipt_handle)
    except ClientError:
        logger.exception('Could not delete the meessage from the - {}.'.format(
            QUEUE_URI))
        raise
    else:
        return response


if __name__ == '__main__':
    while True:
        messages = receive_queue_message()
        print(messages)
        
        if "Messages" in messages: 
            for msg in messages['Messages']:
                msg_body = msg['Body']
                receipt_handle = msg['ReceiptHandle']
                logger.info(f'The message body: {msg_body}')
                logger.info('Deleting message from the queue...')
                resp_delete = delete_queue_message(receipt_handle)
            logger.info(
                'Received and deleted message(s) from {} with message {}.'.format(QUEUE_URI,resp_delete))
