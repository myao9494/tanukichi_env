import random
print ('Usage:')
print ('    gen_passwd.py length count')
passlen = 20
count = 5
s = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ123456789'
for i in range(count):
    password = ''
    for j in range(passlen):
        password += random.choice(s)
    print(password)
