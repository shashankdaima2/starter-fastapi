from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import redis
from models import LogItem;
import uuid

load_dotenv()
app = FastAPI()

redis_host=os.environ.get("REDIS_PUBLIC_ENDPOINT_HOST")
redis_port=int(os.environ.get("REDIS_PUBLIC_ENDPOINT_PORT"))
redis_password=os.environ.get("REDIS_PASSWORD")

redis = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password,
)

# class Item(BaseModel):
#     item_id: int


# @app.get("/")
# async def root():
#     return {"message": os.environ.get("RUN_LOCAL")}


# @app.get('/favicon.ico', include_in_schema=False)
# async def favicon():
#     return FileResponse('favicon.ico')


# @app.get("/item/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# @app.get("/items/")
# async def list_items():
#     return [{"item_id": 1, "name": "Foo"}, {"item_id": 2, "name": "Bar"}]


# @app.post("/items/")
# async def create_item(item: Item):
#     return item


@app.post("/log/")
async def post_log(log: LogItem):
    redis.set(str(uuid.uuid4()), (log.json()))
    return log