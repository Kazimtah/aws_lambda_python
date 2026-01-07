import secrets
import string 



#Generating the token in a hexa decimal formate of python 

print(secrets.token_hex(8))
print(secrets.token_hex(10))
print(secrets.token_bytes(15))
print(secrets.token_urlsafe(20))

# Generating authentication token by using secrte modules

print(secrets.token_urlsafe(8))

def generator_otp_password(lenght):
    digit = string.digits
    password = ''.join(secrets.choice(digit) for _ in range(lenght))
    return password

passord1 = generator_otp_password(20)
print(passord1)
password2 = generator_otp_password(30)
print(password2)
password3 = generator_otp_password(15)
print(password3)
password4 = generator_otp_password( 12)
print(password4)