import os
import unittest
from ..app import Authentication

class AuthenticationTest(unittest.TestCase):
    """ validates users before they enter to their accounts"""
    def test_sign_in(self):
        submited_data = self.login('admin', 'default')
        assert b'You were logged in' in submited_data.data
        submited_data = self.login('adminx', 'default')
        assert b'Invalid username' in submited_data.data
        submited_data = self.login('admin', 'default')
        assert b'Invalid password' in submited_data.data
