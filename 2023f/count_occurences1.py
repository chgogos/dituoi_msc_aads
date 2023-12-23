import random


def binary_search(s, key, low, high):
    if low > high:
        return -1
    middle = (low + high) // 2
    if s[middle] == key:
        return middle
    if s[middle] > key:
        return binary_search(s, key, low, middle - 1)
    else:
        return binary_search(s, key, middle + 1, high)


def count_occurences(s, key):
    pos = binary_search(s, key, 0, len(s) - 1)
    if pos == -1:
        return 0
    count = 1
    i = pos - 1
    while i >= 0 and s[i] == key:
        count += 1
        i -= 1
    i = pos + 1
    while i < len(s) and s[i] == key:
        count += 1
        i += 1
    return count


def scenario1():
    s = [1, 5, 7, 7, 7, 7, 12, 15, 21, 56, 99]
    key = 7
    count = count_occurences(s, key)
    print(count)


if __name__ == "__main__":
    scenario1()
