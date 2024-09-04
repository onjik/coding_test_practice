# 십자가 찾기

# 십자가만을 이용해서, 격자판 모양을 만들 수 있는지 찾아보자

# 만들 수 없으면 -1
# 필요한 십자가 수
# 십자가 x, y, s(크기)

# 여러 경우중 아무거나

# 어차피, 별이 아닌 곳은 점으로 채워져 있으므로, 별만 채우면 된다
# 벽에 딱 붙어서 여러 줄이 있는 경우는 불가능
# 위에서 부터 쭉 훑으면서, 별을 찾으면,
# 좌 우로 쭉 가면서 십자가를 찾는다.
# 방문지에 해당 위치를 포함시킨다.
# 방문하지 않은 십자가를 찾는다.

# 중심지를 기준으로 십자가를 찾자
# 그렇다면, 벽쪽은 스캔 안해도 된다.
# 그 중심을 기준으로 방문안한 별이 동서남북 하나라도 있는지 체크하고
# 있다면, 좌우 최대 길이를 체크
# 그거로 별을 그리고 방문 표시

# 그렇다면, 각 열, 행 별로 미리 별의 갯수를 체크해두자

# input
N, M = map(int, input().split())  # 세로길이, 가로길이
board = [list(input()) for _ in range(N)]
vector = ((0, 1), (1, 0), (0, -1), (-1, 0))
visited = [[False] * M for _ in range(N)]
# 별이 아닌 곳은 방문했다고 친다
for y in range(N):
    for x in range(M):
        if board[y][x] == '.':
            visited[y][x] = True


def scan():
    stars = []
    def cross_size(x, y) -> int:
        """이 위치를 중심으로 한 십자가 사이즈, 십자가 불가능하면, -1"""
        if board[y][x] != '*':
            return -1
        size = -1
        max_distance = min(x, M - x, y, N - y)
        for distance in range(1, max_distance + 1):
            available = True
            for dx, dy in vector:
                nx, ny = x + dx * distance, y + dy * distance
                if not (0 <= nx < M) or not (0 <= ny < N) or board[ny][nx] != '*':
                    available = False
                    break
            if not available:
                break
            size = distance

        if size != -1:
            visited[y][x] = True
            for dx, dy in vector:
                for distance in range(1, size + 1):
                    nx, ny = x + dx * distance, y + dy * distance
                    visited[ny][nx] = True
        return size

    for x in range(1, M - 1):
        for y in range(1, N - 1):
            # 이제 이 위치에서 십자가가 있는지 체크한다.
            size = cross_size(x, y)
            if size == -1:
                continue
            stars.append((y + 1, x + 1, size))
    return stars


stars = scan()
if not all(all(row) for row in visited):
    print(-1)
else:
    print(len(stars))
    for star in stars:
        print(*star)