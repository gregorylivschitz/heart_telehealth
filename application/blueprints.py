from application.views.admin import admin as admin_blueprint
from application.views.auth import auth as auth_blueprint
from application.views.home import home as home_blueprint
from application.views.graph import graph as graph_blueprint

all_blueprints = (admin_blueprint, auth_blueprint, home_blueprint, graph_blueprint)
