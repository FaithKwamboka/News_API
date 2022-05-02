import os

class Config:
    """
    General configuration parent class
    """
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=3e9f12e36a594b67bb9dd46de28e3162'
    ALL_NEWS_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=3e9f12e36a594b67bb9dd46de28e3162'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}