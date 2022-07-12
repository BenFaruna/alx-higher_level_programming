#!/usr/bin/python3
"""test cases for Base class from models/square.py"""
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
from models.square import __doc__ as doc_check


class SquareTestCase(unittest.TestCase):
    """Test cases for square class"""

    def setUp(self):
        """setup before every test"""
        Square._Base__nb_objects = 0

    def test_docstrings(self):
        self.assertIsNotNone(doc_check)
        self.assertIsNotNone(Square.__doc__)
        self.assertIs(hasattr(Square, "__init__"), True)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIs(hasattr(Square, "size"), True)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIsNotNone(Square.y.__doc__)
        self.assertIs(hasattr(Square, "__str__"), True)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIs(hasattr(Square, "update"), True)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIs(hasattr(Square, "to_dictionary"), True)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    # -------------- Task 10 ----------------
    def test_subclass_of_base(self):
        """test that Square is a subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_subclass_of_rectangle(self):
        """test that Square is a subclass of Rectangle"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id_count_square(self):
        """test id count for Square class"""
        s1 = Square(1)
        s2 = Square(2, 0, 0)
        s3 = Square(3, 0, 0, 10)
        s4 = Square(4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 10)
        self.assertEqual(s4.id, 3)

    def test_square_instance_for_inheritance(self):
        """test private instance attributes of square"""
        self.assertTrue(hasattr(Square(1), "_Rectangle__width"))
        self.assertTrue(hasattr(Square(1), "_Rectangle__height"))
        self.assertTrue(hasattr(Square(1), "_Rectangle__x"))
        self.assertTrue(hasattr(Square(1), "_Rectangle__y"))

    def test_instantiation(self):
        """Test Square() instantiation with 1 arguments"""
        Square_test = Square(6)
        self.assertEqual(str(type(Square_test)), "<class \
'models.square.Square'>")
        self.assertTrue(isinstance(Square_test, Base))
        self.assertTrue(isinstance(Square_test, Square))

    def test_instantiation_positional(self):
        """Test Square() positional instantiation"""
        Square_test = Square(4, 12, 7, 8)
        self.assertEqual(str(type(Square_test)), "<class 'models.\
square.Square'>")
        self.assertTrue(isinstance(Square_test, Base))

    def test_instantiation_no_positional(self):
        """Test Square() no positional instantiation"""
        Square_test = Square(id=9, x=4, size=12, y=7)
        self.assertEqual(str(type(Square_test)), "<class 'models.\
square.Square'>")
        self.assertTrue(isinstance(Square_test, Base))

    def test_mix_positional(self):
        """Test Rectangle() positional/no instantiation"""
        Square_test = Square(9, 100, id=12, y=7)
        self.assertEqual(str(type(Square_test)), "<class 'models.\
square.Square'>")
        self.assertTrue(isinstance(Square_test, Base))

    def test_getter_setter(self):
        """Test getters and setters"""
        Square_test = Square(5, 8)
        Square_test.size = 4
        Square_test.x = 3
        Square_test.y = 2
        self.assertEqual(Square_test.width, 4)
        self.assertEqual(Square_test.height, 4)
        self.assertEqual(Square_test.x, 3)
        self.assertEqual(Square_test.y, 2)

    def test_arguments_invalid_type(self):
        """Test invalid arguments types"""
        with self.assertRaises(TypeError) as excep:
            Square("34")
        message = "width must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(TypeError) as excep:
            Square(89, "w")
        message = "x must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(TypeError) as excep:
            Square(89, 6, "holby")
        message = "y must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Square(-7)
        message = "width must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Square(1, -46)
        message = "x must be >= 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Square(9, 2, -6)
        message = "y must be >= 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Square(0)
        message = "width must be > 0"
        self.assertEqual(str(excep.exception), message)

    def invalid_types(self):
        """Returns lists with different invalid cases"""
        types = (3.56, float('inf'), float('Nan'), True,
                 (5, ), -6.792, [8], None, {8, 7})
        return types

    def validate_types(self):
        """Test invalid arguments types with different cases"""
        square_test = Square(8, 5)
        attributes = ["x", "y"]
        for attr in attributes:
            message = "{} must be an integer".format(attr)
            for invalid in self.invalid_types():
                with self.assertRaises(TypeError) as excep:
                    setattr(square_test, attr, self.invalid_types)
                self.assertEqual(str(excep.exception), message)
        message = "width must be an integer"
        for invalid in self.invalid_types():
            with self.assertRaises(TypeError) as excep:
                setattr(square_test, "width", invalid)
            self.assertEqual(str(excep.exception), message)

# ---------------Tests: task 4--------------------------------

    def test_area_only_size(self):
        """Test area() with height and witdth only"""
        Square_test = Square(9)
        Square_test.area()
        self.assertEqual(Square_test.area(), 81)

    def test_area_no_self(self):
        """Test area() without self"""
        with self.assertRaises(TypeError) as excep:
            Square.area()
        message = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

    def test_area_positional(self):
        """Test area() with positional arguments"""
        Square_test = Square(5, 9, 6, 11)
        Square_test.area()
        self.assertEqual(Square_test.area(), 25)

    def test_area_no_positional(self):
        """Test area() with no positional arguments"""
        Square_test = Square(id=5, size=9, y=6, x=11)
        Square_test.area()
        self.assertEqual(Square_test.area(), 81)

    # ---------------Tests: task 5 & 7--------------------------------

    def test_display_no_args(self):
        """Test display() without self"""
        with self.assertRaises(TypeError) as excep:
            Square.display()
        message = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

    def test_display_no_x_y(self):
        """Test display() without x and y"""
        Square_test = Square(1)
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Square_test.display()
        out_hope = "#\n"
        self.assertEqual(out_put.getvalue(), out_hope)
        Square_test.size = 5
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Square_test.display()
        out_hope = "\
#####\n\
#####\n\
#####\n\
#####\n\
#####\n\
"
        self.assertEqual(out_put.getvalue(), out_hope)

    def test_display_with_x_y(self):
        """Test display() with x and y"""
        Square_test = Square(3, 2, 3, 4)
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Square_test.display()
        out_hope = "\
\n\
\n\
\n\
  ###\n\
  ###\n\
  ###\n\
"
        self.assertEqual(out_put.getvalue(), out_hope)

        Square_test = Square(4, 2, 5)
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Square_test.display()
        out_hope = "\
\n\
\n\
\n\
\n\
\n\
  ####\n\
  ####\n\
  ####\n\
  ####\n\
"
        self.assertEqual(out_put.getvalue(), out_hope)

    def test_display_no_x(self):
        """Test display() without x"""
        Square_test = Square(size=5, y=3)
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Square_test.display()
        out_hope = "\
\n\
\n\
\n\
#####\n\
#####\n\
#####\n\
#####\n\
#####\n\
"
        self.assertEqual(out_put.getvalue(), out_hope)

        Square_test = Square(7, 0, 4)
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Square_test.display()
        out_hope = "\
\n\
\n\
\n\
\n\
#######\n\
#######\n\
#######\n\
#######\n\
#######\n\
#######\n\
#######\n\
"
        self.assertEqual(out_put.getvalue(), out_hope)

        def test_display_no_y(self):
            """Test display() without y"""
            Square_test = Square(size=5, x=4)
            out_put = io.StringIO()
            with redirect_stdout(out_put):
                Square_test.display()
            out_hope = "\
    #####\n\
    #####\n\
    #####\n\
    #####\n\
    #####\n\
"
            self.assertEqual(out_put.getvalue(), out_hope)

            Square_test = Square(3, 4)
            out_put = io.StringIO()
            with redirect_stdout(out_put):
                Square_test.display()
            out_hope = "\
        ###\n\
        ###\n\
        ###\n\
    "
            self.assertEqual(out_put.getvalue(), out_hope)

# ---------------Tests: task 6--------------------------------
    def test_str__no_self(self):
        """Test str without self"""
        with self.assertRaises(TypeError) as excep:
            Square.__str__()
        message = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

    def test_n_arg(self):
        """Test str() with different amount of arguments"""
        Square_test = Square(8)
        message = '[Square] (1) 0/0 - 8'
        self.assertEqual(str(Square_test), message)
        Square_test = Square(8, 12)
        message = '[Square] (2) 12/0 - 8'
        self.assertEqual(str(Square_test), message)
        Square_test = Square(8, 12, 3)
        message = '[Square] (3) 12/3 - 8'
        self.assertEqual(str(Square_test), message)
        Square_test = Square(8, 12, 3, 4)
        message = '[Square] (4) 12/3 - 8'
        self.assertEqual(str(Square_test), message)

# ---------------Tests: task 8 & 9--------------------------------

    def test_update_no_self(self):
        """Test update without self"""
        Square_test = Square(5, 9)
        with self.assertRaises(TypeError) as excep:
            Square.update()
        message = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

        dic = Square_test.__dict__.copy()
        Square_test.update()
        self.assertEqual(Square_test.__dict__, dic)

    def test_update_change_args(self):
        """Test update with different amount of arguments"""
        Square_test = Square(7)

        Base._Base__nb_objects = 0
        Square_test = Square(2, 2, 2, 2)
        self.assertEqual(str(Square_test), "[Square] (2) 2/2 - 2")

        Square_test.update(23)
        self.assertEqual(str(Square_test), "[Square] (23) 2/2 - 2")

        Square_test.update(11, 33)
        self.assertEqual(str(Square_test), "[Square] (11) 2/2 - 33")

        Square_test.update(4, 13, 8)
        self.assertEqual(str(Square_test), "[Square] (4) 8/2 - 13")

        Square_test.update(8, 1, 51, 3)
        self.assertEqual(str(Square_test), "[Square] (8) 51/3 - 1")

    def test_update_args_wrong(self):
        """Test update with different invalid arguments(args)"""
        Square_test = Square(11)

        with self.assertRaises(ValueError) as excep:
            Square_test.update(2, 0)
        message = "width must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Square_test.update(9, 1, -98)
        message = "x must be >= 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Square_test.update(9, 1, 98, -4)
        message = "y must be >= 0"
        self.assertEqual(str(excep.exception), message)

    def test_update_args_kwargs(self):
        """Test update with different valid arguments(kwargs)"""
        Square_test = Square(7, 4)

        Square_test.update(id=55)

        Base._Base__nb_objects = 0
        Square_test = Square(2, 2, 2, 2)
        self.assertEqual(str(Square_test), "[Square] (2) 2/2 - 2")

        Square_test.update(x=23)
        self.assertEqual(str(Square_test), "[Square] (2) 23/2 - 2")

        Square_test.update(y=12, x=33)
        self.assertEqual(str(Square_test), "[Square] (2) 33/12 - 2")

        Square_test.update(y=4, x=13, size=8)
        self.assertEqual(str(Square_test), "[Square] (2) 13/4 - 8")

        Square_test.update(size=8, y=1, x=3)
        self.assertEqual(str(Square_test), "[Square] (2) 3/1 - 8")

    def test_update_kwargs_wrong(self):
        """Test update with different invalid arguments(kwargs)"""
        Square_test = Square(10)
        with self.assertRaises(ValueError) as excep:
            Square_test.update(id=9, size=0)
        message = "width must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Square_test.update(size=9, id=1, x=-1)
        message = "x must be >= 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Square_test.update(id=9, x=1, size=98, y=-8)
        message = "y must be >= 0"
        self.assertEqual(str(excep.exception), message)

# -----------------Tests: task 14---------------------------------
    def test_dictionary(self):
        """Test dictionary"""
        with self.assertRaises(TypeError) as excep:
            Square.to_dictionary()
        message = "to_dictionary() missing 1 required \
positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

        Square_test = Square(5, 78)
        dic = {'x': 78, 'id': 1, 'size': 5, 'y': 0}
        self.assertEqual(Square_test.to_dictionary(), dic)

        Square_test = Square(78, 5, 2, 9)
        dic = {'x': 5, 'y': 2, 'id': 9, 'size': 78}
        self.assertEqual(Square_test.to_dictionary(), dic)

        Square_test1 = Square(1, 4, 5, 6)
        Square_test1_dic = Square_test1.to_dictionary()
        Square_test2 = Square(4, 8, 7, 90)
        Square_test2.update(**Square_test1_dic)
        self.assertEqual(str(Square_test1), str(Square_test2))

        Square_test1.update(5, 7, 9, 56)
        dic = {'x': 9, 'y': 56, 'size': 7, 'id': 5}
        self.assertEqual(Square_test1.to_dictionary(), dic)


if __name__ == "__main__":
    unittest.main()

