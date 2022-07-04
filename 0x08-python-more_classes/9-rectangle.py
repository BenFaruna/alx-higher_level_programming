#!/usr/bin/python3

"""
Define a rectangle class
"""


class Rectangle:
    """Representation of a rectangle, using width and
    height for initialization"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the Rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """returns printable string (representation of the rectangle)"""
        rectangle = ""
        if (self.width == 0 or self.height == 0):
            return ("")
        for height in range(self.height):
            rectangle += (str(self.print_symbol) * self.width)
            if (height < self.height - 1):
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """return a string representation for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """prints statement to show object instance is being deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def check_val(name, val):
        """Checkes the values passed as width and height to ensure
        it is a real number"""
        if (type(val) != int):
            raise TypeError("{} must be an integer".format(name))
        elif (val < 0):
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def check_instance(name, instance):
        """Check to ensure values are of instance Rectangle"""
        if type(instance) is not Rectangle:
            raise TypeError("{:s} must be an instance of Rectangle"
                            .format(name))

    @property
    def width(self):
        """getter function for private instance of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter function for private instance of width"""
        Rectangle.check_val("width", width)
        self.__width = width

    @property
    def height(self):
        """getter function for private instance of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """getter function for private instance of heigth"""
        Rectangle.check_val("height", height)
        self.__height = height

    @classmethod
    def square(cls, size=0):
        """returns a new rectangle instance that is a square"""
        return cls(size, size)

    def perimeter(self):
        """Computes the perimeter of a rectangle"""
        if (self.width == 0 or self.height == 0):
            return (0)
        return (2 * (self.width + self.height))

    def area(self):
        """Computes the area of a rectangle"""
        return (self.width * self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """determine the bigger rectangle using area"""
        Rectangle.check_instance("rect_1", rect_1)
        Rectangle.check_instance("rect_2", rect_2)

        if (rect_1.area() == rect_2.area()) or (rect_1.area() > rect_2.area()):
            return rect_1
        else:
            return rect_2
