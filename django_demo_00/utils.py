""" common methods & csts that may be useful somewhere else as well """
# import logging

def get_logs_configs():
    """ configures the logs. logs should be setup from settings.py in django.

        a logger has 4 parts (at most): logger, handler, filter, formatter. 2 main ways of organising logs:

        * with logging.getLogger(__name__): this will instantiate 1 logger per module

        * with logging.getLogger('project.somemodule.someotherthing'): this is a hierarchical naming

    """
    # from the doc - adapted slightly & commented
    LOGGING = {
        'version': 1,                               # python's logging module. currently only 1 version schema, but this will allow for backward compatibility easily
                                                    # all other keys are optional

        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'filters': {

            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                # 'filters': ['special']
            },
            'file': {
                'level':'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'verbose',
                'filename': 'test_logs.log',
                # 'maxBytes': 1e7,
                # 'backupCount':3,
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'myproject.custom': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
            }
        }
    }


    return LOGGING