l1 = lambda x, y: x + y
#print(l1(1,1))

l2 = [lambda x: x + i + 1 for i in range(24, 42)][0](0) 
#print(l2)

# Create a lambda which returns the first item in a list: 
names = ['Carina', 'Ivan', 'Sophia']
l3 = lambda n: n[0]
print(l3(names))

names = [{'Ivan': 12}, {'Anna': 44}]
filtered_names = filter(lambda x: list(x.values())[0]>18, names)
print(list(filtered_names))

sorted_names = sorted(names, key = lambda x: list(x.keys())[0])
print(sorted_names)

# generators
def my_gen(n):
    i = 0
    while i < n:
        yield n
        i += 1
g = my_gen(3)
#print(type(g))
for x in g:
    print(x)




####################################################################################################

# exercises from https://www.youtube.com/watch?v=HBR6wqXj2iY&list=PLH6mU1kedUy84TsNa1654qkHjIeZ_wllA

numbers = [2, 4, 6]
double = map(lambda x: x*x, numbers)
#print(list(double))

strings = ['aaa', 'bbb']
get_upper = map(lambda x: x.upper(), strings)
#print(list(get_upper))

l = [3, 2, 4, 1]
#srt = lambda x: sorted(x)
#print(srt(l))

#srt = lambda x: x.sort()
#srt(l)
#print(l)

#l.sort(key = lambda x: x*3)
#print(l)

t = [('a', 3), ('c', 1), ('b', 2)]
t.sort(key = lambda x: x[1])
#print(t)

countries = ['us', 'uk', 'germany']
#countries_new = filter(lambda x: x if len(x) > 3 else None, countries)
countries_new = filter(lambda x: len(x) > 3, countries) #same output as above
#print(list(countries_new))

from functools import reduce
l_summed_up = reduce(lambda x,y: x+y, l)
#print(l_summed_up)
l_max = reduce(lambda x,y: max(x,y), l)
#print(l_max)

l2 = [3, 2, 4, 1]
l_l2_summed_up = map(lambda x,y: x+y, l,l2)
#print(list(l_l2_summed_up))



