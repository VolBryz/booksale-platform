# main.py
from fastapi import FastAPI
from db import Base, engine
from routers import sellers, books

# Создаём таблицы в БД (если не используем Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sellers.router)
app.include_router(books.router)
