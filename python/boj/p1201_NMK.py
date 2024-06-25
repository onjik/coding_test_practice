# NMK
# 부분집합의 가장 큰 수가 증가하고
# 부분집합의 가장 긴 길이가 감소하도록
# [3,2,1] [5,4]
# 이런식으로

n, m, k = map(int, input().split())
# 우선 N 개의 수 이니까

# 최소 조건은 k + (m - 1)
if n < k + m - 1:
    print(-1)
    exit()
# 만약 k * m개 보다 많은 경우 못만든다
if n > k * m:
    print(-1)
    exit()

if m == 1:
    print(*range(n, 0, -1))
    exit()
if k == 1:
    print(*range(1, n + 1))
    exit()

candi = list(range(k + 1, n + 1))
answer = list(range(1, k + 1))
answer.sort(reverse=True)
# 그 다음 남은거를 몇개씩 배치시킬지
d, r = (n - k) // (m - 1), (n - k) % (m - 1)

cur = 0

while cur <= n:
    nxt = cur + d
    if r:
        nxt += min(r, k - d)
        r -= min(r, k - d)
    answer += sorted(candi[cur:nxt],reverse=True)
    cur = nxt
print(' '.join(map(str, answer)))

"""
# 놓친 부분
- 부분 수열은 내림차순 부분 수열의 수열은 오름차순으로 하는 방법
- 나머지 부분을 단순하게 맨 끝에 붙이게 되면, d + r > k 가 될 수 있어서 최소 수열이 더 길어지게 됨
"""