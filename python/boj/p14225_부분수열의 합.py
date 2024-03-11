# boolean배열로 체크하고, 추후에 가장 작은거를 응답하자
# 그냥 단순 다 대입하는 경우 O(N!) 이고, 20이 되면, 불가능 하다
# 1부터 가능한 것을 찾는 것은 어떨까?
# 원소가 있는지 검사하고, 자기보다 작은 것들만 조합을 찾아보는 식으로


from itertools import combinations

# input
N = int(input())
L = list(map(int, input().split()))
pre_cal = set()

# 작은 자연수부터 가능한 것 탐색
i = 0

while True:
    i += 1
    if i in L:
        continue
    if i in pre_cal:
        continue

    q = list(filter(lambda x: x < i, L))
    exist = False
    for k in range(2, len(q) +1):
        comb_sum = list(map(sum, combinations(q, k)))
        pre_cal.update(comb_sum)
        if i in comb_sum:
            exist = True
            break
    if not exist:
        break

print(i)