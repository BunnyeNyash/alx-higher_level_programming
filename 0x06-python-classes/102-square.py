#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if the square is equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Check if the square is not equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """Check if the square is less than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the square is less than the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Check if the square is less than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the square is less than or equal to the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """Check if the square is greater than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the square is greater than the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Check if the square is greater than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the square is greater than or equal to the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
