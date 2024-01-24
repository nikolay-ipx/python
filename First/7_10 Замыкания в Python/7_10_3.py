# put your python code here
def counter_add():
    def a(s):
        return '<h1>'+s+'</h1>'
    return a
k = input()
cnt=counter_add()
print(cnt(k))