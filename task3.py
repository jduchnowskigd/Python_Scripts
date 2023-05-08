#!/usr/bin/bash

"""
Script that reads the access log from a file, and prints the number of unique User Agents,
as well as the name of each individual User Agent and number of times their name appeared
in the access log
"""

# Open the access.log file for reading
with open('access.log.5', 'r', encoding='utf-8') as file:
    USER_DICT = dict()
    # Loop over each line in the file
    for line in file:

        # Split the line into fields
        fields = line.split()

        USER_AGENT = " ".join(fields[11:])
        if USER_AGENT in USER_DICT:
            USER_DICT[USER_AGENT] += 1
        else:
            USER_DICT[USER_AGENT] = 1
	#print(USER_DICT)
    print(f'Number of unique User Agents = {len(USER_DICT.values())}')
    for entry in USER_DICT.items():
        print(entry)
        print("\n")
