from flask_assets import Environment
from flask_compress import Compress
from flask_htmlmin import HTMLMIN
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# variable initializations
db = SQLAlchemy()
htmlmin = HTMLMIN()
assets = Environment()
login_manager = LoginManager()
migrate = Migrate()
compress = Compress()

login_manager.login_view = 'You must be logged in to access this page'
login_manager.login_message = 'auth.login'
