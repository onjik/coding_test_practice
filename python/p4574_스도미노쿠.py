dx = (0, 1)
dy = (1, 0)


def pos(chess_pos):
    x = int(chess_pos[1]) - 1
    y = ord(chess_pos[0]) - ord("A")
    return (x, y)


def box(x, y):
    return (x // 3) + (y // 3) * 3


def can(x, y, v):
    return not xi[x][v] and not yi[y][v] and not bi[box(x, y)][v]


def is_out(x, y):
    return not (0 <= x < 9) or not (0 <= y < 9)


def check(x, y, v, b):
    xi[x][v] = b
    yi[y][v] = b
    bi[box(x, y)][v] = b


def run(n):
    if n == 81:
        for tmp in board:
            print("".join(map(str,tmp)))
        return True
    x = n % 9
    y = n // 9
    if board[y][x] != 0:
        return run(n + 1)
    else:
        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_out(nx, ny):
                continue
            if board[ny][nx] != 0:
                continue
            for i in range(1, 10):
                if not can(x,y,i):
                    continue
                for j in range(1, 10):
                    if i == j:
                        continue
                    if combi[i][j]:
                        continue
                    if not can(nx,ny,j):
                        continue
                    board[y][x] = i
                    board[ny][nx] = j
                    check(x, y, i, True)
                    check(nx, ny, j, True)
                    combi[i][j] = combi[j][i] = True
                    if run(n + 1):
                        return True
                    board[y][x] = 0
                    board[ny][nx] = 0
                    check(x, y, i, False)
                    check(nx, ny, j, False)
                    combi[i][j] = combi[j][i] = False
    return False


count = 1
while True:
    N = int(input())
    if N == 0:
        break
    print(f"Puzzle {count}")
    count += 1
    # 초기값 정의
    board = [[0] * 9 for _ in range(9)]
    xi = [[False] * 10 for _ in range(10)]
    yi = [[False] * 10 for _ in range(10)]
    bi = [[False] * 10 for _ in range(10)]
    combi = [[False] * 10 for _ in range(10)]
    # input
    for _ in range(N):
        U, LU, V, LV = input().split()
        v1 = int(U)
        x1, y1 = pos(LU)
        v2 = int(V)
        x2, y2 = pos(LV)
        board[y1][x1] = v1
        board[y2][x2] = v2
        combi[v1][v2] = combi[v2][v1] = True
        check(x1, y1, v1, True)
        check(x2, y2, v2, True)

    pl = input().split()
    for i in range(1, 10):
        x, y = pos(pl[i - 1])
        board[y][x] = i
        check(x, y, i, True)

    # 실행
    run(0)