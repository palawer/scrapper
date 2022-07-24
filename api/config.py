from celery import Celery
import os


#
# Constants
#
DATA_PATH     = '/app/data'

RABBITMQ_USER = 'admin'#os.getenv('RABBITMQ_USER')
RABBITMQ_PASS = 'mypass'#os.getenv('RABBITMQ_PASS')

REDIS_PORT    = 6379#FIXME
REDIS_DB      = 0#FIXME

BROKER_URL    = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@rabbit'
BACKEND_URL   = f'redis://redis:{REDIS_PORT}/{REDIS_DB}'


#
# Celery config
#
celery_app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

celery_app.conf.update(
    task_routes = {
        #'app.tasks.*': {'queue': 'default'},
        #'app.tasks.test_task': {'queue': 'testing'},
    }
)
