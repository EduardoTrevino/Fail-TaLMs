import unittest
import requests
from api import get_remote_jobs, get_rss_feed, get_new_jobs_xml

class TestRemoteJobsAPI(unittest.TestCase):

    def test_get_remote_jobs(self):
        response = get_remote_jobs(count=10, geo='usa', industry='marketing', tag='python')
        self.assertIsInstance(response, dict)
        self.assertIn('jobs', response)
        self.assertLessEqual(len(response['jobs']), 10)

    def test_get_rss_feed(self):
        response = get_rss_feed(job_categories='supporting', job_types='full-time', search_region='USA')
        self.assertIsInstance(response, bytes)

    def test_get_new_jobs_xml(self):
        response = get_new_jobs_xml()
        self.assertIsInstance(response, bytes)

if __name__ == '__main__':
    unittest.main()