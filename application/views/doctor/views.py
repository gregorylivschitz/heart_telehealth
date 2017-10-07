from flask import render_template
from flask_login import login_required

from . import doctor


# @login_required
@doctor.route('/doctor/<int:doctor_id>')
@doctor.route('/dashboard/<int:doctor_id>')
def doctor_dashboard(doctor_id):
    # retived doctor object

    mock_pat = {
        111: {
            'name': "patient 1",
            'age': 56,
            'pings': 100
        }
    }

    return render_template('doctor/dashboard.html', doctor=None, doctor_id=doctor_id, patients=None)
    # doctor_obj[doctor_id].patients