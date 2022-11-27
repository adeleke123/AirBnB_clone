#!/usr/bin/python3
"""Unittest for UserModel class"""

from models.base_model import BaseModel
import unittest
from models.user import User


class test_User(unittest.TestCase):
    """Test cases for class UserModel"""

    def setUp(self):
        """Basic setup parameters"""
        self.value = User
        self.name = "User"

    def tearDown(self):
        """Basic teardown functions"""
        pass

    def test_amenity_superclass(self):
        """Test that User is subclass of Base Model"""
        new = self.value()
        self.assertTrue(issubclass(new.__class__, BaseModel))

    def test_first_name(self):
        """Test first name attribute"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last name attribute"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test email attribute"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test password attribute"""
        new = self.value()
        self.assertEqual(type(new.password), str)
