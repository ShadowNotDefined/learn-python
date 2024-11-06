# Import the secrets module
import secrets

# Prompt the user and get their input
password_num = int(input("Number of passwords you want to generate: "))

# A for loop that creates a number of passwords equal to the users input
for i in range(password_num):
    print(secrets.token_urlsafe())