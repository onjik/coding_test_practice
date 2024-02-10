# bfs 로 풀되, 쭉 진행 하며 모두 집어 넣기?
# 대신 Visited를 숫자로 체크해서 자기보다 큰 것만 업데이트 하는 식으로

from collections import deque
import sys

# input
W, H = map(int, input().split())
board = [list(input()) for _ in range(H)]

# 시작 위치 찾기
tmp = []
for y in range(H):
    for x in range(W):
        if board[y][x] == 'C':
            tmp.append((x, y))
(sx, sy), (ex, ey) = tmp

# bfs로 찾는다
dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

q = deque()
visited = [[0] * W for _ in range(H)]

# init
q.append((sx, sy, -1))
visited[sy][sx] = 1

while q:
    # 하나 꺼낸다
    x, y, cnt = q.popleft()
    if x == ex and y == ey:
        print(cnt)
        exit()

    for i in range(4):
        nx, ny = x, y
        while True:
            nx, ny = nx + dx[i], ny + dy[i]

            # 맵체크
            if not (-1 < nx < W) or not (-1 < ny < H):
                break
            # 벽 체크
            if board[ny][nx] == '*':
                break
            # 방문 체크
            # 이미 방문했다고 BREAK를 걸지 않는다(여기서 틀렸었음)
            if not visited[ny][nx]:
                q.append((nx, ny, cnt + 1))
                visited[ny][nx] = 1