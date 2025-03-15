import unittest
from api.requests.v1.requests_pb2 import requests_pb2


class TestProtobufDefinitions(unittest.TestCase):
    def test_create_request(self):
        request = requests_pb2.CreateRequest(name="Test Request", description="Testing ProtoBuf")
        self.assertEqual(request.name, "Test Request")
        self.assertEqual(request.description, "Testing ProtoBuf")

if __name__ == '__main__':
    unittest.main()
