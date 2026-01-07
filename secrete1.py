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

def password_generator(lenght):
    all_chars = all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(set(secrets.choice(all_chars) for i in range(lenght)))
    return password

pasword1 = password_generator(7)
print(pasword1)
password2 = password_generator(10)
print(password2)
password3 = password_generator(15)
print(password3)
