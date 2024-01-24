# put your python code here
def counter_add(n):
    def a(x):
        return n+x

    return a
k = int(input())
cnt=counter_add(2)
print(cnt(k))