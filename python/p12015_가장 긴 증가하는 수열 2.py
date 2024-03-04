# 증가하는 부분수열

# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#s-3.2

# 이진 탐색을 통해
# NlogN
# 그니까 이 방법은, 해당 길이 보다 길어지려면, 어떤 수 이상이어야 하는지
# 지속적으로 업데이트 하는 방법이다

# input
N = int(input())
nums = list(map(int, input().split()))
d = [0]

# 하나씩 iter
for num in nums:
    if d[-1] < num:
        d.append(num)
    else:
        # 이진 탐색
        left, right = 0, len(d)
        while left < right:
            mid = (left + right) // 2
            if d[mid] < num:
                left = mid + 1
            else:
                right = mid
        # 길이별 기준값 업데이트
        d[right] = num
print(len(d) - 1)