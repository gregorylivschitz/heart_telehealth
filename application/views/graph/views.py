import random

from flask import render_template, jsonify
from flask_login import login_required
import pandas as pd
from . import graph

import numpy as np
from scipy.integrate import simps
from numpy import trapz
import datetime



@graph.route('/graph')
def graph():
    # tone_data = pd.read_csv('tone_data')
    values, labels = patient_get_graph()
    return render_template('graph/output.html', values=values, labels=labels)

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