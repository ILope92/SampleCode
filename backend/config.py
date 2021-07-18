from os import getenv
import os
from dotenv import dotenv_values

POSTGRES_DATABASE_URL = dotenv_values(".env.backend")["DATABASE_URL"]
# Email service
NAME_SERVICE = dotenv_values(".env.backend")["NAME_SERVICE"]
EMAIL = dotenv_values(".env.backend")["EMAIL"]
PASSWORD = dotenv_values(".env.backend")["PASSWORD"]
SERVER_SMPT = dotenv_values(".env.backend")["SERVER_SMPT"]
#
HOST_URL = dotenv_values(".env.backend")["HOST_URL"]
