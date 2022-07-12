#!/usr/bin/python3
"""test cases for Base class from models/base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
from models.base import __doc__ as doc_check


class BaseTestCase(unittest.TestCase):
    """Test Base class"""

    def setUp(self):
        """setup code to reset the nb_objects count before every test"""
        Base._Base__nb_objects = 0

    def test_docstrings(self):
        self.assertIsNotNone(doc_check)
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertIs(hasattr(Base, "save_to_file_csv"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file_csv"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

# -------------- Task 1 ----------------
    def test_nb_objects_first_value(self):
        """test the __nb_objbects attribute value before initialisation"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_nb_objects_count(self):
        """test how the nb_objects is incremented after initialisation"""
        Base()
        Base(20)
        Base()
        Base(1)
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 2)

    def test_base_with_id(self):
        """test base class initialised  with id attribute"""
        b1 = Base(10)
        b2 = Base("string")
        b3 = Base([1, 2, 3])
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, "string")
        self.assertEqual(b3.id, [1, 2, 3])

    def test_nb_objects_is_present(self):
        """test the presence of the private attribute nb_objects"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_initialisation_count(self):
        """test how id attribute counts on initialisation"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

# ---------------Tests: task 15 --------------------------------
    def test_json_string(self):
        """Test to_json_string method"""
        with self.assertRaises(TypeError) as excep:
            Base.to_json_string()
        message = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(excep.exception), message)

        self.assertEqual(Base.to_json_string([]), "[]")
        dic = [{}]
        self.assertEqual(Base.to_json_string(dic), '[{}]')
        dic = [{}, {}, {}]
        self.assertEqual(Base.to_json_string(dic), '[{}, {}, {}]')

        dic = [{'width': 657, 'height': 78, 'x': 543, 'y': 965, 'id': 345}]
        self.assertEqual(len(Base.to_json_string(dic)), len(str(dic)))

        dic = [{'width': 65, 'height': 8, 'x': 3, 'y': 5, 'id': 34},
               {'width': 5, 'height': 1, 'x': 2, 'y': 6, 'id': 75}]
        self.assertEqual(len(Base.to_json_string(dic)), len(str(dic)))

        dic = [{'th': 7}, {'holberton': 3}]
        dic_json = '[{"th": 7}, {"holberton": 3}]'
        self.assertEqual(Base.to_json_string(dic), dic_json)

        dic = [{'help': 7}]
        dic_json = '[{"help": 7}]'
        self.assertEqual(Base.to_json_string(dic), dic_json)

        Rect_test = Rectangle(9, 54, 3, 1)
        dic = Rect_test.to_dictionary()
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

        Rect_test1 = Rectangle(5, 6, 2, 9)
        Rect_test2 = Rectangle(78, 16, 9, 1)
        dic = [Rect_test1.to_dictionary(), Rect_test2.to_dictionary()]
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

        Square_test = Square(54, 3, 1)
        dic = Square_test.to_dictionary()
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

        Square_test1 = Square(5, 2, 9)
        Square_test2 = Square(16, 9, 1)
        dic = [Square_test1.to_dictionary(), Square_test2.to_dictionary()]
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

# ---------------Tests: task 16 --------------------------------
    def test_save_to_file(self):
        '''Tests save_to_file() method.'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 107)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 53)

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 39)

# ---------------Tests: task 17 --------------------------------
    def test_from_json_string(self):
        """Test from_json_string method"""
        with self.assertRaises(TypeError) as excep:
            Base.from_json_string()
        message = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(excep.exception), message)

        string = '[{"x": 2, "y": 89, "width": 5, "id": 10, "height": 8}, \
{"x": 4, "y": 19, "width": 7, "id": 13, "height": 9}]'

        dic = [{'x': 2, 'y': 89, 'width': 5, 'id': 10, 'height': 8},
               {'x': 4, 'y': 19, 'width': 7, 'id': 13, 'height': 9}]

        self.assertEqual(Base.from_json_string(string), dic)

        string = '[{}]'
        dic = [{}]
        self.assertEqual(Base.from_json_string(string), dic)

        string = '[{}, {}]'
        dic = [{}, {}]
        self.assertEqual(Base.from_json_string(string), dic)

        string = '[{"hol": 5, "ber": 9, "ton": 11, "is": 1, "awesome": 6}, \
{"a": 4, "b": 19, "c": 7, "d": 13, "e": 9}]'

        dic = [{'hol': 5, 'ber': 9, 'ton': 11, 'is': 1, 'awesome': 6},
               {'a': 4, 'b': 19, 'c': 7, 'd': 13, 'e': 9}]

        self.assertEqual(Base.from_json_string(string), dic)

        list_rect = [{'width': 2, 'height': 5, 'id': 3},
                     {'width': 2, 'height': 5, 'id': 3}]

        list_rev = Rectangle.from_json_string(
            Rectangle.to_json_string(list_rect))
        self.assertEqual(list_rect, list_rev)

        list_square = [{'size': 5, 'id': 3},
                       {'size': 2, 'id': 5}]

        list_rev = Square.from_json_string(
            Square.to_json_string(list_square))
        self.assertEqual(list_square, list_rev)

# ---------------Tests: task 18 --------------------------------
    def test_create(self):
        """Test create method"""
        Rect_test1 = Rectangle(2, 4, 2, 1)
        Rect_dic1 = Rect_test1.to_dictionary()
        Rect_test2 = Rectangle.create(**Rect_dic1)
        self.assertEqual(str(Rect_test1), str(Rect_test2))
        self.assertFalse(Rect_test1 is Rect_test2)
        self.assertFalse(Rect_test1 == Rect_test2)

        Square_test1 = Square(2)
        Square_dic1 = Square_test1.to_dictionary()
        Square_test2 = Square.create(**Square_dic1)
        self.assertEqual(str(Square_test1), str(Square_test2))
        self.assertFalse(Square_test1 is Square_test2)
        self.assertFalse(Square_test1 == Square_test2)

# ---------------Tests: task 19 --------------------------------
    def test_load_from_file(self):
        """Test load_from_file method"""
        Rect_test1 = Rectangle(7, 8)
        Rect_test2 = Rectangle(2, 4, 8, 9)
        list_input = [Rect_test1, Rect_test2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual(str(list_input[0]), str(list_output[0]))
        self.assertNotEqual(id(list_input[0]), id(list_output[0]))
        self.assertEqual(str(list_input[1]), str(list_output[1]))
        self.assertNotEqual(id(list_input[1]), id(list_output[1]))

        Square_test1 = Square(7, 8)
        Square_test2 = Square(2)
        list_input = [Square_test1, Square_test2]
        Square.save_to_file(list_input)
        list_output = Square.load_from_file()
        self.assertEqual(str(list_input[0]), str(list_output[0]))
        self.assertNotEqual(id(list_input[0]), id(list_output[0]))
        self.assertEqual(str(list_input[1]), str(list_output[1]))
        self.assertNotEqual(id(list_input[1]), id(list_output[1]))


if __name__ == "__main__":
    unittest.main()
