#!/bin/sh
exec gunicorn --bind :8080 --workers 2 app:app
