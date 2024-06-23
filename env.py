import pathlib
from decouple import Config, RepositoryEnv  # from python-decouple

BASE_DIR = pathlib.Path(__file__).parent.parent
ENV_PATH = BASE_DIR / ".env"


def get_config():
    """Get configuration from .env file or os Environ"""
    if ENV_PATH.exists():
        return Config(RepositoryEnv(ENV_PATH))
    from decouple import config
    return config


config = get_config()
