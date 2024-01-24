# put your python code here
notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a=list(map(str,input().split()))
b=[]
for i in a:
    if i in notes:
        b.append(notes.index(i))
b=sorted(b)
c=[]
for i in b:
    c.append(notes[i])
print(*c)