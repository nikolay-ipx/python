a=input()
b1='0123456789'
b=['+','7','(',b1,b1,b1,')',b1,b1,b1,'-',b1,b1,'-',b1,b1]
c=0

for i in a:
    if len(a)>16 or len(a)<16:
        print('НЕТ')
        break
    if i not in b[c]:
        print('НЕТ')
        break
    if c==len(a)-1:
        print('ДА')
    else:
        c+=1