#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """Method for printing text with 2 new lines after '.?:' characters.

    Args:
        text: is the string text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
