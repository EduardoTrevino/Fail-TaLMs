import unittest
from api import stations, liveboard, connections, vehicle, composition, disturbances

class TestIRailAPI(unittest.TestCase):
    
    def test_stations(self):
        response = stations()
        self.assertIn('station', response)
    
    def test_liveboard(self):
        response = liveboard('Gent-Sint-Pieters')
        self.assertIn('station', response)
            
    def test_connections(self):
        response = connections('Gent-Sint-Pieters', 'Mechelen', '23082024', '1130')
        self.assertIn('connection', response)

    def test_vehicle(self):
        response = vehicle('BE.NMBS.IC3033')
        self.assertIn('vehicle', response)
    
    def test_composition(self):
        response = composition('S51507')
        self.assertIn('composition', response)
    
    def test_disturbances(self):
        response = disturbances()
        self.assertIn('disturbance', response)

if __name__ == '__main__':
    unittest.main()
