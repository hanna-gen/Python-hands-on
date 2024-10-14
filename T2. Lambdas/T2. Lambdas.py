from pprint import pprint

# Task 1
s1 = 'This is a lAmBdA FuNction task'
my_lambda1 = lambda x: ([i, i.upper(), i.lower(), len(i)] for i in x.split(' '))

l1 = my_lambda1(s1)
final_list1 = [
    next(l1) for i in range(len(s1.split())-1)
               ]

# Task 2
s2 = 'This is a lAmBdA FuNction task'
final_list2 = list(
    map(
    lambda x: [x.upper(), x.lower(), len(x)]
            , s2.split()
            )
)

# Task 3
a = [12, 1, 11, 23, 44, 100, 16]
b = [2, 3, 5, 100, 6, 7, 8, 44, 16, 12]

final_list3 = list(
    filter(
        lambda x: x if x in b else None
    , a
    )
)

# Task 4:
s4 = 'This is a lAmBdA FuNction task'
final_list4 = sorted(s4.split(), key=lambda x: x[::-1])

def main():
    separator = '-' * 40
    results = {
        1: final_list1, 
        2: final_list2, 
        3: final_list3, 
        4: final_list4
    }
    for n in range(1, len(results)+1):
        print(f'Result of task {n}:')
        pprint(results[n])
        print(separator)

if __name__ == '__main__':
    main()


'''
# below function is not lambda, but an algorhythm example on how to iterate through each list only once - relates to task 3:
def intersect(arr1, arr2):
    final_arr = []
    arr1.sort()
    arr2.sort()
    pointer1 = 0
    pointer2 = 0

    while True:
        try:
            if arr1[pointer1] == arr2[pointer2]:
                final_arr.append(arr1[pointer1])
                pointer1 += 1
                pointer2 += 1

            if arr1[pointer1] < arr2[pointer2]:
                pointer1 += 1 

            if arr1[pointer1] > arr2[pointer2]:
                pointer2 += 1
        except:
            IndexError
            break

    print(final_arr)

intersect(a, b) 
'''  


