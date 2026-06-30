#!/usr/bin/env bash
# Render build script — run as the "Build Command": ./build.sh
set -o errexit

pip install -r requirements.txt

# Collect static files so WhiteNoise can serve admin + DRF browsable API CSS
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
