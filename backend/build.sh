#!/usr/bin/env bash
set -o errexit

python -m pip install -r requirements.txt
python src/manage.py collectstatic --no-input
python src/manage.py migrate
python src/manage.py seed_db
