# 아 다 좋은데, 이분탐색의 최대 최소를 최대한 최적화 해야 하는구나
# 또, 나올 수 있는 숫자가 정해져 있으므로(이산적이므로) 범위를 특정해 줄 수 있다
# 그니까, diff = 3 이게 아니라, (1, 4) 이런식으로
# 그리고, 범위를 지정해 줄때, 시작점과 끝점이 가능한지 체크해야 한다.

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 최대 최소값을 구한다.
numbers = set()
for row in board:
    numbers.update(row)
MIN, MAX = min(numbers), max(numbers)
START_VALUE, END_VALUE = board[0][0], board[N - 1][N - 1]

from collections import deque


def bfs(range_start: int, range_end: int) -> bool:
    '''이 범위로 오른쪽 아래를 도달할 수 있는지 체크'''
    q = deque()
    visited = [[False] * N for _ in range(N)]
    q.append((0, 0,))  # x, y
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            # 맵 범위 체크
            if not (0 <= nx < N) or not (0 <= ny < N):
                continue
            # 정답 체크
            if ny == N - 1 and nx == N - 1:
                return True
            # 방문 체크
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            # 범위 체크
            value = board[ny][nx]
            if not (range_start <= value <= range_end):
                continue
            # 후보지에 넣기
            q.append((nx, ny,))
    # 여기까지 왓으면 못가는 거
    return False


def possible(diff: int) -> bool:
    '''이 차이에서 가능한지 체크한다.'''
    for range_start in numbers:
        range_end = range_start + diff
        if not (range_start <= START_VALUE <= range_end) or not (range_start <= END_VALUE <= range_end):
            continue
        if bfs(range_start, range_end):
            return True
    return False


# 이분탐색을 한다.
lb, ub = 0, MAX - MIN  # lower_bound, upper_bound
answer = -1
while lb <= ub:
    mid = (lb + ub) // 2  # 차이
    if possible(mid):
        # 가능하다면, 더 좁은 범위 탐색
        ub = mid - 1
        answer = mid
    else:
        # 불가능하다면, 더 넓은 범위 탐색
        lb = mid + 1
print(answer)