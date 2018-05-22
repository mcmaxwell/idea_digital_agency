import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

def debug(context):
  return {'DEBUG': DEBUG}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'idea/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'idea.local_settings.debug',
                'info.context_processors.info',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '../de1v/static')

STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, "../builds/static"),
    os.path.join(BASE_DIR, "../dev/static"),
]
