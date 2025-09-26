from decouple import Config, RepositoryEnv

from backend.utils.timedelta import parse_timespan

import os
import logging

config = Config(RepositoryEnv("local.env"))
CORS_ORIGIN = "http://localhost:3000"

if os.getenv("ENVIRONMENT") == "STAGE":
    config = Config(RepositoryEnv("stage.env"))
    CORS_ORIGIN = "https://staging.example.com"

if os.getenv("ENVIRONMENT") == "PRODUCTION":
    config = Config(RepositoryEnv("prod.env"))
    CORS_ORIGIN = "https://example.com"

MONGO_URI = config.get("MONGO_URI")
PORT = config.get("PORT", cast=int)

SMTP_MAIL = config.get("MAIL")
SMTP_HOST = config.get("HOST")
SMTP_USER = config.get("USER_NAME")
SMTP_PASS = config.get("PASSWORD")
SMTP_PORT = config.get("MAILPORT", cast=int)
SMTP_TLS = config.get("SECURE", cast=bool)
