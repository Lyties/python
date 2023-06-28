import unittest
from flask import Flask


class Test(unittest.TestCase):
    """
    测试案例
    """
    def setUp(self) -> None:
        app = Flask(__name__)
        self.client = app.test_client()
        return super().setUp()
    
    def test_index(self):
        response = self.client.get('/')
        print(response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
