#!/usr/bin/python3
"""
BaseModel module
"""
import uuid
from datetime import datetime
from models import engine


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)

        if not kwargs or 'id' not in kwargs:
            storage.new(self)

    def __str__(self):
        """
        Return string representation of BaseModel
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute 'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of BaseModel
        """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        obj_dict.pop('_sa_instance_state', None)
        return obj_dict
