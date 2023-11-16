from collections import deque
import sys
input=sys.stdin.readline
Q=deque()

n=int(input())

for _ in range(n):
    
    a=input().rstrip()

    if a[:4]=="push":
        Q.append( int(a[5:]) )
        
    
    
    if a=="front":
        if Q:
            print(Q[0])
        else:
            print(-1)
        

        
    if a=="back":
        if Q:
            print(Q[-1])
        else:
            print(-1)
        

    if a=="size":
        print(len(Q))
        


    if a=="empty":
        
        if not Q:
            print(1)
        else:
            print(0)


        
    if a=="pop":
        if Q:
            print(Q.popleft())
        else:
            print(-1)
        




