import hashlib
# Rtrams
# reverse-Smart
# Splkiyoaner
# skip-lion

email = 'jkr@gmail.com'
pwd = 'ChairOnTableWith3Legs'
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

your_email = 'jkr@gmail.com'
Your_password = '5f4dcc3b5aa765d61d8327deb882cf99'

hashed_your_password = hashlib.md5(Your_password.encode()).hexdigest()
if email == your_email and pwd_hash == hashed_your_password:
    print('right user')
else:
    print('wrong password')

hacker_email = 'jkr@gmail.com'
hacker_password = '5f4dcc3b5aa765d61d8327deb882cf99'

print(pwd)
print(pwd_hash)