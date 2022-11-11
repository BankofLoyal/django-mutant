from __future__ import unicode_literals

from .postgresql_psycopg2 import *  # NOQA
from settings import INSTALLED_APPS

DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

INSTALLED_APPS.extend([
    'django.contrib.gis',
    'mutant.contrib.geo',
])
