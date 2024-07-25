# 사분면

# 그냥 좌표로 전환하고, 좌표를 코드로 전환하자

def code_to_coor(code):
    # 일의 자리 부터 순서대로 더해 간다
    dx = [0, 1, 0, 0, 1]
    dy = [0, 0, 0, 1, 1]

    x,y = 0,0

    radix = 1
    while code > 0:
        r = code % 10
        code = code // 10
        x, y = x + dx[r] * radix, y + dy[r] * radix
        radix *= 2

    return x, y

def coor_to_code(x,y, d) -> str:
    limit = 2 ** d
    if not (0 <= x < limit) or not (0 <= y < limit):
        return "-1"
    if d == 0:
        return ""
    mid = 2 ** (d - 1)
    prefix = None
    if x >= mid and y >= mid:
        prefix = "4"
    elif x < mid and y >= mid:
        prefix = "3"
    elif x < mid and y < mid:
        prefix = "2"
    else:
        prefix = "1"

    if x >= mid:
        x -= mid
    if y >= mid:
        y -= mid
    return prefix + coor_to_code(x,y,d -1)

# input
d, code = map(int,input().split())
dx, dy = map(int, input().split())

x, y  = code_to_coor(code)
print(coor_to_code(x + dx, y - dy, d))


