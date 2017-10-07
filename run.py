import os
import unittest

from application import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    app.run()
