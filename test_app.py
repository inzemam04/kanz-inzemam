import unittest
from app import app

class ScreeningTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_divisible_by_3(self):
        response = self.app.get('/api/v1/screening/9')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"results": ["Kanz"]})

    def test_divisible_by_5(self):
        response = self.app.get('/api/v1/screening/10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"results": ["Way"]})

    def test_divisible_by_3_and_5(self):
        response = self.app.get('/api/v1/screening/15')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"results": ["KanzWay"]})

    def test_not_divisible_by_3_or_5(self):
        response = self.app.get('/api/v1/screening/7')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"results": ["7"]})

if __name__ == '__main__':
    unittest.main()
