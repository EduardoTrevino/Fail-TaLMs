import unittest
from api import (
    get_device_latest,
    get_device_history,
    get_device_date,
    # get_devices_nearest,
    get_project_all,
    get_project_latest,
    get_analysis_adf_emission,
    get_analysis_adf_indoor,
    get_analysis_adf_pollution,
    get_analysis_adf_ranking,
    get_analysis_dcf_latest,
    get_analysis_dcf_nearest,
    get_citation,
    get_citation_adf,
)

class TestPMTwentyFiveAPI(unittest.TestCase):

    def test_get_device_latest(self):
        response = get_device_latest()
        self.assertIn("device_id", response)

    def test_get_device_history(self):
        response = get_device_history()
        self.assertIn("device_id", response)
        self.assertNotIn("error", response)

    def test_get_device_date(self):
        response = get_device_date()
        self.assertIn("device_id", response)
        self.assertNotIn("error", response)

    def test_get_project_all(self):
        response = get_project_all()
        self.assertTrue(response.strip())  # Should return non-empty string
        self.assertNotIn("error", response)

    def test_get_project_latest(self):
        response = get_project_latest()
        self.assertIn("feeds", response)
        self.assertNotIn("error", response)
    def test_get_analysis_adf_emission(self):
        response = get_analysis_adf_emission()
        self.assertIn("feeds", response)
        self.assertNotIn("error", response)

    def test_get_analysis_adf_indoor(self):
        response = get_analysis_adf_indoor()
        self.assertIn("feeds", response)
        self.assertNotIn("error", response)

    def test_get_analysis_adf_pollution(self):
        response = get_analysis_adf_pollution()
        self.assertIn("feeds", response)
        self.assertNotIn("error", response)

    def test_get_analysis_adf_ranking(self):
        response = get_analysis_adf_ranking()
        self.assertIn("feeds", response)
        self.assertNotIn("error", response)

    def test_get_analysis_dcf_latest(self):
        response = get_analysis_dcf_latest()
        self.assertIsInstance(response, list)
        self.assertNotIn("error", response)

    def test_get_analysis_dcf_nearest(self):
        response = get_analysis_dcf_nearest()
        self.assertIn("feeds", response)

    def test_get_citation(self):
        response = get_citation()
        self.assertTrue(response.strip())  # Should return non-empty string

    def test_get_citation_adf(self):
        response = get_citation_adf()
        self.assertTrue(response.strip())  # Should return non-empty string

if __name__ == '__main__':
    unittest.main()