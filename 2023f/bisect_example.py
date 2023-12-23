import bisect
sorted_list = [1, 3, 4, 7, 9, 12]
new_element = 5
insert_position = bisect.bisect(sorted_list, new_element)
sorted_list.insert(insert_position, new_element)
print(sorted_list)

