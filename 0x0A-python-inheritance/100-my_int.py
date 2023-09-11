class MyInt(int):
    """
    A class that inherits from int and inverts the == and != operators.
    """
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """
        Overrides the == operator to invert its behavior.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the objects are not equal, False otherwise.
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """
        Overrides the != operator to invert its behavior.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        return int(self) == int(other)
