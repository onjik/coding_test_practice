global opers
global numbers
global values
global count
global minimum
global maximum


def tracking(idx):
    global minimum, maximum
    # 종료 조건
    if idx is count + 1:
        if minimum > values:
            minimum = values.copy()
        elif maximum < values:
            maximum = values.copy()
        return

    prev = values[idx - 1]
    oper = opers[idx]

    for num in range(10):
        if numbers[num] is True:
            continue
        if (oper == "<" and prev < num) or (oper == ">" and prev > num):
            values[idx] = num
            numbers[num] = True
            tracking(idx + 1)
            values[idx] = -1
            numbers[num] = False


if __name__ == '__main__':

    # init
    count = int(input())
    opers = [-1] + list(map(str, input().split()))
    numbers = [False] * 10
    values = [-1] * (count + 1)
    minimum = [9] * (count + 1)
    maximum = [0] * (count + 1)

    for i in range(10):
        values[0] = i
        numbers[i] = True
        tracking(1)
        numbers[i] = False

    print("".join(map(str, maximum)))
    print("".join(map(str, minimum)))