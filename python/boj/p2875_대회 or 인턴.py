# 대회 or 인턴
# 2명의 여학생 + 1명의 남학생
# k명은 무조건 제외 해야한다

# 가장 많은 팀을 만들어라

# 일단 최대한 팀을 만들고
# 남은 인원으로 최대한 뺀다음
# 기준치 3 씩 팀을 해체하자

n, m, k = map(int, input().split())

# 일단 최대한 팀을 만든다
team_count = min(n // 2, m)
n -= team_count * 2
m -= team_count


# 남은 인원으로 최대한 뺀다
k -= n
k -= m
if k > 0:
    # 만약 남아있으면 팀을 해체하자
    team_count -= (k + 2) // 3
    # team_count -= k // 3 + 1
    # 여기서 에러가 났었다. k가 3일 때 2팀을 지워야 했다.

print(team_count)