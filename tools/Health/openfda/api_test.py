import unittest
from api import get_animal_adr, get_drug_event, get_drug_label, get_device_event, get_device_udi

class TestOpenFDAAPI(unittest.TestCase):

    def test_get_animal_adr(self):
        response = get_animal_adr()
        self.assertIn('meta', response)
        self.assertIn('results', response)

    def test_get_drug_event(self):
        response = get_drug_event()
        self.assertIn('meta', response)
        self.assertIn('results', response)

    def test_get_drug_label(self):
        response = get_drug_label()
        self.assertIn('meta', response)
        self.assertIn('results', response)

    def test_get_device_event(self):
        response = get_device_event()
        self.assertIn('meta', response)
        self.assertIn('results', response)
    
    def test_get_device_udi(self):
        response = get_device_udi()
        self.assertIn('meta', response)
        self.assertIn('results', response)

if __name__ == '__main__':
    unittest.main()