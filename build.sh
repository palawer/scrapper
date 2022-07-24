#!/bin/bash

docker-compose up -d --build --scale worker=1 --remove-orphans
