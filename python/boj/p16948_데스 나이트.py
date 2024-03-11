# 체스판은 0번부터 시작
# N * N크기
# 시작점에서 끝점까지 최소 이동 횟수
import sys

dx = (-2, -2, 0, 0, +2, +2)
dy = (-1, +1, -2, +2, -1, +1)


def is_out(x, y):
    return not (-1 < x < N) or not (-1 < y < N)


def bfs(x1, y1, x2, y2):
    q = []
    q.append((x1, y1))
    visited = []
    step = 0

    while q:
        step += 1
        for _ in range(len(q)):
            pos = q.pop(0)
            for i in range(6):
                nx, ny = pos[0] + dx[i], pos[1] + dy[i]
                # 종료 조건 : 만약 도착했는지
                if nx == x2 and ny == y2:
                    return step
                # 맵 밖으로 나갔는지 체크
                if is_out(nx, ny):
                    continue
                # 방문했는지
                t = (nx, ny)
                if t in visited:
                    continue
                visited.append(t)
                q.append(t)
    return -1


# input
N = int(input())
R1, C1, R2, C2 = map(int, input().split())

ans = bfs(R1, C1, R2, C2)

print(ans)