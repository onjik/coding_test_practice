# 재귀 적으로 분할 정복 하면 될듯
# 맨 끝까지 갔으면 1 하고,

def count(n, x, y):
    global ans
    if n == 1:
        if x == c and y == r:
            print(ans)
            exit()
        ans += 1
        return
    # 만약 이 범위 안에 포함 안되었으면, 한번에 추가 하고 타지 않는다
    if not (x <= c < x + n) and not (y <= r < y + n):
        ans += n ** 2
        return
    nn = n // 2
    for ny in range(y, y + n, nn):
        for nx in range(x, x + n, nn):
            count(nn,nx,ny)

# input
N, r, c = map(int, input().split())
ans = 0
count(2 ** N,0,0)