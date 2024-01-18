a=input().split(' ')
d={}
for i in a:
    kod=i[:2]
    if kod not in d:
        d[kod]=[]
        for c in a:
            if c[:2]==kod:
                d[kod].append(c)
print(*sorted(d.items()))