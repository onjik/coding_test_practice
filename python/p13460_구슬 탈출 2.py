# 세로, 가로 N M
# 빨간 구슬은 빼고, 파란 구슬은 빼면 안된다
# 최소 몇번만에 뺄 수 있는지 찾아내라
# visited를 체크한다(파랑, 빨강 블럭 위치)
# 일단 움직인 다음, 둘이 겹칠 경우, 이전의 값을 비교해서 한 칸 뒤로 민다
# 체크해야할 것은 0이면 그 자리에 멈추고, #이면 진행 안하고 멈추도록
# 모든 움직임이 끝나면, R이 빠지고 파랑이 안빠졌는지 검사
# 맞다면, count를 업데이트 한다.
# 동시에 빠져도 실패다
import sys

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
visited = set()
ans = sys.maxsize


# return []
def move_cases(marvels):
    cases = set()

    for i in range(4):
        dxx, dyy = dx[i], dy[i]
        rx, ry, bx, by = marvels

        blue_out = False
        red_out = False

        # red 부터
        while True:
            # 구멍을 만나면 멈추기
            if board[ry][rx] == 'O':
                red_out = True
                break
            rx += dxx
            ry += dyy
            # 벽을 만나면 뒤로 돌리고 멈추기
            if board[ry][rx] == '#':
                rx -= dxx
                ry -= dyy
                break

        # blue
        while True:
            # 구멍을 만나면 멈추기
            if board[by][bx] == 'O':
                blue_out = True
                break
            bx += dxx
            by += dyy
            # 벽을 만나면 뒤로 돌리고 멈추기
            if board[by][bx] == '#':
                bx -= dxx
                by -= dyy
                break

        # 다 옮겼으면 겹쳤는지 확인한다.
        if (bx == rx and by == ry) and not (red_out or blue_out): # 겹친 경우이면서, 나갔으면 계산  ㄴㄴ
            # 겹쳤다
            if dxx != 0:
                if (marvels[0] > marvels[2]) == (dxx == -1):  # red가 크면서 ddx 가 1
                    rx -= dxx
                else:
                    bx -= dxx
            else:
                if (marvels[1] > marvels[3]) == (dyy == -1):
                    ry -= dyy
                else:
                    by -= dyy

        # case에 추가한다
        cases.add((rx, ry, bx, by))
    return cases

def is_red_out(marvels):
    x, y = marvels[0], marvels[1]
    return board[y][x] == 'O'


def is_blue_out(marvels):
    # blue
    x, y = marvels[2], marvels[3]
    return board[y][x] == 'O'


# step 은 0부터 시작
def dfs(step, marvels):
    global ans
    if is_blue_out(marvels):
        return
    if is_red_out(marvels):
        ans = min(ans, step)
        return
    # 11번째 움직이려고 할 경우 금지
    if step == 10:
        return
    # 성공도, 실패도, step out도 아닌 경우
    for case in move_cases(marvels):
        # visited check
        if case in visited:
            continue
        visited.add(case)
        dfs(step + 1, case)
        visited.remove(case)


def marvel_input():
    mi = [-1] * 4
    red = blue = False
    for y in range(N):
        if red and blue:
            break
        for x in range(M):
            if not red and board[y][x] == 'R':
                mi[0], mi[1] = x, y
                red = True
            if not blue and board[y][x] == 'B':
                mi[2], mi[3] = x, y
                blue = True
            if red and blue:
                break
    return tuple(mi)


# input
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

mi = marvel_input()
visited.add(mi)

dfs(0, mi)

if ans == sys.maxsize:
    ans = -1
print(ans)