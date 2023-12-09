#!/usr/bin/python3
"""
Unit tests for BaseModel (from dictionary)
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelFromDict(unittest.TestCase):
    """
    Test cases for BaseModel class (from dictionary)
    """

    def test_base_model_from_dict(self):
        """
        Test BaseModel class (from dictionary)
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        # Test to_dict method
        my_model_dict = my_model.to_dict()

        # Test BaseModel class (from dictionary)
        my_new_model = BaseModel(**my_model_dict)

        self.assertEqual(my_new_model.id, my_model.id)
        self.assertEqual(my_new_model.name, my_model.name)
        self.assertEqual(my_new_model.my_number, my_model.my_number)
        self.assertEqual(type(my_new_model.created_at), datetime)
        self.assertEqual(my_new_model.created_at, my_model.created_at)
        self.assertEqual(type(my_new_model.updated_at), datetime)
        self.assertEqual(my_new_model.updated_at, my_model.updated_at)


if __name__ == '__main__':
    unittest.main()
