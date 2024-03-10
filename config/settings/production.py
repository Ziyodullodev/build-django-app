from config.settings.base import *

DEBUG = False

CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    # add your frontend url here
    "http://localhost:8000",
    "http://127.0.0.1:9000",
]

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
)
    
CSRF_TRUSTED_ORIGINS = ['localhost:8000']


