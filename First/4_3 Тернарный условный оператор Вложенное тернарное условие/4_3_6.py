m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a,b,c=map(int,input().split())
a=m[a-1]
a='#'+a if a=='до' or a=='фа' else a
b=m[b-1]
b='#'+b if b=='до' or b=='фа' else b
c=m[c-1]
c='#'+c if c=='до' or c=='фа' else c
print(a,b,c)