from os.path import join as os_path_join
from robobrowser import RoboBrowser as RB


def download(path, number):
    browser = RB(parser='html.parser')
    browser.open('https://hymnary.org/hymn/UMH/{}'.format(number))
    raw_hymn = browser.select('#text')
    license_agreement = browser.select('.accept_license_box')

    if license_agreement:
        forms = browser.get_forms()
        forms[-1]['hymnalID'] = 'UMH'
        forms[-1]['number'] = number
        browser.submit_form(forms[-1])
        raw_hymn = browser.select('.licensed_border')
        raw_hymn[-1].div.decompose()

    if not raw_hymn:
        return False

    cleaned_hymn = []
    for each_stanza in raw_hymn[-1].find_all('p'):
        cleaned_hymn.append([each for each in each_stanza.stripped_strings])

    with open(os_path_join(path, 'static', 'hymns', '{}.txt'.format(number)), 'w') as f:
        for each_stanza in cleaned_hymn:
            for each_line in each_stanza:
                f.write(each_line + '\n')
            f.write('\n')
        f.close()

    return True
