# O((N-2)!)
# O(8!) = 40320
# 완전 탐색으로 가자


ans = 0


def dfs(marvels, value):
    global ans
    if len(marvels) == 2:
        # 종료
        ans = max(value, ans)
        return

    # 각 위치를 빼내면서 재귀 호출
    for i in range(1, len(marvels) - 1):
        new_value = value + marvels[i - 1] * marvels[i + 1]
        new_marvels = marvels.copy()
        new_marvels.pop(i)
        dfs(new_marvels, new_value)


# input
N = int(input())
init_marvels = list(map(int, input().split()))

# call
dfs(init_marvels, 0)

# print
print(ans)


