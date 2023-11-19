from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import redis
from models import LogItem;
import uuid

from rabbit_mq_producer_util import send_package_uid_to_rabbitMq

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


@app.post("/log/")
async def post_log(log: LogItem):
    uid=str(uuid.uuid4())
    redis.set(uid, (log.json()))
    send_package_uid_to_rabbitMq(uid)
    return log