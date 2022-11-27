#!/usr/bin/python3
"""Unittest for CityModel class"""

import unittest
from models.city import City


class test_City(unittest.TestCase):
    """Test cases for class CityModel"""

    def setUp(self):
        """Basic setup parameters"""
        self.value = City
        self.name = "City"
        self.attr_list = ["state_id", "name"]

    def tearDown(self):
        """Basic teardown functions"""
        pass

    def test_attributes(self):
        """Test City attributes"""
        new = self.value()
        self.assertTrue(hasattr(new, "state_id"))
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(type(new.state_id),str)
        self.assertTrue(type(new.name),str)
