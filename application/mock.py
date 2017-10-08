import random


def get_mock_pat():
    mock_pat = [
    {
    'id': 1,
    'name': "Jimmy",
    'age': 56,
    'weight': 85,
    'email': "jimmy@jimmy.com",
    'tel': 1234567890,
    'pings': 4,
    'high': 633,
    'low': 451,
    'last_ping': '2016-10-28',
    'status': True
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
    'last_ping': '2017-10-08',
    'status': False
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
    'last_ping': '2016-11-15',
    'status': True
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
    'last_ping': '2017-02-10',
    'staus': False
    }
    ]
    doctor = [{'name':'John Smith', 'email': 'jf837@nyu.edu', 'phone':'777-4444'},
              {'name':'Bob Goldberg', 'email': 'bg837@nyu.edu', 'phone':'553-3465'},
              {'name':'Greg Livschitz', 'email': 'gl837@nyu.edu', 'phone':'332-6578'},
              {'name':'Andrew Jeep', 'email': 'aj837@nyu.edu', 'phone':'223-5764'}]
    nurse = [{'name':'Adelia Young', 'email': 'jf837@nyu.edu', 'phone':'777-4444'},
             {'name':'Agatha Lee', 'email': 'bg837@nyu.edu', 'phone':'553-3465'},
             {'name':'Florence Ram', 'email': 'gl837@nyu.edu', 'phone':'332-6578'},
             {'name':'Frederica Sd', 'email': 'aj837@nyu.edu', 'phone':'223-5764'}]

    for mock_pat_1 in mock_pat:
        mock_pat_1['doctor'] = random.choice(doctor)
        mock_pat_1['nurse'] = random.choice(nurse)
    return mock_pat