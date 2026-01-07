import secrets
import string 

print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)
all_chars = string.ascii_letters + string.digits + string.punctuation
print(all_chars)

# Generating the random passwords
print(secrets.choice(all_chars))

print(secrets.choice(all_chars) for i in range(10))
print(tuple(secrets.choice(all_chars) for i in range(11)))
print(set(secrets.choice(all_chars) for i in range(11)))