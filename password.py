import random

numbers = '1234567890'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
symbols = '!@#$%&*_+|'

all_chars = numbers + upper + lower + symbols


length = int(input('enter password length'))
password = ""
for i in range(length):
  password += random.choice(all_chars)
print(password)
