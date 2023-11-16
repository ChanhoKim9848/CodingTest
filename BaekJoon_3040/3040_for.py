import sys
array=[]
input=sys.stdin.readline

for _ in range(9):
    array.append(int(input()))

array.sort()


for i in range(len(array)):
    for j in range(i+1, len(array)):

        if sum(array)-array[i]-array[j]==100:

            for k in range(len(array)):
                if k==i or k==j:
                    continue

                else:
                    print(array[k])
                
            exit()

# referenced from :https://ji-gwang.tistory.com/244


