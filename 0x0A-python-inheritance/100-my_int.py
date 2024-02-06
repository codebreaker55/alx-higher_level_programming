#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """is a rebel that inherits from int"""

    def __new__(cls, *args, **kwargs):
        """creating new class instance"""

        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """changing == to be !="""

        return int(self) != other

    def __ne__(self, other):
        """changing != to be =="""

        return int(self) == other
