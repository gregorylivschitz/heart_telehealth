import random

from flask import render_template
from flask_login import login_required
from application.mock import get_mock_pat
from . import patient


# @login_required
@patient.route('/patient/<int:patient_id>')
def patient_dashboard(patient_id):
    mock_pat = get_mock_pat()
    for patient in mock_pat:
        if patient['id'] == patient_id:
            return render_template('patient/dashboard.html', patient=patient)
    return render_template('patient/no_found.html')