import unittest
from api import view_basic_access, search_records, search_media, search_recordsets, create_map

class TestIdigibioAPI(unittest.TestCase):

    def test_view_basic_access(self):
        response = view_basic_access(uuid='c5e7b8fe-7f33-404e-96cc-35a201a4b1d9')
        self.assertIn('uuid', response)
    
    def test_search_records(self):
        response = search_records() # rq={"data.dwc:kingdom": "Animalia"}, limit=1
        self.assertIn('itemCount', response)
        self.assertEqual(response['itemCount'], 142693702)
    
    def test_search_media(self):
        response = search_media() # mq={"data.dwc:kingdom": "Animalia"}, limit=1
        self.assertIn('itemCount', response)
        self.assertEqual(response['itemCount'], 57048555)
    
    def test_search_recordsets(self):
        response = search_recordsets() # rsq={"uuid": "137ed4cd-5172-45a5-acdb-8e1de9a64e32"}, limit=1
        self.assertNotIn('error', response)

    def test_create_map(self):
        response = create_map(rq={"data.dwc:kingdom": "Animalia"})
        self.assertIn('shortCode', response)
        self.assertNotIn('error', response)

if __name__ == '__main__':
    unittest.main()