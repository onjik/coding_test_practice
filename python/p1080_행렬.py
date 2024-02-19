# 만약 변환 가능하다면, 바꾸는 순서는 상관없다
# 바꾸는 위치만 상관 있다

def convert(x, y):
    for xx in range(x, x + 3):
        for yy in range(y, y + 3):
            start[yy][xx] = (start[yy][xx] + 1) % 2


def matrix_equal(a, b):
    for x in range(M):
        for y in range(N):
            if a[y][x] != b[y][x]:
                return False
    return True


# input
N, M = map(int, input().split())
start = [list(map(int, list(input()))) for _ in range(N)]
target = [list(map(int, list(input()))) for _ in range(N)]

count = 0
for x in range(M - 2):
    for y in range(N - 2):
        if start[y][x] != target[y][x]:
            convert(x, y)
            count += 1

# check
if matrix_equal(start, target):
    print(count)
else:
    print(-1)