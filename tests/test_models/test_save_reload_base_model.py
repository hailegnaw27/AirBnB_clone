#!/usr/bin/python3
"""
Unit tests for saving and reloading BaseModel instances
"""
import unittest
from models.base_model import BaseModel
from models import storage


class TestSaveReloadBaseModel(unittest.TestCase):
    """
    Test cases for saving and reloading BaseModel instances
    """

    def test_save_reload_base_model(self):
        """
        Test saving and reloading BaseModel instances
        """
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 0)

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        all_objs = storage.all()
        self.assertEqual(len(all_objs), 1)

        new_model = list(all_objs.values())[0]
        self.assertEqual(new_model.id, my_model.id)
        self.assertEqual(new_model.name, my_model.name)
        self.assertEqual(new_model.my_number, my_model.my_number)
