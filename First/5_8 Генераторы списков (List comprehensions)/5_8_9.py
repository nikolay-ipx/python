a=input().split()
lst=[[a[x],int(a[x+1])] for x in range(0,len(a),2)]
print(lst)