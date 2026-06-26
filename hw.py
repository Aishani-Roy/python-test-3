import random
import string
length = int(input("Enter the password length: "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
password = [
    random.choice(lower),
    random.choice(upper),
    random.choice(digits)]
all_characters = lower + upper + digits
for i in range(length - 3):
    password.append(random.choice(all_characters))
random.shuffle(password)
password = "".join(password)
print("Generated Password:", password)