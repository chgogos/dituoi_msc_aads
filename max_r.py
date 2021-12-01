def maxr(a_list):
    if len(a_list) == 2:
        return a_list[0] if a_list[0] > a_list[1] else a_list[1]
    sub_max = maxr(a_list[1:])
    return a_list[0] if a_list[0] > sub_max else sub_max

print(maxr([1,2,3,4,5,6,7,8,9,10]))
    