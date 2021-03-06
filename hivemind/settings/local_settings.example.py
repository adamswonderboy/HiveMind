"""
Example file for local_settings.py

Copy this specific file an rename it to local_settings.py with
the correct settings for your local environment.
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hivemind',
        'USER': 'ruitech',
        'PASSWORD': 'ruitech',
        'HOST': 'localhost',
        'PORT': '',
    }
}

TIME_ZONE = 'UTC+3'
