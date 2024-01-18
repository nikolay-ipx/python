# put your python code here
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
a=int(input())
t2=[x[:a] for x in t[:a]]
for i in t2:
    print(*i)