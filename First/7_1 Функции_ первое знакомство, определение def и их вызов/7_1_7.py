# put your python code here
def out(width,height):
    print(f'Периметр прямоугольника, равен {(width+height)*2}')
width,height= map(int,input().split())
out(width,height)