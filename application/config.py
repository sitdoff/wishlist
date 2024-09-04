from environs import Env

env = Env()
env.read_env()


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = env("SECRET_KEY") or "SECRET_KEY"
    SQLALCHEMY_DATABASE_URI = env("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    PORT = 8000
