import unittest
from api import *

class TestUrlhausAPI(unittest.TestCase):

    def test_query_recent_urls(self):
        response = query_recent_urls(limit=3)
        self.assertIn("query_status", response)
        self.assertIn(response["query_status"], ["ok", "no_results"])

    def test_query_recent_payloads(self):
        response = query_recent_payloads(limit=3)
        self.assertIn("query_status", response)
        self.assertIn(response["query_status"], ["ok", "no_results"])

    def test_query_url_info_with_url(self):
        response = query_url_info(url="http://example.com/malware")
        self.assertIn("query_status", response)
        self.assertIn(response["query_status"], ["ok", "no_results", "invalid_url"])

    def test_query_url_info_with_id(self):
        response = query_url_info(id=105821)
        self.assertIn("query_status", response)
        self.assertIn(response["query_status"], ["ok", "no_results"])

    def test_query_host_info(self):
        response = query_host_info(host="example.com")
        self.assertIn("query_status", response)
        self.assertIn(response["query_status"], ["ok", "no_results", "invalid_host"])

    def test_query_payload_info_by_md5(self):
        response = query_payload_info(md5_hash="12c8aec5766ac3e6f26f2505e2f4a8f2")
        self.assertIn("query_status", response)
        self.assertIn(response["query_status"], ["ok", "no_results", "invalid_md5"])

    def test_query_payload_info_by_sha256(self):
        response = query_payload_info(sha256_hash="254ca6a7a7ef7f17d9884c4a86f88b5d5fd8fe5341c0996eaaf1d4bcb3b2337b")
        self.assertIn("query_status", response)
        self.assertIn(response["query_status"], ["ok", "no_results", "invalid_sha256"])

    def test_query_tag_info(self):
        response = query_tag_info(tag="Gozi")
        self.assertIn("query_status", response)
        self.assertIn(response["query_status"], ["ok", "no_results"])

    def test_query_signature_info(self):
        response = query_signature_info(signature="Heodo")
        self.assertIn("query_status", response)
        self.assertIn(response["query_status"], ["ok", "no_results"])

    def test_download_malware_sample(self):
        response = download_malware_sample(sha256="254ca6a7a7ef7f17d9884c4a86f88b5d5fd8fe5341c0996eaaf1d4bcb3b2337b")
        self.assertTrue(response)  # The response should contain content or an error message

if __name__ == '__main__':
    unittest.main()