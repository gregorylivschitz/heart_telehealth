from flask import Blueprint

hymns = Blueprint('hymns', __name__, url_prefix='/hymns')

from . import views
