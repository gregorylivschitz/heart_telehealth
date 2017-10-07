from unittest import TestCase

from application import create_app


class TestAllRoutes(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.tc = cls.app.test_client()

    def test_routes_apple_stuff(self):
        response = self.tc.get('/apple-touch-icon-152x152.png')
        assert response.status_code == 200

        response = self.tc.get('/apple-touch-icon.png')
        assert response.status_code == 200

        response = self.tc.get('/apple-touch-icon-152x152-precomposed.png')
        assert response.status_code == 200

    def test_routes_favicon(self):
        response = self.tc.get('/favicon.ico')
        assert response.status_code == 200

    def test_routes_blueprint_home(self):
        response = self.tc.get('/')
        assert response.status_code == 200

        response = self.tc.get('/index.html')
        assert response.status_code == 200

        # response = self.tc.get('/dashboard')
        # assert response.status_code == 200

    def test_routes_blueprint_hymns(self):
        response = self.tc.get('/hymns/724351')
        assert response.status_code == 200
        assert 'dummy file'.encode() in response.data

        response = self.tc.post('/hymns/724351')
        assert response.status_code == 200
        assert 'dummy file'.encode() in response.data
