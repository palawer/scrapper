from celery.utils.log import get_task_logger
from config import celery_app
from utils import save_json
import requests
import uuid


logger = get_task_logger(__name__)


@celery_app.task(name='test_task')
def test_task(i, *args, **kwargs):
    logger.info(f'test task {i}')
    return i


@celery_app.task(name='get_url')
def get_url(url, *args, **kwargs):
    try:
        r = requests.get(url)
        data = r.json()
        
        filename = f'result_{str(uuid.uuid4())}.json'
        save_json(data, filename)
        
        return r.status_code
    except Exception as e:
        logger.error(e)
