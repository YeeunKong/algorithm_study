import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, 0, 0, -1, 1]  # 위, 아래, 상, 하, 좌, 우
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

m, n, h = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        graph[i][j] = list(map(int, input().split()))

queue = deque()
day = -1

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if (nx<0) or (nx>=m) or (ny<0) or (ny>=n) or (nz<0) or (nz>=h):
                continue

            if graph[nz][ny][nx] == 0 and graph[nz][ny][nx] != -1:
                queue.append((nx, ny, nz))
                graph[nz][ny][nx] = graph[z][y][x]+1


for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                queue.append((x, y, z))

bfs()

for floor in graph:
    for lst in floor:
        if 0 in lst:
            day = 0
            break
        if max(lst) > day:
            day = max(lst)

print(day-1)

