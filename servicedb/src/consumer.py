from .pika_connection import consume
from .message_handler import handle_appeal_message


def appeals_consumer():
    for message in consume():
        handle_appeal_message(message)
