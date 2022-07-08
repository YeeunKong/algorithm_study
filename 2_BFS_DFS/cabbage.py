from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]  #상, 하, 좌, 우
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue.append((x, y))
    graph[y][x] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 배추밭(graph) 범위에서 벗어나면 다음 칸으로 이동
            if (nx<0) or (nx>=m) or (ny<0) or (ny>=n):
                continue
            # 이동한 배추밭(graph) 숫자가 1이면 queue에 삽입
            if graph[ny][nx] == 1:
                queue.append((nx, ny))
                graph[ny][nx] = 0    

t = int(input())
cnt = [0 for _ in range(t)]
for test in range(t):
    # 입력 받기 및 변수 선언
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for i in range(k):
        u, v = map(int, input().split())
        graph[v][u] = 1
    cnt[test] = 0
    queue = deque()
    for i in range(n):      #세로
        for j in range(m):  #가로
            if graph[i][j] == 1:
                bfs(j, i)
                cnt[test] += 1  

print(*cnt, sep='\n')

