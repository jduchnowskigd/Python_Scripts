#!/usr/bin/python


"""
Script which counts occurences of each character in a string provided
"""
string = input("Input a string which should be parsed")
char_counts = {}
for char in string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1
print(char_counts)
