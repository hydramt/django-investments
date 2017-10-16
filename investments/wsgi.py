"""
WSGI config for investments project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

# add the hellodjango project path into the sys.path
sys.path.append('/home/nginx/portfolios/investments')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/nginx/portfolios/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "investments.settings")

application = get_wsgi_application()
