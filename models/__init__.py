#!/usr/bin/python3
"""
Models package initializer
"""

from models.engine.file_storage import FileStorag
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from models.state import State
from models.city import City

storage = FileStorage()
storage.reload()
