import unittest
from api import *


class TestChineseTextAPI(unittest.TestCase):

    def test_getcapabilities(self):
        response = getcapabilities()
        self.assertIsInstance(response, dict)

    def test_getcharacter(self):
        response = getcharacter(char='仁')
        self.assertIsInstance(response, dict)
        self.assertIn('char', response)

    def test_getdictionaryheadwords(self):
        response = getdictionaryheadwords()
        self.assertIsInstance(response, dict)

    def test_getdynasties(self):
        response = getdynasties()
        self.assertIsInstance(response, dict)

    def test_getlink(self):
        response = getlink(urn='ctp:analects/xue-er')
        self.assertIsInstance(response, dict)

    def test_getstats(self):
        response = getstats()
        self.assertIsInstance(response, dict)

    def test_getstatus(self):
        response = getstatus()
        self.assertIsInstance(response, dict)

    def test_gettext(self):
        response = gettext(urn='ctp:analects/xue-er')
        self.assertIsInstance(response, dict)

    def test_gettextinfo(self):
        response = gettextinfo(urn='ctp:analects/xue-er')
        self.assertIsInstance(response, dict)

    def test_gettexttitles(self):
        response = gettexttitles()
        self.assertIsInstance(response, dict)

    def test_readlink(self):
        response = readlink(url='http://ctext.org/analects/xue-er/zhs')
        self.assertIsInstance(response, dict)

    def test_searchtexts(self):
        response = searchtexts(title='論語')
        self.assertIsInstance(response, dict)


if __name__ == '__main__':
    unittest.main()