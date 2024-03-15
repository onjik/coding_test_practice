# 완전탐색이 가능한지 일단 고민을 해본다
# 완전탐색 하더라도 n^2이다.
# n이 최대 20이므로, n^2 은 400 밖에 안된다.

# 시계방향
# 0 : 0 도, 1 : 90도
def rotate(target, d):
    n = len(target)
    tmp = [[0] * n for _ in range(n)]

    if d == 1:
        for x in range(n):
            for y in range(n):
                tmp[y][x] = target[n - 1 - x][y]
    elif d == 2:
        for x in range(n):
            for y in range(n):
                tmp[y][x] = target[n - 1 - y][n - 1 - x]
    elif d == 3:
        for x in range(n):
            for y in range(n):
                tmp[y][x] = target[x][n - 1 - y]
    else:
        for x in range(n):
            for y in range(n):
                tmp[y][x] = target[y][x]
    return tmp


def check(target):
    n = len(target) // 3
    for r in range(n, n * 2):
        for c in range(n, n * 2):
            if target[r][c] != 1:
                return False
    return True




def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 가로 세로 3배 늘어난 배열을 정의한다
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for x in range(n):
        for y in range(n):
            new_lock[n + y][n + x] = lock[y][x]
    # 그 다음 1부터, n-1까지 쭉 돌면서 체크한다
    for x in range(1, n * 2):
        for y in range(1, n * 2):
            # 쭉 돌리면서 대응한다
            for degree in range(4):
                new_key = rotate(key, degree)
                # 다 더한다음에
                for nx in range(m):
                    for ny in range(m):
                        new_lock[y + ny][x + nx] += new_key[ny][nx]
                # 체크한다.
                if check(new_lock):
                    return True
                # 답이 아니니까 다 빼준다
                for nx in range(m):
                    for ny in range(m):
                        new_lock[y + ny][x + nx] -= new_key[ny][nx]
    return False