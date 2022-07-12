#!/usr/bin/python3
"""module for the base class"""
import json


class Base:
    """Base class with private class attribute nb_objects
    and id for initialisation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialisation of the base class, with default parameter
        """
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dicitonaries):
        """static method for converting a list dictionary into a json string"""
        return json.dumps(list_dicitonaries)

    @staticmethod
    def from_json_string(json_string):
        """static method for converting a json string into list"""
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves list of object into a file as json string"""
        filename = cls.__name__
        str_list = [obj.to_dictionary() for obj in list_objs]

        with open(filename + ".json", "w") as f:
            f.write(Base.to_json_string(str_list))

    @classmethod
    def create(cls, **dictionary):
        """creates a new class from a dictionary"""
        if cls.__name__ == "Rectangle":
            ins = cls(1, 1)
        elif cls.__name__ == "Square":
            ins = cls(1)
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "r") as f:
            attr_list = Base.from_json_string(f.read())
        ins_list = [cls.create(**attr) for attr in attr_list]
        return ins_list
