# + - * /

def num_count_input():
    return int(input())


def num_arr_input():
    return list(map(int, input().split()))


def oper_count_input():
    return list(map(int, input().split()))


# num_idx는 1부터 시작
def tracking(prev_sum, num_idx):
    global max_value
    global min_value
    global num_arr
    global oper_count
    global num_count

    # 종료조건
    if num_count == num_idx:
        # 전체 트래킹이 모두 끝남
        if max_value < prev_sum:
            max_value = prev_sum
        if min_value > prev_sum:
            min_value = prev_sum
        return

    for i in range(4):
        if oper_count[i] == 0:
            continue

        # calculate new sum
        new_sum = prev_sum
        if i == 0:
            new_sum = prev_sum + num_arr[num_idx]
        elif i == 1:
            new_sum = prev_sum - num_arr[num_idx]
        elif i == 2:
            new_sum = prev_sum * num_arr[num_idx]
        elif i == 3 and prev_sum < 0:
            new_sum = (-prev_sum // num_arr[num_idx]) * -1
        elif i == 3 and prev_sum > -1:
            new_sum = prev_sum // num_arr[num_idx]

        # recursive call
        oper_count[i] -= 1
        tracking(new_sum, num_idx + 1)
        oper_count[i] += 1


global max_value
global min_value
global num_arr
global oper_count
global num_count

# input
num_count = num_count_input()
num_arr = num_arr_input()
oper_count = oper_count_input()

# init
min_value = 99999999999
max_value = -1 * min_value

# call
tracking(num_arr[0], 1)

# print
print(max_value)
print(min_value)
