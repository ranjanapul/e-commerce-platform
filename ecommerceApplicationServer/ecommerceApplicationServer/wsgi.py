"""
WSGI config for ecommerceApplicationServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerceApplicationServer.settings')# DJANGO_SETTINGS_MODULE is environment variable containing path to settings.py
# The other parameter is the value assigned to the variable

application = get_wsgi_application() # returns a wsgi callable for the current project.
# When a server receives a request, it uses this variable to invoke
# the project's wsgi application. This application processes the request and set up necessary configurations for reuqest handling
# returns it to the server for further handling
