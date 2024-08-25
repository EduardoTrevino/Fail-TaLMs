import unittest
import requests_mock
from api import stations, liveboard, connections, vehicle, composition, disturbances

class TestIRailAPI(unittest.TestCase):
    
    def test_stations(self):
        with requests_mock.Mocker() as m:
            m.get("https://api.irail.be/stations/", json={'station': {}})
            response = stations()
            self.assertIn('station', response)
    
    def test_liveboard(self):
        with requests_mock.Mocker() as m:
            m.get("https://api.irail.be/liveboard/", json={'station': 'Ghent-Sint-Pieters'})
            response = liveboard('Gent-Sint-Pieters')
            self.assertIn('station', response)
            
    def test_connections(self):
        with requests_mock.Mocker() as m:
            m.get("https://api.irail.be/connections/", json={'connection': []})
            response = connections('Gent-Sint-Pieters', 'Mechelen', '300917', '1230')
            self.assertIn('connection', response)

    def test_vehicle(self):
        with requests_mock.Mocker() as m:
            m.get("https://api.irail.be/vehicle/", json={'vehicle': 'BE.NMBS.IC3033'})
            response = vehicle('BE.NMBS.IC3033')
            self.assertIn('vehicle', response)
    
    def test_composition(self):
        with requests_mock.Mocker() as m:
            m.get("https://api.irail.be/composition/", json={'composition': {}})
            response = composition('S51507')
            self.assertIn('composition', response)
    
    def test_disturbances(self):
        with requests_mock.Mocker() as m:
            m.get("https://api.irail.be/disturbances/", json={'disturbance': []})
            response = disturbances()
            self.assertIn('disturbance', response)

if __name__ == '__main__':
    unittest.main()