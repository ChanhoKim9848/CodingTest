import sys

input=sys.stdin.readline

n=int(input())
card=list(map(int,input().split()))
m=int(input())
test=list(map(int,input().split()))

hash={}

for i in card:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1

for i in test:
    if i in hash:
        print(hash[i],end=' ')
    else:
        print(0,end=' ')






# referenced from: https://hongcoding.tistory.com/12  (NOV.03.23)
