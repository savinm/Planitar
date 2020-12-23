#! /usr/bin/python3

# Importing Working Libraries
import os
from pathlib import Path

input = input("Enter searching directory: ")

str(input)

# Accessing Data about Directories
os.chdir(input)
cwd = os.getcwd()

# Main Loop for recursively itirating for Dockerfile, as well as searching for parent image 
for path in Path(cwd).rglob('Dockerfile'):

    real_path = str(path)[0:-11]

    os.chdir(os.path.join(real_path))

    dockerfile = open('Dockerfile', 'r')
    temp_dockerfile = dockerfile.readlines()
    dockerfile.close()


    for line in temp_dockerfile:
     if str(line).startswith("FROM"):

      final_line = str(line.replace("FROM", ""))
      print(os.path.join(path) + ":" + final_line)

