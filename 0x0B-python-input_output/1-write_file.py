#!/bin/bash/python3

"""A function that writes a string to a text file"""



def write_file(filename="", text=""):

    """
        Writing into a file
    """


    with open(filename, "w", encoding="utf-8"):
        write_text = f.write(text)

    return write_text
