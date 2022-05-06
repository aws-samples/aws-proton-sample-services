import logging
import os
import json
import random, string
import time
import boto3

TOPIC_ARNS = json.loads(os.getenv("SNS_TOPIC_ARN"))
client = boto3.client('sns', region_name = os.getenv("SNS_REGION"))
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

def generate_random(char_length):
   characters = string.ascii_lowercase
   return ''.join(random.choice(characters) for i in range(char_length))

def send_message():
    ping_message = "Hello! Message {} sent at time {}".format(generate_random(5),time.strftime('%A, %B %d %Y, %H:%M:%S'))
    response = client.publish(
        TopicArn=TOPIC_ARNS["ping"],
        Message=ping_message
            )
    message_id = response['MessageId']
    logger.info("Published message: %s.", message_id)
    return message_id

if __name__ == '__main__':
    send_message()
