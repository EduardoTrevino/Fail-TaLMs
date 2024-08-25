import unittest
from api import (
    generate_v1_uuid,
    generate_v3_uuid,
    generate_v4_uuid,
    generate_v5_uuid,
    generate_timestamp_first_uuid,
    decode_uuid
)

class TestUUIDandGUIDGenAPI(unittest.TestCase):
    def test_generate_v1_uuid(self):
        result = generate_v1_uuid(count=3)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(uuid, str) for uuid in result))

    def test_generate_v3_uuid(self):
        namespace = "ns:url"
        name = "https://www.google.com/"
        result = generate_v3_uuid(namespace=namespace, name=name)
        self.assertTrue(isinstance(result, str))

    def test_generate_v4_uuid(self):
        result = generate_v4_uuid(count=3)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(uuid, str) for uuid in result))

    def test_generate_v5_uuid(self):
        namespace = "ns:url"
        name = "https://www.uuidtools.com/generate"
        result = generate_v5_uuid(namespace=namespace, name=name)
        self.assertTrue(isinstance(result, str))

    def test_generate_timestamp_first_uuid(self):
        result = generate_timestamp_first_uuid(count=3)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(uuid, str) for uuid in result))

    def test_decode_uuid(self):
        uuid = "b01eb720-171a-11ea-b949-73c91bba743d"
        result = decode_uuid(uuid=uuid)
        self.assertIn("decode", result)

if __name__ == '__main__':
    unittest.main()