# 문제를 잘 읽자

# 장르별로 가장 많이 재생된 노래 두개씩
# 많이 재생된 장르 먼저
# 많이 재생된 노래 먼저
# 동점일 경우, 고유 번호가 낮은 순서로

# 간단하게 가자
# 딕셔너리에 힙큐를 넣고
import heapq


def solution(genres, plays):
    n = len(plays)

    l = dict()
    for i in range(n):
        genre = genres[i]
        play = plays[i]
        if genre not in l:
            l[genre] = []
        heapq.heappush(l[genre], (play * -1, i))
    # 그 다음, value들을 뽑아서 정렬
    v = list(l.values())
    v.sort(key=lambda x: sum(map(lambda y: y[0] * -1, x)), reverse=True)
    print(v)
    # 그 다음, 장르별로 두개씩 뽑기
    answer = []
    for q in v:
        for _ in range(2):
            if len(q) == 0:
                break
            e = heapq.heappop(q)
            answer.append(e[1])
    return answer
