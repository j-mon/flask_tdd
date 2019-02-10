from app import app

import unittest


class BasicTestClass(unittest.TestCase):
# Testing whether response that we get is "200" and "Hello, World!" is displayed    def text_index(self):
        tester = app.test_client(self)
        response = tester.get('/'. content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')


if __name__ == '__main__':
    unittest.main()


