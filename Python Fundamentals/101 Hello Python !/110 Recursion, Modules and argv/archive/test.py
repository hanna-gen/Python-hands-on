'''def f1(nr):
    if nr-1==0:
        print(f'prime:{nr}')
    elif nr%2==0:
        if nr-2==0:
            print(f'prime:{nr}')
        else:
            print(f'non-prime:{nr}')
        f1(nr-2)
    else:
        f1(nr-1)
f1(15)'''

l = ('hgtf', 'kkkkk')
print(',,,,,'.join(l))