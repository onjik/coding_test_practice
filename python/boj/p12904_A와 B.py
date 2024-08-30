# 핵심은 맨 뒤에 계속 추가한다는 점
# 즉 중간 문자열의 맨 뒤를 계속 수정해야한다.
# 그리고 추가하는 연산 밖에 없으므로, 횟수가 정해져 잇다.

# 즉 그때 그때 최적의 방법이 있다.

# 추가하는 과정에서 T와 S가 달라지면 안되므로,
# T의 뒷부분을 하나씩 지워가면서 길이가 같아지면 비교하면 된다.
# 그냥 이런 류의 문제를 많이 풀어봐야 하는 문제

S = list(input())
T = list(input())

# T를 오히려 지워가면서
count_diff = len(T) - len(S)
for _ in range(count_diff):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]
if T == S:
    print(1)
else:
    print(0)
