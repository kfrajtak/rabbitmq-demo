#!/usr/bin/env python
import pika
import os
from datetime import datetime

host = os.getenv('RABBITMQHOST', 'localhost')
host = "172.17.0.3"
print("RabbitMQ host:", host)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters(host))
try:
    channel = connection.channel()

    # make sure the recipient queue exists
    # create a hello queue to which the message will be delivered:
    # channel.queue_declare(queue='hello')

    now = datetime.now()

    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
finally:
    connection.close()
