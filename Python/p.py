import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
for i in range(8):
    password = password + random.choice(characters)
print("Random Password =", password)