import argparse
import os
import pathlib
import sys
from types import SimpleNamespace
from typing import Union
from configargparse import Namespace
from dotenv import load_dotenv, dotenv_values

from alembic.config import CommandLine, Config

# path to migration scripts
BASE_DIR_ALEMBIC = pathlib.Path(__file__).parent.parent.parent.parent
__base_path__ = f"{BASE_DIR_ALEMBIC}\\alembic\\"


def config_alembic(cmd_opts: Union[Namespace, SimpleNamespace]) -> Config:
    config = Config(file_=cmd_opts.config, ini_section=cmd_opts.name, cmd_opts=cmd_opts)

    config.set_main_option("script_location", __base_path__)
    if cmd_opts.pg_url:
        config.set_main_option("sqlalchemy.url", cmd_opts.pg_url)
    return config


def main():
    BASE_DIR = pathlib.Path(__file__).parent.parent.parent

    load_dotenv(os.path.join(BASE_DIR, ".env.backend"))
    sys.path.append(BASE_DIR)
    POSTGRES_DATABASE_URL = dotenv_values(".env.backend")["DATABASE_URL"]
    alembic = CommandLine()
    alembic.parser.formatter_class = argparse.ArgumentDefaultsHelpFormatter

    alembic.parser.add_argument(
        "--pg-url",
        default=POSTGRES_DATABASE_URL,
        help="Database URL .env.backend var: DATABASE_URL]",
    )

    options = alembic.parser.parse_args()
    if "cmd" not in options:
        alembic.parser.error("too few arguments")
        exit(128)
    else:
        config = config_alembic(options)
        exit(alembic.run_cmd(config, options))


if __name__ == "__main__":
    main()
