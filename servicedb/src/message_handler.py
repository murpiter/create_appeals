import json

from .db_engine import get_db
from .models import Appeal


def handle_appeal_message(message):
    message_dict = json.loads(message)

    db = get_db()

    appeal = Appeal(
        surname=message_dict['surname'],
        name=message_dict['name'],
        patronymic=message_dict['patronymic'],
        phone_number=message_dict['phone_number'],
        appeal=message_dict['appeal'],
    )

    db.add(appeal)
    db.commit()

