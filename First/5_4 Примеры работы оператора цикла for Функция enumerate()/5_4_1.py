s=input()
if not 'ра' in s:
    print(-1)
else:
    for i in range(len(s)-1):
        if s[i]=='р' and s[i+1]=='а':
            print(i,end=' ')