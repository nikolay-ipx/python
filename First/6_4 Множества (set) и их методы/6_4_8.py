# put your python code here
a=set()
while True:
    b=input()
    if b=='q':
        break
    else:
        a.add(b)
print(len(a))