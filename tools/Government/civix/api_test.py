import unittest
from api import get_content, get_document, search_content


class TestCiviXAPI(unittest.TestCase):

    def test_get_content(self):
        response = get_content(aspect='complete')
        self.assertIn(b"<root>", response)  # Checking if response contains XML root

    def test_get_document(self):
        response = get_document(index_id='statreg', document_id='01009_01', xml=True)
        self.assertIn(b"<act:act", response)  # Checking if response contains act namespace

    def test_search_content(self):
        response = search_content(query='water', aspect='complete')
        self.assertIn(b"<results", response)  # Checking if response contains results tag


if __name__ == '__main__':
    unittest.main()