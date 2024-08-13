# 직사각형 체스판
# 각 칸에는 대문자 알파벳 하나
# 좌측 상단 말

# 동서남북
# 같은 알파벳 두번 지날 수 없음

# 최대한 몇칸을 지날 수 있는지

# 지나온 경로를 고려해야 하니까, dfs 백트래킹으로 갈 수 밖에
# 최대 400 번 이동이므로
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

r, c = map(int, input().split())

board = [list(input()) for _ in range(r)]

visited = [False] * 26

max_dist = 1


def dfs(x, y, dist):
    global max_dist
    # 맵 체크
    if not (0 <= x < c) or not (0 <= y < r):
        return
    alpha = board[y][x]
    alpha_idx = ord(alpha) - ord('A')
    # 방문 체크
    if visited[alpha_idx]:
        return
    # 방문 처리
    visited[alpha_idx] = True
    max_dist = max(dist, max_dist)
    # 가지 치기
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        dfs(nx, ny, dist + 1)
    visited[alpha_idx] = False


dfs(0, 0, 1)
print(max_dist)

# 오답 노트
# visited 를 체크할 때, set() 사용을 지양하자
# 특히 알파벳이나 좌표와 같이 나올 수 있는 값의 범위가 정해져 있는 경우
# 배열의 활용해서 O(1)이 되도록 하자
