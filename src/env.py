import io
import os
import pathlib
from functools import lru_cache

# from python-decouple
from decouple import Config, RepositoryEmpty, RepositoryEnv

# maps to "path/to/project"
BASE_DIR = pathlib.Path(__file__).parent.parent

# ensure that `.env` is listed in `.gitignore`
ENV_PATH = BASE_DIR / ".env"

def get_config():
    """Get configuration from .env file or os.environ"""
    if ENV_PATH.exists():
        return Config(RepositoryEnv(ENV_PATH))
    from decouple import config
    return config

config = get_config()
