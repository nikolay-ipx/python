# put your python code here
def get_rec_sum(x, i = 0):
    if i >= len(x):
        return 0
    return x[i] + get_rec_sum(x,i + 1)
a=list(map(int, input().split()))
print(get_rec_sum(a))