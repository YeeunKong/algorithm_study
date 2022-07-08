from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]  #상, 하, 좌, 우
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()
day = 0 

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx<0) or (nx>=m) or (ny<0) or (ny>=n):
                continue

            if graph[ny][nx] == 0 and graph[ny][nx] != -1:

                queue.append((nx, ny))
                graph[ny][nx] = graph[y][x]+1

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            queue.append((x, y))

bfs()

for lst in graph:
    if 0 in lst:
        day = 0
        break
    if max(lst) > day:
        day = max(lst)

print(day-1)
