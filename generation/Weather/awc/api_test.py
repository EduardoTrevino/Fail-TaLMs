import unittest
from api import (
    get_metar, get_taf, get_pirep, get_airsigmet, get_isigmet,
    get_gairmet, get_cwa, get_windtemp, get_areafcst,
    get_fcstdisc, get_mis, get_stationinfo, get_airport,
    get_feature, get_obstacle
)

class TestAWCAPI(unittest.TestCase):
    
    def setUp(self):
        self.api_key = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

    def test_get_metar(self):
        response = get_metar(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_taf(self):
        response = get_taf(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_pirep(self):
        response = get_pirep(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_airsigmet(self):
        response = get_airsigmet(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_isigmet(self):
        response = get_isigmet(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_gairmet(self):
        response = get_gairmet(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_cwa(self):
        response = get_cwa(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_windtemp(self):
        response = get_windtemp(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_areafcst(self):
        response = get_areafcst(region='gulf', toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_fcstdisc(self):
        response = get_fcstdisc(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_mis(self):
        response = get_mis(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_stationinfo(self):
        response = get_stationinfo(toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_airport(self):
        response = get_airport(ids='KMCI', toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_feature(self):
        response = get_feature(bbox='35,-90,45,-80', toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))

    def test_get_obstacle(self):
        response = get_obstacle(bbox='35,-90,45,-80', toolbench_rapidapi_key=self.api_key)
        self.assertNotIn('error', response)
        # self.assertTrue(isinstance(response, dict))
        
if __name__ == '__main__':
    unittest.main()