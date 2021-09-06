from src.config.common import *  # noqa

# Testing
INSTALLED_APPS += ('django_nose', )  # noqa
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['-s', '--nologcapture', '--with-progressive', '--with-fixture-bundling']

STATIC_URL = '/static/'
STATIC_ROOT = './static_files/'

DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"
MINIO_STORAGE_ENDPOINT = 'minio:9000'
MINIO_STORAGE_ACCESS_KEY = 'knotta'
MINIO_STORAGE_SECRET_KEY = 'knottapass'
MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'files'
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_STATIC_BUCKET_NAME = 'public'
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True

# These settings should generally not be used:
MINIO_STORAGE_MEDIA_URL = 'http://minio.local.knotta.ru:9000/files'
MINIO_STORAGE_STATIC_URL = 'http://minio.local.knotta.ru:9000/public'

THUMBNAIL_DEFAULT_STORAGE = 'minio_storage.storage.MinioMediaStorage'