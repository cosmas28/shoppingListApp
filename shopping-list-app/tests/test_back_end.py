import unittest
import os
from app import create_app

class TestCase(TestCase):
    """This class represents the buckist test case"""

    def setUp(self):
        """Define test variables and initialize app. """
        self.sign_up_data = {'username': 'admin', 'password': 'admin123'}
        self.sign_in_data = {'username': 'admin', 'password': 'admin123'}

    def tearDown(self):
        del self.sign_up_data
        del self.sign_in_data
