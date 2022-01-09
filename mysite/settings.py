import os

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration

load_dotenv(".env")

# -------------------------{DJANGO SETTINGS}----------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "https://chrisbarnes2000-37-boroughs-gr5v7pjw2vrr7-8000.githubpreview.dev",
    "boroughs37.herokuapp.com",
]
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True

ROOT_URLCONF = "mysite.urls"
WSGI_APPLICATION = "mysite.wsgi.application"

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Los_Angeles"
USE_I18N = True
USE_L10N = True
USE_TZ = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "rest_framework",
    "imagekit",
    "storages",
    "Boroughs",
    "users",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # 'allauth.socialaccount.providers.amazon',
    # 'allauth.socialaccount.providers.auth0',
    # 'allauth.socialaccount.providers.discord',
    # 'allauth.socialaccount.providers.dropbox',
    # 'allauth.socialaccount.providers.facebook',
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.google",
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.microsoft',
    # 'allauth.socialaccount.providers.paypal',
    # 'allauth.socialaccount.providers.patreon',
    # 'allauth.socialaccount.providers.reddit',
    # 'allauth.socialaccount.providers.robinhood',
    # 'allauth.socialaccount.providers.slack',
    # 'allauth.socialaccount.providers.spotify',
    # 'allauth.socialaccount.providers.steam',
    # 'allauth.socialaccount.providers.stripe',
    # 'allauth.socialaccount.providers.tumblr',
    # 'allauth.socialaccount.providers.twitch',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.vimeo_oauth2',
    # 'allauth.socialaccount.providers.windowslive',
]


# -------------------------{SENTRY SETTINGS}----------------------------------------------
sentry_sdk.init(
    dsn="https://60d120c25a6a40f89d5dc9291a3b8804@o1005817.ingest.sentry.io/6140350",
    integrations=[DjangoIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)


# -------------------------{APP SETTINGS}----------------------------------------------
# BOROUGH app settings
BOROUGH_TITLE_MAX_LENGTH = 200
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


# -------------------------{AUTH/ACCOUNT SETTINGS}----------------------------------------------
# Where to redirect during authentication
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
# Used by all_auth
SITE_ID = 1
AUTH_USER_MODEL = "users.CustomUser"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    # 'allauth.account.auth_backends.AuthenticationBackend',
)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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


# -------------------------{DATABASE SETTINGS}----------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# -------------------------{HTML SETTINGS}----------------------------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # Required for Heroku

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    #  Caching Middleware
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "boroughs37_cache",
    }
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
            # Always use forward slashes, even on Windows.
            # Don't forget to use absolute paths, not relative paths.
            os.path.join(BASE_DIR, "templates").replace("\\", "/"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]


# -------------------------{EMAIL SETTINGS}----------------------------------------------
ADMINS = [
    ("Chris", "christopher.barnes@students.makeschool.com"),
    ("Ariane", "ariane.evans@students.makeschool.com"),
    ("Alanna", "alanna.noguchi@students.makeschool.com"),
    ("Ian", "ian.rones@students.makeschool.com"),
]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_ACCOUNT")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s [%(asctime)s] %(module)s %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'file': {
#             'class': 'logging.handlers.RotatingFileHandler',
#             'formatter': 'verbose',
#             'filename': '/var/www/logs/ibiddjango.log',
#             'maxBytes': 1024000,
#             'backupCount': 3,
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file', 'console','mail_admins'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#     }
# }


# -------------------------{STATIC SETTINGS}----------------------------------------------
USE_S3 = os.getenv("USE_S3", False)

# if USE_S3:
# aws settings
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = "%s.s3.us-east-2.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
# s3 static settings
AWS_STATIC_LOCATION = "static"
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
STATICFILES_STORAGE = "mysite.storage_backends.StaticStorage"
# s3 public media settings
AWS_PUBLIC_MEDIA_LOCATION = "media/public"
DEFAULT_FILE_STORAGE = "mysite.storage_backends.PublicMediaStorage"
# s3 private media settings
AWS_PRIVATE_MEDIA_LOCATION = "media/private"
PRIVATE_FILE_STORAGE = "mysite.storage_backends.PrivateMediaStorage"
# else:
#     STATIC_URL = '/static/'
#     STATICFILE_DIRECTORY = 'static'
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# PROTIP:
# Need to override settings? Create a local_settings.py file
# in this directory, and add settings there.
try:
    from mysite.local_settings import *
except ImportError:
    pass
