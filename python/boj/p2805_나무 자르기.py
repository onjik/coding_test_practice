# 이분 탐색

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

start, end = 1, trees[0],

while start <= end:
    mid = (start + end) // 2


    log = 0
    for tree in trees:
        diff = tree - mid
        if diff <= 0:
            break
        log += diff

    if log >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# 틀렸던 이유, 이분탐색 구현
# 이분 탐색 구현할 떄 단순하게 생각하자, while문은 같을 떄도 돌아가게 하자
# 그니까 엇갈렸을 때만 탈출하도록
# 그리고 같을 때 움직이지 않는 쪽 (여기서는 end)이 정답이다
# 또 하나 놓친 부분은 mid값을 그대로 넣는 것이 아니라, +-1을 해줘야 한다는 것이다.
# 그렇지 않으면 무한 루프가 돌 수 있다.