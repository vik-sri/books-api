import sys
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

PROJECT_DIR = Path(__file__).parents[0]
sys.path.append(
    str(PROJECT_DIR / "books_api")
)

try:
    from books_api.functions.create_book import external_create_book

except Exception as e:
    print(e)


class Book(BaseModel):
    book_id: str


app = FastAPI()


@app.get("/")
def root():
    print(Path(__file__).parent)
    return {"hello": "world"}


@app.post("/books")
def api_create_book(book: Book):
    payload = book.dict()
    response = external_create_book(payload)
    return response
