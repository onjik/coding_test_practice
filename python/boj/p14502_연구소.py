import copy
from collections import deque
import sys
input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def count_safe_zone():
    q = deque()
    test_map = copy.deepcopy(board)
    for x in range(M):
        for y in range(N):
            if test_map[y][x] == 2:
                q.append((x,y))

    while q:
        px, py = q.popleft()

        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]

            if (-1 < nx < M) and (-1< ny < N):
                if test_map[ny][nx] == 0:
                    test_map[ny][nx] = 2
                    q.append((nx,ny))

    # count zero
    count = 0
    for x in range(M):
        for y in range(N):
            if test_map[y][x] == 0:
                count += 1
    return count


# wc : wall count
def dfs(wc):
    global ans, board
    if wc == 3:
        ans = max(ans, count_safe_zone())
        return

    for nx in range(M):
        for ny in range(N):
            if board[ny][nx] == 0:
                board[ny][nx] = 1
                dfs(wc + 1)
                board[ny][nx] = 0

# input
N, M = map(int, input().split())
ans = 0
board = [list(map(int, input().split())) for _ in range(N)]

dfs(0)

print(ans)