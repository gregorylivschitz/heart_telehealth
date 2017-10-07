from unittest import TestCase

from application import create_app, db


class DBTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(config='testing')

    def setUp(self):
        self.db = db
        self.db.create_all()
        self.db.session.commit()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_db_connection(self):
        pass
