# 3가지 경우
# 열이 홀수 -> 전체 순회
# 행이 홀수 -> 전체 순회
# 양쪽 다 짝수
# 격리 칸 정해서 거기만 반대 축으로 순회

def is_odd(i):
    return i % 2 != 0


r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
answer = ''

if is_odd(c):
    answer = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1)
elif is_odd(r):
    answer = ('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1)
else:
    min_x = -1
    min_y = -1
    min_val = int(1e9)
    for x in range(c):
        for y in range(r):
            if (x + y) % 2 == 0:
                continue
            if board[y][x] < min_val:
                min_x = x
                min_y = y
                min_val = board[y][x]
    # 격리 칸 설정
    iso_x = (min_x // 2) * 2

    # 격리 칸 이전 부분 완성시키기
    answer = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (iso_x // 2)

    # 격리 칸 계산하기
    toggle = True  # True : R, False : L
    for y in range(r):
        # y좌표가 같다면 진행 못하고 아래로
        if y != min_y:
            if toggle:
                answer += 'R'
            else:
                answer += 'L'
            toggle = not toggle
        answer += 'D'
    # 맨 마지막에는 다음칸으로 가야함
    answer = answer[:-1] + 'R'

    # 격리 칸 이후 부분 완성시키기
    answer += ('U' * (r - 1) + 'R' + 'D' * (r - 1) + 'R') * (c // 2 - iso_x // 2 - 1)
    # 맨 마지막에 R은 필요 없음
    answer = answer[:-1]

print(answer)