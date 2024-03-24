import pika, sys, os

def main():
    host = os.getenv('RABBITMQHOST', 'localhost')
    print("RabbitMQ host:", host)

    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(host, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='AccountActivated', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except pika.exceptions.AMQPConnectionError as err:
        print("Caught a channel error: {}, stopping...".format(err))        
        
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
