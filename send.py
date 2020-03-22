#!/usr/bin/env python
import pika
import os
from datetime import datetime

host = os.getenv('RABBITMQHOST', 'localhost')
print("RabbitMQ host:", host)

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters(host))
try:
    channel = connection.channel()

    # make sure the recipient queue exists
    # create a hello queue to which the message will be delivered:
    channel.queue_declare(queue='hello')

    now = datetime.now()

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World! ' + now.strftime("%d/%m/%Y %H:%M:%S"))
    print(" [x] Sent 'Hello World!'")
finally:
    connection.close()
