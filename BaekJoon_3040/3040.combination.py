import itertools
a=[int(input()) for i in range(9)]
for i in itertools.combinations(a, 7):
    if sum(i)==100:
        for j in sorted(i):
            print(j)
    break


# referenced from : https://ji-gwang.tistory.com/244