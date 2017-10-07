from os import makedirs, removedirs, listdir, remove
from os.path import join
from unittest import TestCase

from application.views.hymns import helper, scraper
from application.views.hymns.views import HYMNS_ROOT


class TestWebCrawling(TestCase):
    WORKING_DIR = join('temp', 'static', 'hymns')

    @classmethod
    def setUpClass(cls):
        makedirs(cls.WORKING_DIR)

    @classmethod
    def tearDownClass(cls):
        removedirs(cls.WORKING_DIR)

    def setUp(self):
        self.reset_dir()

    def tearDown(self):
        self.reset_dir()

    def reset_dir(self):
        file_list = listdir(self.WORKING_DIR)
        for each in file_list:
            remove(join(self.WORKING_DIR, each))

    def test_helper_exists(self):
        assert helper.check(open, '724351', path=HYMNS_ROOT)

    def test_helper_not_exists(self):
        assert helper.check(open, '123213123213', path=HYMNS_ROOT) is False

    def test_scrapper_normal(self):
        assert scraper.download('temp', '404') is True

    def test_scrapper_hope_publishing(self):
        assert scraper.download('temp', '120') is True

    def test_scrapper_does_not_exist(self):
        assert scraper.download('temp', '3454235') is False

    def test_scrapper_unavailable(self):
        # only image available
        assert scraper.download('temp', '62') is False
        # nothing available
        assert scraper.download('temp', '54') is False
