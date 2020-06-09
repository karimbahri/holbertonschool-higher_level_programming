#!/usr/bin/python3
"""base:
    classes:
        Base
    """
import json


class Base:
    """Base class:
            __init__
        """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__: constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to json representation"""
        if list_dictionaries is None:
            return "[]"
        json_repr = json.dumps(list_dictionaries)
        return json_repr

    @classmethod
    def save_to_file(cls, list_objs):
        """save json repr into file"""
        my_list = list()
        if list_objs is not None:
            for item in list_objs:
                my_list.append(item.to_dictionary())
        my_file_name = cls.__name__ + ".json"
        with open(my_file_name, "w") as my_file:
            my_file.write(cls.to_json_string(my_list))
