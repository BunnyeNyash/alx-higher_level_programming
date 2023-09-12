#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
import os
from json import dumps

# Importing the specific functions from the modules
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

# Check if the file exists, if not, create an empty list
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
