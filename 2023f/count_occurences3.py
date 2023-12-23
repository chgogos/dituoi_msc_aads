import random

epsilon = 0.001


def binary_search_eps(s, key, low, high):
    if low > high:
        return (low + high) / 2
    middle = (low + high) // 2
    if s[middle] == key:
        return middle
    if s[middle] > key:
        return binary_search_eps(s, key, low, middle - 1)
    else:
        return binary_search_eps(s, key, middle + 1, high)


def count_occurences(s, key):
    pos1 = binary_search_eps(s, key - epsilon, 0, len(s) - 1)
    pos2 = binary_search_eps(s, key + epsilon, 0, len(s) - 1)
    if pos1 == pos2:
        return 0
    return int(pos2) - round(pos1) + 1


def scenario1():
    s = [1, 5, 7, 7, 7, 7, 12, 15, 21, 56, 99]
    # s = [7, 7, 7, 7]
    # s = [1, 2, 3, 4, 5]
    key = 7
    count = count_occurences(s, key)
    print(count)


if __name__ == "__main__":
    scenario1()
