#!/usr/bin/python
"""
This module can be used to remove duplicates and
find the maximum and minimal value
in a provided list of integers
"""

numbers=input("Input the number array")

numbers_list = numbers.split()

unique_numbers = tuple(set(numbers_list))

min_number = min(unique_numbers)
max_number = max(unique_numbers)

# Print the results
print("Input list:", numbers_list)
print("Unique numbers:", unique_numbers)
print("Minimum number:", min_number)
print("Maximum number:", max_number)
