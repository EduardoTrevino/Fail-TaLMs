import unittest
from api import *

class TestVehiclesAPI(unittest.TestCase):

    def test_decode_vin(self):
        response = decode_vin("5UXWX7C5*BA", 2011)
        self.assertIn('Results', response)

    def test_decode_vin_values(self):
        response = decode_vin_values("5UXWX7C5*BA", 2011)
        self.assertIn('Results', response)

    def test_decode_vin_extended(self):
        response = decode_vin_extended("5UXWX7C5*BA", 2011)
        self.assertIn('Results', response)

    def test_decode_vin_values_extended(self):
        response = decode_vin_values_extended("5UXWX7C5*BA", 2011)
        self.assertIn('Results', response)

    def test_decode_wmi(self):
        response = decode_wmi("1FD")
        self.assertIn('Results', response)

    def test_get_wmis_for_manufacturer(self):
        response = get_wmis_for_manufacturer("hon")
        self.assertIn('Results', response)

    def test_get_all_makes(self):
        response = get_all_makes()
        self.assertIn('Results', response)

    def test_get_parts(self):
        response = get_parts(565, "1/1/2015", "5/5/2015")
        self.assertIn('Results', response)

    def test_get_all_manufacturers(self):
        response = get_all_manufacturers()
        self.assertIn('Results', response)

    def test_get_manufacturer_details(self):
        response = get_manufacturer_details("honda")
        self.assertIn('Results', response)

    def test_get_make_for_manufacturer(self):
        response = get_make_for_manufacturer("honda")
        self.assertIn('Results', response)

    def test_get_makes_for_manufacturer_and_year(self):
        response = get_makes_for_manufacturer_and_year("mer", 2013)
        self.assertIn('Results', response)

    def test_get_makes_for_vehicle_type(self):
        response = get_makes_for_vehicle_type("car")
        self.assertIn('Results', response)

    def test_get_vehicle_types_for_make(self):
        response = get_vehicle_types_for_make("mercedes")
        self.assertIn('Results', response)

    def test_get_vehicle_types_for_make_id(self):
        response = get_vehicle_types_for_make_id(450)
        self.assertIn('Results', response)

    def test_get_equipment_plant_codes(self):
        response = get_equipment_plant_codes(2015)
        self.assertIn('Results', response)

    def test_get_models_for_make(self):
        response = get_models_for_make("honda")
        self.assertIn('Results', response)

    def test_get_models_for_make_id(self):
        response = get_models_for_make_id(440)
        self.assertIn('Results', response)

    def test_get_models_for_make_year(self):
        response = get_models_for_make_year("honda", 2015, "truck")
        self.assertIn('Results', response)

    def test_get_vehicle_variable_list(self):
        response = get_vehicle_variable_list()
        self.assertIn('Results', response)

    def test_get_vehicle_variable_values_list(self):
        response = get_vehicle_variable_values_list("battery type")
        self.assertIn('Results', response)

    def test_decode_vin_values_batch(self):
        vins = "5UXWX7C5*BA,2011;5YJSA3DS*EF"
        response = decode_vin_values_batch(vins)
        self.assertIn('Results', response)

    def test_get_canadian_vehicle_specifications(self):
        response = get_canadian_vehicle_specifications(2011, "Acura")
        self.assertIn('Results', response)

if __name__ == "__main__":
    unittest.main()