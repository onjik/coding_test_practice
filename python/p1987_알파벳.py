# visited 로 지나온 칸을 체크하고, alpha[26]으로 지금까지 밟아온 알파벳을
# 체크하며, BFS하자

def ao(x, y):
    return ord(board[y][x]) - ord('A')


def movable(x, y):
    if not (-1 < x < C) or not (-1 < y < R):
        return False  # 맵 이탈
    if visited[y][x]:
        return False  # 방문했던 곳
    if alpha[ao(x, y)]:
        return False
    return True


def check(x, y, v):
    visited[y][x] = v
    alpha[ao(x, y)] = v


def dfs(x, y, depth):
    global ans
    ans = max(ans, depth)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not movable(nx,ny):
            continue
        check(nx, ny, True)
        dfs(nx, ny, depth + 1)
        check(nx, ny, False)


# input
R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
alpha = [False] * 26
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
ans = 0

check(0, 0, True)
dfs(0, 0, 1)


print(ans)