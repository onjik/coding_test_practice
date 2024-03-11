from collections import deque

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def bfs(x, y):
    global visited, board
    q = deque()
    q.append((x, y))
    visited[y][x] = True
    count = 0
    while q:
        cx, cy = q.popleft()
        board[cy][cx] = idx
        count += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 맵 밖 체크
            if not (-1 < nx < M) or not (-1 < ny < N):
                continue
            if board[ny][nx] == 1:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            q.append((nx, ny))

    return count


# input
N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
group = dict()
ans = [[0] * M for _ in range(N)]

idx = 2

for x in range(M):
    for y in range(N):
        if board[y][x] == 0 and not visited[y][x]:
            count = bfs(x, y)
            group[idx] = count
            idx += 1
# 돌면서 출력
for y in range(N):
    for x in range(M):
        if board[y][x] != 1: # 원래 빈칸이었던 경우
            continue
        groups = set()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < M) or not (-1 < ny < N):
                continue
            if board[ny][nx] == 1:
                continue
            groups.add(board[ny][nx])
        ans[y][x] = (sum(map(lambda x : group[x], groups)) + 1) % 10

for row in ans:
    print("".join(map(str,row)))