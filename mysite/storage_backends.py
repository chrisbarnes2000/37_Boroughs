from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    if settings.USE_S3:
        location = settings.AWS_STATIC_LOCATION
        default_acl = 'public-read'
    else:
        location = 'static'

class PublicMediaStorage(S3Boto3Storage):
    if settings.USE_S3:
        location = settings.AWS_PUBLIC_MEDIA_LOCATION
        default_acl = 'public-read'
        file_overwrite = False
    else:
        location = 'media'

class PrivateMediaStorage(S3Boto3Storage):
    if settings.USE_S3:
        location = settings.AWS_PRIVATE_MEDIA_LOCATION
        default_acl = 'private'
        file_overwrite = False
        custom_domain = False
    else:
        location = 'private'
