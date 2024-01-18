a=input().split(' ')
a=dict([x.split('=') for x in a])
if 'house' in a and 'True'in a and '5' in a:
    print('ДА')
else:
    print('НЕТ')
