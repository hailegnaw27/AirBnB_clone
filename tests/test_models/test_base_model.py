#!/usr/bin/python3
"""
Unit tests for BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def test_base_model(self):
        """
        Test BaseModel class
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        # Test __str__ method
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

        # Test save method
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertGreater(my_model.updated_at, prev_updated_at)

        # Test to_dict method
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['name'], "My First Model")
        self.assertEqual(my_model_dict['my_number'], 89)
        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
