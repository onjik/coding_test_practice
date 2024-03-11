# N 개의 회의
# 1 개의 회의실
# 안겹치게 최대 몇개?

# 끝나는 시간 -> 시작 시간 순으로 정렬

N = int(input())
meets = [list(map(int, input().split())) for _ in range(N)]

meets.sort(lambda x: (x[1], x[0]))

count = 0
end = -1
for meet in meets:
    if end <= meet[0]:
        end = meet[1]
        count += 1
print(count)