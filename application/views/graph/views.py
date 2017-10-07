from flask import render_template
# import pandas as pd
from . import graph
#
#
# import numpy as np
# # from scipy.integrate import simps
# from numpy import trapz
# import datetime
#


@graph.route('/graph')
def graph():
    # # tone_data = pd.read_csv('tone_data')
    #
    # multiple_tone = []
    # for i in range(0,20):
    #     time_date = datetime.datetime.now()
    #     # rand.in
    #     tone_data = pd.DataFrame({'tone': [105, 115, 130, 120, 122, 105], 'time':[time_date,
    #                                                                 tone_data + datetime.timedelta(seconds=1),
    #                                                                 tone_data + datetime.timedelta(seconds=2),
    #                                                                 tone_data + datetime.timedelta(seconds=3),
    #                                                                 tone_data + datetime.timedelta(seconds=4),
    #                                                                 tone_data + datetime.timedelta(seconds=5)]})
    #     multiple_tone.append(tone_data)
    # multiple_tone_df = pd.concat(multiple_tone, ignore_index=True)
    # multiple_tone_df.to_csv("C:\\Users\\greg1\\dev\\heart_telehealth\\test_data.csv")
    #
    # The y values.  A numpy array is used here,
    # but a python list could also be used.
    # y = np.array([135, 125, 120, 115, 117])
    #
    # Compute the area using the composite trapezoidal rule.
    # area = trapz(y, dx=1)
    # Compute the area using the composite Simpson's rule.
    # area = simps(y, dx=1)
    area = 481
    # print("area =", area)
    return render_template('graph/output.html', area=area, URL_list=['test1', 'test2'])
