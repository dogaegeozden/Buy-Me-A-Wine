# LIBRARIES
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yh!twxuw(rq-^wh80i)ncdmi6$c0v36u^p)q*y)z249!0z6+sy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# A list for the allowed hosts. Hint: Do not include http/https in their domains
ALLOWED_HOSTS = []

# A list for installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wine_store.apps.WineStoreConfig',
    'stripe',
]

# A list for middlewares. "Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output. Each middleware component is responsible for doing some specific function. For example, Django includes a middleware component, AuthenticationMiddleware, that associates users with requests using sessions."
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Project's root's url configuration. Hint: The urls.py file in the root folder is containing url patters and configurations for STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT and debug tool bar
ROOT_URLCONF = 'Donation_project.urls'

# Templates settings to configure how django will look for templates, context processors and etc.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI: Web Server Gateaway Interface -> WSGI is a specification that describes the communication between web servers and Python web applications or frameworks. It explains how a web server communicates with python web applications/frameworks and how web applications/frameworks can be chained for processing a request.
WSGI_APPLICATION = 'Donation_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validators -> Password management is something that should generally not be reinvented unnecessarily, and Django endeavors to provide a secure and flexible set of tools for managing user passwords.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Language setting
LANGUAGE_CODE = 'en-us'

# Time zone setting for the web application
TIME_ZONE = 'America/Toronto'

# The goal of internationalization and localization is to allow a single Web application to offer its content in languages and formats tailored to the audience.
USE_I18N = True
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = Path(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    Path(BASE_DIR, 'static')
]

# A path setting to specify where the user uploaded files will be stored
MEDIA_URL = '/media/'

# A setting to serve user-uploaded media files
MEDIA_ROOT = Path(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Stripe Configuration
STRIPE_PUBLIC_KEY = "stripe public key here"
STRIPE_PRIVATE_KEY = "stripe private key here"
STRIPE_DONATION_PRODUCT_PRICE_ID = "stripe donation product price id here"
