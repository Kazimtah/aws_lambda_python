import secrets
import string

def generat_password(lenght: int):
    """
    This is function is used to generat a random password for a user
    lengh = Argument is used set the lengh of password that this will create
    """
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_chars) for _ in range(lenght))

    return password

def generate_special_password(lenght: int):
    """
    Docstring for generate_special_password
    
    :param lenght: Lenght of the password to be generated 
    :type lenght: int
    """
    while True:
        p = generat_password(lenght)
        if any(c.islower()for c in p and any(c.isupper() for c in p) and any(c.punctuation for c in p)):
            break
    return p
password1_special_password = generate_special_password(15)
print(password1_special_password)
password2 = generat_password(24)
print(password2)