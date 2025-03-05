# db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Данные подключения к базе берём из .env ИЛИ прописываем напрямую (пример)
DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/my_local_db'

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
