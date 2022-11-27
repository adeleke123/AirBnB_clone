#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime, time, date
import os
import pycodestyle


class TestBaseModel(unittest.TestCase):
    """Test cases for class BaseModel"""

    def setUp(self):
        """Displace current json file from it's position if it exits and make a test json file"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")

    def tearDown(self):
        """Delete test json file and return the original json file"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_pycodestyle(self):
        """Applying pycodestyle checker to my BaseModel class"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "there's an error found in the model")
        
    def test_attribute_basics(self):
        """Test if a class has Id, created_at and updated_at"""
        sample = BaseModel()
        self.assertTrue(hasattr(sample, "id"))
        self.assertTrue(hasattr(sample, "created_at"))
        self.assertTrue(hasattr(sample, "updated_at"))

    def test_attribute_basics_types(self):
        """Tests that basic attributes are of correct types"""
        sample = BaseModel()
        self.assertTrue(type(sample.id), str)
        self.assertTrue(type(sample.created_at), datetime)
        self.assertTrue(type(sample.updated_at), datetime)

    def test_attributes_others(self):
        """Test that model can accomodate more attributes"""
        sample = BaseModel()
        sample.name = "My_First_Model"
        sample.age = 22
        self.assertTrue(hasattr(sample, "name"))
        self.assertTrue(hasattr(sample, "age"))

    def test_to_dict(self):
        """Test that to dict method works"""
        tmp = BaseModel().to_dict()
        self.assertTrue(isinstance(tmp, dict))
        self.assertTrue("updated_at" in tmp)
        self.assertTrue("created_at" in tmp)
        self.assertTrue("id" in tmp)
        self.assertTrue("__class__" in tmp)



if __name__ == "__main__":
    unittest.main()
