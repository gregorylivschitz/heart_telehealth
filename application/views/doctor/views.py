from flask import render_template
from flask_login import login_required
from application.mock import get_mock_pat
from . import doctor

import pandas as pd
import numpy as np
from scipy.integrate import simps
from numpy import trapz
import datetime



# @login_required
@doctor.route('/doctor/<int:doctor_id>')
@doctor.route('/dashboard/<int:doctor_id>')
def doctor_dashboard(doctor_id):
    # retived doctor object

    mock_pat = get_mock_pat()
    mock_pat = sorted(mock_pat, key=lambda x: x['last_ping'], reverse=True)

    values, labels = patient_get_graph()
    for mock_pat_1 in mock_pat:
        values, labels = patient_get_graph()
        mock_pat_1['values'] = values
        mock_pat_1['labels'] = labels
        mock_pat_1['high'] = max(values)
        mock_pat_1['low'] = min(values)
    return render_template('doctor/dashboard.html', doctor=None, doctor_id=doctor_id, patients=mock_pat)
    # doctor_obj[doctor_id].patients


def patient_get_graph():
    multiple_tone = []
    for index, i in enumerate(range(0,24)):
        time_date = datetime.datetime.now() + datetime.timedelta(seconds=index)
        print(time_date)
        tone_data = pd.DataFrame({'tone': [105 , 115, 130, 120, 122, 105], 'time':[time_date,
                                                                                   time_date + datetime.timedelta(seconds=1),
                                                                                   time_date + datetime.timedelta(seconds=2),
                                                                                   time_date + datetime.timedelta(seconds=3),
                                                                                   time_date + datetime.timedelta(seconds=4),
                                                                                   time_date + datetime.timedelta(seconds=5)]})
        print(time_date + datetime.timedelta(seconds=1))
        tone_data['rand_num'] = np.random.randint(0,5, size=len(tone_data))
        tone_data['tone'] = tone_data['tone'] + tone_data['rand_num']
        multiple_tone.append(tone_data)

    multiple_tone_df = pd.concat(multiple_tone, ignore_index=True)


    size=len(multiple_tone_df)/6
    size = np.math.floor(size)
    add_integral = []
    labels = []
    values = []
    for i in range(0,size,6):
        if i == 0:
            integral_calc = multiple_tone[i:i+5]
        else:
            integral_calc = multiple_tone[i-5:i]
        # numpy_values = integral_calc.values
        time_things = integral_calc[0].ix[0, ('time')]
        y = integral_calc[0].loc[:, ('tone')]
        area = simps(y, dx=1)
        add_integral.append((area, time_things))
        for value, label in add_integral:
            labels.append(label)
            values.append(value)
    print(labels)
    print(values)
    return values, labels