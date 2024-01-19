# 시작하고 끝칸도 센다
# 한개의 벽 부술 수 있음
# 상하 좌우 이동 가능
# 최단 경로 구해라
# bfs ㄱㄱ
# 벽 부시기 스킬 썻는지 여부 체크
# 불가능시 -1

from collections import deque
import sys

input = sys.stdin.readline

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def bfs():  # 0,0에서 N -1, M -1까지
    q = deque()
    q.append((0, 0, 0))  # x, y, skill_count
    visited = [[[False] * M for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = True

    cur_step = 0
    while q:
        cur_step += 1  # 시작 위치도 포함하므로
        for _ in range(len(q)):
            x, y, skill_count = q.popleft()
            if x == M - 1 and y == N - 1:
                # 성공
                print(cur_step)
                return
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵 밖으로 나가는지 체크
                if not (-1 < nx < M) or not (-1 < ny < N):
                    continue
                # visited 체크
                if visited[skill_count][ny][nx]:
                    continue
                visited[skill_count][ny][nx] = True
                # 벽인지 체크
                is_wall = board[ny][nx] == 1

                # 경우의 수
                # 1. 가는 경우
                # 2. 벽을 뚫고 가는 경우
                # 3. 벽이라서 스킵하는 경우
                if not is_wall:
                    q.append((nx, ny, skill_count))
                elif is_wall and skill_count == 0:
                    q.append((nx, ny, skill_count + 1))
    print(-1)


# input
N, M = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
ans = sys.maxsize

bfs()