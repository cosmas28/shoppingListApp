import unittest
import os
from app import create_app

class TestCase(TestCase):
    """This class represents the buckist test case"""

    def setUp(self):
        """Define test variables and initialize app. """
        self.sign_up_data = {'username': 'admin', 'password': 'admin123'}
        self.sign_in_data = {'username': 'admin', 'password': 'admin123'}
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def tearDown(self):
        del self.sign_up_data
        del self.sign_in_data

    def test_sign_up(self):
        """Test user can sign up """
        pos = self.client().post('/signup/', data=self.sign_up_data)
        self.assertEqual(pos.status_code, 201)
        self.assertIn('admin', str(pos.data))
