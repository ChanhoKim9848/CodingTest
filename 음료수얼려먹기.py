# 첫번째 줄에 얼음 틀의 세로 길이 N과 가로길이 M이 주어진다 
# 두 번째 줄부터 N+1 번째 줄까지 얼음 틀의 형태가 주어진다
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1

#입력예시                출력예시
# 4 5                   3
# 00110
# 00011
# 11111
# 00000

N,M=map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input())))

def dfs(n,m):
    if n>=N or n<0 or m<0 or m>=M:
        return False
    if graph[n][m]==0:
        graph[n][m]=1
        dfs(n-1,m)
        dfs(n,m-1)
        dfs(n,m+1)
        dfs(n+1,m)
        return True
    return False
c=0
for i in range(N):
    for j in range(M):
        if dfs(i,j)==True:
            c+=1
print(c)




