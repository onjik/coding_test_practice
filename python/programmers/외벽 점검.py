# 사람 수가 8명 밖에 안된다
# 진짜 단순하게 반복으로 풀어도
# 사람 순열 8! * 15 정도?
# 그냥 단순하게 반복하자
# 보내야하는 최솟값
from itertools import permutations
def solution(n, weak, dist):
    # weak을 두배로 늘리자
    weak_cnt = len(weak)
    for i in range(weak_cnt):
        weak.append(weak[i] + n)
    # 그 다음 사람들을 배치할 순서를 쭉 돌리자
    answer = len(dist) + 1
    for friends in permutations(dist,len(dist)):
        # weak 부분에서만 출발한다.
        for start in range(weak_cnt):
            count = 1
            position = friends[count - 1] + weak[start]
            # 이제 쭉 돌면서,
            for delta in range(weak_cnt):
                if weak[start + delta] > position:
                    count += 1
                    if len(friends) < count:
                        # 다 사용했으면,
                        break
                    position = friends[count - 1] + weak[start + delta]
            # 다 돌았으면, 이제 최소 값 갱신한다.
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer