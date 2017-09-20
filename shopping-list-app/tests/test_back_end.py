import unittest

from flask import Flask
from flask import abort, url_for
from fask_testing import TestCase

class TestCase(TestCase):
    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update()

        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass
