#!/usr/bin/env python
# coding: utf-8

import os,django
from django.core.handlers.wsgi import WSGIHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djsite.settings")
django.setup()
application = WSGIHandler()
