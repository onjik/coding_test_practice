# N/2마리 가져가기 가능
# 숫자 중복 가능
# 최대 종류값
# 최대 종류 갯수

# 그냥 set하면 될듯

def solution(nums):
    n = len(nums)
    unique_nums = set(nums)
    return min(n // 2, len(unique_nums))