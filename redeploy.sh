#!/bin/bash

tmux kill-server

tmux new 

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate || exit

pip install -r requirements.txt

flask run