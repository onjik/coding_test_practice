# 없는 구조물을 삭제하는 경우는 주어지지 않는다
# n값이 작으므로, 그냥 단순하게 구현하면 될듯
def valid(answer):
    for x,y,a in answer:
        if a == 0: # 기둥의 경우
            if y == 0 or [x - 1, y, 1] in answer or [x,y,1] in answer or [x,y -1,0] in answer:
                continue
            return False
        elif a == 1: # 보의 경우
            if [x, y -1,0] in answer or [x + 1, y - 1, 0] in answer or ([x -1 , y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0:
            # 일단 삭제를 한다
            answer.remove([x, y, a])
            if not valid(answer):
                # 유효하지 않으면 되돌린다.
                answer.append([x,y,a])
        else:
            # 일단 삽입을 한다
            answer.append([x,y,a])
            if not valid(answer):
                # 유효하지 않으면 되돌린다
                answer.remove([x,y,a])
    answer.sort()
    return answer
