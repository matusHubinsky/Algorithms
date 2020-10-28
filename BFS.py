n, m = [int(x) for x in input().split()]
graph = [[0 for _ in range(0)] for _ in range(n)]
visited = [False] * n


def bfs(start, end):
    queue = []
    queue.append(start)
    visited[start] = True
    path_lenght = 0

    while (queue):
        vrchol = queue.pop(0)

        for syn in graph[vrchol]:
            if (not visited[syn]):
                visited[syn] = True
                queue.append(syn)
            path_lenght += 1

            if (syn == end):
                return path_lenght
    return -1


for i in range(m):
    a, b = [int(x) for x in input().split()]
    graph[a - 1].append(b - 1)

start, end = [int(x) for x in input().split()]

if (start == end): 
    print('0')
else: 
    print(bfs(start - 1, end - 1))
