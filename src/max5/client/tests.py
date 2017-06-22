import unittest
from client import MaxClient


class ClientUnitTests(unittest.TestCase):
    def test_login(self):
        client = MaxClient()
        token = client.login()
        self.assertEqual(len(token), 32)
