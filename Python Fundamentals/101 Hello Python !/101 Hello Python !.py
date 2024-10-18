# 101 Hello Python !
# Pythagorean triples
# Modify the program so that it also prints the count of the Pythagorean triples at the end

cnt = 0 
for c in range(1, 48):
    for b in range(1, c):
        for a in range(1, b):
            if a * a + b * b == c * c:
                cnt += 1
                print('{}, {}, {}'.format(a, b, c))
print('Total count: {}'.format(cnt))







