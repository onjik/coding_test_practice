# 30

# 숫자 섞어서 30의 배수가 되는 가장 큰 수를 만들자
# 0으로 시작하지 않는다

# 일단 끝은 무조건 0이 들어와야 하고 -> 조기 종료

# 그리고 앞쪽은 3의 배수여야 하는데
# 3 6 9 12 15 18 21 24 27 30
# 더해서 3 6 9
# 66 69 72
# 12 15 9

# 더해서 3의 배수가 되면 되고,
# 앞쪽에 큰 수가 올 수록 크다

# 모든 수를 다 사용해야한다.
# 즉 3의 배수가 아니면, 끝이다.

n = list(map(int,list(input())))
if 0 not in n:
    print(-1)
    exit()
n.remove(0)

# 오름차순 정렬
n.sort(reverse=True)
