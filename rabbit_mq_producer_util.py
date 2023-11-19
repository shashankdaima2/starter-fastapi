import pika
import time
import random
import os
from dotenv import load_dotenv
def send_package_uid_to_rabbitMq(uid):
    load_dotenv()
    amqp_url=os.environ.get("RABBIT_MQ_URL")
    amqp_queue_name=os.environ.get("RABBIT_MQ_QUEUE_NAME")
    # Parse the URI
    url_parameters = pika.URLParameters(amqp_url)

    # Establish connection
    connection = pika.BlockingConnection(url_parameters)

    channel = connection.channel()

    channel.queue_declare(queue=amqp_queue_name)

    message =uid
    
    channel.basic_publish(exchange='', routing_key=amqp_queue_name, body=message)

    channel.close()
    