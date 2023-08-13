#!/bin/bash
git fetch && git reset origin/main --hard

git pull

source python3-virtualenv/bin/activate

pip install -r requirements.txt

docker stop $(docker ps -a -q)

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build