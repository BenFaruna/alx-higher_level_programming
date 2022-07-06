#!/usr/bin/python3
"""module that defines a student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialisation of the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__.copy()
        return {k: self.__dict__.get(k) for k in attrs
                if k in self.__dict__.keys()}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
