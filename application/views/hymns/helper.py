from os.path import join


def check(open_file, number, path):
    try:
        open_file(join(path, 'static', 'hymns', '{}.txt'.format(number)), 'r')
    except FileNotFoundError:
        return False
    return True
