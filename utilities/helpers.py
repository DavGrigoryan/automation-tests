from utilities.config import config

COMPANY_ID = 2
ADMINISTRATOR_ID = 3


def route_app(url) -> str:
    return config('SUBDOMAIN') + '.' + config('APP_URL') + url
