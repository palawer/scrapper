from typing import Union
from fastapi import FastAPI, Request
from config import celery_app


app = FastAPI()


@app.get("/")
def home():
    return {"status": "OK"}


"""
curl -XGET "http://localhost:5000/test_task/1"
"""
@app.get("/test_task/{num_tasks}")
def test_task(num_tasks: int):
    for i in range(num_tasks):
        celery_app.send_task('test_task', (i,))
    
    return {"test": "task"}


"""
curl -XPOST "http://localhost:5000/get_urls" -H "accept: application/json" -H "Content-Type: application/json" -d'
{
    "urls": [
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/todos"
    ]
}
'
"""
@app.post("/get_urls")
async def get_urls(request: Request):
    data = await request.json()
    
    for i in range(20):
        for url in data.get('urls',[]):
            celery_app.send_task('get_url', (url,))
    
    return {"status": "OK"}
