from flask import Flask
from os.path import abspath, dirname, join

from application import router
from application.blueprints import all_blueprints
from application.extensions import assets, compress, db, htmlmin, login_manager, migrate
from application.database import models
from config import app_config

APP_ROOT_FOLDER = abspath(dirname(router.__file__))
TEMPLATE_FOLDER = join(APP_ROOT_FOLDER, 'templates')
STATIC_FOLDER = join(APP_ROOT_FOLDER, 'static')


def create_app(config='development'):

    app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER, instance_relative_config=True)
    # load instance config before object config
    app.config.from_pyfile('config.py')
    app.config.from_object(app_config[config])

    # Initialize extensions
    compress.init_app(app)
    assets.init_app(app)
    db.init_app(app)
    htmlmin.init_app(app)
    migrate.init_app(app, db)

    # configuring extensions
    # needed for fixing webassets.env.RegisterError: Another bundle is already registered as ...
    assets._named_bundles = {}
    assets.from_yaml(join(APP_ROOT_FOLDER, 'web-assets.yaml'))

    for bp in all_blueprints:
        app.register_blueprint(bp)

    router.init_app(app)

    return app
