# 각 시작점당 4^10 씩 탐색한다.
# 시작점은 N * M = 20N

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = -1
N, M = 0, 0

coins = [-1, -1, -1, -1]


def coin_out(x, y):
    if -1 < x < M and -1 < y < N:
        return False
    else:
        return True


def on_wall(x, y):
    if coin_out(x, y):
        return False
    if MAP[y][x] == "#":
        return True
    else:
        return False


# 이동하고, 변하지 않았으면 False
def move_coins(dx, dy):
    global coins
    # 먼저 이동할 코인이 1
    if dx != 0:
        if dx * coins[0] > dx * coins[2]:
            x1, y1, x2, y2 = coins
        else:
            x2, y2, x1, y1 = coins
    elif dy != 0:
        if dy * coins[1] > dy * coins[3]:
            x1, y1, x2, y2 = coins
        else:
            x2, y2, x1, y1 = coins

    coin1_changed, coin2_changed = True, True
    # 1번 코인 이동
    xx1, yy1 = x1 + dx, y1 + dy
    if on_wall(xx1, yy1):
        # revert
        xx1, yy1 = x1, y1
        coin1_changed = False

    # 2번 코인 이동
    xx2, yy2 = x2 + dx, y2 + dy
    if on_wall(xx2, yy2):
        # revert
        xx2, yy2 = x2, y2
        coin2_changed = False

    # 충돌 체크
    if xx1 == xx2 and yy1 == yy2:
        # 충돌 났으면, 2번째 코인을 되돌린다
        xx2, yy2 = x2, y2
        coin2_changed = False

    if coin1_changed or coin2_changed:
        # 바뀐 위치 업데이트
        coins = [xx1, yy1, xx2, yy2]
        return True
    else:
        return False


# depth 는 1부터
def tracking(depth):
    global coins
    global ans
    if depth > 10:
        # over
        return

    tmp = coins.copy()
    for i in range(4):
        coins = tmp.copy()
        moved = move_coins(dx[i], dy[i])
        if not moved:
            continue
        # 성공 체크
        out1 = coin_out(coins[0], coins[1])
        out2 = coin_out(coins[2], coins[3])

        if out1 and out2:  # 둘다 나간경우
            pass
        elif out1 or out2:  # 한개만 나간경우
            # 성공
            if ans == -1:
                ans = depth
            else:
                ans = min(ans, depth)
            continue
        else:  # 둘다 안나간경우
            tracking(depth + 1)


# input
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]

# coin init
for i in range(N):
    if coins[2] != -1:
        break
    for j in range(M):
        if MAP[i][j] == "o":
            if coins[0] == -1:
                coins[0], coins[1] = j, i
            else:
                coins[2], coins[3] = j, i
                break

tracking(1)

print(ans)
