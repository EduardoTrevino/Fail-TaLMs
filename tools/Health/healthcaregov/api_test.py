import unittest
from api import get_content_object, get_content_collection, get_content_index


class TestHealthcareGovAPI(unittest.TestCase):

    def test_get_content_object(self):
        response = get_content_object("accessibility", toolbench_rapidapi_key='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff')
        self.assertIn("title", response)
        self.assertEqual(response["url"], "/accessibility")

    def test_get_content_collection(self):
        response = get_content_collection("glossary", toolbench_rapidapi_key='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff')
        self.assertIn("glossary", response)

    def test_get_content_index(self):
        response = get_content_index(toolbench_rapidapi_key='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff')
        self.assertIsInstance(response, list)
        if len(response) > 0:
            self.assertIn("tags", response[0])
            self.assertIn("title", response[0])


if __name__ == "__main__":
    unittest.main()