import unittest
from api import (
    search_for_any_match,
    search_by_common_name,
    search_by_common_name_begins_with,
    search_by_common_name_ends_with,
    search_by_scientific_name,
    get_itis_terms,
    get_itis_terms_from_common_name,
    get_itis_terms_from_scientific_name,
    get_tsn_by_vernacular_language,
)

class TestITISAPI(unittest.TestCase):

    def test_search_for_any_match(self):
        result = search_for_any_match("dolphin")

    def test_search_by_common_name(self):
        result = search_by_common_name("bear")

    def test_search_by_common_name_begins_with(self):
        result = search_by_common_name_begins_with("bear")

    def test_search_by_common_name_ends_with(self):
        result = search_by_common_name_ends_with("bear")

    def test_search_by_scientific_name(self):
        result = search_by_scientific_name("ursus")

    def test_get_itis_terms(self):
        result = get_itis_terms("bear")

    def test_get_itis_terms_from_common_name(self):
        result = get_itis_terms_from_common_name("bear")

    def test_get_itis_terms_from_scientific_name(self):
        result = get_itis_terms_from_scientific_name("ursus")

    def test_get_tsn_by_vernacular_language(self):
        result = get_tsn_by_vernacular_language("french")


if __name__ == '__main__':
    unittest.main()