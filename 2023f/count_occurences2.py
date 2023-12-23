import random


def binary_search_high(s, key, low, high):
    if low > high:
        return high
    middle = (low + high) // 2
    if s[middle] > key:
        return binary_search_high(s, key, low, middle - 1)
    else:
        return binary_search_high(s, key, middle + 1, high)


def binary_search_low(s, key, low, high):
    if low > high:
        return low
    middle = (low + high) // 2
    if s[middle] >= key:
        return binary_search_low(s, key, low, middle - 1)
    else:
        return binary_search_low(s, key, middle + 1, high)


def count_occurences(s, key):
    pos1 = binary_search_low(s, key, 0, len(s) - 1)
    pos2 = binary_search_high(s, key, 0, len(s) - 1)
    print(pos1, pos2)
    if pos1 > pos2:
        return 0
    return pos2 - pos1 + 1


def scenario1():
    s = [1, 5, 6, 7, 7, 7, 7, 12, 15, 21, 56, 99]
    # s = [7, 7, 7, 7]
    # s = [1, 2, 3, 4, 5, 7, 7]
    # s = [7, 7, 8, 9, 10]
    # s = [1, 2, 3]
    # s = []
    key = 7
    count = count_occurences(s, key)
    print(count)


if __name__ == "__main__":
    scenario1()
