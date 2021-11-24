"""
Grokking Algorithms - Binary Search
"""


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

#wrapper
def binary_search_r(list, item):
    return binary_search_r_helper(list, item, 0, len(list) - 1)


def binary_search_r_helper(list, item, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
        return mid
    if guess > item:
        return binary_search_r_helper(list, item, low, mid - 1)
    else:
        return binary_search_r_helper(list, item, mid + 1, high)


input_data = list(range(1, 100, 2))

for key in input_data:
    pos1 = binary_search(input_data, key)
    pos2 = binary_search_r(input_data, key)
    print(f"key={key} {pos1} - {pos2}")
    assert pos1 == pos2

key = 101 # not in list
pos1 = binary_search(input_data, key)
pos2 = binary_search_r(input_data, key)
print(f"key={key} {pos1} - {pos2}")
assert pos1 == pos2
