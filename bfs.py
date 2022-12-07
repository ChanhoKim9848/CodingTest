graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9

from collections import deque

def bfs(v):
    visited[v]=True
    Q=deque([v])

    while Q:
        n=Q.popleft()
        print(n, end=" ")
        for i in graph[n]:
            if not visited[i]:
                Q.append(i)
                visited[i]=True

bfs(1)
    


