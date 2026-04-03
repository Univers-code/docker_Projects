from fastapi import FastAPI
from redis import Redis
from rq import Queue
import time

app = FastAPI()

redis_conn = Redis(host="redis", port=6379)
queue = Queue(connection=redis_conn)

def long_task(data):
    time.sleep(5)
    return f"Processed {data}"

@app.post("/task")
def create_task(data: str):
    job = queue.enqueue(long_task, data)
    return {"job_id": job.id}