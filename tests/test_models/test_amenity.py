#!/usr/bin/python3
"""Unittest for AmenityModel class"""

from models.base_model import BaseModel
import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """Test cases for class AmenityModel"""

    def setUp(self):
        """Basic setup parameters"""
        self.value = Amenity
        self.name = "Amenity"

    def tearDown(self):
        """Basic teardown functions"""
        pass

    def test_amenity_superclass(self):
        """Test that Amenity is subclass of Base Model"""
        new = self.value()
        self.assertTrue(issubclass(new.__class__, BaseModel))

    def test_name(self):
        """Test name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
