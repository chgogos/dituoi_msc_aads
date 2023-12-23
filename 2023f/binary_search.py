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


def scenario1():
    s = [1, 5, 7, 12, 15, 21, 56, 99]
    key = 21
    pos = binary_search(s, key, 0, len(s) - 1)
    print(pos)


def scenario2():
    s = [random.randint(0, 1_000) for _ in range(1_000_000)]
    s.sort()
    key = random.randint(0, 1_000)
    pos = binary_search(s, key, 0, len(s) - 1)
    print(f"key={key} is at index {pos}")


if __name__ == "__main__":
    scenario1()
    # scenario2()
