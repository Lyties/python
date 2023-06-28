from flask import Flask
from flask_testing import LiveServerTestCase
import requests

import unittest

class MyTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def test_server_is_up_and_running(self):
        response = requests.get(self.get_server_url())
        print(response.content.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
