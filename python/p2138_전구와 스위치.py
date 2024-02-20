# 맨 처음거만 결정이고, 나머지는 이전 것 기준으로 결정
# 순서는 상관 없다


# input
N = int(input())
start = list(map(bool, map(int, list(input()))))

fliped = start.copy()
fliped[0] = not fliped[0]
fliped[1] = not fliped[1]

target = list(map(bool, map(int, list(input()))))

def flip(l,idx):
    for i in range(idx, idx +3):
        if not (-1 < i < N):
            continue
        l[i] = not l[i]

def flip_count(l):
    count = 0
    for i in range(0, N-1):
        if l[i] == target[i]:
            continue
        count += 1
        flip(l, i)
    if l != target:
        return -1
    else:
        return count


ans = -1
if start == target:
    ans = 0
else:
    ans = flip_count(start)
    if ans == -1:
        ans = flip_count(fliped)
        if ans != -1:
            ans += 1

print(ans)