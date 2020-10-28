import sys


def dfs(node):
    global graph, leaves, visited
    visited[node] = True
    
    if len(graph[node]) != 0:
        for son in graph[node]:
            if not visited[son]:
                dfs(son)
    
    if len(graph[node]) == 1 and node != 0:
        leaves += 1
    

n = int(input())

if (n <= 1):
    print(0)
else:  
    graph = [[] for x in range(n)]
    visited = [False] * (n)
    sys.setrecursionlimit(10**6)
    leaves = 0

    for i in range(n-1):
        a, b = [int(x) for x in input().split()]
        graph[a-1].append(b-1)    
        graph[b-1].append(a-1)
        
    dfs(0)
    print(leaves)