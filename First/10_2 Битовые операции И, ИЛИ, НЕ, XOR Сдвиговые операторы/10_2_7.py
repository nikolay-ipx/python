# put your python code here
a=input()
key=123
b=[]
for i in a:
    i=ord(i)^key
    b.append(chr(i))
print(''.join(b))