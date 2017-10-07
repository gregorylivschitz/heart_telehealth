class Config(object):
    """Common configurations"""
    MINIFY_PAGE = True
    SSL_DISABLE = False

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class DevelopmentConfig(Config):
    """Development configurations"""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    TESTING = False


class TestingConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://cmc_admin_tester:etKh5KL36!qOKm4o@localhost/cmc_testing'


class ProductionConfig(Config):
    """Production configurations"""
    DEBUG = False

app_config = {
    'development': 'config.DevelopmentConfig',
    'production': 'config.ProductionConfig',
    'testing': 'config.TestingConfig'
}
