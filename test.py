
from app import *
import unittest


class YummyTestCase(unittest.TestCase):

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        tester = app.test_client(self)
        response = tester.get('/logout', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_dashboard(self):
        tester = app.test_client(self)
        response = tester.get('/dashboard', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/recipes', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
