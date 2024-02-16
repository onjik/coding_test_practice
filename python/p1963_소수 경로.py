# 한자리만 바꿀 수 있다
# 각 단계는 소수여야 한다
# 몇단계를 거쳐야 바꿀 수 있는지 확인하는 함수 만들어라
# 1000 미만 수는 허용 되지 않는다
import math
from collections import deque


def is_prime_number(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def variant(num, digit):
    og_num = (num // digit) % 10
    tmp = num - og_num * digit
    variants = []
    for i in range(10):
        new = tmp + i * digit
        variants.append(new)
    return variants


def cases(num):
    cases = []
    for digit in [1, 10, 100, 1000]:
        cases += variant(num, digit)
    return cases


def bfs(start, end):
    q = deque()
    visited = set()
    q.append(start)
    visited.add(start)
    ans = 0
    while q:
        for _ in range(len(q)):
            n = q.popleft()
            if n == end:
                return ans
            for case in cases(n):
                # 이미 방문 했는지
                if case in visited:
                    continue
                # 맨 앞자리가 0인지
                if case < 1000:
                    continue
                # 소수 인지
                if not is_prime_number(case):
                    continue
                # 여기까지 왔으면 추가
                visited.add(case)
                q.append(case)
        ans += 1
    # 여기까지 왔으면
    return -1
# input
n = int(input())
for i in range(n):
    start, end = map(int, input().split())
    ans = bfs(start, end)
    if ans == -1:
        print("Impossible")
    else:
        print(ans)