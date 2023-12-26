# + - * /
import sys


def num_count_input():
    return int(input())


def num_array_input():
    return list(map(int, input().split()))


def oper_array_input():
    return list(map(int, input().split()))


def tracking(idx, prev_sum):
    # global var
    global num_count
    global num_array
    global oper_array

    global minimum
    global maximum

    # 종료조건
    if num_count == idx:
        # tracking finish
        if maximum < prev_sum:
            maximum = prev_sum
        if minimum > prev_sum:
            minimum = prev_sum
        return

    # 하나씩 대입하며, 재귀호출
    for i in range(4):
        if oper_array[i] == 0:
            continue
        new_sum = prev_sum

        if i == 0:
            new_sum += num_array[idx]
        elif i == 1:
            new_sum -= num_array[idx]
        elif i == 2:
            new_sum *= num_array[idx]
        elif i == 3 and prev_sum * num_array[idx] < 0:
            new_sum = abs(new_sum) // abs(num_array[idx]) * -1
        elif i == 3:
            new_sum = new_sum // num_array[idx]

        # recursive call
        oper_array[i] -= 1
        tracking(idx + 1, new_sum)
        oper_array[i] += 1


# variable
global num_count
global num_array
global oper_array

global minimum
global maximum

# input
num_count = num_count_input()
num_array = num_array_input()
oper_array = oper_array_input()

# init

minimum = sys.maxsize
maximum = -1 * minimum

# tracking
tracking(1, num_array[0])

# print result
print(maximum)
print(minimum)