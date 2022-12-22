from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError


from .config import DATABASE_URI
from .models import Base


def get_db_engine():
    created_engine = create_engine(
        DATABASE_URI,
        pool_pre_ping=True,
        connect_args={
            "keepalives": 1,
            "keepalives_idle": 30,
            "keepalives_interval": 10,
            "keepalives_count": 5,
        }
    )

    if not database_exists(created_engine.url):
        create_database(created_engine.url)

    Base.metadata.create_all(created_engine)

    return created_engine


engine = get_db_engine()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()

    try:
        return db
    finally:
        db.close()
