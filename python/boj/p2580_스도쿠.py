# 미리 가로줄, 세로줄, 대각선 인덱스를 만들어 놓고,
# 빠르게 검색하도록 하면 어떨까?

done = False


def box_indexer(x_pos, y_pos):
    return (x_pos // 3) + (y_pos // 3) * 3


def play_sudoku(zero_idx):
    global done

    if zero_idx == len(zero_pos):
        # 트래킹이 완료되었다.
        done = True
        return

    global x_i
    global y_i
    global bl_i
    global br_i

    # 채울 녀석
    pos = zero_pos[zero_idx]
    xx = pos[0]
    yy = pos[1]
    box_pos = box_indexer(xx, yy)

    candidates = x_i[xx] & y_i[yy] & box_i[box_pos]

    # 백트래킹
    for candidate in candidates:
        # board에 넣고 인덱스에도 넣는다.
        board[yy][xx] = candidate
        x_i[xx].discard(candidate)
        y_i[yy].discard(candidate)
        box_i[box_pos].discard(candidate)
        play_sudoku(zero_idx + 1)
        if done:
            return
        x_i[xx].add(candidate)
        y_i[yy].add(candidate)
        box_i[box_pos].add(candidate)


# input
board = [list(map(int, input().split())) for _ in range(9)]

# make index
x_i = [set(range(1, 10)) for _ in range(9)]  # 가능한 숫자
y_i = [set(range(1, 10)) for _ in range(9)]
box_i = [set(range(1, 10)) for _ in range(9)]

zero_pos = []

for x in range(9):
    for y in range(9):
        value = board[y][x]
        if value == 0:
            zero_pos.append((x, y))
            continue

        # add index
        x_i[x].discard(value)
        y_i[y].discard(value)
        box_i[box_indexer(x, y)].discard(value)

play_sudoku(0)

# print
for row in board:
    print(" ".join(map(str, row)))
