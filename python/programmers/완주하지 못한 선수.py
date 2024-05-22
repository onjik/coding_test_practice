# 한명 빼고는 모두 완주
# 완주 못한 선수 찾아라
# 동명이인이 있을 수있다.

def solution(participants, completions):
    p = dict()
    for participant in participants:
        if participant not in p:
            p[participant] = 0
        p[participant] += 1
    c = dict()
    for completion in completions:
        if completion not in c:
            c[completion] = 0
        c[completion] += 1
    # 그 다음 이제 제거해 나간다.
    for key, value in c.items():
        p[key] -= value
        if p[key] == 0:
            del p[key]
        else:
            # 만약 제거 했는데 남아있으면 무조건 그 사람임
            return key
    # 한개가 남아있으면
    return list(p.keys())[0]