def sumr(a_list):
    if a_list == []:
        return 0
    return a_list[0] + sumr(a_list[1:])

print(sumr([1,2,3,4,5]))