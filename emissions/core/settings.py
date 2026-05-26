import os
import dj_database_url

from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta


# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()


# ==========================================
# Base Directory
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# Security
# ==========================================

SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'django-insecure-change-this-key'
)

DEBUG = os.getenv(
    'DJANGO_DEBUG',
    'False'
) == 'True'

ALLOWED_HOSTS = ['*']


# ==========================================
# Installed Apps
# ==========================================

INSTALLED_APPS = [

    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Apps
    'rest_framework',
    'django_filters',
    'corsheaders',
    'drf_spectacular',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',

    # Local Apps
    'authentication',
    'companies',
    'emissions',
    'ingestion',
    'audits',
    'reviews',
]


# ==========================================
# Middleware
# ==========================================

MIDDLEWARE = [

    # CORS
    'corsheaders.middleware.CorsMiddleware',

    # Django Middleware
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==========================================
# URL Configuration
# ==========================================

ROOT_URLCONF = 'core.urls'


# ==========================================
# Templates
# ==========================================

TEMPLATES = [
    {
        'BACKEND':
            'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

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


# ==========================================
# WSGI
# ==========================================

WSGI_APPLICATION = 'core.wsgi.application'


# ==========================================
# Database
# ==========================================

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}


# ==========================================
# Password Validation
# ==========================================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ==========================================
# Internationalization
# ==========================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# ==========================================
# Static Files
# ==========================================

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# ==========================================
# Default Auto Field
# ==========================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==========================================
# CORS SETTINGS
# ==========================================

# Allow all origins
CORS_ALLOW_ALL_ORIGINS = True

# Allow credentials
CORS_ALLOW_CREDENTIALS = True

# Allowed Headers
CORS_ALLOWED_HEADERS = [
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

# Allowed Methods
CORS_ALLOWED_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]


# ==========================================
# Django REST Framework
# ==========================================

REST_FRAMEWORK = {

    # Swagger Schema
    'DEFAULT_SCHEMA_CLASS':
        'drf_spectacular.openapi.AutoSchema',

    # JWT Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),

    # Permissions
    'DEFAULT_PERMISSION_CLASSES': (

        'rest_framework.permissions.IsAuthenticated',

    ),

    # Filters
    'DEFAULT_FILTER_BACKENDS': [

        'django_filters.rest_framework.DjangoFilterBackend',

        'rest_framework.filters.SearchFilter',

        'rest_framework.filters.OrderingFilter',
    ],

    # Pagination
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',

    'PAGE_SIZE': 10,
}


# ==========================================
# JWT Settings
# ==========================================

SIMPLE_JWT = {

    'ACCESS_TOKEN_LIFETIME':
        timedelta(minutes=60),

    'REFRESH_TOKEN_LIFETIME':
        timedelta(days=7),

    'ROTATE_REFRESH_TOKENS': True,

    'BLACKLIST_AFTER_ROTATION': True,

    'AUTH_HEADER_TYPES': ('Bearer',),

    'USER_ID_FIELD': 'id',

    'USER_ID_CLAIM': 'user_id',
}


# ==========================================
# Swagger / Redoc
# ==========================================

SPECTACULAR_SETTINGS = {

    'TITLE':
        'ESG Emissions Tracking API',

    'DESCRIPTION':
        'Enterprise ESG & Carbon Emissions Management Backend API',

    'VERSION':
        '1.0.0',

    'SERVE_INCLUDE_SCHEMA': False,
}