from utilities.config import config


def route_app(url) -> str:
    return config('SUBDOMAIN') + '.' + config('APP_URL') + url
