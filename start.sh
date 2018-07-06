#!/bin/bash
export PYTHONPATH=$pwd
export DJANGO_SETTINGS_MODULE=feed_service.db.settings.settings
python feed_service/conf/service_app.py
