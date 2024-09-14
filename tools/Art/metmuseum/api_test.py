import unittest
from api import get_objects, get_object_details, get_departments, search_objects

class TestMetMuseumAPI(unittest.TestCase):

    def test_get_objects(self):
        response = get_objects()
        self.assertIn('total', response)
        self.assertIn('objectIDs', response)

    def test_get_objects_with_params(self):
        response = get_objects(department_ids=[3, 9, 12])
        self.assertIn('total', response)
        self.assertIn('objectIDs', response)

    def test_get_object_details(self):
        object_id = 1  # Use a valid object ID from the Met database for actual testing
        response = get_object_details(object_id)
        self.assertIn('objectID', response)

    def test_get_departments(self):
        response = get_departments()
        self.assertIn('departments', response)

    def test_search_objects(self):
        response = search_objects('sunflowers')
        self.assertIn('total', response)
        self.assertIn('objectIDs', response)

    def test_search_objects_with_params(self):
        response = search_objects('sunflowers', is_highlight=True)
        self.assertIn('total', response)
        self.assertIn('objectIDs', response)
        
if __name__ == '__main__':
    unittest.main()