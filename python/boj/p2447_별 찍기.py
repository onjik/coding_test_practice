# 별찍기
# N은 3의 거듭제곱
# 그니까, 가운데 N / 3 은 무조건 비운다.
# 그리고 그 나머지는 재귀적으로 채운다.

# 즉 f(n) = f(n / 3) * 8 + 빈 칸
# f(3) = 둘러싼 모양

# 최대 3 ^ 8

# 프린트 할 때는 배열을 던져주고 채우게 하자
# 계속 반복 되므로, 캐싱을 하자

cache = dict() # key : n , value : (x,y)

# input
N = int(input())

# 맵 만들기
board = [[False] * N for _ in range(N)]

# 초기값 캐싱 하기
for x in range(3):
    for y in range(3):
        if x == 1 and y == 1:
            continue
        board[y][x] = True
cache[3] = (0,0,)

# 그다음 함수 정의 한다
def fill(x,y,n):
    if n in cache: # 캐시가 있으면 그 부분을 복사한다.
        cx, cy = cache[n]
        for dx in range(n):
            for dy in range(n):
                board[y + dy][x + dx] = board[cy + dy][cx + dx]
    else: # 캐시가 없으면 재귀호출 한다.
        step = n // 3
        for x_idx in range(3):
            for y_idx in range(3):
                if x_idx == 1 and y_idx == 1:
                    continue
                fill(x + x_idx * step, y + y_idx * step, step)

# 그 다음 함수를 호출한다.
fill(0,0,N)

# 그다음 결과를 출력한다.
interprete = lambda x: '*' if x else ' '

for row in board:
    print(''.join(list(map(interprete, row))))