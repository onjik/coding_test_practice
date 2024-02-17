# 상하 좌우 같은 색으 인접칸으로
# 적록 색약은 R과 G를 같은 색으로 본다
# R 다 탐색한 후에
# G 탐색하고
# B 맨 마지막에

from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)


def bfs(x, y, colors):
    q = deque()
    q.append((x, y))
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]
            # 맵 밖에 있으면 안된다
            if not (-1 < nx < n) or not (-1 < ny < n):
                continue
            # 방문 체크
            if visited[ny][nx]:
                continue
            # 색상 체크
            if board[ny][nx] not in colors:
                continue

            # 이제 방문한다
            q.append((nx, ny))
            visited[ny][nx] = True


# input
n = int(input())
board = [list(input()) for _ in range(n)]

# R 하고 G 부터 탐색
ans = 0
d_ans = 0

visited = [[False] * n for _ in range(n)]

# 색맹 아닌사람 체크
for y in range(n):
    for x in range(n):
        if visited[y][x]:
            continue
        colors = set()
        colors.add(board[y][x])
        ans += 1
        bfs(x, y, colors)

visited = [[False] * n for _ in range(n)]

# 색맹 아닌사람 체크
for y in range(n):
    for x in range(n):
        if visited[y][x]:
            continue
        colors = set()
        if board[y][x] == 'R' or board[y][x] == 'G':
            colors.add('R')
            colors.add('G')
        else:
            colors.add('B')
        d_ans += 1
        bfs(x, y, colors)

print(f"{ans} {d_ans}")