def word_count_input():
    return int(input())


def word_list_input(count):
    words = []
    for i in range(count):
        words.append(input())
    return words


def cap_to_int(char):
    return ord(char) - ord("A")


# input
word_count = word_count_input()
words = word_list_input(word_count)

alpha_count = [0] * 26

# count alpha
for word in words:
    for i, c in enumerate(reversed(word)):
        alpha_count[cap_to_int(c)] += 10 ** i

# sort and replace
alpha_count.sort(reverse=True)
total_sum = 0
for i in range(10):
    total_sum += alpha_count[i] * (9 - i)

# return
print(total_sum)
