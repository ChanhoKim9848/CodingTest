n=int(input())
a=[int(input()) for _ in range(n)]
a.sort()


count=[]

for i in range(n):
    c=0
    for j in range(a[i],a[i]+5):
        
        if j not in a:
            c+=1
    
    count.append(c)

print(min(count))
    
# referenced https://yeowool0217.tistory.com/610