from queue import PriorityQueue


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, value = map(int, input().split())
    graph[a].append((value, b))
    graph[b].append((value, a))

begin, end = map(int, input().split())
rada = PriorityQueue()
rada.put((0, begin))
visited = [-1] * (n + 1)

while (not rada.empty()):
    value, vrchol = rada.get()

    if (vrchol == end):
        print(value)
        exit(0)

    if (visited[vrchol] == -1):
        visited[vrchol] = value

        for new_value, sused in graph[vrchol]:
            if (visited[sused] == -1):
                rada.put((new_value + value, sused))


print(-1)
