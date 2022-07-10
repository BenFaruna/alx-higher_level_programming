from .rectangle import Rectangle
"""module for square class inheriting from the rectangle class"""


class Square(Rectangle):
    """square class inheriting from the rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialisatin of the square class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """string representation of the Square class"""
        return "[{}] ({}) {}/{} - {}".format(Square.__name__, self.id,
                                             self.x, self.y, self.size)

    @property
    def size(self):
        """setter function for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function for size attribute"""
        self.__size = value
        self.update(width=value, height=value)

    def update(self, *args, **kwargs):
        """update the attributs of the Square class"""
        if len(args) != 0:
            attr = ["id", "size", "x", "y"]
            attr_index = 0
            for arg in args:
                setattr(self, attr[attr_index], arg)
                attr_index += 1
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        attrs = ["id", "x", "size", "y"]
        return {attr: getattr(self, attr) for attr in attrs}
