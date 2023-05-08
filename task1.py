#!/usr/bin/python

"""
This module prints out the extension of a file
"""

import os

file = input("What file do you want me to check?")
extension = os.path.splitext(file)[1]

if extension:
    print(extension)
else:
    raise AssertionError(f"No extension in the specified file: {file}")
