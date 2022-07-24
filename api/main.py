from typing import Union
from fastapi import FastAPI, Request
from config import celery_app

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "OK"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/test_task")
def read_test_task():
    for i in range(1000):
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
