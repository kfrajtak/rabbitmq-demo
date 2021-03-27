#!/usr/bin/env python
import pika
import os
import json
from datetime import datetime

host = os.getenv('RABBITMQHOST', 'localhost')
host = "172.17.0.3"
print("RabbitMQ host:", host)

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters(host))
try:
    channel = connection.channel()

    # make sure the recipient queue exists
    # create a hello queue to which the message will be delivered:
    # channel.queue_declare(queue='hello')

    now = datetime.now()

    account_create_dict = {
        'currency': 'USD',
        'startingBalance': 1000.0,
        'overdraftLimit': -300.0
    }
    json = json.dumps(account_create_dict)

    channel.basic_publish(exchange='spring-boot-exchange',
                          routing_key='command',
                          properties=pika.BasicProperties(
                              # Add a key/value header
                              headers={'type': 'CreateAccountCommand'}
                          ),
                          body=json)
    print("Message sent.")
finally:
    connection.close()
