# put your python code here
def out(a, tag='h1',up=True):
    if up == True:
        print('<'+tag.upper()+'>'+a+'</'+tag.upper()+'>')
    else:
        print('<'+tag+'>'+a+'</'+tag+'>') 
a=input()
out(a,tag='div')
out(a,tag='div',up=False)