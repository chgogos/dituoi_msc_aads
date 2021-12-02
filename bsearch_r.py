# wrapper
def binary_search(list, item):
    return binary_search_helper(list, item, 0, len(list) - 1)

# call = 0
def binary_search_helper(list, item, low, high):
    """δυαδική αναζήτηση με αναδρομή"""
    # global call
    # call += 1
    # print(f'call= {call} -> low={low}, high={high}')
    if low > high:
        return None
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
        return mid
    if guess > item:
        return binary_search_helper(list, item, low, mid - 1)
    else:
        return binary_search_helper(list, item, mid + 1, high)


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))

# 1
# None
