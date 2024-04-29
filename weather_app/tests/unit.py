"""
    This test checks if the site entered is reachable ergo return a status code of 200
"""
url = "http://10.10.1.3/"

import requests
import unittest

class Test_networking(unittest.TestCase):
    def check_site_availability(self):
        res = requests.get(url)
        assert res.status_code == 200
    

if __name__ == '__main__':
    unittest.main()
