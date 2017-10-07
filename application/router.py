from flask import url_for


def init_app(app):
    # favicon
    @app.route('/favicon.ico')
    def favicon():
        return url_for('static', filename='images/favicon.64x64.png')

    # Apple Stuff
    @app.route('/apple-touch-icon-152x152-precomposed.png')
    @app.route('/apple-touch-icon-152x152.png')
    @app.route('/apple-touch-icon.png')
    def apple():
        return url_for('static', filename='images/apple-touch-icon-152x152.png')
