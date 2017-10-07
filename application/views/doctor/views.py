from flask import render_template
from flask_login import login_required

from . import doctor


# @login_required
@doctor.route('/doctor/<int:doctor_id>')
@doctor.route('/dashboard/<int:doctor_id>')
def doctor_dashboard(doctor_id):
    # retived doctor object

    mock_pat = [
        {
            'id': 111,
            'name': "Jimmy",
            'age': 56,
            'weight': 85,
            'email': "jimmy@jimmy.com",
            'tel': 1234567890,
            'pings': 4,
            'high': 633,
            'low': 451,
            'last_ping': '2016-10-28'
        },
        {
            'id': 112,
            'name': "Sammy",
            'age': 47,
            'weight': 110,
            'email': "sammy@sammy.com",
            'tel': 6546541561,
            'pings': 7,
            'high': 721,
            'low': 523,
            'last_ping': '2017-04-18'
        },
        {
            'id': 124,
            'name': "Greg",
            'age': 29,
            'weight': 75,
            'email': "greg@greg.com",
            'tel': 4513576512,
            'pings': 2,
            'high': 672,
            'low': 510,
            'last_ping': '2016-11-15'
        },
        {
            'id': 278,
            'name': "Benny",
            'age': 62,
            'weight': 79,
            'email': "benny@benny.com",
            'tel': 8794506123,
            'pings': 8,
            'high': 607,
            'low': 492,
            'last_ping': '2017-02-10'
        }
    ]

    mock_pat = sorted(mock_pat, key=lambda x: x['last_ping'], reverse=True)

    return render_template('doctor/dashboard.html', doctor=None, doctor_id=doctor_id, patients=mock_pat)
    # doctor_obj[doctor_id].patients