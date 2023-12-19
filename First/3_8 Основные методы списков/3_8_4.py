lst=list(input())
del lst[0]
lst[0]='8'
lst=''.join(lst)
lst=lst.replace('-','')
print(''.join(lst))