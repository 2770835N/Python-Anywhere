"""
WSGI config for startprojectwas_project1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
path = os.path.expanduser('~/startprojectwas_project1')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'startprojectwas_project1.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
