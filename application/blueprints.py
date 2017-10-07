from application.views.admin import admin as admin_blueprint
from application.views.auth import auth as auth_blueprint
from application.views.home import home as home_blueprint
from application.views.graph import graph as graph_blueprint
from application.views.doctor import doctor as doctor_blueprint
from application.views.patient import patient as patient_blueprint

all_blueprints = (admin_blueprint, auth_blueprint, home_blueprint, graph_blueprint, doctor_blueprint, patient_blueprint)
