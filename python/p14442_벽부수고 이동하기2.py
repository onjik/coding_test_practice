# 시작 끝 칸 포함 최단 경로
# K개 까지 벽을 부수고 이동해도 된다.
# K 차원 Visited?

from collections import deque

dx = (1,-1,0,0)
dy = (0,0,1,-1)

# 0,0 에서 M-1, N-1
def bfs():
    q = deque()
    visited = [[[False] * M for _ in range(N)] for _ in range(K + 1)]
    q.append((0,0,K)) # x, y, skill_left
    visited[0][0][0] = True
    step = 0
    while q:
        step += 1
        for _ in range(len(q)):
            x, y, wc = q.popleft()
            # 정답 체크
            if (x == M - 1) and (y == N - 1):
                return step
            # 가지 치기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # map out
                if not (-1 < nx < M) or not (-1 < ny < N):
                    continue
                # 벽인데 스킬 다쓴 경우
                is_wall = board[ny][nx] == 1
                if is_wall and wc == 0:
                    continue
                # visited
                if visited[wc][ny][nx]:
                    continue
                visited[wc][ny][nx] = True
                # 벽이 아닌 경우 그냥 방문
                if is_wall:
                    q.append((nx,ny,wc - 1))
                else:
                    q.append((nx,ny,wc))
    return -1

# Input
N, M, K = map(int, input().split())
board = [list(map(int,list(input()))) for _ in range(N)]

ans = bfs()
print(ans)