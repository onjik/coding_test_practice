# 그리디 방법이었다.
# 이런 류의 문제를 풀때, 서로가 서로의 배수가 되는지 잘 고민해보자
# 서로가 배수가 된다면, 동전 문제와 비슷하고
# 배수가 되지 않는다면, dP 로 해결해야 한다.

for _ in range(int(input())):
    n = int(input())
    sixties, tens, ones = n // 60, (n % 60) // 10, (n % 10)
    # 이렇게 하고 이제 개선을 시킨다.
    # tens의 범위 0 ~ 5
    # ones가 6,7,8,9,일 경우, 10 더하고 빼는게 이득
    if ones > 5:
        ones -= 10
        tens += 1
    # tens 가 4,5인 경우, 6을 한번 더하고 2번 빼는 게 이득
    if tens > 3:
        tens -= 6
        sixties += 1
    # tens 빼는게 더 적을수록 우선순위가 높다
    if ones == 5 and tens < 0:
        tens += 1
        ones -= 10

    answer = [0] * 5
    answer[0] = sixties
    if tens >= 0:
        answer[1] = tens
    else:
        answer[2] = abs(tens)
    if ones >= 0:
        answer[3] = ones
    else:
        answer[4] = abs(ones)
    print(*answer)

