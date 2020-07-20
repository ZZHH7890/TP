'''
@Author: joker.zhang
@Date: 2020-07-20 22:21:57
@LastEditors: joker.zhang
@LastEditTime: 2020-07-20 22:46:00
@Description: For Automation
'''
a = ['1', '2', '3', '', '5']
b = ','.join(a)
print(b, type(b), len(b))
c = b.split(',')
print(c, type(c), len(c))

d = ['6']
e = ','.join(d)
print(e)

if ',' in "123,44":
    print('true')
else:
    print('false')
