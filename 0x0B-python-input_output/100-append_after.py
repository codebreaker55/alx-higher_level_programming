#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file, after each line
    containing a specific string
    """

    with open(filename, "r", encoding="utf-8") as fil:
        l_list = []
        while True:
            lin = fil.readline()
            if lin == "":
                break
            l_list.append(lin)
            if search_string in lin:
                l_list.append(new_string)

    with open(filename, "w", encoding="utf-8") as fil:
        fil.writelines(l_list)
