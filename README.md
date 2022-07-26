
# Scrapper

A simple example with FastAPI, Celery, Rabbitmq and Redis

## Build and run containers

```
./build.sh
```

## Scrapping example

Test task

```
curl -XGET "http://localhost:5000/test_task/1"
```

Test scrapping json endpoints (20 times)

```
curl -XPOST "http://localhost:5000/get_urls" -H "accept: application/json" -H "Content-Type: application/json" -d'
{
    "urls": [
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/todos"
    ]
}
'
```

### API documentation

http://localhost:5000/docs    
http://localhost:5000/redoc    

### RabbitMQ management

http://localhost:15672    

## Used resources

https://blog.deepjyoti30.dev/celery_compose    
https://github.com/karthikasasanka/fastapi-celery-redis-rabbitmq    
https://pythonspeed.com/articles/base-image-python-docker-images/    
https://github.com/tanchinhiong/decoupled-celery-example    
