#!/bin/bash
git fetch && git reset origin/main --hard

tmux kill-server

tmux new-session -d -s deploy

tmux send-keys 'source python3-virtualenv/bin/activate' C-m

tmux send-keys 'pip install -r requirements.txt' C-m

tmux send-keys 'flask run' C-m

echo "website up and running"
