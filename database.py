from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


USERNAME = "priyanshu"
PASSWORD = "123456"
HOST = "localhost"
PORT = "5432"
DATABASE = "fastAPI_db"


DATABASE_URL = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"


# Connection
engine = create_engine(DATABASE_URL)


# Session
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Base
Base = declarative_base()