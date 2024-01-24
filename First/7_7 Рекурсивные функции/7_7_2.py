# считывание числа N
N = int(input())

#здесь продолжайте программу
def get_rec_N(N):
    if N>0:
        get_rec_N(N-1)
        print(N)