import unittest
from api import contains_profanity, filter_text_json, filter_text_plain, filter_text_xml

class TestPurgoMalumAPI(unittest.TestCase):

    def test_contains_profanity_false(self):
        result = contains_profanity("this is a clean sentence")
        self.assertEqual(result, "false")

    def test_contains_profanity_true(self):
        result = contains_profanity("this is a fucking bad sentence")
        self.assertEqual(result, "true")

    def test_filter_text_json_no_profanity(self):
        result = filter_text_json("this is a clean sentence")
        self.assertEqual(result['result'], "this is a clean sentence")

    def test_filter_text_json_with_profanity(self):
        result = filter_text_json("this is a fucking bad sentence")
        self.assertNotEqual(result['result'], "this is a fucking bad sentence")

    def test_filter_text_plain_with_profanity(self):
        result = filter_text_plain("this is a fucking bad sentence")
        self.assertNotEqual(result, "this is a fucking bad sentence")

    def test_filter_text_xml_with_profanity(self):
        result = filter_text_xml("this is a fucking bad sentence")
        self.assertNotIn("<result>this is a fucking bad sentence</result>", result)

    def test_filter_text_with_custom_replacements(self):
        result = filter_text_json("this is a test", add="test", fill_text="[filtered]")
        self.assertEqual(result['result'], "this is a [filtered]")

if __name__ == '__main__':
    unittest.main()