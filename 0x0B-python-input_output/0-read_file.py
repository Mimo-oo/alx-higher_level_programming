#!/usr/bin/python3

""" This function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):



     """ This function that reads a text file (UTF8) and prints it to stdout"""


     with open(filename,"r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
