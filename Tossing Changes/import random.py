import random
a = []
for i in range (100000000):
    n =1
    while (random.randint(1,6) != 6):
        n += 1
    a.append(n)

print (sum(a)/ len(a))

