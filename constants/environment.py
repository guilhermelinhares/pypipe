import os

DEFAULT_WORKSPACE = os.getenv("DEFAULT_WORKSPACE", "/tmp/")
DEFAULT_TECHNOLOGY = os.getenv("DEFAULT_TECHNOLOGY", None)
APP = os.getenv("APP_NAME", None)
APP_NAME_GIT = os.getenv("APP_NAME_GIT", None)
ENVIRONMENT = os.getenv("ENVIRONMENT", None)
BRANCH_TAG = os.getenv("BRANCH_TAG", None)
GIT_PROJECT = os.getenv("GIT_PROJECT", "sistemas")
VAULT_URL = os.getenv("VAULT_ADDR", "http://vault:8200")
VAULT_ROLE_ID = os.getenv("ROLE_ID", None)
VAULT_SECRET_ID = os.getenv("SECRET_ID", None)
