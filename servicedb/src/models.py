from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Appeal(Base):
    __tablename__ = 'appeals'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    phone_number = Column(String)
    appeal = Column(String)

    def __repr__(self):
        return "<Appeal(id='{}', surname='{}', name={}, patronymic={})>" \
            .format(self.id, self.surname, self.name, self.patronymic)
