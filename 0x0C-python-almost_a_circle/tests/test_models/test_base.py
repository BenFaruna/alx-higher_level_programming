import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test Base class"""

    def test_initialization(self):
        """test initialization of Base class"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

