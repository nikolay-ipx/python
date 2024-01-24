# put your python code here
def counter_add(tag=''):
    def a(s):
        return '<'+tag+'>'+s+'</'+tag+'>'
    return a
k = input()
m = input()
cnt=counter_add(k)
print(cnt(m))