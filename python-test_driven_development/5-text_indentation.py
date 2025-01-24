#!/usr/bin/python3
"""
module : function to indation text

"""


def text_indentation(text):
    """


    Function that prints a text with 2 new lines
    after each
    of these
    characters: '.', '?', ':'.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.

    Examples:
    >>> text_indentation("Hello. How are you? I'm fine: thanks!")
    Hello.

    How are you?

    I'm fine:

    thanks!

    >>> text_indentation("")

    >>> text_indentation("No special chars here")
    No special chars here
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if i == "." or i == "?" or i == ":" or i == ",":
            print(i, end="\n")
            print()
        else:
            print(i, end="")
