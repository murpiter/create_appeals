import time

import pika


CHANNEL_NAME = 'appeals'
RABBIT_URL = 'localhost'


def send_message(channel, data):
    channel.basic_publish(
        exchange='',
        routing_key=CHANNEL_NAME,
        body=data,
    )
    print('new message', data)


def init_sender():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_URL))
        channel = connection.channel()
        channel.queue_declare(queue=CHANNEL_NAME)
    except pika.exceptions.AMQPConnectionError:
        time.sleep(1)
        return init_sender()

    return connection, channel


def destroy_sender(connection, channel):
    channel.close()
    connection.close()
