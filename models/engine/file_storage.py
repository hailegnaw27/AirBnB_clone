#!/usr/bin/python3
"""
File Storage module
"""
import json



class FileStorage:
    """
    FileStorage class
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all objects
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path)
        """
        save_dict = {}
        for key, value in self.__objects.items():
            save_dict[key] = value.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(save_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                load_dict = json.load(file)
                for key, value in load_dict.items():
                    cls_name, obj_id = key.split('.')
                    obj_props = dict(value)
                    obj_props['__class__'] = cls_name
                    obj = eval(cls_name)(**obj_props)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            self.all().pop(key, None)
