"""
WSGI config for asalps_core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asalps_core.settings')

application = get_wsgi_application()

# Automatically seed data whenever the live app boots up
try:
    from django.core.management import call_command
    call_command('seed_data')
except Exception as e:
    print(f"Seeding error: {e}")