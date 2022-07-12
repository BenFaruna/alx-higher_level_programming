import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
"""test cases for Base class from models/rectangle.py"""


class RectangleTestCase(unittest.TestCase):
    """Rectangle Test cases for rectangle class"""

    def setUp(self):
        """reset Base object count before every test"""
        Rectangle._Base__nb_objects = 0

    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_display_stdout(self, ins, expected_output, mock_stdout):
        """used to test print for display method"""
        ins.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_str_stdout(self, ins, expected_output, mock_stdout):
        """used to test string representation of Rectangle class"""
        print(ins)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # -------------- Task 2 ----------------
    def test_subclass_of_base(self):
        """test that Rectangle is a subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rectangle_instance_attributes(self):
        """test private instance attributes of rectangle"""
        self.assertTrue(hasattr(Rectangle(1, 1), "_Rectangle__width"))
        self.assertTrue(hasattr(Rectangle(1, 1), "_Rectangle__height"))
        self.assertTrue(hasattr(Rectangle(1, 1), "_Rectangle__x"))
        self.assertTrue(hasattr(Rectangle(1, 1), "_Rectangle__y"))

    def test_rectangle_id_count(self):
        """test how object count works using the base model inheritance"""
        r1 = Rectangle(4, 3)
        r2 = Rectangle(2, 6)
        r3 = Rectangle(1, 1, 0, 0, 20)
        r4 = Rectangle(2, 4, 1, 10)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 20)
        self.assertEqual(r4.id, 3)

    def test_rectangle_id_assignment(self):
        """test the id initialisation of rectangle class"""
        r1 = Rectangle(1, 1, id=10)
        r2 = Rectangle(1, 2, id=0)
        r3 = Rectangle(2, 1, id=1)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r2.id, 0)
        self.assertEqual(r3.id, 1)

    def test_attribute_assinment(self):
        """test for proper attribute assignment during initialisation"""
        rect = Rectangle(1, 5, 0, 2, 100)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 100)

    def test_positional_argument(self):
        """test initialisation with and without a positional argument"""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1, 0, 0, 10)
        self.assertTrue(isinstance(r1, Rectangle))
        self.assertTrue(isinstance(r2, Rectangle))
        with self.assertRaises(TypeError):
            Rectangle()

    # -------------- Task 3 ----------------
    def test_getter_setter(self):
        """Test getters and setters"""
        rect_test = Rectangle(5, 8)
        rect_test.width = 54
        rect_test.height = 43
        rect_test.x = 3
        rect_test.y = 2
        d = {'_Rectangle__height': 43,
             '_Rectangle__width': 54,
             '_Rectangle__x': 3,
             '_Rectangle__y': 2,
             'id': 1}
        self.assertEqual(rect_test.__dict__, d)
        self.assertEqual(rect_test.width, 54)
        self.assertEqual(rect_test.height, 43)
        self.assertEqual(rect_test.x, 3)
        self.assertEqual(rect_test.y, 2)

    def test_input_type(self):
        """check helper function that checks if argument is an integer"""
        self.assertIsNone(Rectangle.check_int("width", 1))
        self.assertIsNone(Rectangle.check_int("height", 1))

        with self.assertRaises(TypeError) as e:
            Rectangle.check_int("width", "str")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle.check_int("height", 10.2)
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle.check_int("width", [1, 2, 3, 4])
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Rectangle.check_int("height", None)
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_input_greater_than_or_equal_zero(self):
        """test for helper function to determine if input is >= zero"""
        self.assertIsNone(Rectangle.under_zero("width", 1))
        self.assertIsNone(Rectangle.under_zero("height", 5))
        self.assertIsNone(Rectangle.under_zero("width", 0))
        self.assertIsNone(Rectangle.under_zero("height", 0))

        with self.assertRaises(ValueError) as e:
            Rectangle.under_zero("width", -1)
        msg = "width must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            Rectangle.under_zero("height", -5)
        msg = "height must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_input_greater_than_zero(self):
        """test for helper function to determine if input is > zero"""
        self.assertIsNone(Rectangle.under_or_equal_zero("width", 1))
        self.assertIsNone(Rectangle.under_or_equal_zero("height", 5))

        with self.assertRaises(ValueError) as e:
            Rectangle.under_or_equal_zero("width", -1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            Rectangle.under_or_equal_zero("height", -5)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            Rectangle.under_or_equal_zero("height", 0)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_initialization_with_various_input(self):
        """test creating new instance with paramaters of different types"""
        self.assertTrue(Rectangle(2, 1))
        self.assertTrue(Rectangle(10, 20))
        self.assertTrue(Rectangle(5, 3, 1, 0))
        self.assertTrue(Rectangle(3, 7, 10, 5))

        with self.assertRaises((TypeError, ValueError)):
            self.assertRaises(TypeError, Rectangle("1", 5))
            self.assertRaises(TypeError, Rectangle(20, "string"))
            self.assertRaises(TypeError, Rectangle((1, 2), 5))
            self.assertRaises(TypeError, Rectangle(5, {"a": 5, "b": 2}))

    # -------------- Task 4 ----------------
    def test_area_method(self):
        """test the area method to confirm right output"""
        r1 = Rectangle(2, 4)
        r2 = Rectangle(1, 3, 5, 4, 10)
        r3 = Rectangle(100, 5, 4)

        self.assertEqual(r1.area(), 8)
        self.assertEqual(r2.area(), 3)
        self.assertEqual(r3.area(), 500)

    def test_area_no_self(self):
        """Test area() without self"""

        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        message = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), message)

    def test_area_no_positional(self):
        """Test area() with no positional arguments"""
        Rect_test = Rectangle(id=5, height=9, y=6, x=11, width=2)
        Rect_test.area()
        self.assertEqual(Rect_test.area(), 18)

    # -------------- Task 5 ----------------
    def test_display_width_height(self):
        """test display after creating an instance"""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 5)
        output1 = "#\n"
        output2 = "##\n##\n##\n##\n##\n"
        self.assert_display_stdout(r1, output1)
        self.assert_display_stdout(r2, output2)

    def test_display_with_instance(self):
        """test display with instance"""
        output = "###\n###\n"
        self.assert_display_stdout(Rectangle(3, 2), output)

    # -------------- Task # ----------------
    def test_string_output(self):
        """test the __str__ method of the rectangle class"""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 3)
        r3 = Rectangle(1, 5)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 1/1")
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 2/3")
        self.assertEqual(str(r3), "[Rectangle] (3) 0/0 - 1/5")

    def test_string_output_with_optional_parameters(self):
        """test __str__ method of rectangle class with optional parameters"""
        r1 = Rectangle(1, 2, 5, 3, 1)
        r2 = Rectangle(4, 6, 0, 2, 10)
        r3 = Rectangle(2, 3, 1, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 5/3 - 1/2")
        self.assertEqual(str(r2), "[Rectangle] (10) 0/2 - 4/6")
        self.assertEqual(str(r3), "[Rectangle] (1) 1/1 - 2/3")

    def test_string_with_print(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 3)
        r3 = Rectangle(1, 5)
        r4 = Rectangle(1, 2, 5, 3, 1)
        r5 = Rectangle(4, 6, 0, 2, 10)
        r6 = Rectangle(2, 3, 1, 1)
        self.assert_str_stdout(r1, "[Rectangle] (1) 0/0 - 1/1\n")
        self.assert_str_stdout(r2, "[Rectangle] (2) 0/0 - 2/3\n")
        self.assert_str_stdout(r3, "[Rectangle] (3) 0/0 - 1/5\n")
        self.assert_str_stdout(r4, "[Rectangle] (1) 5/3 - 1/2\n")
        self.assert_str_stdout(r5, "[Rectangle] (10) 0/2 - 4/6\n")
        self.assert_str_stdout(r6, "[Rectangle] (4) 1/1 - 2/3\n")

    # -------------- Task # ----------------
    # -------------- Task # ----------------
    # -------------- Task # ----------------
    # -------------- Task # ----------------
    # -------------- Task # ----------------
    # -------------- Task # ----------------
    # -------------- Task # ----------------
