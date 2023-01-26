import random
from string import ascii_lowercase,digits
CHOICE = ascii_lowercase + digits + '_' + '.'
a=''.join([random.choice(CHOICE) for i in range(random.randint(1,100))])+'@gmail.com'
b=True
for i in a:
    if a.count('@') != 1:
        b=False
    elif i not in CHOICE and i not in '_@.':
        b=False
    #elif len(a)


print(b)
print(a)
print(a.find("e"))
a=a.split('@')
print(a)