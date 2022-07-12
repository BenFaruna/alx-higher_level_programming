import unittest
from models.base import Base
"""test cases for Base class from models/base.py"""


class BaseTestCase(unittest.TestCase):
    """Test Base class"""

    def setUp(self):
        """setup code to reset the nb_objects count before every test"""
        Base._Base__nb_objects = 0

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

# -------------- Task # ----------------
