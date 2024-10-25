"""
Django settings for django_basic project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(".env", override=True)
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#set up neo4j
NEO4J_RESOURCE_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#h(3(brxlnwa#%h49ccp%3%)d6!m@_gqqhxw7#m7g5-@t6b^+*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# load environment variables


ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = ['https://*.agent.bap.jp', 
                        "https://*.bap-software.net", 
                        "https://*.bap.jp", 
                        'https://*.bappartners.com',
                        ]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

CORS_ALLOWED_ORIGINS = [
    'https://*.bappartners.com',
    'https://localhost:8000',
    'https://*.bap.jp'
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]



SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': True,
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    # 'LOGIN_URL': 'rest_framework:login',  # Configuring login URL for Swagger
    # 'LOGOUT_URL': 'rest_framework:logout',  # Configuring logout URL for Swagger
}

REDOC_SETTINGS = {
    'LAZY_RENDERING': False,
}


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core_app",
    "rest_framework",
    "rest_framework_swagger", # Django rest framework
    "drf_yasg", # Yet another swagger generator
    "corsheaders",
    "rest_framework.authtoken",
    "django_crontab", # cron job
]

ASGI_APPLICATION = "django_basic.asgi.application"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'core_app.authentication.BearerTokenAuthentication', 
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=30),
}


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # Thêm các backend khác nếu cần
]


CORS_ALLOW_ALL_ORIGINS = True


ROOT_URLCONF = "django_basic.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_basic.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ['DB_NAME'],
    'USER': os.environ['DB_USERNAME'],
    'PASSWORD': os.environ['DB_PASSWORD'],
    'HOST': os.environ['DB_HOST'],
    'PORT': os.environ['DB_PORT'],
    },


}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


SWAGGER_SETTINGS = {
   'USE_SESSION_AUTH': True
}


CRONTAB_COMMAND_PREFIX = f"DB_NAME={os.getenv('DB_NAME')} \
                        DB_HOST={os.getenv('DB_HOST')} \
                        DB_USERNAME={os.getenv('DB_USERNAME')} \
                        DB_PASSWORD={os.getenv('DB_PASSWORD')} \
                        DB_PORT={os.getenv('DB_PORT')} \
                        OPENAI_API_KEY={os.getenv('OPENAI_API_KEY')} \
                        OPENAI_API_BASE={os.getenv('OPENAI_API_BASE')}"

CRONJOBS = [
    ('*/1 * * * *', 'core_app.tasks.delete_old_facedata', '>> /tmp/django_crontab_log.log 2>&1'),
    # Add more cron jobs as needed
]


