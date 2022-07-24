#!/bin/sh

echo "$(date +'%Y-%m-%dT%H:%M:%S') Starting worker"

su -m celery_user -c "celery -A tasks worker --pool=gevent --concurrency=20 --loglevel=INFO --logfile=/app/logs/celery.log"
