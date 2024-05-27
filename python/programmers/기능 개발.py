# 100%일 때 반영 가능
# 선후 관계 있음 : 뒤에꺼 먼저 개발되면, 앞에꺼 완료될 때 같이 배포됨

# 각 배포마다 몇개의 기능이 배포되는지 Return

# 100 개 이하

# 하루가 끝났을때 100 이상인 것이 끝난 걸로 판단

# 앞에서 부터 구하면서 max 함수 활용하자

def solution(progresses, speeds):
    n = len(speeds)
    finish = [-1] * n
    answer = []
    max_day = 0

    # 이제 앞에서 부터 구하기 시작
    for i in range(n):
        left = 100 - progresses[i]
        speed = speeds[i]
        day = left // speed
        if left % speed > 0:
            day += 1
        if i == 0 or day > finish[i - 1]:
            finish[i] = day
            answer.append(1)
        else:
            finish[i] = finish[i - 1]
            answer[-1] += 1

    return answer