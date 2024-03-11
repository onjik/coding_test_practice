# 시작칸 끝칸 포함 최단 경로
# 이동하지 않고 같은 칸에 머무는 것도 가능
# 한번 이동할 때마다 낮 밤 바뀜
# 벽을 K개 까지 부술 수 있다.
# 낮에만 부술 수 있다.
# 시작시 낮
import sys
# K 차원 visited 체크를 하면서 bfs
# 낮 밤은 홀 짝으로 체크하고
# 가지치기 시 visited 체크를 하고,
# 제자리에 있는 경우는 특수한 경우로 q에 추가
from collections import deque

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)




# input
N, M, K = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
MAX = sys.maxsize

q = deque()
visited = [[[MAX] * M for _ in range(N)] for _ in range(K + 1)]
q.append((0, 0, K))  # x, y, skill_left
# 1 = 낮, 0 = 밤
# visited[1][K][0][0] = True

step = 0

while q:
    step += 1
    daytime = step % 2
    for _ in range(len(q)):
        x, y, left = q.popleft()
        if x == M-1 and y == N -1:
            print(step)
            exit()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 맵 체크
            if not (-1 < nx < M) or not (-1 < ny < N):
                continue
            if board[ny][nx] == 1 and left and visited[left-1][ny][nx] > step:
                if daytime:
                    visited[left-1][ny][nx] = step
                    q.append((nx,ny,left-1))
                else:
                    q.append((x,y,left)) # 제자리에서 기다림
            elif board[ny][nx] == 0 and visited[left][ny][nx] > step:
                visited[left][ny][nx] = step
                q.append((nx,ny,left))

print(-1)