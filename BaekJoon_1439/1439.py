s=input()
c=0
prev=""
#101010
for i in s:
    if prev!=i:
        prev=i
        c+=1
print(c//2)

# referenced from https://codingpractices.tistory.com/72