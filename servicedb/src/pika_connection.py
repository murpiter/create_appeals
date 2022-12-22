import pika


def consume():
    connection = pika.BlockingConnection()
    channel = connection.channel()

    for method_frame, properties, body in channel.consume('appeals'):
        yield body

    channel.close()
    connection.close()
