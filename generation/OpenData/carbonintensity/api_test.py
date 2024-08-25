import unittest
from api import (
    get_current_intensity,
    get_intensity_by_date,
    get_intensity_factors,
    get_intensity_statistics,
    get_generation_mix_current,
    get_regional_intensity
)


class TestCarbonIntensityAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

    def test_get_current_intensity(self):
        response = get_current_intensity(self.api_key)
        self.assertIn('data', response)

    def test_get_intensity_by_date(self):
        response = get_intensity_by_date('2018-01-20', self.api_key)
        self.assertIn('data', response)

    def test_get_intensity_factors(self):
        response = get_intensity_factors(self.api_key)
        self.assertIn('data', response)

    def test_get_intensity_statistics(self):
        response = get_intensity_statistics('2018-01-20T12:00Z', '2018-01-21T12:00Z', self.api_key)
        self.assertIn('data', response)

    def test_get_generation_mix_current(self):
        response = get_generation_mix_current(self.api_key)
        self.assertIn('data', response)

    def test_get_regional_intensity(self):
        response = get_regional_intensity(self.api_key)
        self.assertIn('data', response)


if __name__ == '__main__':
    unittest.main()