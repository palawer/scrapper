#!/bin/sh

echo "$(date +'%Y-%m-%dT%H:%M:%S') Starting API"

su -m api_user -c "uvicorn main:app --host 0.0.0.0 --port 5000 --reload"
