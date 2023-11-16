import sys
input=sys.stdin.readline

n=int(input())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append([y,x])

a.sort()

for y,x in a:
    print(x, y)

