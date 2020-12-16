import itertools


def valid(nums, index, prev=25):
    if index < prev:
        return True
    nums_prev = nums[index - prev:index]
    for (a, b) in itertools.product(nums_prev, nums_prev):
        if a == b:
            continue
        if (a + b) == nums[index]:
            return True
    return False


def find_contiguous(nums, value):
    total = 0
    index = 0
    start_index = 0
    end_index = -1
    while True:
        if total == value:
            end_index = index - 1
            min_nums = min(nums[start_index:end_index])
            max_nums = max(nums[start_index:end_index])
            return min_nums + max_nums
        elif total < value:
            total += nums[index]
            index += 1
        else:
            total -= nums[start_index]
            start_index += 1


numbers = open("numbers.txt").read().splitlines()
# numbers = """35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576""".splitlines()

numbers = [int(n) for n in numbers]

for i in range(len(numbers)):
    if not valid(numbers, i):
        x = numbers[i]
        break

print(x, find_contiguous(numbers, x))
