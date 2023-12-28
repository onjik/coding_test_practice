# bfs 활용

import sys

input = lambda: sys.stdin.readline().rstrip()


# 초기값 전달
def bfs(x1, y1, x2, y2):
    q.clear()
    q.append([x1, y1, x2, y2])
    # 방문 체크용
    visited = [[[[-1] * N for _ in range(M)] for _ in range(N)] for _ in range(M)]

    # 첫번째 방문 처리
    visited[x1][y1][x2][y2] = 0

    while q:
        x1, y1, x2, y2 = q.pop(0)
        if visited[x1][y1][x2][y2] >= 10:
            break
        for i in range(4):
            xx1 = x1 + dx[i]
            yy1 = y1 + dy[i]
            xx2 = x2 + dx[i]
            yy2 = y2 + dy[i]

            # 둘다 나가면, 나가리
            if not (0 <= xx1 < M and 0 <= yy1 < N) and not (0 <= xx2 < M and 0 <= yy2 < N):
                continue
            # 하나만 나가면, 성공
            if not (0 <= xx1 < M and 0 <= yy1 < N) or not (0 <= xx2 < M and 0 <= yy2 < N):
                return visited[x1][y1][x2][y2] + 1
            # 벽을 만난경우, 되돌리기
            if graph[yy1][xx1] == "#":
                xx1, yy1 = x1, y1
            if graph[yy2][xx2] == "#":
                xx2, yy2 = x2, y2

            # 처음 발생하는 케이스면, 큐에 넣고, 진행
            if visited[xx1][yy1][xx2][yy2] == -1:
                visited[xx1][yy1][xx2][yy2] = visited[x1][y1][x2][y2] + 1
                q.append([xx1, yy1, xx2, yy2])
        # 정답이 없고, 큐가 다 소진된 경우
    return -1


N, M = map(int, input().split())
q = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

a, b, c, d = -1, -1, -1, -1

graph = [list(input()) for _ in range(N)]

# 초기값 결정
for i in range(N):
    for j in range(M):
        if graph[i][j] == "o":
            if a == -1:
                a, b = j, i
            else:
                c, d = j, i
# 호출
print(bfs(a, b, c, d))

