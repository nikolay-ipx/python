# put your python code here
def get_path(N):
    if N == 0 or N == 1 or N == 2:
        return N
    else:
        return get_path(N-2)+get_path(N-1)
N=int(input())
print(get_path(N))