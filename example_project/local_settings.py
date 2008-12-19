# Settings for devel server
import os
ROOT_PATH = os.path.dirname(__file__)
DEBUG = True
TEMPLATE_DEBUG = DEBUG
CACHE_BACKEND="locmem:///"
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(ROOT_PATH, 'example_portfolio.sqlite')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')
MEDIA_URL = 'http://127.0.0.1:8000/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'
