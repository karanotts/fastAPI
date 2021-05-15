from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []


class Item(BaseModel):
    name: str
    quantity: int


@app.get("/")
async def index():
    return {"key": "value"}


@app.get("/items")
def get_items():
    return db


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return db[item_id-1]


@app.post("/items")
def post_item(item: Item):
    db.append(item.dict())
    return db[-1]


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db.pop(item_id-1)
    return db