import math
import random

l=len('warjklk')
max_nr=math.factorial(len('warjklk'))
'''
cnt=1

while cnt <= 5:
    for i in range(1, max_nr):
        if i == random.randint(1, max_nr):
            print(i)
            cnt = cnt + 1
'''
lst=[]
#c=1
while len(lst)<=5:
    lst.append(random.randint(1, max_nr))
#print(lst)
for i in range(1, max_nr):
    for ii in lst:
        if i == ii:
            print(i)



