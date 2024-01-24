# put your python code here
def counter_add(tp='list'):
    def a(s):
        if tp=='list':
            return [x for x in s]
        else:
            return tuple(s)
    return a
k = input()
m = list(map(int,input().split()))
cnt=counter_add(k)
print(cnt(m))