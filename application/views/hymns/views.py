from flask import render_template

from . import hymns, helper, scraper


@hymns.route('/<int:number>', methods=['GET', 'POST'])
def render_hymns(number):
    # if str(request.referrer) == 'http://localhost:5000':
    if helper.check(open_file=hymns.open_resource, number=number, path=hymns.root_path):
        return render_template('hymns/hymn-viewer.html', open_file=hymns.open_resource, number=number)
    else:
        status = scraper.download(path=hymns.root_path, number=number)
        if status:
            return render_template('hymns/hymn-viewer.html', open_file=hymns.open_resource, number=number)
        else:
            return render_template('hymns/hymn-viewer.html', open_file=hymns.open_resource, number=None)


HYMNS_ROOT = hymns.root_path
