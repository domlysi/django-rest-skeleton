from .common import *

DEBUG = True

WSGI_APPLICATION = '{{ project_name }}.wsgi.dev.application'

ALLOWED_HOSTS += ['*']

CORS_ALLOW_ALL_ORIGINS = True

# uncomment the following line to include i18n
# from .i18n import *

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname}\t{name}\t{message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'WARNING',
        },
        'apps': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
    }
}
