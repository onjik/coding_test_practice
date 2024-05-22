from collections import deque

# 딕셔너리로 간단하게 트리 만들자
tree = dict()
END = 'E'


# 겹치는게 있으면 false, 없으면 true
def append(s: str) -> bool:
    cur = tree
    for c in list(s):
        if c not in cur:
            cur[c] = dict()
        cur = cur[c]
        if END in cur:
            return False
    cur[END] = END
    return True


def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for phone in phone_book:
        # False, 즉 겹치는게 나오면 즉시 False
        if append(phone) == False:
            return False
    return True