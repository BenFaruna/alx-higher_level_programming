#!/usr/bin/python3
"""module for the base class"""
import json
from os import path
import csv


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
    def to_json_string(list_dictionaries):
        """converting a list dictionary into a json string"""
        if not list_dictionaries or not len(list_dictionaries) or \
        list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """static method for converting a json string into list"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves list of object into a file as json string"""
        if not list_objs:
            list_objs = []
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
        if not path.isfile(filename):
            return []
        with open(filename, "r") as f:
            attr_list = Base.from_json_string(f.read())
        ins_list = [cls.create(**attr) for attr in attr_list]
        return ins_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Converts 'list_objs' to csv format"""
        if not list_objs:
            list_objs = []
        with open("{}.csv".format(cls.__name__), 'w', encoding="utf-8") as fil:
            if cls.__name__ == "Rectangle":
                fields = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fields = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(fil, fieldnames=fields)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads file containing csv representation"""
        list_objs = []
        with open("{}.csv".format(cls.__name__), 'r') as file_csv:
            if cls.__name__ == "Rectangle":
                fields = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fields = ['id', 'size', 'x', 'y']
            reader = csv.DictReader(file_csv, fieldnames=fields)
            list_objs = []
            for row in reader:
                for key in row:
                    row[key] = int(row[key])
                list_objs.append(cls.create(**row))
        return list_objs

