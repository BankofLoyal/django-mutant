from __future__ import unicode_literals

from django.conf import settings
from django.core.cache import DEFAULT_CACHE_ALIAS

STATE_HANDLER = getattr(
    settings, 'MUTANT_STATE_HANDLER',
    'mutant.state.handlers.memory.MemoryStateHandler'
)

STATE_CACHE_ALIAS = getattr(
    settings, 'MUTANT_STATE_CACHE_ALIAS', DEFAULT_CACHE_ALIAS
)

STATE_PUBSUB = getattr(
    settings, 'MUTANT_STATE_PUBSUB', (
        'mutant.state.handlers.pubsub.engines.Redis', {}
    )
)

INSTALLED_APPS = [
    'django.contrib.auth',  # This is needed because of django bug
    'django.contrib.contenttypes',
    'polymodels',
    'mutant',
    'tests',
    'mutant.contrib.boolean',
    'mutant.contrib.temporal',
    'mutant.contrib.file',
    'mutant.contrib.numeric',
    'mutant.contrib.text',
    'mutant.contrib.web',
    'mutant.contrib.related',
]