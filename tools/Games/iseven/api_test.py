import unittest
from api import iseven


class TestIsEvenAPI(unittest.TestCase):
    def setUp(self):
        self.toolbench_rapidapi_key = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

    def test_iseven_even_number(self):
        result = iseven(4, self.toolbench_rapidapi_key)
        self.assertIn('iseven', result)
        self.assertTrue(result['iseven'])

    def test_iseven_odd_number(self):
        result = iseven(3, self.toolbench_rapidapi_key)
        self.assertIn('iseven', result)
        self.assertFalse(result['iseven'])


if __name__ == '__main__':
    unittest.main()