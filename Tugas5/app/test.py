import requests
import unittest

class TestWebsite(unittest.TestCase):
    def test_website_reachable(self):
        url = 'http://127.0.0.1/'  # Arrange
        response = requests.get(url)    # Action
        self.assertLess(response.status_code, 400)    # or assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

