import random
import string
password_length = int(input("Enter the length of the password: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(password_length):
  password = password + random.choice(characters)
print("password is: " + password)
