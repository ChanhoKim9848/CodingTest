import random
a=[]
for i in range(9):
    a.append(int(input()))
b=random.sample(a,7)
while sum(b)!=100:
    b=random.sample(a,7)
b.sort()
for i in b:
    print(i)

