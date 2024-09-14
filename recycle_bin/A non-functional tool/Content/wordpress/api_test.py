import unittest
from api import (
    list_posts,
    create_post,
    list_categories,
    retrieve_category,
    list_tags,
    list_users,
    retrieve_user
)

class TestWordPressApi(unittest.TestCase):

    def setUp(self):
        self.api_key = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

    def test_list_posts(self):
        response = list_posts(toolbench_rapidapi_key=self.api_key)
        self.assertIsInstance(response, dict)
        self.assertIn('data', response)

    def test_create_post(self):
        response = create_post(
            title="Test Post",
            content="This is a test post.",
            toolbench_rapidapi_key=self.api_key
        )
        self.assertIsInstance(response, dict)
        self.assertIn('id', response)

    def test_list_categories(self):
        response = list_categories(toolbench_rapidapi_key=self.api_key)
        self.assertIsInstance(response, dict)
        self.assertIn('data', response)

    def test_retrieve_category(self):
        response = retrieve_category(category_id=1, toolbench_rapidapi_key=self.api_key)
        self.assertIsInstance(response, dict)
        self.assertIn('id', response)

    def test_list_tags(self):
        response = list_tags(toolbench_rapidapi_key=self.api_key)
        self.assertIsInstance(response, dict)
        self.assertIn('data', response)

    def test_list_users(self):
        response = list_users(toolbench_rapidapi_key=self.api_key)
        self.assertIsInstance(response, dict)
        self.assertIn('data', response)

    def test_retrieve_user(self):
        response = retrieve_user(user_id=1, toolbench_rapidapi_key=self.api_key)
        self.assertIsInstance(response, dict)
        self.assertIn('id', response)

if __name__ == '__main__':
    unittest.main()