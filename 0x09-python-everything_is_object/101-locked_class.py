#!/usr/bin/python3
"""module that difines LockedClass with no class object"""


class LockedClass:
    """that prevents the user from dynamically creating new instance attributes
    except if the new instance attribute is called first_name"""

    __name__ = ["first_name"]
