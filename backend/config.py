from os import getenv
import os
from dotenv import dotenv_values

POSTGRES_DATABASE_URL = dotenv_values(".env.backend")["DATABASE_URL"]
