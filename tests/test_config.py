#### Not valid for ####

# from flask import current_app
# from hashlib import sha256
# from unittest import TestCase
#
# from application import create_app
#
# SECRET_KEY_HASH = '446c5f36fdfbe509ba93e45fd3731af479698afc814b57dda70d56a56d419815'
# SQLALCHEMY_DATABASE_URI_DEV_HASH = '976e535a03884a3dda9652961e38f4d6a3344ffa46079f8b03b27ffe4fcc2ee1'
# SQLALCHEMY_DATABASE_URI_TEST_HASH = '3f32a46a4fd63f02e0edc8798afe36cfe6065894a5e66a9c242b525d8862ee39'
#
#
# def hash_it(input_text):
#     return sha256(input_text.encode()).hexdigest()
#
#
# class TestDevelopmentConfig(TestCase):
#     def setUp(self):
#         self.app = create_app(config='development')
#
#     def test_config_app_is_development(self):
#         self.assertTrue(hash_it(self.app.config['SECRET_KEY']) == SECRET_KEY_HASH)
#         self.assertTrue(self.app.config['DEBUG'] is True)
#         self.assertFalse(current_app is None)
#         self.assertTrue(hash_it(self.app.config['SQLALCHEMY_DATABASE_URI']) == SQLALCHEMY_DATABASE_URI_DEV_HASH)
#
#
# class TestTestingConfig(TestCase):
#     def setUp(self):
#         self.app = create_app(config='testing')
#
#     def test_config_app_is_testing(self):
#         self.assertTrue(hash_it(self.app.config['SECRET_KEY']) == SECRET_KEY_HASH)
#         self.assertTrue(self.app.config['DEBUG'])
#         self.assertTrue(self.app.config['TESTING'])
#         self.assertFalse(self.app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
#         self.assertTrue(hash_it(self.app.config['SQLALCHEMY_DATABASE_URI']) == SQLALCHEMY_DATABASE_URI_TEST_HASH)
#
#
# class TestProductionConfig(TestCase):
#     def setUp(self):
#         self.app = create_app(config='production')
#
#     def test_config_app_is_production(self):
#         self.assertTrue(hash_it(self.app.config['SECRET_KEY']) == SECRET_KEY_HASH)
#         self.assertFalse(self.app.config['DEBUG'])
#         self.assertFalse(self.app.config['TESTING'])
