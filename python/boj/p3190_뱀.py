# 그냥 단순하게 가면 되는데
# Visited를 숫자로 체크하자

n = int(input())
k = int(input())
apples = [[False] * n for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    apples[y-1][x-1] = True
l = int(input())
turn = [0] * (n * n)
for _ in range(l):
    tmp = input().split()
    turn[int(tmp[0])] = 1 if tmp[1] == 'D' else -1

# visited
visited = [[-2] * n for _ in range(n)]

x, y = 0, 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
time_limit = -1
direction = 0 # 오 아 왼 위
for time in range(n * n):
    # 맵 체크
    if not (0<=x < n) or not (0<=y<n):
        print(time)
        exit()
    # 방문 체크하기
    if visited[y][x] >= time_limit:
        print(time)
        exit()
    visited[y][x] = time

    # 돌아야하는지 체크
    if turn[time] != 0:
        direction += 4
        direction += turn[time]
        direction %= 4

    # 사과를 체크한다
    if not apples[y][x]:
        time_limit += 1
    else:
        apples[y][x] = False

    # 그 다음 진행한다
    x, y = x + dx[direction], y + dy[direction]

print(n * n)

# 문제 잘 읽자