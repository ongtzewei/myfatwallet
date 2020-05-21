import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '46ryv($lnuq6%n4y(o@===$p21#yuvogd4j$fziq457p)0q&o8'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'XXX',                      # Or path to database file if using sqlite3.
        'USER': 'XXX',                      # Not used with sqlite3.
        'PASSWORD': 'XXX',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
        'ATOMIC_REQUESTS': True,
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}
                                    
# django default
ALLOWED_HOSTS = ('.cronuts.com',)

# used by django-hosts
PARENT_HOST = ''

# used by django-cors-headers
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_REPLACE_HTTPS_REFERER = False
CORS_ORIGIN_WHITELIST = ()

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_NAME = 'myfatwallet'
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN = '.'
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = SESSION_COOKIE_HTTPONLY = False
