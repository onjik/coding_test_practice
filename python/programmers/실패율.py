def solution(N, stages):
    length = len(stages)
    answer = []
    for i in range(1, N + 1):
        cnt = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = cnt / length
        answer.append((i, fail))
        length -= cnt

    # 정렬
    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [i[0] for i in answer]
    return answer