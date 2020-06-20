#!/bin/sh
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
python3 get_trends.py
python3 sync_credentials.py -y
