# python-draft.py

# Advent of Code 2023
# Draft File

# This file contains a function to parse a text file
#placing each line into a string.

def parseFile(filename):
    with open (filename, "r") as input_file:
        input_string = input_file.read()

    return input_string

input_string = parseFile("filename")

