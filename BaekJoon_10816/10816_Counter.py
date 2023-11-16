import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
card=list(map(int,input().split()))
m=int(input())
test=list(map(int,input().split()))

count=Counter(card)

for i in test:
    if i in count:
        print(count[i],end=' ')
    else:
        print(0, end=' ')

