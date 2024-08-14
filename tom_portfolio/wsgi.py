"""
WSGI config for tom_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tom_portfolio.settings')

application = get_wsgi_application()
<<<<<<< HEAD
app =application
=======
app = application
>>>>>>> efe42a339669e9f1d05e3a8b23c57125d4a78f5b
