# 1 ~ n까지 n개
# 유효기간 지나면 파기
# 약관마다 유효기간 있음
# 오늘날짜로 파기해야할 개인정보 번호 구하라
# 모든 달은 28일까지 있다

# 풀이 아이디어
# 수집 일자는 그냥 쭉 이어서 숫자 형으로 만든다
# 각 약관 마다 오늘 기준으로 한계 날짜를 정한다
# 그래서 dict에 넣어두자

# 그거 이전에 있는 것들은 파기해야하므로, 리스트에 추가하자

def c_to_date(c):
    return tuple(map(int, c.split('.')))


def date_before(date, delta_month):
    copy = [a for a in date]
    if copy[1] <= delta_month:
        yn = (delta_month - copy[1]) // 12 + 1
        copy[0] -= yn
        copy[1] += 12 * yn
    copy[1] -= delta_month
    return tuple(copy)


def solution(today, terms, privacies):
    n_today = c_to_date(today)
    n_terms = {}
    for term in terms:
        tmp = term.split()
        n_terms[tmp[0]] = date_before(n_today, int(tmp[1]))
    answer = []
    for idx, privacy in enumerate(privacies):
        a, b = privacy.split()
        if c_to_date(a) <= n_terms[b]:
            answer.append(idx + 1)
    return answer