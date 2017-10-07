from flask import render_template
from flask_login import login_required

from . import patient


# @login_required
@patient.route('/dashboard/<int:patient_id>')
def patient_dashboard(patient_id):
    # retived doctor object
    return render_template('patient/dashboard.html', patient=None, P_ID=patient_id)
