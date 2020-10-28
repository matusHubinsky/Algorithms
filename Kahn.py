n, m = [int(x) for x in input().split()]
graph = [[0 for _ in range(0)] for _ in range(n)]
neighbors = [0] * n
order = []
queue = []
visited = 0

for i in range(m):
    a, b = [int(x) for x in input().split()]
    graph[a - 1].append(b - 1)
    neighbors[b - 1] += 1

for i in range(len(neighbors)):
    if (neighbors[i] == 0):
        queue.append(i)

while (len(queue) != 0):
    index = 0
    visited += 1

    for prvok in graph[queue[index]]:
        neighbors[prvok] -= 1

        if (neighbors[prvok] == 0):
            queue.append(prvok)

    order.append(queue[index] + 1)
    queue.pop(0)

if (visited != n):
    print('-1')
else:
    print(' '.join([str(x) for x in order]))
