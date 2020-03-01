#!/bin/sh
exec gunicorn --bind :$PORT app:app
