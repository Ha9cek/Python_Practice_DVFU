from fastapi import FastAPI

from app.db.db import engine
from app.db.models import Base
from app.api import books, categories

# создаём таблицы, если их ещё нет
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Books API")

app.include_router(categories.router)
app.include_router(books.router)


@app.get("/health")
def health():
    return {"status": "ok"}