# 110 Recursion, Modules and argv 
# Heap's algorithm
# Modify the script to work with long words. We require that it prints approx. 20 randomly chosen permutations of the input word. 
# It is important that the printed permutations are chosen at random, but it is not important to print exactly 20 each time. 
# (Hint: import math, random. You are allowed to use global variables!) 

import sys
import math
import random

cnt_perm=0
cnt_print=20
lst_rnd=[]

def generate_permutations(a, n):
    max_nr_perm=math.factorial(len(a))
    while len(lst_rnd) < cnt_print:
        lst_rnd.append(random.randint(1, max_nr_perm))
    if n == 0:
        global cnt_perm
        cnt_perm=cnt_perm+1
        #if cnt_perm==random.randint(1, max_nr_perm):
        for i in lst_rnd:
            if cnt_perm == i:
                print(''.join(a))               
    else:
        for i in range(n): 
            generate_permutations(a, n-1)  
            j = 0 if n % 2 == 0 else i 
            a[j], a[n] = a[n], a[j] 
        generate_permutations(a, n-1) 

if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

word=sys.argv[1]

generate_permutations(list(word), len(word)-1)

#give the following arguments in the terminal to run the same:
#python "C:\Users\hanna.marushchak\OneDrive - Adastra, s.r.o\Desktop\Python Advanced\latest\110 Recursion, Modules and argv.py" war


'''import sys, re

counts = {}
for line in sys.stdin:
    for word in re.findall(r'[a-z\']+', line.lower()):
        counts[word] = counts.get(word, 0) + 1
        for word, count in sorted(counts.items()):
            print(f'word: {word}, count: {count}')'''


