# 문제 : K개 글자를 가지고 읽을 수 있는 최대 단어
# 시작은 anta, 끝은 tica, 전체 단어 antic
# 비트 마스킹
from itertools import combinations

def ctob(c):
    return 1 << (ord(c) - ord('a'))

def atob(s):
    tmp = 0
    for c in s:
        tmp |= ctob(c)
    return tmp

# input
N, K = map(int, input().split())
words = [atob(input()) for _ in range(N)]
ans = 0

if K < 5:
    print(0)
    exit()

# 조합 생성

base = 0
candi = [1 << i for i in range(26)]
for c in ['a','n','t','i','c']:
    candi.remove(atob(c))
    base |= atob(c)

for combi in combinations(candi, K - 5):
    bi, cnt = base, 0
    for i in combi:
        bi |= i
    # 이게 가능한지
    for word in words:
        if word & bi == word:
            cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)